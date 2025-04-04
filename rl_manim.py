"""
Reinforcement Learning Animation Suite
Created for: Machine Learning Bonus Assignment Submission
Author: Sagnik Das
Description: This module contains animations demonstrating core concepts of RL
"""

from manim import *


class IntroRLScene(Scene):
    """Introduction scene demonstrating basic RL concepts through a grid world example"""
    
    def construct(self):
        # Initialize title sequence
        title = Text("Reinforcement Learning: 101", font_size=60, color=YELLOW)
        self.play(Write(title), run_time=1.0)
        self.wait(0.5)
        presenter = Text("Presented by Sagnik Das", font_size=36, color=BLUE).next_to(
            title, DOWN, buff=0.5
        )
        self.play(Write(presenter), run_time=0.9)
        self.wait(0.9)
        self.play(FadeOut(VGroup(title, presenter)), run_time=0.9)

        # Create 3x3 grid environment
        grid = VGroup()
        for x in range(3):
            for y in range(3):
                square = Square(side_length=1.2, stroke_width=2).move_to(
                    RIGHT * x + DOWN * y
                )
                grid.add(square)
        grid.move_to(ORIGIN)
        self.play(Create(grid), run_time=1.2)

        # Initialize agent and goal states
        agent = Dot(color=RED).move_to(grid[6].get_center())  # Starting position
        goal_flag = (
            SVGMobject("flag.svg")
            .scale(0.2)
            .set_color(GOLD)
            .move_to(grid[2].get_center())
        )
        self.play(FadeIn(agent), FadeIn(goal_flag), run_time=0.9)

        # Demonstrate wrong path with penalty
        wrong_path = [grid[6], grid[3]]
        for cell in wrong_path:
            self.play(agent.animate.move_to(cell.get_center()), run_time=0.26)

        penalty_cell = grid[4]
        penalty_label = Text("-1", font_size=30, color=RED).move_to(
            penalty_cell.get_center()
        )
        self.play(FadeIn(penalty_label), run_time=0.35)

        self.play(agent.animate.move_to(grid[4].get_center()), run_time=0.26)
        self.play(Flash(agent), run_time=0.26)
        wrong_icon = (
            SVGMobject("cross.svg")
            .scale(0.2)
            .move_to(grid.get_corner(UR) + RIGHT * 0.5)
        )
        self.play(FadeIn(wrong_icon), run_time=0.26)
        self.wait(0.3)
        self.play(FadeOut(wrong_icon), FadeOut(penalty_label), run_time=0.26)
        self.wait(0.5)

        self.play(agent.animate.move_to(grid[6].get_center()), run_time=0.26)

        # Demonstrate correct path to goal
        correct_path = [grid[6], grid[7], grid[8], grid[5], grid[2]]
        for cell in correct_path:
            self.play(agent.animate.move_to(cell.get_center()), run_time=0.26)
        self.play(Indicate(goal_flag, scale_factor=1.5), run_time=0.26)

        success_icon = SVGMobject("accept.svg").scale(0.4)
        success_icon.move_to(grid.get_corner(UR) + RIGHT * 0.8 + DOWN * 0.2)
        self.play(FadeIn(success_icon), run_time=0.35)
        self.wait(0.3)
        self.play(FadeOut(success_icon), run_time=0.35)

        subtitle = Text("Learning by Trial and Error", font_size=40, color=BLUE)
        subtitle.next_to(grid, DOWN, buff=0.8)
        self.play(Write(subtitle), run_time=0.9)
        self.wait(0.9)
        self.play(FadeOut(VGroup(grid, agent, goal_flag, subtitle)), run_time=0.9)
        self.wait(0.8)


