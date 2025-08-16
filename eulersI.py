from manim import *
import numpy as np

class EulersIdentity(Scene):
    def construct(self):
        # Title and watermark
        title = Text("The Most Beautiful Equation Ever", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Steps - adjusted for visual demo
        steps = [
            r"e^{i\pi} + 1 = 0",
            r"\text{But what does } e^{i\theta} \text{ actually do?}",
            r"\text{It rotates around a circle!}",
            r"\text{When } \theta = \pi \text{, we get...}",
            r"e^{i\pi} = -1",
            r"\text{So } e^{i\pi} + 1 = 0",
            r"\text{The most beautiful equation!}",
        ]

        # Step 1: Show the equation immediately
        step_text = MathTex(steps[0], font_size=52, color=GOLD).next_to(watermark, DOWN, buff=0.8)
        self.play(Write(step_text), run_time=1.2)
        self.wait(0.8)

        # Step 2: What does it mean?
        new_step = MathTex(steps[1], font_size=36, color=ORANGE).next_to(watermark, DOWN, buff=0.8)
        self.play(Transform(step_text, new_step), run_time=1.0)
        self.wait(0.5)

        # Create unit circle visualization
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=4,
            y_length=4,
            axis_config={"color": DARK_GREY, "stroke_width": 2},
            tips=False,
        ).shift(DOWN * 1.5)

        # Unit circle
        unit_circle = Circle(radius=2, color=WHITE, stroke_width=3).move_to(axes.get_origin())
        
        # Add labels
        real_label = MathTex("\\text{Real}", font_size=20, color=WHITE).next_to(axes.get_x_axis(), RIGHT)
        imag_label = MathTex("\\text{Imaginary}", font_size=20, color=WHITE).next_to(axes.get_y_axis(), UP)
        
        self.play(Create(axes), Create(unit_circle), Write(real_label), Write(imag_label), run_time=1.0)

        # Step 3: It rotates!
        new_step = MathTex(steps[2], font_size=36, color=GREEN).next_to(watermark, DOWN, buff=0.8)
        self.play(Transform(step_text, new_step), run_time=0.8)

        # Show rotation animation
        # Start at (1,0) - which is e^(i*0)
        rotating_dot = Dot(axes.c2p(1, 0), color=YELLOW, radius=0.12)
        radius_line = Line(axes.get_origin(), axes.c2p(1, 0), color=YELLOW, stroke_width=3)
        
        # Angle arc
        angle_arc = Arc(
            radius=0.5,
            start_angle=0,
            angle=0.1,  # Start with small angle so it's visible
            color=PURPLE,
            stroke_width=3
        ).move_to(axes.get_origin())
        
        # Angle label
        theta_label = MathTex("\\theta", font_size=28, color=PURPLE).move_to(axes.c2p(0.7, 0.3))
        
        self.play(Create(rotating_dot), Create(radius_line), Create(angle_arc), Write(theta_label), run_time=0.8)

        # Animate rotation from 0 to π
        def update_dot(mob, alpha):
            angle = alpha * PI
            new_pos = axes.c2p(np.cos(angle), np.sin(angle))
            mob.move_to(new_pos)
            
        def update_line(mob, alpha):
            angle = alpha * PI
            new_end = axes.c2p(np.cos(angle), np.sin(angle))
            mob.put_start_and_end_on(axes.get_origin(), new_end)
            
        def update_arc(mob, alpha):
            angle = alpha * PI
            new_arc = Arc(
                radius=0.5,
                start_angle=0,
                angle=angle,
                color=PURPLE,
                stroke_width=3
            ).move_to(axes.get_origin())
            mob.become(new_arc)

        # Create updater functions and animate
        rotating_dot.add_updater(lambda m, dt: None)  # Clear any existing updaters
        radius_line.add_updater(lambda m, dt: None)
        angle_arc.add_updater(lambda m, dt: None)
        
        self.play(
            rotating_dot.animate.move_to(axes.c2p(-1, 0)),
            Transform(
                radius_line, 
                Line(axes.get_origin(), axes.c2p(-1, 0), color=YELLOW, stroke_width=3)
            ),
            Transform(
                angle_arc,
                Arc(radius=0.5, start_angle=0, angle=PI, color=PURPLE, stroke_width=3).move_to(axes.get_origin())
            ),
            run_time=2.5,
            rate_func=smooth
        )

        # Step 4: When theta = π
        new_step = MathTex(steps[3], font_size=36, color=RED).next_to(watermark, DOWN, buff=0.8)
        self.play(Transform(step_text, new_step), run_time=0.8)
        
        # Highlight that we're at (-1, 0)
        pi_label = MathTex("\\pi", font_size=32, color=RED).move_to(axes.c2p(-0.7, 0.3))
        self.play(Transform(theta_label, pi_label), run_time=0.5)
        
        # Show coordinates
        coords_label = MathTex("(-1, 0)", font_size=28, color=YELLOW).next_to(rotating_dot, LEFT, buff=0.3)
        self.play(Write(coords_label), run_time=0.6)
        self.wait(0.5)

        # Step 5: e^(iπ) = -1
        new_step = MathTex(steps[4], font_size=44, color=PURPLE).next_to(watermark, DOWN, buff=0.8)
        self.play(Transform(step_text, new_step), run_time=1.0)
        self.wait(0.8)

        # Clear the circle visualization - theta_label is the one on screen after transform
        circle_group = VGroup(axes, unit_circle, real_label, imag_label, rotating_dot, 
                            radius_line, angle_arc, theta_label, coords_label)
        self.play(FadeOut(circle_group), run_time=0.8)

        # Step 6: So the equation works!
        new_step = MathTex(steps[5], font_size=44, color=GREEN).next_to(watermark, DOWN, buff=0.8)
        self.play(Transform(step_text, new_step), run_time=1.0)
        self.wait(0.8)

        # Step 7: Final beautiful equation
        new_step = MathTex(steps[6], font_size=40, color=GOLD).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step), run_time=0.8)

        # Show the final equation one more time, bigger
        final_equation = MathTex("e^{i\\pi} + 1 = 0", font_size=56, color=GOLD).next_to(step_text, DOWN, buff=0.8)
        self.play(Write(final_equation), run_time=1.5)

        # Final glow effect
        final_glow = SurroundingRectangle(
            VGroup(step_text, final_equation), 
            color=GOLD, 
            buff=0.5, 
            stroke_width=4,
            fill_opacity=0.15
        )
        final_glow.round_corners(radius=0.3)
        
        self.play(Create(final_glow), run_time=1.0)
        self.wait(1.0)