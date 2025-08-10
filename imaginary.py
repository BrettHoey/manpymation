from manim import *
import numpy as np

class ImaginaryNumbersTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Why We Need Imaginary Numbers", font_size=44, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Steps for 45-second video
        steps = [
            r"\text{'Imaginary' numbers sound fake...}",
            r"\text{But they solve REAL problems!}",
            r"x^2 = -1 \text{ has no real solution}",
            r"\text{So we invented } i = \sqrt{-1}",
            r"x^2 + 1 = 0 \text{ becomes } x = \pm i",
            r"\text{AC electricity uses imaginary numbers!}",
            r"V = V_0 e^{i\omega t}",
            r"\text{Quantum mechanics needs them too!}",
            r"\psi = ae^{i\theta}",
            r"\text{Every smartphone uses imaginary math!}",
            r"\text{They're more 'real' than real numbers!}",
        ]

        # Step 1: Hook - sound fake (0-3 seconds)
        step_text = MathTex(steps[0], font_size=40, color=ORANGE).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text), run_time=1)
        self.wait(2)

        # Step 2: But solve real problems (3-6 seconds)
        new_step = MathTex(steps[1], font_size=40, color=GREEN).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step), run_time=1)
        self.wait(2)

        # Step 3: Show the problem (6-9 seconds)
        new_step = MathTex(steps[2], font_size=40, color=RED).next_to(watermark, DOWN, buff=1)
        
        # Show smaller x-axis with no solution
        number_line = NumberLine(x_range=[-2, 2, 1], length=4, color=WHITE).shift(DOWN * 1.5)
        no_solution = Text("NO SOLUTION!", font_size=28, color=RED).shift(DOWN * 1.9)
        
        self.play(Transform(step_text, new_step), Create(number_line), Write(no_solution), run_time=1)
        self.wait(2)

        # Step 4: Invent i (9-12 seconds)
        new_step = MathTex(steps[3], font_size=40, color=PURPLE).next_to(watermark, DOWN, buff=1)
        i_point = Dot(number_line.n2p(0) + UP * 1.5, color=PURPLE, radius=0.12)
        i_label = MathTex("i", font_size=36, color=PURPLE).next_to(i_point, RIGHT)
        
        self.play(
            Transform(step_text, new_step), 
            Transform(no_solution, Text("SOLUTION FOUND!", font_size=28, color=GREEN).shift(DOWN * 1.9)),
            Create(i_point), Write(i_label),
            run_time=1
        )
        self.wait(2)

        # Step 5: Show the solution (12-15 seconds)
        new_step = MathTex(steps[4], font_size=38, color=BLUE).next_to(watermark, DOWN, buff=1)
        minus_i_point = Dot(number_line.n2p(0) + DOWN * 1.5, color=BLUE, radius=0.12)
        minus_i_label = MathTex("-i", font_size=36, color=BLUE).next_to(minus_i_point, RIGHT)
        
        self.play(
            Transform(step_text, new_step),
            Create(minus_i_point), Write(minus_i_label),
            run_time=1
        )
        self.wait(2)

        # Clear the number line visual
        self.play(
            FadeOut(number_line), FadeOut(no_solution), FadeOut(i_point), 
            FadeOut(i_label), FadeOut(minus_i_point), FadeOut(minus_i_label),
            run_time=0.5
        )

        # Step 6: AC electricity intro (15-18 seconds)
        new_step = MathTex(steps[5], font_size=40, color=YELLOW).next_to(watermark, DOWN, buff=1)
        
        # Show electrical circuit symbol
        circuit = VGroup(
            Circle(radius=0.3, color=YELLOW).shift(LEFT * 1 + DOWN * 2.5),
            Line(LEFT * 0.7, RIGHT * 0.7, color=YELLOW).shift(DOWN * 2.5),
            Text("AC", font_size=24, color=YELLOW).shift(LEFT * 1 + DOWN * 2.5)
        )
        
        self.play(Transform(step_text, new_step), Create(circuit), run_time=1)
        self.wait(2)

        # Step 7: AC voltage equation (18-21 seconds)
        new_step = MathTex(steps[6], font_size=36, color=YELLOW).next_to(watermark, DOWN, buff=1)
        
        # Show oscillating wave
        wave_axes = Axes(
            x_range=[0, 4, 1], y_range=[-1, 1, 0.5],
            x_length=3, y_length=1.5,
            axis_config={"color": GREY, "stroke_width": 1}
        ).shift(RIGHT * 1.5 + DOWN * 2.5)
        
        sine_wave = wave_axes.plot(lambda x: np.sin(2*x), color=YELLOW, stroke_width=3)
        
        self.play(
            Transform(step_text, new_step),
            Transform(circuit, VGroup(wave_axes, sine_wave)),
            run_time=1
        )
        self.wait(2)

        # Step 8: Quantum mechanics intro (21-24 seconds)
        new_step = MathTex(steps[7], font_size=40, color=TEAL).next_to(watermark, DOWN, buff=1)
        
        # Show atom symbol
        atom = VGroup(
            Circle(radius=0.4, color=TEAL).shift(DOWN * 2.5),
            Circle(radius=0.6, color=TEAL, stroke_width=2).shift(DOWN * 2.5),
            Circle(radius=0.8, color=TEAL, stroke_width=2).shift(DOWN * 2.5),
            Dot(color=TEAL, radius=0.08).shift(DOWN * 2.5)
        )
        
        self.play(Transform(step_text, new_step), Transform(circuit, atom), run_time=1)
        self.wait(2)

        # Step 9: Quantum wave function (24-27 seconds)
        new_step = MathTex(steps[8], font_size=40, color=TEAL).next_to(watermark, DOWN, buff=1)
        
        # Show complex wave
        complex_axes = Axes(
            x_range=[0, 4, 1], y_range=[-1, 1, 0.5],
            x_length=3, y_length=1.5,
            axis_config={"color": GREY, "stroke_width": 1}
        ).shift(DOWN * 2.5)
        
        complex_wave = complex_axes.plot(lambda x: np.cos(3*x) * np.exp(-x/4), color=TEAL, stroke_width=3)
        
        self.play(
            Transform(step_text, new_step),
            Transform(circuit, VGroup(complex_axes, complex_wave)),
            run_time=1
        )
        self.wait(2)

        # Clear visual
        self.play(FadeOut(circuit), run_time=0.5)

        # Step 10: Smartphone connection (27-32 seconds)
        new_step = MathTex(steps[9], font_size=38, color=GOLD).next_to(watermark, DOWN, buff=1)
        
        # Show smartphone with signal waves
        phone = VGroup(
            RoundedRectangle(width=1, height=1.6, corner_radius=0.1, color=WHITE, fill_opacity=0.2),
            Text("📱", font_size=40)
        ).shift(LEFT * 2 + DOWN * 2.5)
        
        # Signal waves
        signals = VGroup()
        for i in range(3):
            arc = Arc(radius=0.5 + i*0.3, angle=PI/2, color=GOLD, stroke_width=2)
            arc.move_to(phone.get_center() + RIGHT * 0.5)
            signals.add(arc)
        
        apps_text = Text("WiFi • GPS • Bluetooth", font_size=24, color=GOLD).shift(RIGHT * 1.5 + DOWN * 2.2)
        
        self.play(
            Transform(step_text, new_step),
            Create(phone), Create(signals), Write(apps_text),
            run_time=1
        )
        self.wait(2.3)

        # Clear smartphone visual
        self.play(FadeOut(phone), FadeOut(signals), FadeOut(apps_text), run_time=0.5)

        # Step 11: Mind-blowing finale (32-37 seconds)
        new_step = MathTex(steps[10], font_size=38, color=PURPLE).next_to(watermark, DOWN, buff=1)
        
        # Create emphasis box
        final_box = SurroundingRectangle(step_text, color=PURPLE, buff=0.3)
        
        self.play(Transform(step_text, new_step), Create(final_box), run_time=1)
        self.wait(1)

        # Final emphasis
        self.play(final_box.animate.set_stroke(width=6))
        self.wait(1)