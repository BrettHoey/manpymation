from manim import *

class ContourIntegrationTikTok(Scene):
    def construct(self):
        # Title and watermark
        title = Text("Contour Integration Example", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Step 1: Start with the integral
        step_text = MathTex(r"\oint_C \frac{1}{z^2+1}\, dz", font_size=48, color=BLUE).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text))
        self.wait(0.5)

        # Bring in unit circle on right
        circle = Circle(radius=1.2, color=WHITE).to_edge(RIGHT, buff=1)
        circle_label = Text("C: Unit Circle", font_size=28, color=WHITE).next_to(circle, DOWN* 0.5)
        self.play(FadeIn(circle, shift=LEFT), FadeIn(circle_label))

        # Animate traversal
        moving_dot = Dot(color=YELLOW).move_to(circle.point_at_angle(0))
        self.play(MoveAlongPath(moving_dot, circle), run_time=1.5, rate_func=linear)

        # Show poles directly on the circle
        pole1 = Dot(point=circle.point_at_angle(PI/2), color=RED)   # at angle 90°
        pole2 = Dot(point=circle.point_at_angle(3*PI/2), color=RED) # at angle 270°
        pole1_label = MathTex("i", font_size=32, color=RED).next_to(pole1, DOWN, buff=0.2)
        pole2_label = MathTex("-i", font_size=32, color=RED).next_to(pole2, DOWN, buff=0.2).shift(UP*0.2)
        # shift a little down to avoid overlap with circle label
        self.play(FadeIn(pole1, pole1_label, pole2, pole2_label))
        self.wait(1)

        # Step 2: Factor denominator
        new_step = MathTex(r"= \oint_C \frac{1}{(z - i)(z + i)} \, dz", font_size=48, color=WHITE).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Step 3: Residue Theorem
        new_step = MathTex(
            r"\oint_C f(z)\, dz = 2\pi i \sum \text{Res}(f, \text{poles in C})",
            font_size=44, color=WHITE
        ).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Show a separate callout: "Inside C: pole at z=i"
        glow = Circle(radius=0.25, color=ORANGE).move_to(pole1.get_center())
        glow.set_stroke(width=6)
        glow.set_fill(ORANGE, opacity=0.3)
        callout = Text("Inside C: pole at z=i", font_size=34, color=ORANGE).to_edge(DOWN).shift(UP*0.7)
        self.play(Create(glow), FadeIn(callout))
        self.wait(2)
        self.play(FadeOut(glow), FadeOut(callout))

        # Fade out circle and poles (declutter before math continues)
        self.play(FadeOut(circle, circle_label, moving_dot, pole1, pole2, pole1_label, pole2_label))

        # Step 4: Compute the residue
        new_step = MathTex(
            r"\text{Res}_{z=i} f(z) = \lim_{z\to i}(z-i)\frac{1}{(z-i)(z+i)}",
            font_size=44, color=BLUE
        ).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(2)

        # Step 5: Simplify residue
        new_step = MathTex(
            r"= \frac{1}{(i+i)} = \frac{1}{2i}",
            font_size=44, color=GREEN
        ).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Step 6: Final Answer
        new_step = MathTex(
            r"\oint_C \frac{1}{z^2+1}\, dz = 2\pi i \cdot \frac{1}{2i} = \pi",
            font_size=48, color=YELLOW
        ).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1)

        # Highlight the final answer
        box = SurroundingRectangle(step_text, color=YELLOW, buff=0.3)
        self.play(Create(box))
        self.wait(0.5)

        # Closing text
        end_text = Text("Final Answer: π", font_size=42, color=YELLOW).to_edge(DOWN).shift(UP * 0.7)
        self.play(Write(end_text))
        self.wait(1.5)
