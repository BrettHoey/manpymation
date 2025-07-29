from manim import *
import numpy as np

class AreaBetweenCurves(Scene):
    def construct(self):
        # Title with shadow (matching your other video)
        title = Text("Area Between Two Curves", font_size=50, weight=MEDIUM)
        title.to_edge(UP)
        title_shadow = title.copy().set_color(BLACK).set_opacity(0.25).shift(0.05*DOWN + 0.05*RIGHT)
        self.add(title_shadow, title)

        # Watermark below title
        watermark = Text("@calc4dumb", font_size=26, color=GRAY).next_to(title, DOWN).shift(DOWN*0.15)
        self.play(FadeIn(watermark, shift=UP, run_time=1.2))
        self.wait(0.5)

        # Background grid (light and faint like previous video)
        grid = NumberPlane(
            x_range=[-2, 3, 1],
            y_range=[-1, 5, 1],
            background_line_style={"stroke_color": BLUE_D, "stroke_width": 1, "stroke_opacity": 0.15},
            faded_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.1},
            x_axis_config={"stroke_opacity": 0},
            y_axis_config={"stroke_opacity": 0},
        )
        grid.to_edge(DOWN).shift(DOWN*0.5)
        self.add(grid)

        # Axes (light blue, no tips, matching style)
        axes = Axes(
            x_range=[-2, 3, 1],
            y_range=[-1, 5, 1],
            x_length=5.5,
            y_length=3,
            axis_config={"color": BLUE_D, "include_tip": False, "stroke_width": 2},
        ).to_edge(DOWN).shift(DOWN*0.5)
        self.play(Create(axes), run_time=1.5)

        # Functions
        quad_func = lambda x: x**2
        line_func = lambda x: x + 2

        quad_graph = axes.plot(quad_func, color=TEAL, stroke_width=5, x_range=[-2, 2.3])
        line_graph = axes.plot(line_func, color=ORANGE, stroke_width=5, x_range=[-2, 2.3])

        self.play(Create(quad_graph), run_time=1.5)
        self.play(Create(line_graph), run_time=1.5)

        # Labels - positioned to the right of curves, slightly outside graph
        quad_label = MathTex("y = x^2", font_size=36).set_color(TEAL)
        quad_label.next_to(axes.c2p(2.3, quad_func(2.3)), RIGHT, buff=0.3)  # right side of parabola
        quad_shadow = quad_label.copy().set_color(BLACK).set_opacity(0.3).shift(0.05*DOWN + 0.05*RIGHT)
        self.add(quad_shadow)

        line_label = MathTex("y = x+2", font_size=36).set_color(ORANGE)
        line_label.next_to(axes.c2p(2.3, line_func(2.3)), RIGHT, buff=0.3)  # right side of line
        line_shadow = line_label.copy().set_color(BLACK).set_opacity(0.3).shift(0.05*DOWN + 0.05*RIGHT)
        self.add(line_shadow)

        self.play(FadeIn(quad_label, shift=UP), FadeIn(line_label, shift=UP))
        self.wait(0.5)

        # Intersection points: x = -1 and x = 2
        x_left, x_right = -1, 2

        # Shaded area between curves
        area_between = axes.get_area(
            line_graph,
            x_range=[x_left, x_right],
            bounded_graph=quad_graph,
            color=GREEN,
            opacity=0.4
        )

        # Utility to create each math formula with shadow (consistent style)
        def make_formula(tex, scale=1.0, color=TEAL):
            m = MathTex(tex).scale(scale).set_color(color).next_to(title, DOWN).shift(DOWN*0.7)
            shadow = m.copy().set_color(BLACK).set_opacity(0.25).shift(0.05*DOWN + 0.05*RIGHT)
            return m, shadow

        # All the math steps (each morphs into the next)
        steps = [
            r"\text{Area} = \int_a^b [R(x)-r(x)]dx",
            r"\int_{-1}^{2}[(x+2)-x^2]dx",
            r"= \int_{-1}^{2}x+2\,dx - \int_{-1}^{2}x^2\,dx",
            r"= \Big[\frac{x^2}{2}+2x\Big]_{-1}^{2} - \Big[\frac{x^3}{3}\Big]_{-1}^{2}",
            r"= \Big(\frac{4}{2}+4\Big) - \Big(\frac{1}{2}-2\Big) - \Big(\frac{8}{3}-\frac{-1}{3}\Big)",
            r"= 6 - (-\frac{3}{2}) - 3",
            r"= \frac{15}{2}"
        ]

        current_formula, shadow = make_formula(steps[0])
        self.add(shadow)
        self.play(Write(current_formula), run_time=1.5)
        self.wait(1)

        self.play(FadeIn(area_between, shift=UP, run_time=1.5))

        for step in steps[1:]:
            new_formula, new_shadow = make_formula(step)
            self.play(Transform(current_formula, new_formula), Transform(shadow, new_shadow), run_time=1.5)
            self.wait(1)

        # Smaller highlight box for final answer (tight fit)
        highlight_box = SurroundingRectangle(current_formula, color=YELLOW, buff=0.15)
        self.play(Create(highlight_box), Indicate(current_formula, scale_factor=1.1, color=YELLOW, run_time=1.5))
        self.wait(2)
