from manim import *
import numpy as np

class NetflixFTC(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Your Netflix Queue Uses Calculus", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Axes for probability graph
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.2, 0.2],
            x_length=6,
            y_length=3,
            axis_config={"color": GREY},
            tips=False
        ).to_edge(DOWN, buff=0.1)

        x_label = axes.get_x_axis_label("Genres →", edge=RIGHT, direction=DOWN)
        y_label = axes.get_y_axis_label("Probability", edge=UP, direction=LEFT)
        self.play(Create(axes), Write(x_label), Write(y_label))

        # Define the PDF function
        def pdf(x):
            return 0.8 * np.exp(-0.5 * ((x - 5) / 1.5) ** 2)

        # Plot the PDF curve with animation
        pdf_curve = axes.plot(pdf, x_range=[0, 10], color=RED, stroke_width=4)

        # Steps to show
        steps = [
            r"\text{Netflix predicts what you'll watch...}",
            r"\text{using a probability curve!}",
            r"f(x) = \text{likelihood of liking genre } x",
            r"\text{But how do we get RECOMMENDATIONS?}",
            r"\text{We integrate: total probability up to a point}",
            r"F(x) = \int_{0}^{x} f(t) \, dt",
            r"\text{This is the Fundamental Theorem of Calculus}",
            r"\text{Your binge list is PURE math!}"
        ]

        # Show step 1 with curve drawing
        step_text = MathTex(steps[0], font_size=44, color=BLUE).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text))
        self.play(Create(pdf_curve, run_time=3))
        self.wait(1)

        # Show steps 2 and 3
        for i, color in [(1, ORANGE), (2, WHITE)]:
            new_step = MathTex(steps[i], font_size=40, color=color).next_to(watermark, DOWN, buff=1)
            self.play(Transform(step_text, new_step))
            self.wait(1.5)

        # Step 4 - question
        new_step = MathTex(steps[3], font_size=40, color=YELLOW).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Step 5 - shade area under curve up to x=6
        shade_area = axes.get_area(pdf_curve, x_range=[0, 6], color=BLUE, opacity=0.4)
        new_step = MathTex(steps[4], font_size=40, color=GREEN).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step), Create(shade_area, run_time=2))
        self.wait(1.5)

        # Step 6 - show FTC integral equation
        new_step = MathTex(steps[5], font_size=40, color=PURPLE).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Step 7 - FTC statement
        new_step = MathTex(steps[6], font_size=40, color=ORANGE).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Step 8 - punchline
        new_step = MathTex(steps[7], font_size=44, color=GREEN).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1)

        # Highlight curve and area
        self.play(pdf_curve.animate.set_stroke(width=8, color=GOLD))
        self.play(shade_area.animate.set_fill(opacity=0.6))

        # Draw a green box around final text
        box = SurroundingRectangle(step_text, color=GREEN, buff=0.3)
        self.play(Create(box))
        self.wait(2)
