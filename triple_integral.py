from manim import *
import numpy as np

TESTING = True  # Toggle for fast render

class TripleIntegralApprox(ThreeDScene):
    def construct(self):
        # Lower the graph slightly
        graph_shift = DOWN * 0.8

        # Axes and graph
        axes = ThreeDAxes(
            x_range=[-PI, PI, PI/2],
            y_range=[-PI, PI, PI/2],
            z_range=[0, 4, 1],
            x_length=4,
            y_length=4,
            z_length=3,
        ).shift(graph_shift)
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES, zoom=0.8)
        self.add(axes)

        def func(x, y):
            return np.sin(x) * np.cos(y) + 2

        surface = Surface(
            lambda u, v: axes.c2p(u, v, func(u, v)),
            u_range=[-PI, PI],
            v_range=[-PI, PI],
            resolution=(10, 10) if TESTING else (30, 30),
            fill_opacity=0.4,
            checkerboard_colors=[BLUE_D, BLUE_E],
        ).shift(graph_shift)
        self.add(surface)

        dx = dy = PI / 4 if TESTING else PI / 6
        x_vals = np.arange(-PI, PI, dx)
        y_vals = np.arange(-PI, PI, dy)
        boxes = VGroup()

        for x in x_vals:
            for y in y_vals:
                z = func(x + dx / 2, y + dy / 2)
                cube = Cube(side_length=1).scale([dx, dy, z])
                cube.move_to(axes.c2p(x + dx / 2, y + dy / 2, z / 2))
                cube.shift(graph_shift)
                cube.set_fill(ORANGE, opacity=1.0 if TESTING else 0.6)
                cube.set_stroke(width=0 if TESTING else 0.5, color=BLACK)
                boxes.add(cube)

        # Title and watermark at top
        title = Text("Triple Integral Approximation").scale(0.7).to_edge(UP, buff=0.1)
        watermark = Text("@calc4dumb", font_size=30, color=GRAY).next_to(title, DOWN, buff=0.05)
        function_tex = MathTex(
            r"f(x,y) = \sin(x)\cos(y) + 2"
        ).scale(0.7).next_to(watermark, DOWN, buff=0.2)

        self.add_fixed_in_frame_mobjects(title, watermark, function_tex)
        self.play(Write(title), Write(watermark), Write(function_tex))

        self.play(LaggedStart(*[GrowFromCenter(box) for box in boxes], lag_ratio=0.03, run_time=4 if not TESTING else 1))
        self.wait(1)

        # Fixed-position solving steps (always readable)
        math_center = ORIGIN + DOWN * 2.8  # Bottom center of screen

        riemann_sum = MathTex(
            r"\sum_{i=1}^n \sum_{j=1}^n f(x_i^*, y_j^*) \Delta x \Delta y"
        ).scale(0.7).move_to(math_center)
        self.add_fixed_in_frame_mobjects(riemann_sum)
        self.play(Write(riemann_sum))
        self.wait(1)

        integral_tex = MathTex(
            r"\int_{-\pi}^{\pi} \int_{-\pi}^{\pi} \left(\sin(x)\cos(y)+2\right) \, dy\, dx"
        ).scale(0.7).move_to(math_center)
        self.play(Transform(riemann_sum, integral_tex))
        self.wait(1)

        step1 = MathTex(
            r"\int_{-\pi}^{\pi} \int_{-\pi}^{\pi} 2 \, dy\, dx"
        ).scale(0.7).move_to(math_center)
        self.play(FadeOut(integral_tex), FadeIn(step1))
        self.wait(1)

        step2 = MathTex(
            r"2 \cdot (2\pi) \cdot (2\pi)"
        ).scale(0.7).move_to(math_center)
        self.play(FadeOut(step1), FadeIn(step2))
        self.wait(1)

        step3 = MathTex(
            r"= 8\pi^2"
        ).scale(0.9).set_color(YELLOW).move_to(math_center)
        self.play(Transform(step2, step3))
        self.wait(2)

        # Final smooth camera movement
        self.move_camera(phi=75 * DEGREES, theta=60 * DEGREES, run_time=6)
        self.wait(2)
