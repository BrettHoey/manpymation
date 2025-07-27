from manim import *
import math
import numpy as np

class TaylorSeriesExp(Scene):
    def construct(self):
        # Title (top center)
        title = Text("Taylor Series Approximation for e^x").scale(0.8)
        title.to_edge(UP).shift(DOWN*0.4)  # Leave a little space at the top

        # Watermark (just below title, smaller font)
        watermark = Text("@calc4dumb", font_size=28, color=GRAY)
        watermark.next_to(title, DOWN)  # Place directly under the title

        self.play(FadeIn(title), FadeIn(watermark))

        # Axes (shifted down for spacing)
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 10, 1],
            x_length=7,
            y_length=5,
            axis_config={"color": BLUE},
            tips=False
        ).shift(DOWN*1.8)

        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(labels))

        # e^x curve
        exp_graph = axes.plot(lambda x: np.exp(x), color=YELLOW)
        exp_label = axes.get_graph_label(exp_graph, label="e^x", x_val=2, direction=UP)
        self.play(Create(exp_graph), Write(exp_label))
        self.wait(0.5)

        # Taylor expansion function
        def taylor_expansion(x, n_terms=1):
            return sum([x**k / math.factorial(k) for k in range(n_terms)])

        # First approximation (just "1")
        approx_graph = axes.plot(lambda x: taylor_expansion(x, 1), color=RED)
        self.play(Create(approx_graph))
        self.wait(0.5)

        # Initial formula (placed low enough to avoid title & watermark)
        formula = MathTex("1").scale(0.9).set_color(RED)
        formula.to_corner(UL).shift(RIGHT*2.0 + DOWN*1.5)
        self.play(Write(formula))

        # Colors for each successive approximation
        colors = [RED, ORANGE, GREEN, PURPLE, TEAL, PINK, BLUE]

        # Animate partial sums up to x^6 / 6!
        for n in range(2, 8):
            new_graph = axes.plot(lambda x, n=n: taylor_expansion(x, n), color=colors[(n-1) % len(colors)])
            
            # Update formula
            terms = ["1"] + [f"\\frac{{x^{k}}}{{{k}!}}" for k in range(1, n)]
            series_tex = "+".join(terms)
            new_formula = MathTex(series_tex).scale(0.9).set_color(colors[(n-1) % len(colors)])
            new_formula.to_corner(UL).shift(RIGHT*2.0 + DOWN*1.5)

            # Morph graph & formula together
            self.play(
                Transform(approx_graph, new_graph),
                Transform(formula, new_formula),
                run_time=1.5
            )
            self.wait(0.3)

        # Final pause
        self.wait(2)
