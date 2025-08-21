from manim import *
import numpy as np

class WeirdDInCalculus(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("What's that weird 'd' in calculus?", font_size=44, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Hook steps - remove the graph visualization step
        steps = [
            r"\text{You see this 'd' EVERYWHERE in calculus...}",
            r"\frac{dy}{dx}, \quad \int f(x) \, dx, \quad \frac{d}{dt}(x^2)",
            r"\text{But what IS it?}",
            r"\text{It's NOT multiplication!}",
            r"\text{It means 'an infinitely small piece'}",
            r"dx = \text{'tiny piece of x'}",
            r"dy = \text{'tiny piece of y'}",
        ]

        # Speed up all transitions and waits
        step_text = MathTex(steps[0], font_size=40, color=BLUE).next_to(watermark, DOWN, buff=1.2)
        self.play(Write(step_text), run_time=0.8)
        self.wait(1)

        # Step 2: Show the 'd' everywhere with dramatic reveal
        new_step = MathTex(steps[1], font_size=38, color=RED).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step), run_time=0.8)
        
        # Create floating 'd' letters around the equations for emphasis
        floating_ds = VGroup()
        for i in range(8):
            d_letter = Text("d", font_size=60, color=RED, weight=BOLD)
            # Random positions around the screen
            x_pos = np.random.uniform(-6, 6)
            y_pos = np.random.uniform(-2, 2)
            d_letter.move_to([x_pos, y_pos, 0])
            d_letter.set_opacity(0.3)
            floating_ds.add(d_letter)
        
        self.play(LaggedStart(*[FadeIn(d, scale=2) for d in floating_ds], lag_ratio=0.05), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(floating_ds), run_time=0.6)

        # Step 3: The big question
        new_step = MathTex(steps[2], font_size=44, color=ORANGE).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step), run_time=0.8)
        self.wait(1)

        # Step 4: It's NOT multiplication
        new_step = MathTex(steps[3], font_size=44, color=RED).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step), run_time=0.8)
        
        # Show crossed out multiplication symbol
        wrong_mult = MathTex(r"d \times x", font_size=48, color=RED).next_to(step_text, DOWN, buff=0.5)
        cross_out = Line(
            wrong_mult.get_corner(DL) + LEFT*0.2 + DOWN*0.2, 
            wrong_mult.get_corner(UR) + RIGHT*0.2 + UP*0.2, 
            color=RED, stroke_width=8
        )
        
        self.play(Write(wrong_mult), run_time=0.6)
        self.play(Create(cross_out), run_time=0.6)
        self.wait(1)
        self.play(FadeOut(wrong_mult), FadeOut(cross_out), run_time=0.5)

        # Step 5: The big reveal
        new_step = MathTex(steps[4], font_size=40, color=GREEN).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step), run_time=0.8)
        self.wait(1.2)

        # Step 6-7: Show specific examples - faster pace
        for i in range(5, 7):
            new_step = MathTex(steps[i], font_size=45, color=PURPLE).next_to(watermark, DOWN, buff=1.2)
            self.play(Transform(step_text, new_step), run_time=0.8)
            self.wait(1)

        # Clear the step_text before moving to final revelation
        self.play(FadeOut(step_text), run_time=0.5)

        # Final revelation steps - faster pace
        final_steps = [
            r"\text{So } \frac{dy}{dx} \text{ means...}",
            r"\text{'tiny change in y' over 'tiny change in x'}",
            r"\text{This gives us the SLOPE at any point!}",
            r"\text{The 'd' unlocks all of calculus!}",
        ]

        # Show final concepts with faster transitions
        final_text = MathTex(final_steps[0], font_size=45, color=BLUE).next_to(watermark, DOWN, buff=1.2)
        self.play(Write(final_text), run_time=0.8)
        self.wait(1)

        for i in range(1, 4):
            color = [WHITE, GREEN, GOLD][i-1]
            new_step = MathTex(final_steps[i], font_size=45, color=color).next_to(watermark, DOWN, buff=1.2)
            self.play(Transform(final_text, new_step), run_time=0.8)
            self.wait(1)

        # Show the key derivatives with 'd' highlighted - faster reveal
        derivatives_showcase = VGroup(
            MathTex(r"\frac{d}{dx}(x^2) = 2x", font_size=36),
            MathTex(r"\frac{d}{dx}(\sin x) = \cos x", font_size=36),
            MathTex(r"\frac{d}{dx}(e^x) = e^x", font_size=36),
        ).arrange(DOWN, buff=0.4).next_to(final_text, DOWN, buff=0.7)
        
        # Highlight all the 'd's in these equations
        for eq in derivatives_showcase:
            eq.set_color_by_tex("d", YELLOW)
        
        self.play(LaggedStart(*[Write(eq) for eq in derivatives_showcase], lag_ratio=0.15), run_time=1.5)
        self.wait(1.5)

        # Final dramatic frame with mind-blown effect - quicker finale
        everything_group = VGroup(final_text, derivatives_showcase)
        final_frame = RoundedRectangle(
            width=everything_group.width + 1.5,
            height=everything_group.height + 1,
            corner_radius=0.3,
            color=GOLD,
            stroke_width=5,
            fill_opacity=0.1
        ).move_to(everything_group.get_center())
        
    
        
        self.play(
            Create(final_frame),
            final_frame.animate.set_stroke(width=8).set_fill(opacity=0.2),
            run_time=1.2
        )
        
        # Quick pulsing effect for extra drama
        self.play(
            final_frame.animate.scale(1.1).set_fill(opacity=0.3),
            rate_func=there_and_back,
            run_time=0.8
        )
        
        self.wait(1)