from manim import *

class ChainRuleTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Chain Rule", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Smaller graph on bottom left
        axes = Axes(
            x_range=[-1, 1, 0.5],
            y_range=[-1, 8, 2],
            x_length=4,
            y_length=2.5,
            axis_config={"color": GREY},
            tips=False,
        ).to_corner(DL)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN)
        y_label = Text("f(x) = (2x+1)³", font_size=30, color=WHITE).next_to(axes, UP, buff=0.1).align_to(axes, LEFT)
        self.play(Create(axes), Write(x_label), Write(y_label))

        def func(x):
            return (2*x + 1)**3

        graph = axes.plot(func, x_range=[-0.8, 0.8], color=YELLOW)
        
        self.play(Create(graph))

        # Steps to show, centered below watermark/title
        steps = [
            r"f(x) = (2x + 1)^3",
            r"\text{Outer: } u^3, \text{ Inner: } u = 2x + 1",
            r"f'(u) = 3u^2, \quad u'(x) = 2",
            r"f'(x) = f'(u) \cdot u'(x)",
            r"= 3u^2 \cdot 2 = 6u^2",
            r"f'(x) = 6(2x + 1)^2",
        ]
        
        step_labels = [
            "",
            "Step 1: Identify functions",
            "Step 2: Find derivatives", 
            "Step 3: Apply chain rule",
            "Step 4: Simplify",
            "Step 5: Substitute back"
        ]

        # Create first step centered below watermark/title
        step_text = MathTex(steps[0], font_size=48, color=BLUE).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text))
        self.wait(1)

        # Iterate through remaining steps, showing both label and math
        for i in range(1, len(steps)):
            new_color = GREEN if i == len(steps) - 1 else WHITE
                
            # Show the actual step
            new_step = MathTex(steps[i], font_size=48, color=new_color).next_to(watermark, DOWN, buff=1)
            
            # Show step label below the math if it exists
            if step_labels[i]:
                label = Text(step_labels[i], font_size=32, color=ORANGE).next_to(new_step, DOWN, buff=0.3)
                self.play(Transform(step_text, new_step), Write(label))
                self.wait(1)
                # Remove the label before next step
                if i < len(steps) - 1:
                    self.play(FadeOut(label))
            else:
                self.play(Transform(step_text, new_step))
                self.wait(1.4 if i < len(steps) - 1 else 1)

        # Highlight final answer with box
        box = SurroundingRectangle(step_text, color=GREEN, buff=0.3)
        self.play(Create(box))
        self.wait(0.5)

        # End text moved a bit up from bottom
        end_text = Text("Chain rule complete!", font_size=42, color=GREEN).to_edge(DOWN).shift(UP * 0.7)
        self.play(Write(end_text))
        self.wait(1)