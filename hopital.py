from manim import *
import numpy as np

class LHopital(Scene):
    def construct(self):
        # Colors for highlights
        sin_color = TEAL
        cos_color = ORANGE
        const_color = YELLOW_E
        frac_color = RED
        d_color = PURPLE

        # Title and watermark (persistent)
        title = Text("L'Hôpital's Rule Example", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Axes config for both graphs (same for consistency)
        axes_config = dict(
            x_range=[-0.5, 0.5, 0.1],
            y_range=[-1, 1, 0.5],
            x_length=4,
            y_length=2.5,
            axis_config={"color": GREY},
            tips=False,
        )

        # Create numerator axes bottom left (shifted left)
        num_axes = Axes(**axes_config).to_edge(DL).shift(LEFT * 2)
        num_label = Text("Numerator", font_size=24, color=TEAL).next_to(num_axes, UP, buff=0.1)

        # Create denominator axes bottom right (shifted right)
        denom_axes = Axes(**axes_config).to_edge(DL).shift(RIGHT * 2)
        denom_label = Text("Denominator", font_size=24, color=ORANGE).next_to(denom_axes, UP, buff=0.1)

        # Show axes and labels
        self.play(Create(num_axes), Write(num_label))
        self.play(Create(denom_axes), Write(denom_label))

        # Define original numerator and denominator functions
        def numerator_0(x):  # original numerator
            return np.sin(5 * x) - 5 * x

        def denominator_0(x):  # original denominator
            return x - np.sin(x)

        # First derivatives
        def numerator_1(x):
            return 5 * np.cos(5 * x) - 5

        def denominator_1(x):
            return 1 - np.cos(x)

        # Second derivatives
        def numerator_2(x):
            return -25 * np.sin(5 * x)

        def denominator_2(x):
            return np.sin(x)

        # Plot initial numerator and denominator graphs (inside axes bounds)
        num_graph = num_axes.plot(numerator_0, x_range=[-0.5, 0.5], color=TEAL)
        denom_graph = denom_axes.plot(denominator_0, x_range=[-0.5, 0.5], color=ORANGE)
        self.play(Create(num_graph), Create(denom_graph))
        self.wait(2)

        # Steps with derivative and limit text
        steps = [
            r"\lim_{x \to 0} \frac{\sin(5x) - 5x}{x - \sin(x)} = \frac{0}{0}",
            r"d/dx \left[\sin(5x) - 5x\right] = 5\cos(5x) - 5",
            r"d/dx \left[x - \sin(x)\right] = 1 - \cos(x)",
            r"\lim_{x \to 0} \frac{5\cos(5x) - 5}{1 - \cos(x)} = \frac{0}{0}",
            r"d/dx \left[5\cos(5x) - 5\right] = -25\sin(5x)",
            r"d/dx \left[1 - \cos(x)\right] = \sin(x)",
            r"\lim_{x \to 0} \frac{-25\sin(5x)}{\sin(x)}",
            r"\lim_{x \to 0} \frac{-25(5x)}{x}",
            r"= -125",
        ]

        colors = {
            "sin": sin_color,
            "cos": cos_color,
            "5": const_color,
            "25": const_color,
            r"\frac{0}{0}": frac_color,
            "d/dx": d_color,
        }

        def style_eq(eq):
            for key, color in colors.items():
                eq.set_color_by_tex(key, color)
            eq.set_stroke(BLACK, 2, 0.25)
            return eq

        # Show first step, positioned above the graphs (avoid overlap)
        step_text = style_eq(MathTex(steps[0], font_size=48)).next_to(watermark, DOWN, buff=1.5)
        self.play(Write(step_text))
        self.wait(1.5)

        # Helper to morph graphs smoothly
        def morph_graph(old_graph, new_func, axes, color):
            new_graph = axes.plot(new_func, x_range=[-0.5, 0.5], color=color)
            self.play(Transform(old_graph, new_graph), run_time=2)
            return old_graph

        # Step 1->2 numerator derivative
        step_1_2 = style_eq(MathTex(steps[1], font_size=48)).next_to(watermark, DOWN, buff=1.5)
        self.play(Transform(step_text, step_1_2))
        self.wait(0.5)
        num_graph = morph_graph(num_graph, numerator_1, num_axes, TEAL)
        self.wait(1)

        # Step 2->3 denominator derivative
        step_2_3 = style_eq(MathTex(steps[2], font_size=48)).next_to(watermark, DOWN, buff=1.5)
        self.play(Transform(step_text, step_2_3))
        self.wait(0.5)
        denom_graph = morph_graph(denom_graph, denominator_1, denom_axes, ORANGE)
        self.wait(1)

        # Step 3->4 limit after first derivative
        step_3_4 = style_eq(MathTex(steps[3], font_size=48)).next_to(watermark, DOWN, buff=1.5)
        self.play(Transform(step_text, step_3_4))
        self.wait(1.5)

        # Step 4->5 numerator second derivative
        step_4_5 = style_eq(MathTex(steps[4], font_size=48)).next_to(watermark, DOWN, buff=1.5)
        self.play(Transform(step_text, step_4_5))
        self.wait(0.5)
        num_graph = morph_graph(num_graph, numerator_2, num_axes, TEAL)
        self.wait(1)

        # Step 5->6 denominator second derivative
        step_5_6 = style_eq(MathTex(steps[5], font_size=48)).next_to(watermark, DOWN, buff=1.5)
        self.play(Transform(step_text, step_5_6))
        self.wait(0.5)
        denom_graph = morph_graph(denom_graph, denominator_2, denom_axes, ORANGE)
        self.wait(1)

        # Step 6->7 limit after second derivative
        step_6_7 = style_eq(MathTex(steps[6], font_size=48)).next_to(watermark, DOWN, buff=1.5)
        self.play(Transform(step_text, step_6_7))
        self.wait(1.5)

        # Step 7->8 simplified limit
        step_7_8 = style_eq(MathTex(steps[7], font_size=48)).next_to(watermark, DOWN, buff=1.5)
        self.play(Transform(step_text, step_7_8))
        self.wait(1.5)

        # Step 8->9 final answer (highlighted)
        step_8_9 = style_eq(MathTex(steps[8], font_size=48, color=YELLOW)).next_to(watermark, DOWN, buff=1.5)
        self.play(Transform(step_text, step_8_9))

        box = SurroundingRectangle(step_text, color=YELLOW, buff=0.3)
        self.play(Create(box))
        self.wait(2)
