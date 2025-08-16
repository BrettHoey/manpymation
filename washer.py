from manim import *
import numpy as np

class WasherMethodTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Washer Method: Volume with a Hole", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Smaller graph on bottom left
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 4, 1],
            x_length=4,
            y_length=3,
            axis_config={"color": GREY},
            tips=False,
        ).to_corner(DL)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN)
        y_label = axes.get_y_axis_label("y", edge=UP, direction=LEFT)
        
        # Two function labels
        outer_label = MathTex(r"y = \sqrt{x}", font_size=26, color=YELLOW).next_to(axes, UP, buff=0.1).align_to(axes, LEFT)
        inner_label = MathTex(r"y = 1", font_size=26, color=ORANGE).next_to(outer_label, DOWN, buff=0.1)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Write(outer_label), Write(inner_label))

        def outer_func(x):
            return np.sqrt(x)

        def inner_func(x):
            return 1

        # Plot both curves
        outer_graph = axes.plot(outer_func, x_range=[0, 3.5], color=YELLOW, stroke_width=4)
        inner_graph = axes.plot(inner_func, x_range=[0, 3.5], color=ORANGE, stroke_width=4)
        
        # Show the region between curves from x=1 to x=4
        area_between = axes.get_area(
            outer_graph, 
            x_range=[1, 3.5], 
            bounded_graph=inner_graph,
            color=GREEN, 
            opacity=0.3
        )
        
        # Add vertical lines at bounds
        line_1 = axes.get_vertical_line(axes.c2p(1, 1), color=RED, stroke_width=3)
        line_4 = axes.get_vertical_line(axes.c2p(3.5, outer_func(3.5)), color=RED, stroke_width=3)
        
        self.play(Create(outer_graph), Create(inner_graph))
        self.play(Create(line_1), Create(line_4), FadeIn(area_between))
        
        # Add rotation arrow
        rotation_arrow = CurvedArrow(
            axes.c2p(2, 2), 
            axes.c2p(2, -1.5), 
            color=GREEN, 
            stroke_width=3
        )
        rotation_label = Text("rotate around x-axis", font_size=24, color=GREEN, weight=BOLD).next_to(axes, UP, buff=0.1).shift(RIGHT * 1.5)
        
        self.play(Create(rotation_arrow), Write(rotation_label))
        self.wait(0.7)

        # Steps to show, centered below watermark/title
        steps = [
            r"V = \int_1^4 \pi [R(x)^2 - r(x)^2] \, dx",
            r"\text{Step 1: Identify outer and inner radii}",
            r"R(x) = \sqrt{x}, \quad r(x) = 1",
            r"\text{Step 2: Set up washer method}",
            r"V = \int_1^4 \pi [(\sqrt{x})^2 - 1^2] \, dx",
            r"\text{Step 3: Simplify}",
            r"V = \int_1^4 \pi (x - 1) \, dx",
            r"\text{Step 4: Factor out } \pi",
            r"V = \pi \int_1^4 (x - 1) \, dx",
            r"\text{Step 5: Integrate}",
            r"V = \pi \left[\frac{x^2}{2} - x\right]_1^4",
            r"\text{Step 6: Evaluate}",
            r"V = \pi \left[(8 - 4) - (\frac{1}{2} - 1)\right] = \frac{9\pi}{2}",
        ]

        # Create first step centered below watermark/title
        step_text = MathTex(steps[0], font_size=38, color=BLUE).next_to(watermark, DOWN, buff=1)
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

            new_step = MathTex(steps[i], font_size=38, color=new_color).next_to(watermark, DOWN, buff=1)
            self.play(Transform(step_text, new_step))
            
            # Special animations for key steps
            if i == 2:  # Show radius functions
                # Highlight both curves
                self.play(
                    outer_graph.animate.set_stroke(width=6, color=GOLD),
                    inner_graph.animate.set_stroke(width=6, color=RED),
                    run_time=0.7
                )
                self.play(
                    outer_graph.animate.set_stroke(width=4, color=YELLOW),
                    inner_graph.animate.set_stroke(width=4, color=ORANGE),
                    run_time=0.3
                )
                self.wait(1)
            elif i == 4:  # Set up washer method - show washer visualization
                # Add a sample washer
                sample_x = 2.5
                outer_radius = outer_func(sample_x)
                inner_radius = inner_func(sample_x)
                
                # Create annulus (washer shape)
                washer = Annulus(
                    inner_radius=inner_radius * 0.3, 
                    outer_radius=outer_radius * 0.3, 
                    color=PURPLE, 
                    fill_opacity=0.4
                )
                washer.move_to(axes.c2p(sample_x, 0))
                
                # Radius lines
                outer_line = Line(
                    axes.c2p(sample_x, 0), 
                    axes.c2p(sample_x, outer_radius), 
                    color=PURPLE, 
                    stroke_width=3
                )
                inner_line = Line(
                    axes.c2p(sample_x, 0), 
                    axes.c2p(sample_x, inner_radius), 
                    color=RED, 
                    stroke_width=3
                )
                
                outer_r_label = MathTex("R(x)", font_size=20, color=PURPLE).next_to(outer_line, RIGHT)
                inner_r_label = MathTex("r(x)", font_size=20, color=RED).next_to(inner_line, LEFT)
                
                self.play(
                    Create(washer), 
                    Create(outer_line), 
                    Create(inner_line),
                    Write(outer_r_label), 
                    Write(inner_r_label)
                )
                self.wait(1)
                self.play(FadeOut(washer), FadeOut(outer_line), FadeOut(inner_line), 
                         FadeOut(outer_r_label), FadeOut(inner_r_label))
            elif i == 10:  # Integration step
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
        end_text = Text("Volume = 9π/2 cubic units!", font_size=38, color=GREEN).to_edge(DOWN).shift(UP * 0.7)
        self.play(Write(end_text))
        self.wait(0.8)

        # Quick reminder of the concept
        concept_text = Text("Washer Method: π(R² - r²) × thickness", font_size=28, color=YELLOW).next_to(end_text, UP, buff=0.3)
        self.play(FadeIn(concept_text))
        self.wait(0.7)