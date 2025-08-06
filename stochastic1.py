from manim import *
import numpy as np
import random

class StochasticCalculusTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Why dt ≠ 0 in Finance (Mind = Blown)", font_size=44, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Steps to show
        steps = [
            r"\text{In regular calculus: } dt \to 0",
            r"\text{But in finance math...}",
            r"dt \text{ actually MATTERS!}",
            r"\text{Meet: Stochastic Calculus}",
            r"(dW)^2 = dt \text{ (What?!)}",
            r"\text{Itô's Lemma: } df = \frac{\partial f}{\partial t}dt + \frac{\partial f}{\partial S}dS + \frac{1}{2}\frac{\partial^2 f}{\partial S^2}(dS)^2",
            r"\text{That extra term changes EVERYTHING}",
            r"\text{Your Black-Scholes comes from this!}",
        ]

        # Create animated comparison of regular vs stochastic functions
        axes_regular = Axes(
            x_range=[0, 4, 1],
            y_range=[-1, 3, 1],
            x_length=4,
            y_length=2.8,
            axis_config={"color": DARK_GREY, "font_size": 18, "stroke_width": 2},
        ).shift(LEFT * 3.2 + DOWN * 1.8)

        axes_stochastic = Axes(
            x_range=[0, 4, 1],
            y_range=[-1, 3, 1],
            x_length=4,
            y_length=2.8,
            axis_config={"color": DARK_GREY, "font_size": 18, "stroke_width": 2},
        ).shift(RIGHT * 3.2 + DOWN * 1.8)

        # Labels for the axes with better styling
        regular_label = Text("Regular Calculus", font_size=28, color=WHITE, weight=BOLD).next_to(axes_regular, UP, buff=0.3)
        stochastic_label = Text("Stochastic Calculus", font_size=28, color=WHITE, weight=BOLD).next_to(axes_stochastic, UP, buff=0.3)

        # Step 1: Regular calculus - smooth function
        step_text = MathTex(steps[0], font_size=42, color=BLUE).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text))
        self.wait(1)

        # Show smooth function for regular calculus with gradient effect
        self.play(
            Create(axes_regular, run_time=0.8), 
            FadeIn(regular_label, shift=DOWN*0.5)
        )
        regular_func = axes_regular.plot(lambda x: 1 + 0.5*x + 0.3*np.sin(2*x), color=BLUE, stroke_width=5)
        # Add subtle glow effect
        regular_glow = axes_regular.plot(lambda x: 1 + 0.5*x + 0.3*np.sin(2*x), color=BLUE, stroke_width=12)
        regular_glow.set_stroke(opacity=0.3)
        self.play(Create(regular_glow), Create(regular_func, run_time=2))
        self.wait(1)

        # Step 2: But in finance...
        new_step = MathTex(steps[1], font_size=42, color=ORANGE).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1)

        # Step 3: dt matters!
        new_step = MathTex(steps[2], font_size=42, color=RED).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1)

        # Show jagged stochastic function with better effects
        self.play(
            Create(axes_stochastic, run_time=0.8), 
            FadeIn(stochastic_label, shift=DOWN*0.5)
        )
        
        # Generate random walk for stochastic function
        np.random.seed(42)
        t_vals = np.linspace(0, 4, 300)
        dt = t_vals[1] - t_vals[0]
        random_increments = np.random.normal(0, np.sqrt(dt), len(t_vals))
        brownian_path = np.cumsum(random_increments)
        stochastic_vals = 1 + 0.5*t_vals + 0.6*brownian_path
        
        stochastic_points = [axes_stochastic.c2p(t, val) for t, val in zip(t_vals, stochastic_vals)]
        stochastic_func = VMobject()
        stochastic_func.set_points_smoothly(stochastic_points)
        stochastic_func.set_color(RED)
        stochastic_func.set_stroke(width=4)
        
        # Add dramatic glow effect for stochastic function
        stochastic_glow = VMobject()
        stochastic_glow.set_points_smoothly(stochastic_points)
        stochastic_glow.set_color(RED)
        stochastic_glow.set_stroke(width=15)
        stochastic_glow.set_stroke(opacity=0.2)
        
        self.play(Create(stochastic_glow), Create(stochastic_func, run_time=2.5))
        self.wait(1)

        # Step 4: Introduce stochastic calculus
        new_step = MathTex(steps[3], font_size=42, color=PURPLE).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Step 5: The shocking rule
        new_step = MathTex(steps[4], font_size=38, color=YELLOW).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        
        # Animate the "shock" with some visual effects
        self.play(
            stochastic_func.animate.set_stroke(width=7, color=GOLD),
            stochastic_glow.animate.set_stroke(width=20, color=GOLD).set_stroke(opacity=0.4),
            regular_func.animate.set_stroke(width=3, color=DARK_GREY),
            regular_glow.animate.set_stroke(width=8, color=DARK_GREY).set_stroke(opacity=0.1)
        )
        self.wait(2)

        # Clear the axes for the main equation with smooth transitions
        self.play(
            *[FadeOut(obj, shift=DOWN*0.5) for obj in [
                axes_regular, axes_stochastic, regular_func, stochastic_func,
                regular_glow, stochastic_glow, regular_label, stochastic_label
            ]],
            run_time=1.5
        )

        # Step 6: Itô's lemma - the big reveal with better styling
        new_step = MathTex(steps[5], font_size=32, color=GREEN).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(3)

        # Create a subtle highlight effect around the extra term in the existing equation
        # Create a highlight circle positioned over the second derivative term
        highlight_circle = Circle(
            radius=0.8, 
            color=YELLOW, 
            stroke_width=4, 
            fill_opacity=0.1
        )
        # Position it over the second derivative term in the equation
        highlight_circle.move_to(new_step.get_center() + RIGHT*2.5 + DOWN*0.05)
        
        # Animated highlight sequence
        self.play(
            Create(highlight_circle, run_time=1),
            step_text.animate.set_color(WHITE),  # Make base equation white so highlight stands out
            run_time=1.5
        )
        
        self.wait(2)
        
        # Clean up the highlight
        self.play(
            FadeOut(highlight_circle),
            step_text.animate.set_color(GREEN),  # Back to green
            run_time=1
        )

        # Step 7: This changes everything
        new_step = MathTex(steps[6], font_size=40, color=ORANGE).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Step 8: Black-Scholes revelation
        new_step = MathTex(steps[7], font_size=40, color=GOLD).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1)

        # Show the Black-Scholes PDE with cinematic reveal
        bs_equation = MathTex(
            r"\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} = rV",
            font_size=36,
            color=GOLD
        ).next_to(step_text, DOWN, buff=0.7)
        
        # Add subtle background glow to the equation
        bs_glow = BackgroundRectangle(bs_equation, color=GOLD, fill_opacity=0.1, buff=0.3)
        bs_glow.round_corners(radius=0.2)
        
        self.play(
            FadeIn(bs_glow, scale=0.8),
            Write(bs_equation, run_time=2.5)
        )
        self.wait(2)

        # Final dramatic emphasis with clean effects
        everything_group = VGroup(step_text, bs_glow, bs_equation)
        
        # Create an elegant frame instead of a simple box
        final_frame = RoundedRectangle(
            width=everything_group.width + 1,
            height=everything_group.height + 0.8,
            corner_radius=0.3,
            color=GOLD,
            stroke_width=4,
            fill_opacity=0.05
        ).move_to(everything_group.get_center())
        
        self.play(Create(final_frame, run_time=2))
        
        # Final glow effect only
        self.play(
            final_frame.animate.set_fill(opacity=0.15).set_stroke(width=6),
            run_time=1
        )
        
        self.wait(2)