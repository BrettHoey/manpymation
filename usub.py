from manim import *

class USubstitutionTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("U-Substitution Method", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Small visual on bottom left - transformation concept
        axes = Axes(
            x_range=[-2, 4, 1],
            y_range=[0, 3, 0.5],
            x_length=4.5,
            y_length=2.5,
            axis_config={"color": GREY},
            tips=False,
        ).to_corner(DL)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN)
        u_label = Text("→ u", font_size=18, color=ORANGE).next_to(x_label, RIGHT, buff=0.2)
        
        # Show a complicated curve transforming to simple curve
        complex_curve = axes.plot(lambda x: 0.5 * (x + 1)**2 * np.exp(-0.3 * x), 
                                 x_range=[-1, 3], color=RED, stroke_width=3)
        simple_curve = axes.plot(lambda x: 0.8 * x**2, 
                                x_range=[0, 2], color=GREEN, stroke_width=3)
        
        self.play(Create(axes), Write(x_label), Write(u_label))
        self.play(Create(complex_curve))
        
        # Steps to show
        steps = [
            r"\int 2x(x^2 + 1)^3 \, dx",
            r"\text{Step 1: Choose } u = x^2 + 1",
            r"\text{Step 2: Find } du = 2x \, dx",
            r"\text{Step 3: Substitute}",
            r"\int u^3 \, du",
            r"\text{Step 4: Integrate}",
            r"\frac{u^4}{4} + C",
            r"\text{Step 5: Back-substitute}",
            r"\frac{(x^2 + 1)^4}{4} + C",
        ]

        # Create first step centered below watermark/title
        step_text = MathTex(steps[0], font_size=44, color=BLUE).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text))
        self.wait(1.5)

        # Iterate through remaining steps
        for i in range(1, len(steps)):
            # Special colors for different types of steps
            if "Choose" in steps[i] or "Find" in steps[i]:
                new_color = YELLOW
            elif "Substitute" in steps[i] or "Back-substitute" in steps[i]:
                new_color = ORANGE
            elif "Integrate" in steps[i]:
                new_color = PURPLE
            elif i == len(steps) - 1:  # Final answer
                new_color = GREEN
            else:
                new_color = WHITE

            new_step = MathTex(steps[i], font_size=44, color=new_color).next_to(watermark, DOWN, buff=1)
            self.play(Transform(step_text, new_step))
            
            # Special animations for key steps
            if i == 4:  # Show the substitution transformation
                self.play(Transform(original_curve, transformed_curve), run_time=1.5)
            elif i == 7:  # Back-substitution - transform back
                self.play(Transform(original_curve, transformed_curve), run_time=1.5)
            
            # Timing adjustments
            if i == 1 or i == 2 or i == 4 or i == 7:  # Key conceptual steps
                self.wait(2)
            elif i == len(steps) - 1:  # Final answer
                self.wait(1.5)
            else:
                self.wait(1.8)

        # Highlight final answer with animated box
        box = SurroundingRectangle(step_text, color=GREEN, buff=0.3)
        self.play(Create(box))
        self.wait(0.5)

        # End text with key insight
        end_text = Text("U-sub turns complex → simple!", font_size=42, color=GREEN).to_edge(DOWN).shift(UP * 0.7)
        self.play(Write(end_text))
        self.wait(1.2)

        # Quick reminder of the strategy
        strategy_text = Text("Look for function & its derivative!", font_size=32, color=YELLOW).next_to(end_text, UP, buff=0.3)
        self.play(FadeIn(strategy_text))
        self.wait(1)