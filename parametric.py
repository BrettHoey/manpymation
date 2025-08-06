from manim import *

class ParametricArcLengthTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Parametric Arc Length", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Small visual on bottom left - parametric curve
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=4,
            y_length=2.5,
            axis_config={"color": GREY},
            tips=False,
        ).to_corner(DL, buff=0.8)

        # Create a parametric curve (circle): x = 2cos(t), y = 2sin(t)
        def param_curve(t):
            x = 2 * np.cos(t)
            y = 1.5 * np.sin(t)
            return axes.c2p(x, y)
        
        curve = ParametricFunction(
            param_curve,
            t_range=[0, 2*PI],
            color=YELLOW,
            stroke_width=4
        )
        
        # Add parameter point that moves along curve
        dot = Dot(color=RED, radius=0.08).move_to(param_curve(0))
        
        # Add parameter labels
        param_label = MathTex("t", font_size=30, color=RED).next_to(dot, UR, buff=0.1)
        curve_label = Text("x = 2cos(t), y = 1.5sin(t)", font_size=26, color=YELLOW).next_to(axes, DOWN, buff=0.2)
        
        self.play(Create(axes))
        self.play(Create(curve), Write(curve_label))
        self.play(FadeIn(dot), Write(param_label))
        
        # Steps to show
        steps = [
            r"\text{Find arc length from } t = 0 \text{ to } t = \pi",
            r"\text{Formula: } L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt",
            r"\text{Step 1: Find derivatives}",
            r"\frac{dx}{dt} = -2\sin(t), \quad \frac{dy}{dt} = 1.5\cos(t)",
            r"\text{Step 2: Square and add}",
            r"\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 = 4\sin^2(t) + 2.25\cos^2(t)",
            r"\text{Step 3: Set up integral}",
            r"L = \int_0^\pi \sqrt{4\sin^2(t) + 2.25\cos^2(t)} \, dt",
            r"\text{Result: } L \approx 6.28 \text{ units}",
        ]

        # Create first step
        step_text = MathTex(steps[0], font_size=38, color=BLUE).next_to(watermark, DOWN, buff=0.8)
        self.play(Write(step_text))
        self.wait(1)

        # Animate dot moving along curve during first step
        self.play(MoveAlongPath(dot, curve), MoveAlongPath(param_label, curve), 
                 rate_func=linear, run_time=2)

        # Iterate through remaining steps
        for i in range(1, len(steps)):
            # Color coding for different step types
            if "Formula" in steps[i]:
                new_color = PURPLE
            elif "derivatives" in steps[i] or "Square and add" in steps[i]:
                new_color = YELLOW
            elif "integral" in steps[i]:
                new_color = ORANGE
            elif "Result" in steps[i]:
                new_color = GREEN
            else:
                new_color = WHITE

            new_step = MathTex(steps[i], font_size=38, color=new_color).next_to(watermark, DOWN, buff=0.8)
            self.play(Transform(step_text, new_step))
            
            # Special animations for key steps
            if i == 1:  # Show the general formula
                # Highlight the curve briefly
                self.play(curve.animate.set_stroke(width=6), run_time=0.5)
                self.play(curve.animate.set_stroke(width=4), run_time=0.5)
                self.wait(1)
            elif i == 3:  # Show derivatives step
                # Move dot to show dx/dt and dy/dt concept
                self.play(dot.animate.move_to(param_curve(PI/4)), 
                         param_label.animate.move_to(param_curve(PI/4) + 0.2*UP + 0.2*RIGHT))
                self.wait(0.5)
            elif i == 7:  # Setup integral - show the arc we're measuring
                # Create arc from t=0 to t=π (half the ellipse)
                half_curve = ParametricFunction(
                    param_curve,
                    t_range=[0, PI],
                    color=RED,
                    stroke_width=6
                )
                self.play(Create(half_curve))
                self.wait(1)
            elif i == len(steps) - 1:  # Final result
                self.wait(0.6)
            else:
                self.wait(1)

        # Highlight final answer
        box = SurroundingRectangle(step_text, color=GREEN, buff=0.3)
        self.play(Create(box))
        self.wait(0.5)

        # End text with key insight
        end_text = Text("Arc length = distance along curve!", font_size=32, color=GREEN).to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(end_text))
        self.wait(0.5)

        # Key formula reminder
        formula_reminder = MathTex(r"L = \int \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt", 
                                 font_size=28, color=PURPLE).next_to(end_text, UP, buff=0.2)
        self.play(FadeIn(formula_reminder))
        self.wait(1)