class MDPPolicyScene(Scene):
    """Demonstrates Markov Decision Process and Policy concepts"""
    
    def construct(self):
        # Title for MDP section
        title = Text(
            "Markov Decision Process & Policy", font_size=50, color=YELLOW
        ).to_edge(UP)
        self.play(Write(title), run_time=1.0)

        # Create state transition diagram
        state = Circle(color=BLUE).shift(LEFT * 3)  # Current state
        state_label = Text("State", font_size=30).next_to(state, DOWN)

        next_state = Circle(color=GREEN).shift(RIGHT * 3)  # Next state
        next_state_label = Text("Next State", font_size=30).next_to(next_state, DOWN)

        action = Arrow(state.get_right(), next_state.get_left(), buff=0.1)  # Action
        action_label = Text("Action", font_size=30).next_to(action, UP)

        reward = Text("Reward", font_size=30, color=GOLD).next_to(next_state, UP)

        self.play(Create(state), Write(state_label), run_time=0.9)
        self.play(Create(next_state), Write(next_state_label), run_time=0.9)
        self.play(GrowArrow(action), Write(action_label), run_time=0.9)
        self.play(Write(reward), run_time=0.8)

        # Policy box and definition
        policy_box = Rectangle(width=6, height=1.2, color=WHITE).shift(DOWN * 3)
        policy_text = Text("Policy: π(s) → a", font_size=34).move_to(
            policy_box.get_center()
        )
        self.play(Create(policy_box), Write(policy_text), run_time=1.0)

        def_box = Rectangle(width=8, height=1.8, color=WHITE).next_to(
            policy_box, DOWN, buff=0.5
        )
        def_text = Text(
            "A policy defines the agent's way of behaving at a given state.",
            font_size=30,
            line_spacing=0.8,
        ).move_to(def_box.get_center())
        self.play(Create(def_box), Write(def_text), run_time=1.2)

        self.wait(2.5)
        self.play(
            FadeOut(
                VGroup(
                    title,
                    state,
                    state_label,
                    action,
                    action_label,
                    next_state,
                    next_state_label,
                    reward,
                    policy_box,
                    policy_text,
                    def_box,
                    def_text,
                )
            )
        )


class DiscountedRewardsScene(Scene):
    """Illustrates the concept of discounted rewards in RL"""
    
    def construct(self):
        title = Text(
            "Discounted Rewards (γ = 0.8)", font_size=48, color=YELLOW
        ).to_edge(UP)
        self.play(Write(title), run_time=1.2)

        now_box = Square().set_color(BLUE).move_to(LEFT * 4)
        now_label = Text("Now", font_size=30).next_to(now_box, DOWN)

        self.play(FadeIn(now_box), Write(now_label), run_time=0.9)

        gamma = 0.8
        base_size = 0.9
        rewards = VGroup()
        for i in range(8):
            scale = base_size * (gamma ** (i + 1))
            box = (
                Square()
                .set_color(GREEN)
                .scale(scale)
                .move_to(LEFT * 4 + RIGHT * (i + 1) * 1.2)
            )
            label = MathTex(rf"0.8^{(i+1)}", font_size=24).next_to(box, DOWN)
            rewards.add(VGroup(box, label))

        for reward_group in rewards:
            self.play(FadeIn(reward_group), run_time=0.35)

        formula = MathTex(
            r"R(s) = r_1 + \gamma r_2 + \gamma^2 r_3 + \gamma^3 r_4 + \gamma^4 r_5 + \cdots",
            font_size=36,
        ).move_to(DOWN * 2)
        self.play(Write(formula), run_time=1.5)
        now_box.set_stroke(width=2)
        self.wait(2.8)
        self.play(FadeOut(VGroup(title, now_box, now_label, rewards, formula)))


class ValueGuidesScene(Scene):
    """Shows how value functions guide the agent's decisions"""
    
    def construct(self):
        title = Text("Value Leads the Way", font_size=50, color=YELLOW).to_edge(UP)
        self.play(Write(title), run_time=1.2)

        grid = VGroup()
        values = {
            0: "-0.04",
            1: "-0.04",
            2: "-0.04",
            3: "+1.0",
            4: "-0.04",
            5: "-0.04",
            6: "-0.04",
            7: "-1.0",
            8: "START",
            9: "-0.04",
            10: "-0.04",
            11: "-0.04",
        }

        positions = []
        for i in range(3):
            for j in range(4):
                idx = (2 - i) * 4 + j
                pos = RIGHT * j + DOWN * (2 - i)
                square = Square(side_length=1.2, stroke_width=2).move_to(pos)
                label_text = values.get(idx, "-0.04")
                label = Text(label_text, font_size=22).move_to(square.get_center())
                if label_text == "+1.0":
                    label.set_color(GOLD)
                cell = VGroup(square, label)
                grid.add(cell)
                positions.append(pos)

        grid.move_to(ORIGIN)
        self.play(Create(grid), run_time=1.4)

        start_idx = 0
        agent = Dot(color=RED).scale(1.2).move_to(grid[start_idx][0].get_center())

        self.play(FadeIn(agent), run_time=0.6)

        path_indices = [0, 1, 2, 6, 10, 11]
        for idx in path_indices:
            self.play(agent.animate.move_to(grid[idx][0].get_center()), run_time=0.5)

        bellman_eq = MathTex(
            r"V^*(s) = \max_{a \epsilon A} \sum_{s' \epsilon S} T(s, a, s') \left[ R(s, a, s') + \gamma V^*(s') \right]",
            font_size=34,
        ).next_to(grid, DOWN, buff=1)
        self.play(Write(bellman_eq), run_time=1.5)
        self.wait(2)
        elements = VGroup(title, *grid, agent, bellman_eq)
        self.play(FadeOut(elements))


