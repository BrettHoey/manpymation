from manim import *
import numpy as np

class HeartRateCalculusTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Your Fitness Tracker is Solving Calculus", font_size=46, color=RED).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Create smartwatch visual
        watch_body = RoundedRectangle(
            width=2, height=1.5, corner_radius=0.3,
            color=DARK_GREY, fill_opacity=0.8
        ).shift(LEFT * 3 + DOWN * 1.5)
        
        watch_screen = Rectangle(
            width=1.6, height=1.1, color=BLACK, fill_opacity=1
        ).move_to(watch_body.get_center())
        
        watch_band1 = Rectangle(
            width=0.3, height=1, color=DARK_GREY, fill_opacity=0.8
        ).next_to(watch_body, LEFT, buff=0)
        
        watch_band2 = Rectangle(
            width=0.3, height=1, color=DARK_GREY, fill_opacity=0.8
        ).next_to(watch_body, RIGHT, buff=0)
        
        watch = VGroup(watch_body, watch_screen, watch_band1, watch_band2)

        # Heart rate graph area
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[60, 100, 10],
            x_length=4,
            y_length=2.5,
            axis_config={"color": GREY, "stroke_width": 2},
            tips=False,
        ).shift(RIGHT * 2 + DOWN * 1.5)

        x_label = axes.get_x_axis_label("Time (sec)", edge=RIGHT, direction=DOWN)
        y_label = axes.get_y_axis_label("BPM", edge=UP, direction=LEFT)
        
        # Scale the labels to make them smaller
        x_label.scale(0.7)
        y_label.scale(0.7)

        # Generate realistic heart rate data with noise
        np.random.seed(42)
        t_values = np.linspace(0, 10, 100)
        
        # Base heart rate with realistic variation
        base_hr = 75 + 10 * np.sin(0.5 * t_values)  # Slow breathing variation
        noise = np.random.normal(0, 2, len(t_values))  # Sensor noise
        measured_hr = base_hr + noise
        
        # Clip to reasonable range
        measured_hr = np.clip(measured_hr, 65, 95)

        # Create noisy heart rate curve (what sensor actually measures)
        hr_points = [axes.c2p(t, hr) for t, hr in zip(t_values, measured_hr)]
        noisy_curve = VMobject()
        noisy_curve.set_points_smoothly(hr_points)
        noisy_curve.set_color(RED)
        noisy_curve.set_stroke(width=3)

        # Create smooth heart rate curve (what phone calculates)
        smooth_hr = base_hr  # The true underlying signal
        smooth_points = [axes.c2p(t, hr) for t, hr in zip(t_values, smooth_hr)]
        smooth_curve = VMobject()
        smooth_curve.set_points_smoothly(smooth_points)
        smooth_curve.set_color(GREEN)
        smooth_curve.set_stroke(width=4)

        self.play(Create(watch), Create(axes), Write(x_label), Write(y_label))

        # Steps to show
        steps = [
            r"\text{Your watch shows smooth heart rate...}",
            r"\text{But the sensor data is CHAOS!}",
            r"\text{Your phone solves this equation:}",
            r"\frac{dy}{dt} + \alpha y = u(t) + \epsilon(t)",
            r"\text{Where } \epsilon(t) = \text{sensor noise}",
            r"\text{Solution: } y(t) = e^{-\alpha t} \int_0^t u(s)e^{\alpha s} ds",
            r"\text{Low-pass filter + Kalman filtering}",
            r"\text{Pure differential equations!}",
        ]

        # Step 1: Show smooth result first
        step_text = MathTex(steps[0], font_size=36, color=BLUE).next_to(watermark, DOWN, buff=0.3)
        self.play(Write(step_text))
        
        # Show the smooth curve on watch screen
        mini_smooth = smooth_curve.copy().scale(0.3).move_to(watch_screen.get_center())
        mini_smooth.set_stroke(width=2)
        
        # Heart rate number display
        hr_display = Text("78", font_size=32, color=GREEN).next_to(mini_smooth, UP, buff=0.1)
        bpm_label = Text("BPM", font_size=16, color=WHITE).next_to(hr_display, RIGHT, buff=0.1)
        
        self.play(Create(mini_smooth), Write(hr_display), Write(bpm_label))
        self.play(Create(smooth_curve, run_time=2))
        self.wait(1)

        # Step 2: The big reveal - show the chaos
        new_step = MathTex(steps[1], font_size=36, color=ORANGE).next_to(watermark, DOWN, buff=0.3)
        self.play(Transform(step_text, new_step))
        
        # Show the actual noisy sensor data
        self.play(Create(noisy_curve, run_time=2))
        
        # Make the noise "jump around" to emphasize chaos
        for _ in range(3):
            self.play(noisy_curve.animate.set_stroke(width=5), run_time=0.3)
            self.play(noisy_curve.animate.set_stroke(width=3), run_time=0.2)
        
        self.wait(1)

        # Step 3: This is calculus
        new_step = MathTex(steps[2], font_size=36, color=PURPLE).next_to(watermark, DOWN, buff=0.3)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Step 4: The differential equation
        new_step = MathTex(steps[3], font_size=38, color=YELLOW).next_to(watermark, DOWN, buff=0.3)
        self.play(Transform(step_text, new_step))
        
        # Highlight the difference between noisy and smooth
        self.play(
            noisy_curve.animate.set_stroke(width=6, color=RED),
            smooth_curve.animate.set_stroke(width=6, color=GREEN)
        )
        self.wait(2)

        # Step 5: Break down the equation
        new_step = MathTex(steps[4], font_size=32, color=WHITE).next_to(watermark, DOWN, buff=0.3)
        self.play(Transform(step_text, new_step))
        
        # Show noise visually - add random dots
        noise_dots = VGroup()
        for i in range(0, len(hr_points), 5):
            dot = Dot(hr_points[i], color=RED, radius=0.03)
            noise_dots.add(dot)
        
        self.play(Create(noise_dots))
        self.wait(1)
        self.play(FadeOut(noise_dots))

        # Step 6: The solution formula
        new_step = MathTex(steps[5], font_size=38, color=PINK).next_to(watermark, DOWN, buff=0.3)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Step 7: Technical terms
        new_step = MathTex(steps[6], font_size=38, color=BLUE).next_to(watermark, DOWN, buff=0.3)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Step 8: Mind-blown finale
        new_step = MathTex(steps[7], font_size=36, color=GREEN).next_to(watermark, DOWN, buff=0.3)
        self.play(Transform(step_text, new_step))

        # Show the filtering process in real-time
        # Multiple noisy signals being processed
        for round in range(3):
            temp_signals = VGroup()
            
            # Create several noisy signals
            for i in range(5):
                temp_noise = np.random.normal(0, 3, len(t_values))
                temp_hr = base_hr + temp_noise
                temp_hr = np.clip(temp_hr, 60, 100)
                
                temp_points = [axes.c2p(t, hr) for t, hr in zip(t_values, temp_hr)]
                temp_curve = VMobject()
                temp_curve.set_points_smoothly(temp_points)
                temp_curve.set_color(RED)
                temp_curve.set_stroke(width=2)
                temp_signals.add(temp_curve)
            
            # Show noisy signals
            self.play(Create(temp_signals, run_time=0.4))
            
            # "Filter" them into smooth signal
            self.play(
                Transform(temp_signals, smooth_curve.copy().set_stroke(width=2, color=GREEN)),
                run_time=0.6
            )
            self.play(FadeOut(temp_signals, run_time=0.3))

        # Final dramatic emphasis
        self.play(
            smooth_curve.animate.set_stroke(width=8, color=GOLD),
            mini_smooth.animate.set_stroke(width=4, color=GOLD),
            hr_display.animate.set_color(GOLD)
        )

        # Final box around the answer
        box = SurroundingRectangle(step_text, color=GREEN, buff=0.3)
        self.play(Create(box))

        # Add processing indicator
        processing_text = Text("Processing: Real-time filtering", font_size=20, color=YELLOW)
        processing_text.next_to(box, DOWN, buff=0.3)
        self.play(Write(processing_text))
        
        # Make processing indicator pulse
        for _ in range(4):
            self.play(processing_text.animate.set_opacity(0.4), run_time=0.2)
            self.play(processing_text.animate.set_opacity(1), run_time=0.2)
        
        self.wait(1)