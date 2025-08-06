from manim import *

class FundamentalTheoremTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Fundamental Theorem of Calculus", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Smaller graph on bottom left
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 3, 0.5],
            x_length=5,
            y_length=3,
            axis_config={"color": GREY},
            tips=False,
        ).to_corner(DL)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN)
        y_label = axes.get_y_axis_label("f(x) = x^2", edge=UP, direction=LEFT)
        self.play(Create(axes), Write(x_label), Write(y_label))

        def func(x):
            return x**2

        graph = axes.plot(func, x_range=[0, 2.5], color=YELLOW)
        
        # Show area under curve from 0 to 2
        area = axes.get_area(graph, x_range=[0, 2], color=YELLOW, opacity=0.3)
        
        # Add vertical lines at x=0 and x=2
        line_0 = axes.get_vertical_line(axes.c2p(0, 0), color=RED)
        line_2 = axes.get_vertical_line(axes.c2p(2, func(2)), color=RED)
        
        self.play(Create(graph))
        self.play(Create(line_0), Create(line_2), FadeIn(area))

        # Steps to show, centered below watermark/title
        steps = [
            r"\int_0^2 x^2 \, dx",
            r"\text{Step 1: Find antiderivative}",
            r"F(x) = \int x^2 \, dx = \frac{x^3}{3} + C",
            r"\text{Step 2: Apply FTC}",
            r"F(2) - F(0)",
            r"= \frac{2^3}{3} - \frac{0^3}{3}",
            r"= \frac{8}{3} - 0 = \frac{8}{3}",
        ]

        # Create first step centered below watermark/title
        step_text = MathTex(steps[0], font_size=48, color=BLUE).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text))
        self.wait(1)

        # Iterate through remaining steps, smoothly transforming old into new
        for i in range(1, len(steps)):
            new_color = GREEN if i == len(steps) - 1 else WHITE
            # Add special highlighting for the bounds substitution
            if i == 4:  # F(2) - F(0) step
                new_color = ORANGE
            new_step = MathTex(steps[i], font_size=48, color=new_color).next_to(watermark, DOWN, buff=1)
            self.play(Transform(step_text, new_step))
            
            # Extra pause for key steps
            if i == 2 or i == 4:  # Antiderivative and bounds substitution
                self.wait(1.5)
            else:
                self.wait(2 if i < len(steps) - 1 else 1.5)

        # Highlight final answer with box
        box = SurroundingRectangle(step_text, color=GREEN, buff=0.3)
        self.play(Create(box))
        self.wait(0.5)

        # End text moved a bit up from bottom
        end_text = Text("Area under curve = 8/3!", font_size=42, color=GREEN).to_edge(DOWN).shift(UP * 0.7)
        self.play(Write(end_text))
        self.wait(1)