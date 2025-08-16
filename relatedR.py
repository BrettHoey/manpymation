from manim import *
import numpy as np

class RelatedRatesTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Related Rates: Balloon Problem", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Create animated balloon on bottom left (moved lower)
        balloon_center = LEFT * 3 + DOWN * 2
        balloon = Circle(radius=1, color=RED, fill_opacity=0.3, stroke_width=4)
        balloon.move_to(balloon_center)
        
        # Balloon string
        string = Line(balloon_center + DOWN * 1, balloon_center + DOWN * 1.5, color=GREY_BROWN, stroke_width=3)
        
        # Air particles to show inflation
        air_particles = VGroup()
        for i in range(8):
            angle = i * PI / 4
            particle = Dot(
                balloon_center + 0.6 * np.array([np.cos(angle), np.sin(angle), 0]),
                color=BLUE,
                radius=0.05
            )
            air_particles.add(particle)
        
        self.play(Create(balloon), Create(string), Create(air_particles))
        
        # Problem statement label (moved higher with balloon lower)
        problem_label = Text("Balloon inflating at 3 cm³/s", font_size=24, color=RED, weight=BOLD).next_to(balloon, UP, buff=0.5)
        question_label = Text("How fast is radius changing?", font_size=24, color=GREEN, weight=BOLD).next_to(problem_label, DOWN, buff=0.1)
        
        self.play(Write(problem_label), Write(question_label))
        self.wait(0.7)

        # Steps to show, centered below watermark/title
        steps = [
            r"\text{Given: } \frac{dV}{dt} = 3 \text{ cm}^3\text{/s}",
            r"\text{Find: } \frac{dr}{dt} \text{ when } r = 5 \text{ cm}",
            r"V = \frac{4}{3}\pi r^3",
            r"\frac{dV}{dt} = \frac{d}{dt}\left(\frac{4}{3}\pi r^3\right)",
            r"\frac{dV}{dt} = \frac{4}{3}\pi \cdot 3r^2 \cdot \frac{dr}{dt}",
            r"3 = 4\pi r^2 \cdot \frac{dr}{dt}",
            r"\frac{dr}{dt} = \frac{3}{4\pi r^2}",
            r"\frac{dr}{dt} = \frac{3}{4\pi (5)^2} = \frac{3}{100\pi} \text{ cm/s}",
        ]

        # Create first step centered below watermark/title
        step_text = MathTex(steps[0], font_size=38, color=BLUE).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text))
        self.wait(0.7)

        # Iterate through remaining steps
        for i in range(1, len(steps)):
            # Final answer gets special color
            new_color = GREEN if i == len(steps) - 1 else WHITE

            new_step = MathTex(steps[i], font_size=38, color=new_color).next_to(watermark, DOWN, buff=1)
            self.play(Transform(step_text, new_step))
            
            # Special animations for key steps
            if i == 2:  # Volume formula - expand balloon
                self.play(
                    balloon.animate.scale(1.3),
                    air_particles.animate.scale(1.3),
                    run_time=0.8
                )
                self.play(
                    balloon.animate.scale(1/1.3),
                    air_particles.animate.scale(1/1.3),
                    run_time=0.5
                )
                self.wait(0.8)
            elif i == 3:  # Taking derivative - show chain rule concept
                # Add arrows showing the chain rule (positioned to not block text)
                chain_arrow1 = Arrow(
                    step_text.get_center() + DOWN * 0.8 + LEFT * 1,
                    step_text.get_center() + DOWN * 0.8 + RIGHT * 1,
                    color=ORANGE,
                    stroke_width=3,
                    max_tip_length_to_length_ratio=0.3
                )
                chain_label = Text("Chain Rule!", font_size=20, color=ORANGE).next_to(chain_arrow1, DOWN, buff=0.1)
                
                self.play(Create(chain_arrow1), Write(chain_label))
                self.wait(0.8)
                self.play(FadeOut(chain_arrow1), FadeOut(chain_label))
            elif i == 4:  # Chain rule result - animate differentiation
                self.wait(1.2)
            elif i == 5:  # Substitute known values
                # Highlight the substitution
                self.play(step_text.animate.set_color(YELLOW))
                self.wait(0.8)
                self.play(step_text.animate.set_color(WHITE))
            elif i == 6:  # Solve for dr/dt
                # Show solving step
                solve_arrow = Arrow(UP * 0.5, DOWN * 0.5, color=PURPLE).next_to(step_text, RIGHT)
                solve_label = Text("Solve!", font_size=18, color=PURPLE).next_to(solve_arrow, RIGHT)
                self.play(Create(solve_arrow), Write(solve_label))
                self.wait(0.8)
                self.play(FadeOut(solve_arrow), FadeOut(solve_label))
            elif i == len(steps) - 1:  # Final answer
                self.wait(1)
            else:
                self.wait(1)

        # Highlight final answer with animated box
        box = SurroundingRectangle(step_text, color=GREEN, buff=0.3)
        self.play(Create(box))
        self.wait(0.3)

        # End text with key insight
        end_text = Text("Radius growing at 3/(100π) cm/s!", font_size=36, color=GREEN).to_edge(DOWN).shift(UP * 0.7)
        self.play(Write(end_text))
        self.wait(0.8)

       