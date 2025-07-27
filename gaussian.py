from manim import *

class GaussianIntegral(Scene):
    def construct(self):

        # Title
        title = Text("Solving the Gaussian Integral").scale(0.8).to_edge(UP)
        self.play(Write(title))

        # Watermark (under the title, stays the whole time)
        watermark = Text("@calc4dumb", font_size=28, color=GRAY).next_to(title, DOWN)
        self.add(watermark)

        self.wait(1)

        # Step 1: Original integral
        eq1 = MathTex(r"I = \int_{-\infty}^\infty e^{-x^2} dx").scale(1.2)
        self.play(Write(eq1))
        self.wait(2)

        # Step 2: Square the integral
        eq2 = MathTex(
            r"I^2 = \left(\int_{-\infty}^\infty e^{-x^2} dx\right)^2"
        ).scale(1.1)
        self.play(Transform(eq1, eq2))
        self.wait(2)

        # Step 3: Convert to double integral
        eq3 = MathTex(
            r"I^2 = \int_{-\infty}^\infty \int_{-\infty}^\infty e^{-(x^2+y^2)} dx\,dy"
        ).scale(1)
        self.play(Transform(eq1, eq3))
        self.wait(2)

        # Step 4: Show polar substitutions
        subs = MathTex(
            r"x = r\cos\theta,\quad y = r\sin\theta"
        ).scale(0.9).next_to(eq1, DOWN, buff=1)
        self.play(FadeIn(subs, shift=DOWN))
        self.wait(2)

        # Step 5: Show the Jacobian matrix
        jacobian_matrix = MathTex(
            r"J = \begin{bmatrix}"
            r"\frac{\partial x}{\partial r} & \frac{\partial x}{\partial \theta} \\"
            r"\frac{\partial y}{\partial r} & \frac{\partial y}{\partial \theta}"
            r"\end{bmatrix}"
        ).scale(0.9).next_to(subs, DOWN)
        self.play(TransformFromCopy(subs, jacobian_matrix))
        self.wait(2)

        # Step 6: Substitute partial derivatives into the matrix
        jacobian_filled = MathTex(
            r"J = \begin{bmatrix}"
            r"\cos\theta & -r\sin\theta \\"
            r"\sin\theta & r\cos\theta"
            r"\end{bmatrix}"
        ).scale(0.9).move_to(jacobian_matrix.get_center())
        self.play(Transform(jacobian_matrix, jacobian_filled))
        self.wait(2)

        # Step 7: Show determinant step
        det_step = MathTex(
            r"\det(J) = r(\cos^2\theta + \sin^2\theta) = r"
        ).scale(0.9).next_to(jacobian_matrix, DOWN)
        self.play(FadeIn(det_step, shift=DOWN))
        self.wait(2)

        # Step 8: Final Jacobian result
        jacobian_final = MathTex(
            r"dx\,dy = |\det(J)|\,dr\,d\theta = r\,dr\,d\theta"
        ).scale(1).next_to(det_step, DOWN)
        self.play(FadeIn(jacobian_final, shift=DOWN))
        self.wait(2)

        # Fade out Jacobian derivation
        self.play(FadeOut(subs), FadeOut(jacobian_matrix), FadeOut(det_step), FadeOut(jacobian_final))

        # Step 9: Write the integral in polar coordinates
        eq4 = MathTex(
            r"I^2 = \int_0^{2\pi} \int_0^\infty e^{-r^2} r\,dr\,d\theta"
        ).scale(1)
        self.play(Transform(eq1, eq4))
        self.wait(2)

        # Step 10: Factor out theta integral
        eq5 = MathTex(
            r"I^2 = 2\pi \int_0^\infty e^{-r^2} r\,dr"
        ).scale(1)
        self.play(Transform(eq1, eq5))
        self.wait(2)

        # Step 11: Solve the radial integral
        eq6 = MathTex(
            r"I^2 = 2\pi \cdot \frac{1}{2} = \pi"
        ).scale(1)
        self.play(Transform(eq1, eq6))
        self.wait(2)

        # Step 12: Final result
        eq7 = MathTex(
            r"I = \sqrt{\pi}"
        ).scale(1.5).set_color(YELLOW)
        self.play(Transform(eq1, eq7))
        self.wait(3)
