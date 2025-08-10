from manim import *
import numpy as np

class Determinant2x2Proof(Scene):
    def construct(self):
        # Title and watermark
        title = Text("The Determinant is Just Area!", font_size=42, color=BLUE).to_edge(UP, buff=0.2)
        watermark = Text("@calc4dumb", font_size=20, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Create coordinate system - centered but shifted right slightly
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 4, 1],
            x_length=5,
            y_length=3.5,
            axis_config={"color": GREY, "stroke_width": 2},
            tips=True,
        ).shift(RIGHT * 1.5 + DOWN * 0.8)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN)
        y_label = axes.get_y_axis_label("y", edge=UP, direction=LEFT)
        self.play(Create(axes), Write(x_label), Write(y_label))

        # Define two vectors
        vector_a = [3, 1]  # First column of matrix
        vector_b = [1, 2]  # Second column of matrix

        # Show the matrix first - positioned on left, visible
        matrix_text = MathTex(
            r"A = \begin{bmatrix} 3 & 1 \\ 1 & 2 \end{bmatrix}",
            font_size=36,
            color=WHITE
        ).to_edge(LEFT, buff=0.5).shift(UP * 1.5)
        
        self.play(Write(matrix_text))
        self.wait(1)

        # Draw vectors
        vec_a = Arrow(
            axes.c2p(0, 0), 
            axes.c2p(vector_a[0], vector_a[1]), 
            color=RED, 
            stroke_width=6,
            buff=0
        )
        vec_b = Arrow(
            axes.c2p(0, 0), 
            axes.c2p(vector_b[0], vector_b[1]), 
            color=BLUE, 
            stroke_width=6,
            buff=0
        )
        
        # Vector labels next to matrix
        vec_labels = MathTex(
            r"\vec{a} = \begin{bmatrix} 3 \\ 1 \end{bmatrix}, \quad \vec{b} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}",
            font_size=28, 
            color=WHITE
        ).next_to(matrix_text, DOWN, buff=0.3)
        
        self.play(Create(vec_a), Create(vec_b), Write(vec_labels))
        self.wait(1)

        # Form parallelogram by completing the vectors
        vec_a_translated = Arrow(
            axes.c2p(vector_b[0], vector_b[1]), 
            axes.c2p(vector_a[0] + vector_b[0], vector_a[1] + vector_b[1]), 
            color=RED, 
            stroke_width=4,
            stroke_opacity=0.7,
            buff=0
        )

        vec_b_translated = Arrow(
            axes.c2p(vector_a[0], vector_a[1]), 
            axes.c2p(vector_a[0] + vector_b[0], vector_a[1] + vector_b[1]), 
            color=BLUE, 
            stroke_width=4,
            stroke_opacity=0.7,
            buff=0
        )

        step1_text = Text("1. Form parallelogram", font_size=26, color=GREEN).next_to(vec_labels, DOWN, buff=0.4)
        self.play(Write(step1_text))
        
        self.play(Create(vec_a_translated), Create(vec_b_translated))

        # Fill the parallelogram
        parallelogram_points = [
            axes.c2p(0, 0),
            axes.c2p(vector_a[0], vector_a[1]),
            axes.c2p(vector_a[0] + vector_b[0], vector_a[1] + vector_b[1]),
            axes.c2p(vector_b[0], vector_b[1])
        ]
        
        parallelogram = Polygon(*parallelogram_points, color=YELLOW, fill_opacity=0.3, stroke_width=2, stroke_color=YELLOW)
        self.play(FadeIn(parallelogram))
        self.wait(1)

        # Method: Use the shear transformation approach instead
        step2_text = Text("2. Use base × height method", font_size=26, color=ORANGE).next_to(step1_text, DOWN, buff=0.3)
        self.play(Write(step2_text))

        # Show base vector and its length
        base_line = Line(axes.c2p(0, 0), axes.c2p(vector_a[0], vector_a[1]), color=RED, stroke_width=6)
        base_length = np.sqrt(vector_a[0]**2 + vector_a[1]**2)
        
        # Show height as perpendicular distance from vector b to line containing vector a
        # Height = |det(a,b)| / |a|
        height_value = abs(vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]) / base_length
        
        # Project vector b onto vector a
        proj_scalar = (vector_a[0] * vector_b[0] + vector_a[1] * vector_b[1]) / (vector_a[0]**2 + vector_a[1]**2)
        proj_point = [proj_scalar * vector_a[0], proj_scalar * vector_a[1]]
        
        # Draw height line (perpendicular from b to line a)
        height_line = DashedLine(
            axes.c2p(vector_b[0], vector_b[1]),
            axes.c2p(proj_point[0], proj_point[1]),
            color=GREEN,
            stroke_width=4
        )
        
        base_text = MathTex(f"\\text{{base}} = \\sqrt{{10}}", font_size=24, color=RED).next_to(step2_text, DOWN, buff=0.3)
        height_text = MathTex(f"\\text{{height}} = \\frac{{5}}{{\\sqrt{{10}}}}", font_size=24, color=GREEN).next_to(base_text, DOWN, buff=0.2)
        
        self.play(Create(height_line), Write(base_text), Write(height_text))
        self.wait(1)

        # Simplify to direct formula
        step3_text = Text("3. OR use direct formula!", font_size=26, color=PURPLE).next_to(height_text, DOWN, buff=0.4)
        self.play(Write(step3_text))

        # Show the direct determinant calculation
        det_calc = MathTex(
            r"\text{Area} = |ad - bc|",
            font_size=28,
            color=PURPLE
        ).next_to(step3_text, DOWN, buff=0.3)
        self.play(Write(det_calc))

        # Substitute values
        det_substitute = MathTex(
            r"= |3 \times 2 - 1 \times 1|",
            font_size=28,
            color=PURPLE
        ).next_to(det_calc, DOWN, buff=0.2)
        self.play(Write(det_substitute))

        # Final result
        det_result = MathTex(
            r"= |6 - 1| = 5",
            font_size=28,
            color=PURPLE
        ).next_to(det_substitute, DOWN, buff=0.2)
        self.play(Write(det_result))
        self.wait(1)

        # Clear the height construction
        self.play(FadeOut(height_line), FadeOut(base_text), FadeOut(height_text))

        # Show determinant formula
        det_formula = MathTex(
            r"\det\begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc",
            font_size=30,
            color=GREEN
        ).next_to(det_result, DOWN, buff=0.4)
        self.play(Write(det_formula))
        self.wait(1)

        # The revelation
        revelation = Text("Determinant = Parallelogram Area!", font_size=30, color=GOLD).to_edge(DOWN, buff=0.3)
        self.play(Write(revelation))
        
        # Final highlight - show why determinant can be negative
        sign_note = Text("(Sign shows orientation!)", font_size=24, color=ORANGE).next_to(revelation, UP, buff=0.2)
        self.play(Write(sign_note))
        
        # Final highlight
        self.play(
            parallelogram.animate.set_fill(opacity=0.6).set_color(GOLD),
            Indicate(parallelogram, scale_factor=1.1, color=GOLD)
        )
        
        # Box around the key result
        key_group = VGroup(det_formula)
        final_box = SurroundingRectangle(key_group, color=GOLD, buff=0.2)
        self.play(Create(final_box))
        self.wait(2)