from manim import *

class DoubleIntegralTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Double Integral", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Regular 2D graph on bottom left showing the region
        axes = Axes(
            x_range=[0, 2.5, 1],
            y_range=[0, 1.5, 0.5],
            x_length=4,
            y_length=3,
            axis_config={"color": GREY},
            tips=False,
        ).to_corner(DL)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN)
        y_label = axes.get_y_axis_label("y", edge=UP, direction=LEFT)
        func_label = MathTex(r"f(x,y) = xy", font_size=30, color=WHITE).next_to(axes, UP, buff=0.3).align_to(axes, LEFT)
        
        self.play(Create(axes), Write(x_label), Write(y_label), Write(func_label))

        # Show the region of integration as a rectangle
        region = Rectangle(
            width=axes.x_axis.unit_size * 2,  # x from 0 to 2
            height=axes.y_axis.unit_size * 1,  # y from 0 to 1
            color=YELLOW,
            fill_opacity=0.3,
            stroke_width=3
        ).move_to(axes.c2p(1, 0.5, 0))
        
        # Add boundary lines
        region_label = Text("R", font_size=24, color=YELLOW).move_to(axes.c2p(1, 0.5, 0))
        
        self.play(Create(region), Write(region_label))

        # Steps to show, centered below watermark/title
        steps = [
            r"\iint_R xy \, dA",
            r"R: 0 \leq x \leq 2, \, 0 \leq y \leq 1",
            r"\int_0^2 \int_0^1 xy \, dy \, dx",
            r"\int_0^2 x \left[\frac{y^2}{2}\right]_0^1 dx",
            r"\int_0^2 x \cdot \frac{1}{2} \, dx",
            r"\frac{1}{2} \int_0^2 x \, dx",
            r"\frac{1}{2} \left[\frac{x^2}{2}\right]_0^2 = 1",
        ]
        
        step_labels = [
            "",
            "Step 1: Define region R",
            "Step 2: Set up iterated integral", 
            "Step 3: Integrate with respect to y",
            "Step 4: Evaluate y bounds",
            "Step 5: Factor out constant",
            "Step 6: Final integration"
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
        end_text = Text("Volume = 1!", font_size=36, color=GREEN).to_edge(DOWN).shift(UP * 0.4)
        self.play(Write(end_text), run_time=0.8)
        self.wait(1)