from manim import *

class MeanValueTheoremTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Mean Value Theorem", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Graph on bottom middle
        axes = Axes(
            x_range=[-0.5, 2.5, 0.5],
            y_range=[-3, 2, 1],
            x_length=4.5,
            y_length=3,
            axis_config={"color": GREY},
            tips=False,
        ).to_edge(DOWN, buff=0.1)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN)
        y_label = axes.get_y_axis_label("f(x) = x^3 - 3x", edge=UP, direction=LEFT)
        self.play(Create(axes), Write(x_label), Write(y_label))

        def func(x):
            return x**3 - 3*x

        # Function values at endpoints
        a, b = 0, 2
        fa, fb = func(a), func(b)  # f(0) = 0, f(2) = 8 - 6 = 2

        graph = axes.plot(func, x_range=[-0.3, 2.3], color=YELLOW)
        
        # Endpoint dots
        dot_a = Dot(axes.c2p(a, fa), color=RED)
        dot_b = Dot(axes.c2p(b, fb), color=RED)
        
        self.play(Create(graph))
        self.play(Create(dot_a), Create(dot_b))

        # Steps to show, centered below watermark/title
        steps = [
            r"\text{There's ALWAYS a point where...}",
            r"\text{the tangent is parallel to the secant!}",
            r"\text{Secant slope: } \frac{f(2) - f(0)}{2 - 0}",
            r"= \frac{2 - 0}{2} = 1",
            r"\text{Find } c \text{ where } f'(c) = 1",
            r"f'(x) = 3x^2 - 3",
            r"3c^2 - 3 = 1 \Rightarrow c^2 = \frac{4}{3}",
            r"c = \frac{2}{\sqrt{3}} \approx 1.15",
        ]

        # Create first step
        step_text = MathTex(steps[0], font_size=44, color=BLUE).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text))
        self.wait(1.5)

        # Second step with secant line appearing
        new_step = MathTex(steps[1], font_size=44, color=BLUE).next_to(watermark, DOWN, buff=1)
        secant_line = Line(axes.c2p(a, fa), axes.c2p(b, fb), color=GREEN, stroke_width=6)
        self.play(Transform(step_text, new_step), Create(secant_line))
        self.wait(1.5)

        # Steps 3-4: Calculate secant slope
        for i in range(2, 4):
            new_step = MathTex(steps[i], font_size=44, color=WHITE).next_to(watermark, DOWN, buff=1)
            self.play(Transform(step_text, new_step))
            self.wait(1.5)

        # Step 5: Set up equation
        new_step = MathTex(steps[4], font_size=44, color=ORANGE).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Steps 6-7: Solve for c
        for i in range(5, 7):
            new_step = MathTex(steps[i], font_size=44, color=WHITE).next_to(watermark, DOWN, buff=1)
            self.play(Transform(step_text, new_step))
            self.wait(1.5)

        # Final step with dramatic reveal
        c_value = 2/np.sqrt(3)
        fc_value = func(c_value)
        
        new_step = MathTex(steps[7], font_size=44, color=GREEN).next_to(watermark, DOWN, buff=1)
        
        # Create the special point and tangent line
        dot_c = Dot(axes.c2p(c_value, fc_value), color=ORANGE, radius=0.12)
        
        # Tangent line at c (slope = 1, same as secant!)
        tangent_slope = 1
        tangent_length = 1.5
        tangent_start = axes.c2p(c_value - tangent_length/2, fc_value - tangent_slope * tangent_length/2)
        tangent_end = axes.c2p(c_value + tangent_length/2, fc_value + tangent_slope * tangent_length/2)
        tangent_line = Line(tangent_start, tangent_end, color=ORANGE, stroke_width=6)
        
        self.play(
            Transform(step_text, new_step),
            Create(dot_c),
            Create(tangent_line)
        )
        self.wait(1)

        # Highlight the parallel lines with pulsing
        self.play(
            secant_line.animate.set_stroke(width=8),
            tangent_line.animate.set_stroke(width=8)
        )
        self.wait(0.5)

        # Final dramatic box around the answer
        box = SurroundingRectangle(step_text, color=GREEN, buff=0.3)
        self.play(Create(box))
        self.wait(2)