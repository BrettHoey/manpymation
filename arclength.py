from manim import *
import numpy as np

class arcLength(Scene):
    def construct(self):
        # Title with sheen and shadow for smooth edges
        title = Text("How long is a curve, really?", font_size=50, weight=MEDIUM)
        title.to_edge(UP)
        title_shadow = title.copy().set_color(BLACK).set_opacity(0.25).shift(0.05*DOWN + 0.05*RIGHT)
        self.add(title_shadow, title)

        # Watermark below title
        watermark = Text("@calc4dumb", font_size=26, color=GRAY).next_to(title, DOWN).shift(DOWN*0.15)
        self.play(FadeIn(watermark, shift=UP, run_time=1.2))
        self.wait(1)

        # Background grid WITHOUT axes lines (hide axes using stroke_opacity=0)
        grid = NumberPlane(
            x_range=[0, 7, 1],
            y_range=[-2, 2, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.15,
            },
            faded_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.1,
            },
            x_axis_config={"stroke_opacity": 0},  # hide x-axis lines
            y_axis_config={"stroke_opacity": 0},  # hide y-axis lines
        )
        grid.to_edge(DOWN).shift(DOWN*0.5)
        self.add(grid)

        # Axes with light blue color, no tips
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[-2, 2, 1],
            x_length=5.5,
            y_length=3,
            axis_config={
                "color": BLUE_D,
                "include_tip": False,
                "stroke_width": 2,
            }
        ).to_edge(DOWN).shift(DOWN*0.5)
        self.play(Create(axes), run_time=1.5)

        # Plot curve y = sin(x)
        curve = axes.plot(lambda x: np.sin(x), color=TEAL, stroke_width=5)
        self.play(Create(curve), run_time=2)
        self.wait(0.3)

        # Curve label with shadow
        curve_label = MathTex("y = \\sin(x)", font_size=36).set_color(TEAL)
        curve_label.next_to(curve, UP, buff=0.3)
        shadow = curve_label.copy().set_color(BLACK).set_opacity(0.3).shift(0.05*DOWN + 0.05*RIGHT)
        self.add(shadow)

        self.play(FadeIn(curve_label, shift=UP))
        self.wait(0.5)

        # Highlight segment and braces
        segment = Line(
            axes.c2p(1, np.sin(1)),
            axes.c2p(1.5, np.sin(1.5)),
            color=ORANGE,
            stroke_width=4
        )
        self.play(Create(segment), run_time=1)

        dx_brace = Brace(segment, DOWN, buff=0.1, color=ORANGE)
        dx_text = dx_brace.get_tex(r"\Delta x").scale(0.8).set_color(ORANGE)

        dy_line = Line(
            axes.c2p(1, np.sin(1)),
            axes.c2p(1, np.sin(1.5)),
            color=GREEN,
            stroke_width=4
        )
        dy_brace = Brace(dy_line, LEFT, buff=0.1, color=GREEN)
        dy_text = dy_brace.get_tex(r"\Delta y").scale(0.8).set_color(GREEN)
        dy_text.shift(LEFT * 0.2)

        self.play(
            GrowFromCenter(dx_brace),
            FadeIn(dx_text, scale=1.2),
            run_time=1.3
        )
        self.play(
            Create(dy_line),
            GrowFromCenter(dy_brace),
            FadeIn(dy_text, scale=1.2),
            run_time=1.3
        )
        self.wait(1.5)

        # Delta s approx under title with subtle shadow
        delta_s_group = VGroup(
            MathTex(r"\Delta s").scale(1.0).set_color(TEAL),
            MathTex(r"\approx").scale(1.0).set_color(TEAL),
            MathTex(r"\sqrt{(\Delta x)^2 + (\Delta y)^2}").scale(1.0).set_color(TEAL)
        )
        delta_s_group.arrange(RIGHT, buff=0.25)
        delta_s_group.next_to(title, DOWN, buff=0.8)
        delta_shadow = delta_s_group.copy().set_color(BLACK).set_opacity(0.25).shift(0.05*DOWN + 0.05*RIGHT)
        self.add(delta_shadow)

        self.play(
            Write(delta_s_group),
            run_time=2
        )
        self.wait(1.5)
        self.play(FadeOut(delta_s_group, shift=UP))
        self.remove(delta_shadow)

        # Summation formula
        sum_formula = MathTex(
            r"L \approx \sum \sqrt{1 + \left(\frac{\Delta y}{\Delta x}\right)^2} \Delta x"
        ).scale(1.0).set_color(TEAL).next_to(title, DOWN).shift(DOWN*0.7)
        self.play(Write(sum_formula), run_time=2)
        self.wait(1.5)

        # Transform summation to integral
        integral_formula = MathTex(
            r"L = \int_a^b \sqrt{1 + (f'(x))^2}\,dx"
        ).scale(1.0).set_color(TEAL).next_to(title, DOWN).shift(DOWN*0.7)
        integral_shadow = integral_formula.copy().set_color(BLACK).set_opacity(0.25).shift(0.05*DOWN + 0.05*RIGHT)
        self.add(integral_shadow)

        self.play(Transform(sum_formula, integral_formula), run_time=2)
        self.wait(2)
        self.play(FadeOut(sum_formula, shift=UP))
        self.remove(integral_shadow)

        # Length applied to y = sin(x)
        apply_text = MathTex(
            r"\text{Length of } y = \sin(x) \text{ from } 0 \text{ to } 2\pi"
        ).scale(0.95).set_color(TEAL).next_to(title, DOWN).shift(DOWN*0.7)
        self.play(FadeIn(apply_text, shift=UP, run_time=1.5))
        self.wait(1.5)

        # Transform to sine integral
        sine_integral = MathTex(
            r"L = \int_0^{2\pi} \sqrt{1 + (\cos(x))^2}\,dx"
        ).scale(1.0).set_color(TEAL).next_to(title, DOWN).shift(DOWN*0.7)
        sine_shadow = sine_integral.copy().set_color(BLACK).set_opacity(0.25).shift(0.05*DOWN + 0.05*RIGHT)
        self.add(sine_shadow)

        self.play(Transform(apply_text, sine_integral), run_time=2)
        self.wait(1.5)
        self.remove(sine_shadow)

        # Numeric approx result to the right
        numeric_result = MathTex(
            r"\approx 7.64"
        ).scale(1.0).set_color(TEAL)
        numeric_result.next_to(sine_integral, RIGHT, buff=0.6)
        numeric_shadow = numeric_result.copy().set_color(BLACK).set_opacity(0.25).shift(0.05*DOWN + 0.05*RIGHT)
        self.add(numeric_shadow)

        self.play(FadeIn(numeric_result, shift=RIGHT, run_time=1.2))
        self.wait(1.5)
        self.remove(numeric_shadow)


        # Glow highlight on curve with smooth pulse
        glow_curve = curve.copy().set_color(YELLOW).set_stroke(width=8)
        self.play(Indicate(glow_curve, scale_factor=1.1, color=YELLOW, run_time=1.5))
        self.wait(1)
