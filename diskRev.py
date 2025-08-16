from manim import *
import numpy as np

class DiskMethodTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Disk Method: Volume of Revolution", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Smaller graph on bottom left
        axes = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 3, 1],
            x_length=4,
            y_length=3,
            axis_config={"color": GREY},
            tips=False,
        ).to_corner(DL)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN)
        y_label = axes.get_y_axis_label("y", edge=UP, direction=LEFT)
        func_label = MathTex(r"y = \sqrt{x}", font_size=30, color=WHITE).next_to(axes, UP, buff=0.3).align_to(axes, LEFT)
        
        self.play(Create(axes), Write(x_label), Write(y_label), Write(func_label))

        def func(x):
            return np.sqrt(x)

        graph = axes.plot(func, x_range=[0, 2.5], color=YELLOW, stroke_width=4)
        
        # Show the region from x=0 to x=4 (but only plot visible part)
        area = axes.get_area(graph, x_range=[0, 2.5], color=YELLOW, opacity=0.3)
        
        # Add vertical lines at bounds
        line_0 = axes.get_vertical_line(axes.c2p(0, 0), color=RED, stroke_width=3)
        line_2 = axes.get_vertical_line(axes.c2p(2, func(2)), color=RED, stroke_width=3)
        
        self.play(Create(graph))
        self.play(Create(line_0), Create(line_2), FadeIn(area))
        
        # Add rotation arrow to show revolution
        rotation_arrow = CurvedArrow(
            axes.c2p(1, func(1)), 
            axes.c2p(1, -func(1)), 
            color=GREEN, 
            stroke_width=3
        )
        rotation_label = Text("rotate around x-axis", font_size=24, color=GREEN, weight=BOLD).next_to(axes, UP, buff=0.1).shift(RIGHT * 1.5)
        
        self.play(Create(rotation_arrow), Write(rotation_label))
        self.wait(0.7)

        # Steps to show, centered below watermark/title
        steps = [
            r"V = \int_0^4 \pi [R(x)]^2 \, dx",
            r"\text{Step 1: Identify radius function}",
            r"R(x) = \sqrt{x}",
            r"\text{Step 2: Set up disk method}",
            r"V = \int_0^4 \pi (\sqrt{x})^2 \, dx",
            r"\text{Step 3: Simplify}",
            r"V = \int_0^4 \pi x \, dx",
            r"\text{Step 4: Integrate}",
            r"V = \pi \left[\frac{x^2}{2}\right]_0^4",
            r"\text{Step 5: Evaluate}",
            r"V = \pi \left(\frac{16}{2} - 0\right) = 8\pi",
        ]
        
        step_labels = [
            "",
            "",
            "Step 1: Identify radius function", 
            "",
            "Step 2: Set up disk method",
            "",
            "Step 3: Simplify",
            "",
            "Step 4: Integrate",
            "",
            "Step 5: Final answer"
        ]

        # Create first step centered below watermark/title
        step_text = MathTex(steps[0], font_size=42, color=BLUE).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text))
        self.wait(0.7)

        # Iterate through remaining steps
        for i in range(1, len(steps)):
            # Special colors for different types of steps
            if "Step" in steps[i]:
                new_color = ORANGE
            elif i == len(steps) - 1:  # Final answer
                new_color = GREEN
            else:
                new_color = WHITE

            new_step = MathTex(steps[i], font_size=42, color=new_color).next_to(watermark, DOWN, buff=1)
            self.play(Transform(step_text, new_step))
            
            # Special animations for key steps
            if i == 2:  # Show radius function
                # Highlight the curve as the radius
                self.play(graph.animate.set_stroke(width=6, color=GOLD), run_time=0.7)
                self.play(graph.animate.set_stroke(width=4, color=YELLOW), run_time=0.3)
                self.wait(1)
            elif i == 4:  # Set up disk method - show disk visualization
                # Add a sample disk
                sample_x = 1.5
                sample_radius = func(sample_x)
                disk = Circle(radius=sample_radius * 0.4, color=PURPLE, fill_opacity=0.3)
                disk.move_to(axes.c2p(sample_x, 0))
                disk_line = Line(
                    axes.c2p(sample_x, 0), 
                    axes.c2p(sample_x, sample_radius), 
                    color=PURPLE, 
                    stroke_width=3
                )
                radius_label = MathTex("R(x)", font_size=24, color=PURPLE).next_to(disk_line, RIGHT)
                
                self.play(Create(disk), Create(disk_line), Write(radius_label))
                self.wait(1)
                self.play(FadeOut(disk), FadeOut(disk_line), FadeOut(radius_label))
            elif i == 8:  # Integration step
                self.wait(1.3)
            elif i == len(steps) - 1:  # Final answer
                self.wait(1)
            else:
                self.wait(1.2)

        # Highlight final answer with animated box
        box = SurroundingRectangle(step_text, color=GREEN, buff=0.3)
        self.play(Create(box))
        self.wait(0.3)

        # End text with key insight
        end_text = Text("Volume = 8π cubic units!", font_size=42, color=GREEN).to_edge(DOWN).shift(UP * 0.7)
        self.play(Write(end_text))
        self.wait(0.8)

        # Quick reminder of the concept
        concept_text = Text("Disk Method: π × radius² × thickness", font_size=32, color=YELLOW).next_to(end_text, UP, buff=0.3)
        self.play(FadeIn(concept_text))
        self.wait(0.7)