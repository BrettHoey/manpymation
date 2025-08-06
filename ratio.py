from manim import *

class SeriesConvergenceTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Ratio Test for Series", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Graph showing convergence visualization
        axes = Axes(
            x_range=[1, 10, 1],
            y_range=[0, 1, 0.2],
            x_length=4,
            y_length=3,
            axis_config={"color": GREY},
            tips=False,
        ).to_corner(DL)

        x_label = axes.get_x_axis_label("n", edge=RIGHT, direction=DOWN)
        y_label = axes.get_y_axis_label("a_n", edge=UP, direction=LEFT).shift(UP * 0.2)
        func_label = MathTex(r"a_n = \frac{2^n}{n!}", font_size=32, color=WHITE).next_to(axes, UP, buff=0.3).align_to(axes, LEFT)
        
        self.play(Create(axes), Write(x_label), Write(y_label), Write(func_label))

        # Plot points showing terms decreasing rapidly
        def term_func(n):
            import math
            return (2**n) / math.factorial(int(n))

        points = []
        for n in range(1, 8):
            point = Dot(axes.c2p(n, min(term_func(n), 1)), color=YELLOW, radius=0.06)
            points.append(point)
        
        self.play(*[Create(point) for point in points])

        # Steps to show, centered below watermark/title
        steps = [
            r"\sum_{n=1}^{\infty} \frac{2^n}{n!}",
            r"a_n = \frac{2^n}{n!}",
            r"L = \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right|",
            r"\frac{a_{n+1}}{a_n} = \frac{2^{n+1}}{(n+1)!} \cdot \frac{n!}{2^n}",
            r"= \frac{2^{n+1} \cdot n!}{(n+1)! \cdot 2^n}",
            r"= \frac{2 \cdot 2^n \cdot n!}{(n+1) \cdot n! \cdot 2^n}",
            r"= \frac{2}{n+1}",
            r"L = \lim_{n \to \infty} \frac{2}{n+1} = 0",
            r"\text{Since } L = 0 < 1, \text{ series converges}",
        ]
        
        step_labels = [
            "",
            "Step 1: Identify the series",
            "Step 2: Set up ratio test", 
            "Step 3: Calculate ratio",
            "Step 4: Expand factorials",
            "Step 5: Simplify powers of 2",
            "Step 6: Cancel terms",
            "Step 7: Take the limit",
            "Step 8: Apply ratio test"
        ]

        # Create first step centered below watermark/title
        step_text = MathTex(steps[0], font_size=42, color=BLUE).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text))
        self.wait(1)

        # Iterate through remaining steps with moderate timing
        for i in range(1, len(steps)):
            if i == len(steps) - 1:  # Final conclusion
                new_color = GREEN
            elif i == 7:  # Limit calculation
                new_color = PURPLE
            else:
                new_color = WHITE
                
            # Show the actual step
            new_step = MathTex(steps[i], font_size=42, color=new_color).next_to(watermark, DOWN, buff=1)
            
            # Show step label below the math if it exists
            if step_labels[i]:
                label = Text(step_labels[i], font_size=26, color=ORANGE).next_to(new_step, DOWN, buff=0.4)
                self.play(Transform(step_text, new_step), Write(label), run_time=1)
                self.wait(1.8)
                # Remove the label before next step
                if i < len(steps) - 1:
                    self.play(FadeOut(label), run_time=0.6)
            else:
                self.play(Transform(step_text, new_step), run_time=1)
                self.wait(1.8)

        # Highlight final answer with box
        box = SurroundingRectangle(step_text, color=GREEN, buff=0.3)
        self.play(Create(box), run_time=0.8)
        self.wait(1)

        # Show convergence animation on the graph
        convergence_text = Text("Terms → 0 rapidly!", font_size=28, color=GREEN).next_to(axes, RIGHT, buff=0.5)
        self.play(Write(convergence_text), run_time=1)
        
        # Animate points getting smaller
        for point in points[3:]:
            self.play(point.animate.scale(0.3), run_time=0.3)
        
        self.wait(1)

        # End text
        end_text = Text("Series converges by ratio test!", font_size=38, color=GREEN).to_edge(DOWN).shift(UP * 0.4)
        self.play(Write(end_text), run_time=1)
        self.wait(2)