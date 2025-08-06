from manim import *

class IntegrationByPartsTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Integration by Parts", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Smaller graph on bottom left
        axes = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 6, 2],
            x_length=4,
            y_length=3,
            axis_config={"color": GREY},
            tips=False,
        ).to_corner(DL)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN)
        func_label = MathTex("f(x) = xe^x", font_size=40, color=WHITE).next_to(axes, UP, buff=0.1).align_to(axes, LEFT)
        self.play(Create(axes), Write(x_label), Write(func_label))

        def func(x):
            return x * np.exp(x)

        graph = axes.plot(func, x_range=[0, 1.8], color=YELLOW)
        
        # Show area under curve from 0 to 2 with bounds
        area = axes.get_area(graph, x_range=[0, 1.5], color=YELLOW, opacity=0.3)
        
        # Add vertical lines at bounds
        line_0 = axes.get_vertical_line(axes.c2p(0, 0), color=RED)
        line_1_5 = axes.get_vertical_line(axes.c2p(1.5, func(1.5)), color=RED)
        
        self.play(Create(graph))
        self.play(Create(line_0), Create(line_1_5), FadeIn(area))

        # Steps to show, centered below watermark/title
        steps = [
            r"\int_0^{1.5} x e^x \, dx",
            r"u = x, \quad dv = e^x dx",
            r"du = dx, \quad v = e^x",
            r"\int u \, dv = uv - \int v \, du",
            r"= x \cdot e^x - \int e^x \, dx",
            r"= xe^x - e^x + C",
            r"= e^x(x - 1) \Big|_0^{1.5}",
            r"= e^{1.5}(1.5 - 1) - e^0(0 - 1)",
            r"= 0.5e^{1.5} + 1 \approx 3.24",
        ]
        
        step_labels = [
            "",
            "Step 1: Choose u and dv",
            "Step 2: Find du and v", 
            "Step 3: Apply formula",
            "Step 4: Substitute",
            "Step 5: Integrate",
            "Step 6: Apply bounds",
            "Step 7: Substitute values",
            "Step 8: Final answer"
        ]

        # Create first step centered below watermark/title
        step_text = MathTex(steps[0], font_size=48, color=BLUE).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text))
        self.wait(0.5)

        # Iterate through remaining steps, showing both label and math
        for i in range(1, len(steps)):
            new_color = GREEN if i == len(steps) - 1 else WHITE
                
            # Show the actual step
            new_step = MathTex(steps[i], font_size=48, color=new_color).next_to(watermark, DOWN, buff=1)
            
            # Show step label below the math if it exists
            if step_labels[i]:
                label = Text(step_labels[i], font_size=32, color=ORANGE).next_to(new_step, DOWN, buff=0.3)
                self.play(Transform(step_text, new_step), Write(label))
                self.wait(2)
                # Remove the label before next step
                if i < len(steps) - 1:
                    self.play(FadeOut(label))
            else:
                self.play(Transform(step_text, new_step))
                self.wait(1 if i < len(steps) - 1 else 0.5)

        # Highlight final answer with box
        box = SurroundingRectangle(step_text, color=GREEN, buff=0.3)
        self.play(Create(box))
        self.wait(0.5)

        # End text moved a bit up from bottom
        end_text = Text("Integration by parts complete!", font_size=42, color=GREEN).to_edge(DOWN).shift(UP * 0.7)
        self.play(Write(end_text))
        self.wait(1)