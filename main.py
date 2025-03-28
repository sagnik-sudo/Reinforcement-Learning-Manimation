from manim import *

class IntroRLScene(Scene):
    def construct(self):
        # Title intro
        title = Text("Introduction to Reinforcement Learning", font_size=60, color=YELLOW)
        self.play(Write(title), run_time=2)
        self.wait(1)
        self.play(FadeOut(title))

        # Setup grid with thin lines
        grid = VGroup()
        for x in range(3):
            for y in range(3):
                square = Square(side_length=1.2, stroke_width=2).move_to(RIGHT*x + DOWN*y)
                grid.add(square)
        grid.move_to(ORIGIN)
        self.play(Create(grid), run_time=1.5)

        # Agent & goal
        agent = Dot(color=RED).move_to(grid[6].get_center())  # bottom-left
        goal_flag = SVGMobject("flag.svg").scale(0.2).set_color(GOLD).move_to(grid[2].get_center())  # top-right

        self.play(FadeIn(agent), FadeIn(goal_flag), run_time=1)

        # First (wrong) path
        wrong_path = [grid[6], grid[3], grid[4]]
        for cell in wrong_path:
            self.play(agent.animate.move_to(cell.get_center()), run_time=0.5)
        self.play(Flash(agent), run_time=0.5)
        self.wait(0.5)

        # Reset agent
        self.play(agent.animate.move_to(grid[6].get_center()), run_time=0.5)

        # Correct path
        correct_path = [grid[6], grid[7], grid[8], grid[5], grid[2]]
        for cell in correct_path:
            self.play(agent.animate.move_to(cell.get_center()), run_time=0.5)
        self.play(Indicate(goal_flag, scale_factor=1.5), run_time=0.5)

        # Add subtitle below grid
        subtitle = Text("Learning by Trial and Error", font_size=40, color=BLUE)
        subtitle.next_to(grid, DOWN, buff=0.8)
        self.play(Write(subtitle), run_time=1.5)

        self.wait(2)
        self.play(FadeOut(VGroup(grid, agent, goal_flag, subtitle)))

class MDPPolicyScene(Scene):
    def construct(self):
        # Title
        title = Text("Markov Decision Process & Policy", font_size=50, color=YELLOW).to_edge(UP)
        self.play(Write(title), run_time=1.5)

        # MDP Elements
        state = Circle(color=BLUE).shift(LEFT*3)
        state_label = Text("State", font_size=30).next_to(state, DOWN)

        next_state = Circle(color=GREEN).shift(RIGHT*3)
        next_state_label = Text("Next State", font_size=30).next_to(next_state, DOWN)

        action = Arrow(state.get_right(), next_state.get_left(), buff=0.1)
        action_label = Text("Action", font_size=30).next_to(action, UP)

        reward = Text("Reward", font_size=30, color=GOLD).next_to(next_state, UP)

        self.play(Create(state), Write(state_label))
        self.play(Create(next_state), Write(next_state_label))
        self.play(GrowArrow(action), Write(action_label))
        self.play(Write(reward))

        # Policy formula
        policy_box = Rectangle(width=6, height=1.2, color=WHITE).shift(DOWN*3)
        policy_text = Text("Policy: π(s) → a", font_size=34).move_to(policy_box.get_center())
        self.play(Create(policy_box), Write(policy_text))

        # Policy explanation
        def_box = Rectangle(width=8, height=1.8, color=WHITE).next_to(policy_box, DOWN, buff=0.5)
        def_text = Text("A policy defines the agent's way of behaving at a given state.",
                        font_size=30, line_spacing=0.8).move_to(def_box.get_center())
        self.play(Create(def_box), Write(def_text))

        self.wait(1.5)
        self.play(FadeOut(VGroup(
            title, state, state_label, action, action_label,
            next_state, next_state_label, reward,
            policy_box, policy_text, def_box, def_text
        )))

class DiscountedRewardsScene(Scene):
    def construct(self):
        # Title
        title = Text("Discounted Rewards (γ = 0.8)", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # "Now" box
        now_box = Square().set_color(BLUE).move_to(LEFT*4)
        now_label = Text("Now", font_size=30).next_to(now_box, DOWN)

        self.play(FadeIn(now_box), Write(now_label))

        # Future rewards with γ=0.8
        gamma = 0.8
        base_size = 0.9
        rewards = VGroup()
        for i in range(8):
            scale = base_size * (gamma ** (i+1))
            box = Square().set_color(GREEN).scale(scale).move_to(LEFT*4 + RIGHT*(i+1)*1.2)
            label = MathTex(rf"0.8^{(i+1)}", font_size=24).next_to(box, DOWN)
            rewards.add(VGroup(box, label))

        for reward_group in rewards:
            self.play(FadeIn(reward_group), run_time=0.4)

        # Show discounted return formula below
        formula = MathTex(
            r"R(s) = r_1 + \gamma r_2 + \gamma^2 r_3 + \gamma^3 r_4 + \gamma^4 r_5 + \cdots",
            font_size=36
        ).move_to(DOWN*2)
        self.play(Write(formula))
        box.set_stroke(width=2)
        self.wait(2)
        self.play(FadeOut(VGroup(title, now_box, now_label, rewards, formula)))