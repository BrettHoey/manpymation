from manim import *

class ImproperIntegralTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Improper Integral Example", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Smaller graph on bottom left
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.5, 0.25],
            x_length=5,
            y_length=3,
            axis_config={"color": GREY},
            tips=False,
        ).to_corner(DL)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN)
        y_label = axes.get_y_axis_label("f(x) = 1/x^2", edge=UP, direction=LEFT)
        self.play(Create(axes), Write(x_label), Write(y_label))

        def func(x):
            return 1 / (x**2)

        graph = axes.plot(func, x_range=[1, 10], color=YELLOW)
        area = axes.get_area(graph, x_range=[1, 10], color=YELLOW, opacity=0.3)
        self.play(Create(graph), FadeIn(area))

        # Steps to show, centered below watermark/title
        steps = [
            r"\int_1^\infty \frac{1}{x^2} \, dx",
            r"= \lim_{b \to \infty} \int_1^b \frac{1}{x^2} \, dx",
            r"= \lim_{b \to \infty} \left[-\frac{1}{x}\right]_1^b",
            r"= \lim_{b \to \infty} \left(-\frac{1}{b} + 1\right)",
            r"= 0 + 1 = 1",
        ]

        # Create first step centered below watermark/title
        step_text = MathTex(steps[0], font_size=48, color=BLUE).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text))
        self.wait(1)

        # Iterate through remaining steps, smoothly transforming old into new
        for i in range(1, len(steps)):
            new_color = GREEN if i == len(steps) - 1 else WHITE
            new_step = MathTex(steps[i], font_size=48, color=new_color).next_to(watermark, DOWN, buff=1)
            self.play(Transform(step_text, new_step))
            self.wait(2 if i < len(steps) - 1 else 1.5)

        # Highlight final answer with box
        box = SurroundingRectangle(step_text, color=GREEN, buff=0.3)
        self.play(Create(box))
        self.wait(1)

        # End text moved a bit up from bottom
        end_text = Text("Integral converges to 1!", font_size=42, color=GREEN).to_edge(DOWN).shift(UP * 0.7)
        self.play(Write(end_text))
        self.wait(2)
