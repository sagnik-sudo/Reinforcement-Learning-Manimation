from manim import *
import numpy as np

class TitleHookScene(Scene):
    def construct(self):
        title = Text("Reinforcement Learning", font_size=60)
        subtitle = Text("From MDPs to Optimal Policies", font_size=36)
        self.play(FadeIn(title, shift=UP), run_time=1.5)
        self.wait(0.5)
        self.play(Transform(title, subtitle), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(title), run_time=1)

class MotivationScene(Scene):
    def construct(self):
        sq = Square(side_length=8, color=BLUE_E).set_fill(BLUE_E, opacity=0.2)
        self.add(sq)
        dots = VGroup(*[Dot(np.array([np.cos(theta), np.sin(theta), 0])*3, color=YELLOW) for theta in np.linspace(0, TAU, 20, endpoint=False)])
        self.play(LaggedStartMap(FadeIn, dots, lag_ratio=0.1), run_time=2)
        arrow1 = Arrow(LEFT*4, LEFT*2, buff=0.1, color=WHITE)
        arrow2 = Arrow(RIGHT*4, RIGHT*2, buff=0.1, color=WHITE)
        self.play(Create(arrow1), Create(arrow2), run_time=1)
        self.wait(1)
        self.play(FadeOut(VGroup(sq, dots, arrow1, arrow2)), run_time=1)

class RLDefinitionScene(Scene):
    def construct(self):
        agent = Dot(color=RED).move_to(LEFT*4)
        reward = MathTex("+1", font_size=36).move_to(RIGHT*4)
        path = VMobject()
        path.set_points_as_corners([LEFT*4, ORIGIN, RIGHT*4])
        self.play(FadeIn(agent), Create(path), run_time=1.5)
        self.play(MoveAlongPath(agent, path), run_time=2)
        self.play(Write(reward), run_time=1)
        self.wait(1)
        self.play(FadeOut(VGroup(agent, path, reward)), run_time=1)

class GridWorldMDPScene(Scene):
    def construct(self):
        rows, cols = 3, 4
        cell_size = 1.5
        grid = {}
        grid_group = VGroup()
        for r in range(rows):
            for c in range(cols):
                x = (c - (cols - 1) / 2) * cell_size
                y = ((rows - 1) / 2 - r) * cell_size
                pos = np.array([x, y, 0])
                if (r, c) == (1, 1):
                    cell = Square(side_length=cell_size, color=RED)
                    cell.move_to(pos)
                    txt = Text("Wall", font_size=20).move_to(pos)
                    grid[(r, c)] = {"cell": cell, "terminal": False, "reward": None, "value": None}
                    grid_group.add(cell, txt)
                else:
                    cell = Square(side_length=cell_size, color=WHITE)
                    cell.move_to(pos)
                    terminal = False
                    rwd = -0.04
                    if (r, c) == (0, 3):
                        terminal = True; rwd = 1
                    elif (r, c) == (1, 3):
                        terminal = True; rwd = -1
                    txt = Text(f"S({r},{c})", font_size=20).move_to(pos + UP * 0.4)
                    val = DecimalNumber(rwd if terminal else 0, num_decimal_places=2, font_size=20).move_to(pos + DOWN * 0.4)
                    grid[(r, c)] = {"cell": cell, "terminal": terminal, "reward": rwd, "value": val}
                    grid_group.add(cell, txt, val)
        self.play(Create(grid_group), run_time=2)
        iterations = {
            (0, 0): [0, -0.04, -0.06, -0.07],
            (0, 1): [0, -0.04, -0.05, -0.06],
            (0, 2): [0, -0.03, -0.04, -0.05],
            (0, 3): [1, 1, 1, 1],
            (1, 0): [0, -0.04, -0.05, -0.06],
            (1, 2): [0, -0.03, -0.04, -0.05],
            (1, 3): [-1, -1, -1, -1],
            (2, 0): [0, -0.04, -0.04, -0.05],
            (2, 1): [0, -0.04, -0.04, -0.04],
            (2, 2): [0, -0.04, -0.04, -0.04],
            (2, 3): [0, -0.04, -0.04, -0.04],
        }
        for i in range(1, 4):
            updates = []
            for key, vals in iterations.items():
                if key in grid and not grid[key]["terminal"]:
                    new_val = DecimalNumber(vals[i], num_decimal_places=2, font_size=20).move_to(grid[key]["cell"].get_center() + DOWN * 0.4)
                    updates.append(Transform(grid[key]["value"], new_val))
            self.play(*updates, run_time=1.5)
            self.wait(0.5)
        self.wait(1)
        self.play(FadeOut(grid_group), run_time=1)

