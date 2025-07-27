from manim import *
import numpy as np

class TripleIntegralApprox(ThreeDScene):
    def construct(self):
        # Axes and 3D graph (centered)
        axes = ThreeDAxes(
            x_range=[-PI, PI, PI/2],
            y_range=[-PI, PI, PI/2],
            z_range=[0, 4, 1],
            x_length=6,
            y_length=6,
            z_length=4,
        )
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES, zoom=0.8)
        self.add(axes)

        def func(x, y):
            return np.sin(x) * np.cos(y) + 2

        # Add surface ONCE and keep it visible throughout
        surface = Surface(
            lambda u, v: axes.c2p(u, v, func(u, v)),
            u_range=[-PI, PI],
            v_range=[-PI, PI],
            resolution=(30, 30),
            fill_opacity=0.4,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )
        self.add(surface)  # Add once

        dx, dy = PI / 6, PI / 6
        x_vals = np.arange(-PI, PI, dx)
        y_vals = np.arange(-PI, PI, dy)
        boxes = VGroup()

        for x in x_vals:
            for y in y_vals:
                z_height = func(x + dx / 2, y + dy / 2)
                box = Cube(side_length=1)
                box.scale([dx, dy, z_height])
                box.move_to(axes.c2p(x + dx / 2, y + dy / 2, z_height / 2))
                box.set_fill(ORANGE, opacity=0.6).set_stroke(BLACK, width=0.5)
                boxes.add(box)

        # Title and watermark pinned at very top (fixed frame)
        title = Text("Triple Integral Approximation").scale(0.7).to_edge(UP, buff=0.1)
        watermark = Text("@calc4dumb", font_size=30, color=GRAY).next_to(title, DOWN, buff=0.05)
        self.add_fixed_in_frame_mobjects(title, watermark)
        self.play(Write(title), Write(watermark))

        # Move series/integral slightly lower by increasing buff
        riemann_series = MathTex(
            r"\sum_{i=1}^n \sum_{j=1}^n f(x_i^*, y_j^*) \Delta x \Delta y"
        ).scale(0.7).to_edge(DOWN, buff=2.5)  # was 1.8, now 2.5

        function_tex = MathTex(
            r"f(x,y) = \sin{\left(x\right)} \cos{\left(y\right)} + 2"
        ).scale(0.7).next_to(riemann_series, DOWN, buff=0.5)

        self.add_fixed_in_frame_mobjects(riemann_series, function_tex)
        self.play(Write(riemann_series), Write(function_tex))

        # Animate boxes appearing, keep surface visible
        self.play(LaggedStart(*[GrowFromCenter(box) for box in boxes], lag_ratio=0.03, run_time=4))
        self.bring_to_front(surface)  # bring surface to front after animation
        self.wait(1)

        # Transition Riemann sum to double integral below graph
        integral_tex = MathTex(
            r"\int_{-\pi}^{\pi} \int_{-\pi}^{\pi} \left(\sin{\left(x\right)} \cos{\left(y\right)} + 2\right) dy\,dx"
        ).scale(0.7).move_to(riemann_series.get_center())

        self.play(Transform(riemann_series, integral_tex))
        self.bring_to_front(surface)
        self.wait(1)

        # Integral simplification steps (same position)
        step1 = MathTex(
            r"= \int_{-\pi}^{\pi} \int_{-\pi}^{\pi} 2 \, dy\, dx"
        ).scale(0.7).move_to(integral_tex.get_center())
        self.play(Transform(riemann_series, step1), run_time=2)
        self.bring_to_front(surface)
        self.wait(1)

        step2 = MathTex(
            r"= 2 \times (2 \pi) \times (2 \pi)"
        ).scale(0.7).move_to(integral_tex.get_center())
        self.play(Transform(riemann_series, step2), run_time=2)
        self.bring_to_front(surface)
        self.wait(1)

        step3 = MathTex(
            r"= 8 \pi^{2}"
        ).scale(0.8).set_color(YELLOW).move_to(integral_tex.get_center())
        self.play(Transform(riemann_series, step3), run_time=2)
        self.bring_to_front(surface)
        self.wait(2)

        # Final slow camera rotation around graph
        self.move_camera(phi=75 * DEGREES, theta=60 * DEGREES, run_time=6)
        self.bring_to_front(surface)
        self.wait(2)
