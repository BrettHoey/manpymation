from manim import *
import numpy as np

class WhatIsETikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("What is 'e' and Why Should You Care?", font_size=44, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Steps timed for actual 45 seconds
        steps = [
            r"e = 2.71828...",
            r"\text{You know } \pi \text{, but what about } e?",
            r"\text{Invest \$1 at 100\% interest...}",
            r"\text{Annually: } (1+1)^1 = \$2.00",
            r"\text{Monthly: } \left(1+\frac{1}{12}\right)^{12} = \$2.61",
            r"\text{Daily: } \left(1+\frac{1}{365}\right)^{365} = \$2.715",
            r"\text{Every second: approaches } e!",
            r"e = \lim_{n \to \infty} \left(1+\frac{1}{n}\right)^n",
            r"\text{Population growth: } P(t) = P_0 e^{rt}",
            r"\text{Radioactive decay: } N(t) = N_0 e^{-\lambda t}",
            r"e^{i\pi} + 1 = 0",
            r"\text{e connects everything in math!}",
        ]

        # Step 1: Introduce e (0-3 seconds)
        step_text = MathTex(steps[0], font_size=48, color=ORANGE).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text), run_time=1)
        self.wait(1)

        # Step 2: Compare to pi (3-6 seconds)
        new_step = MathTex(steps[1], font_size=40, color=BLUE).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step), run_time=1)
        self.wait(1)

        # Step 3: Investment setup (6-9 seconds)
        new_step = MathTex(steps[2], font_size=40, color=GREEN).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step), run_time=1)
        self.wait(1)

        # Step 4: Annual compounding (9-12 seconds)
        new_step = MathTex(steps[3], font_size=38, color=WHITE).next_to(watermark, DOWN, buff=1)
        dollar = Text("$2.00", font_size=40, color=GREEN).shift(DOWN * 2.5)
        self.play(Transform(step_text, new_step), Write(dollar), run_time=1)
        self.wait(1)

        # Step 5: Monthly compounding (12-15 seconds)
        new_step = MathTex(steps[4], font_size=36, color=WHITE).next_to(watermark, DOWN, buff=1)
        new_dollar = Text("$2.61", font_size=40, color=YELLOW).shift(DOWN * 2.5)
        self.play(Transform(step_text, new_step), Transform(dollar, new_dollar), run_time=1)
        self.wait(1)

        # Step 6: Daily compounding (15-18 seconds)
        new_step = MathTex(steps[5], font_size=34, color=WHITE).next_to(watermark, DOWN, buff=1)
        new_dollar = Text("$2.715", font_size=40, color=ORANGE).shift(DOWN * 2.5)
        self.play(Transform(step_text, new_step), Transform(dollar, new_dollar), run_time=1)
        self.wait(1)

        # Step 7: Approach e (18-21 seconds)
        new_step = MathTex(steps[6], font_size=38, color=PURPLE).next_to(watermark, DOWN, buff=1)
        e_dollar = MathTex(r"e \approx \$2.718", font_size=40, color=PURPLE).shift(DOWN * 2.5)
        self.play(Transform(step_text, new_step), Transform(dollar, e_dollar), run_time=1)
        self.wait(1)

        # Clear money visual
        self.play(FadeOut(dollar), run_time=0.5)

        # Step 8: Mathematical definition (21-25 seconds)
        new_step = MathTex(steps[7], font_size=32, color=RED).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step), run_time=1)
        self.wait(1.5)

        # Step 9: Population growth (25-29 seconds)
        new_step = MathTex(steps[8], font_size=36, color=BLUE).next_to(watermark, DOWN, buff=1)
        axes = Axes(x_range=[0, 2, 1], y_range=[0, 4, 1], x_length=3, y_length=1.5,
                   axis_config={"color": GREY, "stroke_width": 1}).shift(DOWN * 2.5)
        growth_curve = axes.plot(lambda x: np.exp(x), color=BLUE, stroke_width=4)
        self.play(Transform(step_text, new_step), Create(axes), Create(growth_curve), run_time=1)
        self.wait(1.5)

        # Step 10: Decay (29-33 seconds)
        new_step = MathTex(steps[9], font_size=36, color=RED).next_to(watermark, DOWN, buff=1)
        decay_curve = axes.plot(lambda x: np.exp(-x), color=RED, stroke_width=4)
        self.play(Transform(step_text, new_step), Transform(growth_curve, decay_curve), run_time=1)
        self.wait(1.5)

        # Clear graph
        self.play(FadeOut(axes), FadeOut(growth_curve), run_time=0.5)

        # Step 11: Euler's identity (33-38 seconds)
        new_step = MathTex(steps[10], font_size=44, color=GOLD).next_to(watermark, DOWN, buff=1)
        euler_box = SurroundingRectangle(step_text, color=GOLD, buff=0.3)
        self.play(Transform(step_text, new_step), Create(euler_box), run_time=1)
        self.wait(2)

        # Remove box before final message
        self.play(FadeOut(euler_box), run_time=0.5)

        # Step 12: Final message (38-42 seconds)
        new_step = MathTex(steps[11], font_size=40, color=GREEN).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step), run_time=1)
        self.wait(1.5)