class TemporalDifferenceScene(Scene):
    """Explains Temporal-Difference Learning with examples"""
    
    def construct(self):
        title = Text(
            "Temporal-Difference Learning", font_size=48, color=YELLOW
        ).to_edge(UP)
        self.play(Write(title), run_time=1.2)

        tiles = VGroup()
        values = [0.5, 0.6, 0.2, 0.0]
        for i, v in enumerate(values):
            tile = Square(side_length=1.2, color=BLUE).move_to(RIGHT * (i - 1.5) * 2)
            label = Text(f"S{i}", font_size=24).next_to(tile, UP, buff=0.1)
            value = Text(f"V={v}", font_size=24).next_to(tile, DOWN, buff=0.1)
            tiles.add(VGroup(tile, label, value))

        tiles.move_to(ORIGIN)
        self.play(Create(tiles), run_time=1.3)

        agent = Dot(color=RED).scale(1.2).move_to(tiles[0][0].get_center())
        self.play(FadeIn(agent), run_time=0.5)

        reward1 = Text("r = +1", font_size=28, color=GOLD).next_to(
            tiles[1][0], UP, buff=0.5
        )
        update_eq1 = MathTex(
            r"V(S_0) \leftarrow 0.5 + 0.1 \cdot [1 + 0.9 \cdot 0.6 - 0.5] = 0.59",
            font_size=28,
        ).to_edge(DOWN)
        self.play(agent.animate.move_to(tiles[1][0].get_center()), run_time=0.6)
        self.play(Write(reward1), Write(update_eq1), run_time=1.0)
        self.wait(0.4)
        self.play(FadeOut(reward1), FadeOut(update_eq1), run_time=0.5)

        reward2 = Text("r = 0", font_size=28, color=GOLD).next_to(
            tiles[2][0], UP, buff=0.5
        )
        update_eq2 = MathTex(
            r"V(S_1) \leftarrow 0.6 + 0.1 \cdot [0 + 0.9 \cdot 0.2 - 0.6] = 0.57",
            font_size=28,
        ).to_edge(DOWN)
        self.play(agent.animate.move_to(tiles[2][0].get_center()), run_time=0.6)
        self.play(Write(reward2), Write(update_eq2), run_time=1.0)
        self.wait(0.4)
        self.play(FadeOut(reward2), FadeOut(update_eq2), run_time=0.5)

        summary = Text(
            "TD(0): Update after every step using next state's value",
            font_size=30,
            color=BLUE,
        ).next_to(tiles, DOWN, buff=0.8)
        self.play(Write(summary), run_time=1.2)
        self.wait(1.8)
        self.play(FadeOut(VGroup(title, tiles, agent, summary)), run_time=0.6)


