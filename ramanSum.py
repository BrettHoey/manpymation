from manim import *
import numpy as np

class RamanujanSum(Scene):
    def construct(self):
        # Title and watermark
        title = Text("Why 1 + 2 + 3 + 4 + ... = -1/12", font_size=44, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Steps for the proof
        steps = [
            r"\text{This breaks every rule you know...}",
            r"1 + 2 + 3 + 4 + 5 + ... = ?",
            r"\text{Let's use some math magic}",
            r"S_1 = 1 - 1 + 1 - 1 + 1 - ... = \frac{1}{2}",
            r"S_2 = 1 - 2 + 3 - 4 + 5 - ... = \frac{1}{4}",
            r"\text{Now for the crazy part...}",
            r"S - S_2 = (1+2+3+...) - (1-2+3-4+...)",
            r"S - S_2 = 4 + 8 + 12 + ... = 4(1+2+3+...)",
            r"S - \frac{1}{4} = 4S",
            r"S = -\frac{1}{12}",
            r"\text{Used in string theory and quantum physics!}",
        ]

        # Step 1: The hook
        step_text = MathTex(steps[0], font_size=40, color=RED).next_to(watermark, DOWN, buff=0.8)
        self.play(Write(step_text), run_time=1.2)
        self.wait(0.8)

        # Step 2: The impossible equation
        new_step = MathTex(steps[1], font_size=44, color=BLUE).next_to(watermark, DOWN, buff=0.8)
        self.play(Transform(step_text, new_step), run_time=1.0)
        self.wait(1.0)

        # Show the sum visually growing
        sum_visual = VGroup()
        terms = ["1", "2", "3", "4", "5", "..."]
        colors = [GREEN, ORANGE, PURPLE, YELLOW, PINK, WHITE]
        
        for i, (term, color) in enumerate(zip(terms, colors)):
            if i == 0:
                term_obj = MathTex(term, font_size=36, color=color).shift(LEFT*3 + DOWN*2)
            else:
                plus = MathTex("+", font_size=32, color=WHITE)
                term_obj = MathTex(term, font_size=36, color=color)
                if i == 1:
                    group = VGroup(plus, term_obj).arrange(RIGHT, buff=0.2).next_to(sum_visual, RIGHT, buff=0.2)
                else:
                    group = VGroup(plus, term_obj).arrange(RIGHT, buff=0.2).next_to(sum_visual, RIGHT, buff=0.2)
                term_obj = group
            sum_visual.add(term_obj)
            self.play(Write(term_obj), run_time=0.3)
        
        self.wait(0.5)

        # Step 3: Math magic
        new_step = MathTex(steps[2], font_size=40, color=PURPLE).next_to(watermark, DOWN, buff=0.8)
        self.play(Transform(step_text, new_step), FadeOut(sum_visual), run_time=0.8)
        self.wait(0.5)

        # Step 4: First helper series
        new_step = MathTex(steps[3], font_size=38, color=GREEN).next_to(watermark, DOWN, buff=0.8)
        self.play(Transform(step_text, new_step), run_time=1.0)
        
        # Show the alternating series visually
        alt_series1 = MathTex("1 - 1 + 1 - 1 + 1 - 1 + ...", font_size=32, color=GREEN).next_to(step_text, DOWN, buff=0.5)
        self.play(Write(alt_series1), run_time=1.0)
        self.wait(0.8)
        
        # Clear the visual
        self.play(FadeOut(alt_series1), run_time=0.5)

        # Step 5: Second helper series
        new_step = MathTex(steps[4], font_size=38, color=ORANGE).next_to(watermark, DOWN, buff=0.8)
        self.play(Transform(step_text, new_step), run_time=1.0)
        
        # Show the second alternating series
        alt_series2 = MathTex("1 - 2 + 3 - 4 + 5 - 6 + ...", font_size=32, color=ORANGE).next_to(step_text, DOWN, buff=0.5)
        self.play(Write(alt_series2), run_time=1.0)
        self.wait(0.8)
        
        # Clear the visual
        self.play(FadeOut(alt_series2), run_time=0.5)

        # Step 6: The crazy part
        new_step = MathTex(steps[5], font_size=40, color=RED).next_to(watermark, DOWN, buff=0.8)
        self.play(Transform(step_text, new_step), run_time=0.8)
        self.wait(0.5)

        # Step 7: Subtract the series
        new_step = MathTex(steps[6], font_size=34, color=WHITE).next_to(watermark, DOWN, buff=0.8)
        self.play(Transform(step_text, new_step), run_time=1.2)
        self.wait(1.0)

        # Step 8: Show what happens
        new_step = MathTex(steps[7], font_size=34, color=YELLOW).next_to(watermark, DOWN, buff=0.8)
        self.play(Transform(step_text, new_step), run_time=1.2)
        
        # Show the subtraction visually
        subtraction_visual = VGroup(
            MathTex("(1+2+3+4+5+...)", font_size=28, color=BLUE),
            MathTex("-", font_size=28, color=WHITE),
            MathTex("(1-2+3-4+5-...)", font_size=28, color=ORANGE),
        ).arrange(RIGHT, buff=0.3).next_to(step_text, DOWN, buff=0.5)
        
        self.play(Write(subtraction_visual), run_time=1.0)
        self.wait(0.8)
        
        # Show result
        result_visual = MathTex("= 0+4+0+8+0+12+... = 4(1+2+3+...)", font_size=28, color=YELLOW).next_to(subtraction_visual, DOWN, buff=0.3)
        self.play(Write(result_visual), run_time=1.0)
        self.wait(1.0)
        
        # Clear visuals
        self.play(FadeOut(subtraction_visual), FadeOut(result_visual), run_time=0.5)

        # Step 9: The equation
        new_step = MathTex(steps[8], font_size=40, color=PURPLE).next_to(watermark, DOWN, buff=0.8)
        self.play(Transform(step_text, new_step), run_time=1.0)
        self.wait(1.0)

        # Step 10: The shocking result
        new_step = MathTex(steps[9], font_size=48, color=GOLD).next_to(watermark, DOWN, buff=0.8)
        self.play(Transform(step_text, new_step), run_time=1.5)
        
        # Add shock effect
        shock_box = SurroundingRectangle(step_text, color=GOLD, buff=0.4, stroke_width=4)
        shock_box.set_fill(GOLD, opacity=0.1)
        self.play(Create(shock_box), run_time=0.8)
        self.wait(1.2)

        # Step 11: Real physics application
        new_step = MathTex(steps[10], font_size=36, color=GREEN).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step), FadeOut(shock_box), run_time=1.0)
        
        # Show physics applications
        physics_apps = VGroup(
            Text("• String Theory", font_size=24, color=WHITE),
            Text("• Quantum Field Theory", font_size=24, color=WHITE),
            Text("• Casimir Effect", font_size=24, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(step_text, DOWN, buff=0.6)
        
        self.play(Write(physics_apps), run_time=1.5)
        self.wait(1.0)

        # Final equation display
        final_equation = MathTex("1 + 2 + 3 + 4 + ... = -\\frac{1}{12}", font_size=44, color=GOLD).next_to(physics_apps, DOWN, buff=0.8)
        self.play(Write(final_equation), run_time=1.2)

        # Final glow effect
        final_glow = SurroundingRectangle(
            VGroup(step_text, physics_apps, final_equation), 
            color=GOLD, 
            buff=0.6, 
            stroke_width=4,
            fill_opacity=0.15
        )
        final_glow.round_corners(radius=0.3)
        
        self.play(Create(final_glow), run_time=1.0)
        self.wait(1.5)