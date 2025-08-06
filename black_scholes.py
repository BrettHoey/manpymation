from manim import *
import numpy as np

class BlackScholesTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Your Stock Price is Doing Calculus", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Stock chart on bottom middle
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[80, 120, 10],
            x_length=4.5,
            y_length=3,
            axis_config={"color": GREY},
            tips=False,
        ).to_edge(DOWN, buff=0.1)

        x_label = axes.get_x_axis_label("Time", edge=RIGHT, direction=DOWN)
        y_label = axes.get_y_axis_label("Stock Price", edge=UP, direction=LEFT)
        self.play(Create(axes), Write(x_label), Write(y_label))

        # Generate random stock price path (geometric Brownian motion simulation)
        np.random.seed(42)  # For consistent animation
        dt = 0.05
        t_values = np.arange(0, 5, dt)
        S0 = 100  # Initial stock price
        mu = 0.02  # Reduced drift rate
        sigma = 0.15  # Reduced volatility
        
        # Simulate stock price path with bounds checking
        random_shocks = np.random.normal(0, 1, len(t_values))
        stock_prices = [S0]
        
        for i in range(1, len(t_values)):
            dS = stock_prices[i-1] * (mu * dt + sigma * np.sqrt(dt) * random_shocks[i])
            new_price = stock_prices[i-1] + dS
            # Keep price within reasonable bounds (85-115)
            new_price = max(85, min(115, new_price))
            stock_prices.append(new_price)
        
        # Create the wiggly stock curve
        stock_points = [axes.c2p(t, price) for t, price in zip(t_values, stock_prices)]
        stock_curve = VMobject()
        stock_curve.set_points_smoothly(stock_points)
        stock_curve.set_color(GREEN)
        stock_curve.set_stroke(width=4)

        # Steps to show
        steps = [
            r"\text{Stock prices look random...}",
            r"\text{But they follow a CALCULUS equation!}",
            r"\text{Black-Scholes Model:}",
            r"dS = \mu S dt + \sigma S dW",
            r"\text{Where } dS = \text{price change}",
            r"\mu = \text{drift, } \sigma = \text{volatility}",
            r"dW = \text{random 'Brownian motion'}",
            r"\text{Your portfolio is pure mathematics!}",
        ]

        # Create first step with animated stock curve
        step_text = MathTex(steps[0], font_size=44, color=BLUE).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text), Create(stock_curve, run_time=3))
        self.wait(1)

        # Make the curve "wiggle" more to emphasize randomness
        self.play(stock_curve.animate.set_stroke(width=6))
        self.wait(1)

        # Step 2: The big reveal
        new_step = MathTex(steps[1], font_size=44, color=ORANGE).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Step 3: Introduce Black-Scholes
        new_step = MathTex(steps[2], font_size=44, color=PURPLE).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Step 4: The main equation
        new_step = MathTex(steps[3], font_size=40, color=YELLOW).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(2)

        # Step 5-7: Break down the equation
        for i in range(4, 7):
            color = WHITE if i != 6 else GREEN
            new_step = MathTex(steps[i], font_size=38, color=color).next_to(watermark, DOWN, buff=1)
            self.play(Transform(step_text, new_step))
            self.wait(1.5)

        # Add visual emphasis to the random component
        if i == 6:  # When showing Brownian motion
            # Add some "random" dots along the curve to show the noise
            random_dots = VGroup(*[
                Dot(stock_points[i], color=RED, radius=0.05) 
                for i in range(0, len(stock_points), 5)
            ])
            self.play(Create(random_dots))
            self.wait(1)
            self.play(FadeOut(random_dots))

        # Final step with dramatic reveal
        new_step = MathTex(steps[7], font_size=44, color=GREEN).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1)

        # Highlight the equation and curve connection
        self.play(
            stock_curve.animate.set_stroke(width=8, color=GOLD),
        )
        self.wait(0.5)

        # Final dramatic box around the answer
        box = SurroundingRectangle(step_text, color=GREEN, buff=0.3)
        self.play(Create(box))
        self.wait(2)