class SarsaVsQLearningScene(Scene):
    """Compares Sarsa and Q-Learning algorithms"""
    
    def construct(self):
        title = Text("Sarsa vs Q-Learning", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title), run_time=1.2)

        sarsa_grid = VGroup()
        q_grid = VGroup()
        for i in range(3):
            s_tile = Square(side_length=1).move_to(LEFT * 4 + RIGHT * i * 1.2)
            q_tile = Square(side_length=1).move_to(RIGHT * 1 + RIGHT * i * 1.2)
            sarsa_grid.add(s_tile)
            q_grid.add(q_tile)

        self.play(Create(sarsa_grid), Create(q_grid), run_time=0.9)

        sarsa_label = Text("Sarsa (On-policy)", font_size=28, color=BLUE).next_to(
            sarsa_grid, UP
        )
        q_label = Text("Q-Learning (Off-policy)", font_size=28, color=RED).next_to(
            q_grid, UP
        )
        self.play(Write(sarsa_label, run_time=0.9), Write(q_label, run_time=0.9))

        agent_s = Dot(color=BLUE).scale(1.2).move_to(sarsa_grid[0].get_center())
        agent_q = Dot(color=RED).scale(1.2).move_to(q_grid[0].get_center())
        self.play(FadeIn(agent_s), FadeIn(agent_q), run_time=0.8)

        self.play(agent_s.animate.move_to(sarsa_grid[1].get_center()), run_time=0.6)
        update_s = (
            MathTex(
                r"Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma Q(s',a') - Q(s,a)]",
                color=BLUE,
            )
            .scale(0.8)
            .shift(LEFT * 3 + DOWN * 1.5)
        )

        a_label = Text("Follows taken action a'", font_size=24, color=BLUE).next_to(
            sarsa_grid, DOWN, buff=0.5
        )

        self.play(agent_q.animate.move_to(q_grid[1].get_center()), run_time=0.6)
        update_q = (
            MathTex(
                r"Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma \max_{a'} Q(s',a') - Q(s,a)]",
                color=RED,
            )
            .scale(0.8)
            .shift(RIGHT * 3 + DOWN * 1.5)
        )

        q_label2 = Text("Assumes best future action", font_size=24, color=RED).next_to(
            q_grid, DOWN, buff=0.5
        )

        eq_group = (
            VGroup(update_s, update_q).arrange(DOWN, buff=0.3).move_to(DOWN * 2.5)
        )

        self.play(
            Write(eq_group, run_time=1.2),
            Write(a_label, run_time=0.9),
            Write(q_label2, run_time=0.9),
        )
        self.wait(1.8)

        summary = Text(
            "Sarsa: Learns from experience  |  Q-Learning: Learns from imagined optimal future",
            font_size=28,
            color=WHITE,
        ).to_edge(DOWN)
        self.play(Write(summary), run_time=0.9)

        self.wait(1.4)
        self.play(
            FadeOut(
                VGroup(
                    title,
                    sarsa_grid,
                    q_grid,
                    agent_s,
                    agent_q,
                    update_s,
                    update_q,
                    a_label,
                    q_label2,
                    sarsa_label,
                    q_label,
                    summary,
                )
            ),
            run_time=1.2,
        )


class DeepQScene(Scene):
    """Illustrates Deep Q-Learning with neural networks"""
    
    def construct(self):
        title = Text("Deep Q-Learning", font_size=50, color=YELLOW).to_edge(UP)
        self.play(Write(title), run_time=1.2)

        frame = Square(side_length=1.2, color=BLUE).shift(LEFT * 4)
        frame_label = Text("State (image)", font_size=24).next_to(frame, DOWN)
        self.play(Create(frame), Write(frame_label), run_time=1.1)

        layers = VGroup()
        for i in range(4):
            layer = Rectangle(width=0.4, height=1.2 - i * 0.2, color=WHITE).shift(
                RIGHT * (i + 1) * 1.2
            )
            layers.add(layer)
        net = VGroup(*layers).move_to(RIGHT * 0.5)

        self.play(TransformFromCopy(frame, layers[0]), Create(layers[1:]), run_time=1.5)

        q_vals = (
            VGroup(
                Text("Q(Left)", font_size=24),
                Text("Q(Right)", font_size=24),
                Text("Q(Jump)", font_size=24),
            )
            .arrange(DOWN, buff=0.2)
            .next_to(layers[-1], RIGHT, buff=0.6)
        )
        self.play(Write(q_vals), run_time=1.2)

        loss_eq = MathTex(
            r"L(\theta) = \left(r + \gamma \max_{a'} Q(s', a') - Q(s, a)\right)^2",
            font_size=32,
        ).next_to(q_vals, DOWN, buff=0.8)
        self.play(Write(loss_eq), run_time=1.4)

        memory = Rectangle(width=2, height=1, color=GREEN).to_corner(DOWN + LEFT)
        mem_label = Text("Replay Buffer", font_size=24).next_to(memory, UP, buff=0.1)
        batch = Rectangle(width=1, height=0.4, color=GOLD).next_to(
            memory, RIGHT, buff=0.5
        )
        batch_label = Text("Sample Batch", font_size=20).next_to(batch, UP, buff=0.1)

        self.play(Create(memory), Write(mem_label), run_time=0.9)
        self.play(FadeIn(batch), Write(batch_label), run_time=0.9)

        summary = Text(
            "Scaling RL with pixels & neural nets", font_size=28, color=BLUE
        ).to_edge(DOWN)
        self.play(Write(summary), run_time=1.4)
        self.wait(1.5)

        self.play(
            FadeOut(
                VGroup(
                    title,
                    frame,
                    frame_label,
                    layers,
                    q_vals,
                    loss_eq,
                    memory,
                    mem_label,
                    batch,
                    batch_label,
                    summary,
                )
            ),
            run_time=0.9,
        )


