from manim import *
import numpy as np

class IntegralExplanationTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("What is that SQUIGGLY LINE in Calculus?", font_size=44, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Start with the mysterious integral symbol
        big_integral = MathTex(r"\int", font_size=120, color=RED).next_to(watermark, DOWN, buff=1)
        question_marks = VGroup(
            MathTex("?", font_size=60, color=ORANGE).next_to(big_integral, LEFT),
            MathTex("?", font_size=60, color=ORANGE).next_to(big_integral, RIGHT),
            MathTex("?", font_size=60, color=ORANGE).next_to(big_integral, UP),
        )
        
        self.play(Write(big_integral), Write(question_marks))
        self.wait(1)
        
        # Fade out the mystery
        self.play(FadeOut(big_integral), FadeOut(question_marks))

        # Create axes for the main demonstration
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 4, 1],
            x_length=4.5,
            y_length=2.5,
            axis_config={"color": GREY},
            tips=False,
        ).shift(DOWN * 1)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN)
        y_label = axes.get_y_axis_label("y", edge=UP, direction=LEFT)
        
        self.play(Create(axes), Write(x_label), Write(y_label))

        # Define a nice curve
        def func(x):
            return 0.5 * x**2 + 0.5

        curve = axes.plot(func, x_range=[0.5, 3.5], color=BLUE, stroke_width=4)
        curve_label = MathTex(r"y = f(x)", font_size=32, color=BLUE).next_to(curve, UP, buff=0.2).shift(LEFT)
        
        self.play(Create(curve), Write(curve_label))
        self.wait(0.5)

        # Explanation steps
        steps = [
            "We want to find the AREA under this curve",
            "But curves are weird... rectangles are easy!",
            "Let's use rectangles to approximate",
            "More rectangles = better approximation",
            "What if we use INFINITE rectangles?",
            r"\text{Width approaches } dx \text{ (infinitely small)}",
            r"\int_a^b f(x) \, dx = \text{Sum of infinite rectangles}",
            "The squiggly line means 'sum it up'!",
        ]

        # Step 1: We want area
        step_text = Text(steps[0], font_size=36, color=GREEN).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text))
        
        # Show the area we want
        area = axes.get_area(curve, x_range=[1, 3], color=GREEN, opacity=0.3)
        self.play(Create(area))
        self.wait(1)

        # Step 2: Rectangles are easier
        new_step = Text(steps[1], font_size=36, color=ORANGE).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1)

        # Step 3: Let's approximate
        new_step = Text(steps[2], font_size=36, color=PURPLE).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        
        # Show 4 wide rectangles
        rectangles_4 = axes.get_riemann_rectangles(curve, x_range=[1, 3], dx=0.5, color=YELLOW, fill_opacity=0.6)
        self.play(Create(rectangles_4))
        self.wait(1)

        # Step 4: More rectangles
        new_step = Text(steps[3], font_size=36, color=RED).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        
        # Replace with 8 rectangles
        rectangles_8 = axes.get_riemann_rectangles(curve, x_range=[1, 3], dx=0.25, color=ORANGE, fill_opacity=0.6)
        self.play(Transform(rectangles_4, rectangles_8))
        self.wait(1)
        
        # Replace with 16 rectangles
        rectangles_16 = axes.get_riemann_rectangles(curve, x_range=[1, 3], dx=0.125, color=RED, fill_opacity=0.6)
        self.play(Transform(rectangles_4, rectangles_16))
        self.wait(1)

        # Step 5: Infinite rectangles
        new_step = Text(steps[4], font_size=36, color=GOLD).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        
        # Show very thin rectangles
        rectangles_many = axes.get_riemann_rectangles(curve, x_range=[1, 3], dx=0.05, color=GOLD, fill_opacity=0.7)
        self.play(Transform(rectangles_4, rectangles_many))
        self.wait(1)

        # Clear the graph after showing infinite rectangles
        self.play(
            FadeOut(rectangles_4), FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
            FadeOut(curve), FadeOut(curve_label), FadeOut(area)
        )

        # Step 6: Introduce dx
        new_step = MathTex(steps[5], font_size=36, color=TEAL).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Step 7: The integral formula
        new_step = MathTex(steps[6], font_size=36, color=BLUE).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Step 8: What the symbol means
        new_step = Text(steps[7], font_size=36, color=GREEN).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        
        # Show the integral symbol morphing from a sum
        sum_symbol = MathTex(r"\sum", font_size=80, color=GREEN).next_to(step_text, DOWN, buff=0.5)
        self.play(Write(sum_symbol))
        self.wait(0.8)
        
        # Transform sum to integral
        integral_symbol = MathTex(r"\int", font_size=80, color=GREEN).move_to(sum_symbol.get_center())
        self.play(Transform(sum_symbol, integral_symbol))
        self.wait(1)

        # Highlight final answer with animated box
        final_group = VGroup(step_text, sum_symbol)
        box = SurroundingRectangle(final_group, color=GREEN, buff=0.3)
        self.play(Create(box))
        self.wait(0.3)

        # Clear everything off screen
        self.play(
            FadeOut(step_text), FadeOut(sum_symbol), FadeOut(box)
        )
        self.wait(0.5)