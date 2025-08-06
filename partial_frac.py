from manim import *

class PartialFractionsTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Partial Fractions", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Smaller graph on bottom left
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-2, 6, 2],
            x_length=4,
            y_length=3,
            axis_config={"color": GREY},
            tips=False,
        ).to_corner(DL)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN)
        func_label = MathTex(r"f(x) = \frac{2x+1}{x^2-1}", font_size=30, color=WHITE).next_to(axes, UP, buff=0.8).align_to(axes, LEFT)
        self.play(Create(axes), Write(x_label), Write(func_label))

        def func(x):
            if abs(x - 1) < 0.1 or abs(x + 1) < 0.1:
                return 0
            return (2*x + 1) / (x**2 - 1)

        # Plot with discontinuities at x = ±1
        graph1 = axes.plot(func, x_range=[-0.8, 0.8], color=YELLOW)
        graph2 = axes.plot(func, x_range=[1.2, 3.5], color=YELLOW)
        
        # Add vertical asymptotes
        asymptote1 = DashedLine(axes.c2p(-1, -2), axes.c2p(-1, 6), color=RED, stroke_width=2)
        asymptote2 = DashedLine(axes.c2p(1, -2), axes.c2p(1, 6), color=RED, stroke_width=2)
        
        self.play(Create(graph1), Create(graph2), Create(asymptote1), Create(asymptote2))

        # Steps to show, centered below watermark/title
        steps = [
            r"\int \frac{2x+1}{x^2-1} dx",
            r"\frac{2x+1}{(x-1)(x+1)} = \frac{A}{x-1} + \frac{B}{x+1}",
            r"2x+1 = A(x+1) + B(x-1)",
            r"x=1: 3 = 2A \Rightarrow A = \frac{3}{2}",
            r"x=-1: -1 = -2B \Rightarrow B = \frac{1}{2}",
            r"\int \left(\frac{3/2}{x-1} + \frac{1/2}{x+1}\right) dx",
            r"= \frac{3}{2}\ln|x-1| + \frac{1}{2}\ln|x+1| + C",
        ]
        
        step_labels = [
            "",
            "Step 1: Set up partial fractions",
            "Step 2: Clear denominators", 
            "Step 3: Solve for A",
            "Step 4: Solve for B",
            "Step 5: Integrate each term",
            "Step 6: Final answer"
        ]

        # Create first step centered below watermark/title
        step_text = MathTex(steps[0], font_size=40, color=BLUE).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text))
        self.wait(0.8)

        # Iterate through remaining steps with faster timing
        for i in range(1, len(steps)):
            new_color = GREEN if i == len(steps) - 1 else WHITE
                
            # Show the actual step
            new_step = MathTex(steps[i], font_size=40, color=new_color).next_to(watermark, DOWN, buff=1)
            
            # Show step label below the math if it exists
            if step_labels[i]:
                label = Text(step_labels[i], font_size=24, color=ORANGE).next_to(new_step, DOWN, buff=0.4)
                self.play(Transform(step_text, new_step), Write(label), run_time=0.8)
                self.wait(1.2)
                # Remove the label before next step
                if i < len(steps) - 1:
                    self.play(FadeOut(label), run_time=0.5)
            else:
                self.play(Transform(step_text, new_step), run_time=0.8)
                self.wait(1.2)

        # Highlight final answer with box
        box = SurroundingRectangle(step_text, color=GREEN, buff=0.3)
        self.play(Create(box), run_time=0.6)
        self.wait(0.5)

        # End text moved a bit up from bottom
        end_text = Text("Partial fractions solved!", font_size=36, color=GREEN).to_edge(DOWN).shift(UP * 0.4)
        self.play(Write(end_text), run_time=0.8)
        self.wait(1)