class BellmanEquationScene(Scene):
    def construct(self):
        eq = MathTex("v(s)=\\max_{a}\\sum_{s'}p(s'|s,a)[R(s,a,s')+\\gamma v(s')]").scale(1.2)
        self.play(FadeIn(eq), run_time=2)
        self.wait(2)
        self.play(FadeOut(eq), run_time=1)

class PolicyIterationScene(Scene):
    def construct(self):
        rows, cols = 3, 4
        cell_size = 1.5
        grid = {}
        grid_group = VGroup()
        for r in range(rows):
            for c in range(cols):
                x = (c - (cols - 1) / 2) * cell_size
                y = ((rows - 1) / 2 - r) * cell_size
                pos = np.array([x, y, 0])
                if (r, c) == (1, 1):
                    cell = Square(side_length=cell_size, color=RED)
                    cell.move_to(pos)
                    txt = Text("Wall", font_size=20).move_to(pos)
                    grid[(r, c)] = {"cell": cell}
                    grid_group.add(cell, txt)
                else:
                    cell = Square(side_length=cell_size, color=WHITE)
                    cell.move_to(pos)
                    txt = Text(f"S({r},{c})", font_size=20).move_to(pos + UP * 0.4)
                    grid[(r, c)] = {"cell": cell}
                    grid_group.add(cell, txt)
        self.play(Create(grid_group), run_time=2)
        policy_arrows = VGroup()
        moves = { (0,0):(0,1), (0,1):(0,2), (0,2):(0,3),
                  (1,0):(0,0), (1,2):(0,2),
                  (2,0):(1,0), (2,1):(2,2), (2,2):(2,3), (2,3):(1,3)}
        for (r,c), (nr,nc) in moves.items():
            start = grid[(r,c)]["cell"].get_center()
            end = grid[(nr,nc)]["cell"].get_center()
            arrow = Arrow(start, end, buff=0.1, stroke_width=4, color=YELLOW)
            policy_arrows.add(arrow)
            self.play(Create(arrow), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(VGroup(grid_group, policy_arrows)), run_time=1)

class AgentEnvironmentLoopScene(Scene):
    def construct(self):
        rows, cols = 3, 4
        cell_size = 1.5
        grid_group = VGroup()
        grid = {}
        for r in range(rows):
            for c in range(cols):
                x = (c - (cols - 1) / 2) * cell_size
                y = ((rows - 1) / 2 - r) * cell_size
                pos = np.array([x, y, 0])
                if (r, c) == (1,1):
                    cell = Square(side_length=cell_size, color=RED).move_to(pos)
                    txt = Text("Wall", font_size=20).move_to(pos)
                    grid[(r,c)] = cell
                    grid_group.add(cell, txt)
                else:
                    cell = Square(side_length=cell_size, color=WHITE).move_to(pos)
                    txt = Text(f"S({r},{c})", font_size=20).move_to(pos + UP*0.4)
                    grid[(r,c)] = cell
                    grid_group.add(cell, txt)
        self.play(Create(grid_group), run_time=2)
        agent = Dot(color=RED).move_to(grid[(2,0)].get_center())
        self.play(FadeIn(agent), run_time=1)
        traj = [(2,0), (1,0), (0,0), (0,1), (0,2), (0,3)]
        for state in traj:
            target = grid[state].get_center()
            self.play(agent.animate.move_to(target), run_time=1)
            self.play(Indicate(agent, scale_factor=1.5), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(VGroup(grid_group, agent)), run_time=1)

class OutroScene(Scene):
    def construct(self):
        ref = Text("Sutton & Barto", font_size=36, color=BLUE)
        self.play(FadeIn(ref), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(ref), run_time=1)