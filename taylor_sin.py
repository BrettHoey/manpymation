from manim import *
import numpy as np

class SineTaylorSeries(Scene):
    def construct(self):
        # Title + watermark
        title = Text("Taylor Series for sin(x)", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Axes centered, smaller x range but same visual size
        axes = Axes(
            x_range=[-3.5, 3.5, 0.5],
            y_range=[-3, 3, 1],
            x_length=4.5,   
            y_length=2.5,
            axis_config={"color": GREY},
            tips=False,
        ).to_edge(DOWN, buff=1)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN)
        y_label = axes.get_y_axis_label("y", edge=UP, direction=LEFT)
        self.play(Create(axes), Write(x_label), Write(y_label))

        # sin(x) curve over full displayed x_range
        sin_graph = axes.plot(lambda x: np.sin(x), color=YELLOW, x_range=[-3.5, 3.5])
        self.play(Create(sin_graph), run_time=1)

        # Define Taylor approximations up to x^7
        def T1(x): return x
        def T3(x): return x - (x**3)/6
        def T5(x): return x - (x**3)/6 + (x**5)/120
        def T7(x): return x - (x**3)/6 + (x**5)/120 - (x**7)/5040

        approximations = [
            (T1, r"x"),
            (T3, r"x - \frac{x^3}{3!}"),
            (T5, r"x - \frac{x^3}{3!} + \frac{x^5}{5!}"),
            (T7, r"x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!}")
        ]

        colors = [BLUE, GREEN, ORANGE, RED]

        # Base equation above center, shifted left
        eq_base = MathTex(r"\sin(x) \approx", font_size=46, color=WHITE)\
            .next_to(watermark, DOWN, buff=1.2)\
            .shift(LEFT * 2)
        self.play(Write(eq_base))

        # Use same x_range for all since small domain
        x_range = [-3.5, 3.5]

        # Initialize the first Taylor graph and terms
        first_func, first_terms = approximations[0]
        taylor_graph = axes.plot(
            first_func,
            color=colors[0],
            x_range=x_range
        )
        eq_terms = MathTex(first_terms, font_size=46, color=colors[0]).next_to(eq_base, RIGHT, buff=0.5)

        self.play(Create(taylor_graph), Write(eq_terms), run_time=1)
        self.wait(0.5)

        prev_eq = eq_terms

        # Loop through rest, morphing the curve and terms
        for i, (func, terms) in enumerate(approximations[1:], start=1):
            new_graph = axes.plot(
                func,
                color=colors[i],
                x_range=x_range
            )
            new_eq = MathTex(terms, font_size=46, color=colors[i]).next_to(eq_base, RIGHT, buff=0.5)

            self.play(Transform(taylor_graph, new_graph), Transform(prev_eq, new_eq), run_time=0.7)
            prev_eq = new_eq
            self.wait(0.5)

        # Highlight final approximation
        box = SurroundingRectangle(VGroup(eq_base, prev_eq), color=YELLOW, buff=0.3)
        self.play(Create(box), run_time=1)
        self.wait(0.7)

        # Closing text
        end_text = Text("More terms → Closer to sin(x)! 🎯", font_size=40, color=YELLOW).to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(end_text))
        self.wait(1)