class PolicyGradientScene(Scene):
    """Explains Policy Gradient Methods in RL"""
    
    def construct(self):
        title = Text("Policy Gradient Methods", font_size=50, color=YELLOW).to_edge(UP)
        self.play(Write(title), run_time=1.2)

        state = Square(color=BLUE).scale(1).shift(LEFT * 4)
        state_label = Text("State s", font_size=24).next_to(state, DOWN)
        self.play(FadeIn(state), Write(state_label), run_time=0.9)

        action_probs = (
            VGroup(
                Text("π(left|s)", font_size=24),
                Text("π(right|s)", font_size=24),
                Text("π(jump|s)", font_size=24),
            )
            .arrange(DOWN, buff=0.4)
            .shift(RIGHT * 3)
        )

        for i, action in enumerate(action_probs):
            arrow = Arrow(state.get_right(), action.get_left(), buff=0.1)
            self.play(GrowArrow(arrow), Write(action), run_time=0.6)

        reinforce = MathTex(
            r"\theta \leftarrow \theta + \alpha G_t \nabla \log \pi(a|s, \theta)",
            font_size=32,
        ).to_edge(DOWN)
        self.play(Write(reinforce), run_time=1.4)

        summary = Text(
            "REINFORCE: Learn policy directly from returns", font_size=28, color=BLUE
        ).next_to(reinforce, UP, buff=0.4)
        self.play(Write(summary), run_time=1.2)

        self.wait(1.4)
        self.play(
            FadeOut(
                VGroup(title, state, state_label, action_probs, reinforce, summary)
            ),
            run_time=1.1,
        )


class OutroScene(Scene):
    """Concluding scene with academic references and acknowledgments"""
    
    def construct(self):
        # Display bibliography
        title = Text("References", font_size=46, color=YELLOW).to_edge(UP)
        self.play(Write(title), run_time=1)

        # Academic references formatting
        references = (
            VGroup(
                Tex(
                    r"[1] R. S. Sutton and A. G. Barto, \textit{Reinforcement Learning: An Introduction}, 2nd ed., MIT Press, 2018.",
                    font_size=28,
                    tex_environment=None,
                ),
                Tex(
                    r"[2] F. Walter, Machine Learning Basic Modules, UTN: Learning Units 8-1 to 8-3, 2024.",
                    font_size=28,
                    tex_environment=None,
                ),
                Tex(
                    r"[3] S. Russell and P. Norvig, \textit{Artificial Intelligence: A Modern Approach}, 4th ed., Pearson, 2021.",
                    font_size=28,
                    tex_environment=None,
                ),
                Tex(
                    r"[4] Microsoft Copilot, used to assist with code review and debugging, Accessed: Mar. 28, 2025.",
                    font_size=28,
                    tex_environment=None,
                ),
                Tex(
                    r"[5] Manim Community Developers, \textit{Manim – Mathematical Animation Engine}. [Online]. Available: https://www.manim.community",
                    font_size=28,
                    tex_environment=None,
                ),
                Tex(
                    r"[6] SVG assets from \textit{https://www.svgrepo.com}, Accessed: Mar. 2025.",
                    font_size=28,
                    tex_environment=None,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.9)
            .next_to(title, DOWN, buff=0.8)
        )
        self.play(LaggedStartMap(Write, references, lag_ratio=0.1), run_time=2)

        thanks = Text("Thank you for watching!", font_size=40, color=BLUE).to_edge(DOWN)
        self.play(Write(thanks), run_time=1)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, references, thanks)), run_time=0.8)
        self.wait(6)
