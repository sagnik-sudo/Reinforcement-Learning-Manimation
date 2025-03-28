from manim import *
import numpy as np

class FullRLAnimation(Scene):
    def construct(self):
        # Title Section
        title = Text("Reinforcement Learning:\nFrom MDPs to DP", font_size=42)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # MDP Example Section
        mdp_title = Text("A Simple MDP Example", font_size=36)
        self.play(Write(mdp_title))
        self.wait(1)
        mdp_title.to_edge(UP)

        s0 = Circle(radius=0.5, color=BLUE).shift(LEFT*4)
        s1 = Circle(radius=0.5, color=BLUE)
        s2 = Circle(radius=0.5, color=BLUE).shift(RIGHT*4)
        label0 = Text("S0", font_size=24).move_to(s0.get_center())
        label1 = Text("S1", font_size=24).move_to(s1.get_center())
        label2 = Text("S2", font_size=24).move_to(s2.get_center())

        self.play(Create(s0), Write(label0))
        self.play(Create(s1), Write(label1))
        self.play(Create(s2), Write(label2))
        self.wait(1)
        arrow01 = Arrow(s0.get_right(), s1.get_left(), buff=0.1)
        arrow12 = Arrow(s1.get_right(), s2.get_left(), buff=0.1)
        arrow22 = Arrow(s2.get_right(), s2.get_right() + RIGHT*1, buff=0.1)
        self.play(Create(arrow01), Create(arrow12), Create(arrow22))
        self.wait(1)
        reward01 = MathTex("+1", font_size=24).next_to(arrow01, UP)
        reward12 = MathTex("+2", font_size=24).next_to(arrow12, UP)
        reward22 = MathTex("0", font_size=24).next_to(arrow22, UP)
        self.play(Write(reward01), Write(reward12), Write(reward22))
        self.wait(3)
        self.play(FadeOut(VGroup(mdp_title, s0, s1, s2, label0, label1, label2,
                                  arrow01, arrow12, arrow22, reward01, reward12, reward22)))

        # Bellman Equation Breakdown Section
        bellman_title = Text("Bellman Equation Breakdown", font_size=36)
        self.play(Write(bellman_title))
        self.wait(1)
        eq_simple = MathTex("v(s)", "=", "R", "+", "\\gamma V(s')")
        eq_simple.scale(1.2)
        eq_simple.next_to(bellman_title, DOWN, buff=1)
        self.play(Write(eq_simple))
        self.wait(2)
        self.play(eq_simple[2].animate.set_color(RED))
        current_label = Text("Current reward", font_size=24).next_to(eq_simple[2], DOWN)
        self.play(Write(current_label))
        self.wait(1)
        self.play(FadeOut(current_label))
        self.play(eq_simple[4].animate.set_color(BLUE))
        gamma_label = Text("Discount factor", font_size=24).next_to(eq_simple[4], DOWN)
        self.play(Write(gamma_label))
        self.wait(1)
        self.play(FadeOut(gamma_label))
        eq_full = MathTex(
            "v(s)", "=",
            "\\sum_{a} \\pi(a|s)",
            "\\sum_{s',r} p(s',r|s,a)",
            "[R + \\gamma V(s')]"
        )
        eq_full.scale(0.9)
        eq_full.next_to(eq_simple, DOWN, buff=1)
        self.play(Transform(eq_simple, eq_full))
        self.wait(2)
        policy_label = Text("Policy", font_size=24).next_to(eq_full[2], DOWN)
        prob_label = Text("Transition probability", font_size=24).next_to(eq_full[3], DOWN)
        self.play(Write(policy_label), Write(prob_label))
        self.wait(2)
        self.play(FadeOut(VGroup(bellman_title, eq_simple, policy_label, prob_label)))

        # Policy Evaluation Section
        eval_title = Text("Policy Evaluation via Iterative Updates", font_size=36)
        self.play(Write(eval_title))
        self.wait(1)
        eval_title.to_edge(UP)
        s0 = Circle(radius=0.5, color=GREEN).shift(LEFT*4)
        s1 = Circle(radius=0.5, color=GREEN)
        s2 = Circle(radius=0.5, color=GREEN).shift(RIGHT*4)
        label0 = Text("S0", font_size=24).move_to(s0.get_center())
        label1 = Text("S1", font_size=24).move_to(s1.get_center())
        label2 = Text("S2", font_size=24).move_to(s2.get_center())
        self.play(Create(s0), Create(s1), Create(s2), Write(label0), Write(label1), Write(label2))
        self.wait(1)
        v0 = DecimalNumber(0, num_decimal_places=2, font_size=24).move_to(s0.get_center() + DOWN*0.7)
        v1 = DecimalNumber(0, num_decimal_places=2, font_size=24).move_to(s1.get_center() + DOWN*0.7)
        v2 = DecimalNumber(0, num_decimal_places=2, font_size=24).move_to(s2.get_center() + DOWN*0.7)
        self.play(Write(v0), Write(v1), Write(v2))
        self.wait(1)
        iterations = [(1.0, 1.2, 0.8), (1.5, 1.8, 1.2), (1.8, 2.0, 1.3)]
        for vals in iterations:
            self.play(
                Transform(v0, DecimalNumber(vals[0], num_decimal_places=2, font_size=24).move_to(s0.get_center() + DOWN*0.7)),
                Transform(v1, DecimalNumber(vals[1], num_decimal_places=2, font_size=24).move_to(s1.get_center() + DOWN*0.7)),
                Transform(v2, DecimalNumber(vals[2], num_decimal_places=2, font_size=24).move_to(s2.get_center() + DOWN*0.7)),
                run_time=2
            )
            self.wait(1)
        self.wait(2)
        self.play(FadeOut(VGroup(eval_title, s0, s1, s2, label0, label1, label2, v0, v1, v2)))

        # Policy Improvement & Convergence Section
        imp_title = Text("Policy Improvement & Value Convergence", font_size=36)
        self.play(Write(imp_title))
        self.wait(1)
        imp_title.to_edge(UP)
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 3, 0.5],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True}
        )
        axes.to_edge(DOWN)
        self.play(Create(axes))
        iterations = list(range(11))
        values = [2 - 2 * np.exp(-i/3) for i in iterations]
        points = [axes.coords_to_point(x, y) for x, y in zip(iterations, values)]
        graph = VMobject()
        graph.set_points_as_corners(points)
        graph.set_color(YELLOW)
        self.play(Create(graph))
        dot = Dot(color=RED).move_to(points[0])
        self.play(FadeIn(dot))
        for point in points[1:]:
            self.play(dot.animate.move_to(point), run_time=0.5)
        convergence_label = Text("Converged Value ≈ 2.0", font_size=24).next_to(axes, UP)
        self.play(Write(convergence_label))
        self.wait(2)
        self.play(FadeOut(VGroup(imp_title, axes, graph, dot, convergence_label)))

        # Dynamic Programming Section
        dp_title = Text("Dynamic Programming", font_size=36)
        self.play(Write(dp_title))
        self.wait(1)
        dp_expl = Text("Iteratively evaluate and improve the policy", font_size=28)
        dp_expl.next_to(dp_title, DOWN, buff=0.8)
        self.play(Write(dp_expl))
        self.wait(2)
        update_eq = MathTex(
            "v_{k+1}(s)", "=",
            "\\sum_{a}\\pi(a|s)", "\\sum_{s',r}p(s',r|s,a)",
            "[R + \\gamma v_k(s')]"
        )
        update_eq.scale(1.0)
        update_eq.next_to(dp_expl, DOWN, buff=1)
        self.play(Write(update_eq))
        self.wait(3)
        self.play(FadeOut(VGroup(dp_title, dp_expl, update_eq)))

        # Conclusion Section
        conclusion = Text("Learn, Evaluate, Improve", font_size=36)
        self.play(Write(conclusion))
        self.wait(3)
        self.play(FadeOut(conclusion))