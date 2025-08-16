from manim import *
import numpy as np

class VolatilitySmileTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Black-Scholes Says THIS... Reality Says THIS", font_size=44, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Technically accurate steps
        steps = [
            r"\text{Black-Scholes assumes constant volatility}",
            r"\text{So IMPLIED volatility should be...}",
            r"\text{FLAT across all strikes}",
            r"\text{But market data shows...}",
            r"\text{The VOLATILITY SMILE!}",
            r"\text{Same stock, different vol estimates?}",
            r"\text{Market expects more tail risk}",
            r"\text{Than log-normal distribution predicts}",
            r"\text{Smile = market's tail risk premium}",
        ]

        # Graph positioned bottom center
        axes = Axes(
            x_range=[0.8, 1.2, 0.1],
            y_range=[0.15, 0.35, 0.05],
            x_length=4,
            y_length=2.5,
            axis_config={"color": WHITE, "stroke_width": 2},
        ).to_edge(DOWN, buff=0.8)

        x_label = MathTex("K/S_0", font_size=18).next_to(axes, DOWN, buff=0.2)
        y_label = MathTex(r"\sigma_{impl}", font_size=18).next_to(axes, LEFT, buff=0.2)

        # Step 1: Black-Scholes assumption
        step_text = MathTex(steps[0], font_size=38, color=BLUE).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text))
        self.wait(1.6)

        # Step 2: IMPLIED volatility clarification
        new_step = MathTex(steps[1], font_size=38, color=ORANGE).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.4)

        # Show axes with proper labels
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=1.2)

        # Step 3: Flat across strikes
        new_step = MathTex(steps[2], font_size=38, color=GREEN).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))

        # Show flat implied volatility
        flat_line = axes.plot(lambda x: 0.25, x_range=[0.8, 1.2], color=GREEN, stroke_width=4)
        flat_label = Text("BS Theory", font_size=16, color=GREEN).next_to(flat_line, UP, buff=0.15)
        self.play(Create(flat_line, run_time=1.4), Write(flat_label))
        self.wait(1.2)

        # Step 4: But market data shows...
        new_step = MathTex(steps[3], font_size=38, color=RED).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.2)

        # Step 5: The volatility smile
        new_step = MathTex(steps[4], font_size=38, color=PURPLE).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))

        # Realistic volatility smile (U-shaped, higher at extremes)
        def realistic_smile(x):
            # Typical equity smile - higher vol for OTM puts and calls
            return 0.20 + 0.15 * (x - 1)**2 + 0.05 * (x - 1)**4

        smile_curve = axes.plot(realistic_smile, x_range=[0.8, 1.2], color=PURPLE, stroke_width=6)
        smile_glow = axes.plot(realistic_smile, x_range=[0.8, 1.2], color=PURPLE, stroke_width=12)
        smile_glow.set_stroke(opacity=0.3)
        
        smile_label = Text("Market Data", font_size=16, color=PURPLE).next_to(axes.c2p(1, realistic_smile(1)), UP, buff=0.25)
        
        self.play(
            Create(smile_glow),
            Create(smile_curve, run_time=2),
            Write(smile_label)
        )
        self.wait(1.4)

        # Step 6: Paradox explanation
        new_step = MathTex(steps[5], font_size=36, color=ORANGE).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        
        # Fade flat line to show the discrepancy
        self.play(
            flat_line.animate.set_stroke(opacity=0.4),
            flat_label.animate.set_opacity(0.4),
        )
        self.wait(1.4)

        # Step 7: Market expects more tail risk
        new_step = MathTex(steps[6], font_size=38, color=YELLOW).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.3)

        # Step 8: Than log-normal predicts
        new_step = MathTex(steps[7], font_size=36, color=RED).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))

        # Show log-normal vs empirical distributions
        dist_axes = Axes(
            x_range=[-4, 4, 2],
            y_range=[0, 0.5, 0.2],
            x_length=3,
            y_length=1.8,
            axis_config={"color": GREY, "stroke_width": 1},
        ).next_to(axes, RIGHT, buff=0.4)

        # Log-normal assumption (what BS uses)
        lognormal = dist_axes.plot(
            lambda x: 0.4 * np.exp(-x**2/2) / np.sqrt(2*np.pi), 
            x_range=[-3, 3], 
            color=GREEN, 
            stroke_width=3
        )
        
        # Empirical distribution with fat tails and negative skew
        def empirical_dist(x):
            # Skewed distribution with fat tails (more realistic for equity returns)
            return 0.35 * np.exp(-(x + 0.5)**2/1.5) / np.sqrt(1.5*np.pi) if x < 0 else 0.35 * np.exp(-x**2/3) / np.sqrt(3*np.pi)
        
        empirical = dist_axes.plot(empirical_dist, x_range=[-3.5, 3.5], color=RED, stroke_width=3)

        dist_labels = VGroup(
            Text("Log-normal", font_size=14, color=GREEN),
            Text("Empirical", font_size=14, color=RED)
        ).arrange(DOWN, buff=0.1).next_to(dist_axes, UP, buff=0.1)

        self.play(Create(dist_axes), run_time=0.8)
        self.play(Create(lognormal), Write(dist_labels[0]), run_time=1)
        self.play(Create(empirical), Write(dist_labels[1]), run_time=1)
        self.wait(1.2)

        # Step 9: Smile = tail risk premium
        new_step = MathTex(steps[8], font_size=36, color=GOLD).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.4)

        # Final emphasis on the smile
        self.play(
            smile_curve.animate.set_stroke(width=8, color=GOLD),
            smile_glow.animate.set_stroke(width=18, color=GOLD, opacity=0.4)
        )
        
        # Create final frame
        key_elements = VGroup(step_text, axes, smile_curve, dist_axes, lognormal, empirical)
        final_box = SurroundingRectangle(key_elements, color=GOLD, buff=0.3)
        self.play(Create(final_box))
        self.wait(1.8)