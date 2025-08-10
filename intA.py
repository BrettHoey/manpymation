from manim import *
import numpy as np

class SmoothIntegralWithGraph(Scene):
    def construct(self):
        # Title and watermark
        title = Text("Tough Integral Step-by-Step", font_size=42, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=20, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Small graph setup on right side
        axes = Axes(
            x_range=[-1, 1, 0.5],
            y_range=[-1, 1, 0.5],
            x_length=4,
            y_length=3,
            axis_config={"color": GREY},
            tips=False,
        ).to_edge(RIGHT, buff=1).shift(DOWN * 0.5)
        
        func = axes.plot(lambda x: (x**3) / np.sqrt(1 - x**2 + 1e-6), color=BLUE, stroke_width=3)
        func_label = MathTex(r"f(x) = \frac{x^3}{\sqrt{1-x^2}}", font_size=28, color=BLUE).next_to(axes, UP, buff=0.3)
        self.add(axes, func, func_label)

        # Integral initial expression
        integral = MathTex(r"\int \frac{x^3}{\sqrt{1 - x^2}} \, dx", font_size=48, color=BLUE)
        integral.to_edge(LEFT, buff=1.5).shift(UP * 1)
        self.play(Write(integral), run_time=1)

        # Step 1: u substitution
        sub1 = MathTex(r"u = 1 - x^2", font_size=42, color=YELLOW).next_to(integral, DOWN, buff=0.7)
        self.play(Write(sub1), run_time=0.7)
        self.wait(0.4)
        du = MathTex(r"du = -2x \, dx", font_size=42, color=YELLOW).next_to(sub1, DOWN, buff=0.5)
        self.play(Write(du), run_time=0.7)
        self.wait(0.4)

        # Smooth transform integral into rewritten form with substitution parts
        rewrite1 = MathTex(r"x^3 = x \cdot x^2", font_size=40, color=ORANGE).next_to(du, DOWN, buff=1)
        self.play(Write(rewrite1), run_time=0.7)
        self.wait(0.4)
        rewrite2 = MathTex(r"x^2 = 1 - u", font_size=40, color=ORANGE).next_to(rewrite1, DOWN, buff=0.5)
        self.play(Write(rewrite2), run_time=0.7)
        self.wait(0.4)

        # Combine rewrite lines to build next integral step
        self.play(
            FadeOut(sub1), FadeOut(du), FadeOut(rewrite1), FadeOut(rewrite2),
            run_time=0.5
        )
        next_integral = MathTex(
            r"\int \frac{x \cdot (1 - u)}{\sqrt{u}} \, dx", font_size=48, color=BLUE
        ).move_to(integral.get_center())
        self.play(Transform(integral, next_integral), run_time=1)
        self.wait(0.5)

        # Express dx in terms of du
        dx_expr = MathTex(r"du = -2x\, dx \implies dx = \frac{du}{-2x}", font_size=40, color=BLUE).next_to(integral, DOWN, buff=0.7)
        self.play(Write(dx_expr), run_time=1)
        self.wait(0.5)

        # Substitute dx into integral and simplify
        new_integral = MathTex(
            r"\int \frac{x \cdot (1 - u)}{\sqrt{u}} \cdot \frac{du}{-2x} = \int \frac{1 - u}{-2 \sqrt{u}} \, du",
            font_size=40, color=PURPLE
        ).move_to(integral.get_center())
        self.play(FadeOut(dx_expr), Transform(integral, new_integral), run_time=1)
        self.wait(0.7)

        # Simplify further and split integral
        split_integral = MathTex(
            r"= -\frac{1}{2} \int \left( \frac{1}{\sqrt{u}} - \sqrt{u} \right) du",
            font_size=40, color=PURPLE
        ).move_to(integral.get_center())
        self.play(Transform(integral, split_integral), run_time=1)
        self.wait(0.7)

        # Write powers for integral
        powers_integral = MathTex(
            r"= -\frac{1}{2} \left( \int u^{-\frac{1}{2}} du - \int u^{\frac{1}{2}} du \right)",
            font_size=40, color=GREEN
        ).move_to(integral.get_center())
        self.play(Transform(integral, powers_integral), run_time=1)
        self.wait(0.7)

        # Integrate each term separately
        int1 = MathTex(r"\int u^{-\frac{1}{2}} du = 2 u^{\frac{1}{2}}", font_size=36, color=YELLOW).next_to(integral, DOWN, buff=0.8)
        int2 = MathTex(r"\int u^{\frac{1}{2}} du = \frac{2}{3} u^{\frac{3}{2}}", font_size=36, color=YELLOW).next_to(int1, DOWN, buff=0.5)
        self.play(FadeIn(int1), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(int2), run_time=0.6)
        self.wait(0.7)

        self.play(FadeOut(int1), FadeOut(int2))

        # Put it all together
        combined = MathTex(
            r"= -\frac{1}{2} \left( 2 u^{\frac{1}{2}} - \frac{2}{3} u^{\frac{3}{2}} \right) + C",
            font_size=40, color=BLUE
        ).move_to(integral.get_center())
        self.play(Transform(integral, combined), run_time=1)
        self.wait(0.7)

        # Simplify constants
        simplified = MathTex(
            r"= - \left( u^{\frac{1}{2}} - \frac{1}{3} u^{\frac{3}{2}} \right) + C",
            font_size=40, color=BLUE
        ).move_to(integral.get_center())
        self.play(Transform(integral, simplified), run_time=0.7)
        self.wait(0.7)

        # Substitute back u = 1 - x^2
        final_answer = MathTex(
            r"= - \sqrt{1 - x^2} + \frac{1}{3} (1 - x^2)^{\frac{3}{2}} + C",
            font_size=40, color=BLUE
        ).move_to(integral.get_center())
        self.play(Transform(integral, final_answer), run_time=0.8)
        self.wait(1)

        # Box final answer with subtle pulse
        box = SurroundingRectangle(integral, color=GOLD, buff=0.1)
        self.play(Create(box))
        for _ in range(2):
            self.play(box.animate.set_stroke(width=6), run_time=0.5)
            self.play(box.animate.set_stroke(width=3), run_time=0.5)
        self.wait(1)
