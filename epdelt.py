from manim import *

class EpsilonDeltaTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("What LIMIT Actually Means", font_size=48, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Graph on bottom middle
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 10, 2],
            x_length=4.5,
            y_length=3,
            axis_config={"color": GREY},
            tips=False,
        ).to_edge(DOWN, buff=0.1)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN)
        y_label = axes.get_y_axis_label("f(x) = 2x + 1", edge=UP, direction=LEFT)
        self.play(Create(axes), Write(x_label), Write(y_label))

        def func(x):
            return 2*x + 1

        # Key values
        a = 2  # approaching x = 2
        L = 5  # limit value f(2) = 5
        epsilon = 1  # epsilon value for visualization
        delta = epsilon / 2  # delta = epsilon/2 for this linear function

        graph = axes.plot(func, x_range=[0.5, 3.5], color=YELLOW)
        
        # Point we're approaching
        limit_point = Dot(axes.c2p(a, L), color=RED, radius=0.1)
        
        self.play(Create(graph), Create(limit_point))

        # Steps to show
        steps = [
            r"\lim_{x \to 2} (2x + 1) = 5",
            r"\text{But what does 'approaches' mean?}",
            r"\text{For ANY } \epsilon > 0 \text{ (error tolerance)}",
            r"\text{We can find } \delta > 0 \text{ such that:}",
            r"\text{If } |x - 2| < \delta",
            r"\text{Then } |f(x) - 5| < \epsilon",
            r"\text{Example: } \epsilon = 1, \text{ so } \delta = 0.5",
            r"\forall \epsilon > 0, \exists \delta > 0: |x-a|<\delta \Rightarrow |f(x)-L|<\epsilon",
            r"\text{This is what limit REALLY means!}",
        ]

        # Create first step
        step_text = MathTex(steps[0], font_size=44, color=BLUE).next_to(watermark, DOWN, buff=1)
        self.play(Write(step_text))
        self.wait(1.5)

        # Second step - the big question
        new_step = MathTex(steps[1], font_size=44, color=ORANGE).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Steps 3-4: Set up the definition
        for i in range(2, 4):
            new_step = MathTex(steps[i], font_size=40, color=WHITE).next_to(watermark, DOWN, buff=1)
            self.play(Transform(step_text, new_step))
            self.wait(1.5)

        # Step 5: Show the x condition with delta interval
        new_step = MathTex(steps[4], font_size=40, color=GREEN).next_to(watermark, DOWN, buff=1)
        
        # Delta interval on x-axis
        delta_left = axes.c2p(a - delta, 0)
        delta_right = axes.c2p(a + delta, 0)
        delta_interval = Line(delta_left, delta_right, color=GREEN, stroke_width=8)
        delta_brackets = VGroup(
            Line(axes.c2p(a - delta, -0.1), axes.c2p(a - delta, 0.1), color=GREEN, stroke_width=4),
            Line(axes.c2p(a + delta, -0.1), axes.c2p(a + delta, 0.1), color=GREEN, stroke_width=4)
        )
        
        self.play(
            Transform(step_text, new_step),
            Create(delta_interval),
            Create(delta_brackets)
        )
        self.wait(1.5)

        # Step 6: Show the f(x) condition with epsilon band
        new_step = MathTex(steps[5], font_size=40, color=PURPLE).next_to(watermark, DOWN, buff=1)
        
        # Epsilon band around L = 5
        epsilon_top = axes.c2p(0, L + epsilon)
        epsilon_bottom = axes.c2p(0, L - epsilon)
        epsilon_top_line = axes.get_horizontal_line(axes.c2p(4, L + epsilon), color=PURPLE, stroke_width=4)
        epsilon_bottom_line = axes.get_horizontal_line(axes.c2p(4, L - epsilon), color=PURPLE, stroke_width=4)
        
        # Connecting lines to show the guarantee
        connect_left_top = DashedLine(axes.c2p(a - delta, func(a - delta)), axes.c2p(0, func(a - delta)), color=PURPLE, stroke_width=2)
        connect_left_bottom = DashedLine(axes.c2p(a - delta, func(a - delta)), axes.c2p(0, func(a - delta)), color=PURPLE, stroke_width=2)
        connect_right_top = DashedLine(axes.c2p(a + delta, func(a + delta)), axes.c2p(0, func(a + delta)), color=PURPLE, stroke_width=2)
        connect_right_bottom = DashedLine(axes.c2p(a + delta, func(a + delta)), axes.c2p(0, func(a + delta)), color=PURPLE, stroke_width=2)
        
        self.play(
            Transform(step_text, new_step),
            Create(epsilon_top_line),
            Create(epsilon_bottom_line),
            Create(connect_left_top),
            Create(connect_right_top)
        )
        self.wait(1.5)

        # Step 7: Specific example
        new_step = MathTex(steps[6], font_size=40, color=YELLOW).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Step 8: Formal definition
        new_step = MathTex(steps[7], font_size=36, color=GOLD).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(2)

        # Final step with dramatic reveal
        new_step = MathTex(steps[8], font_size=44, color=GREEN).next_to(watermark, DOWN, buff=1)
        self.play(Transform(step_text, new_step))
        self.wait(1)

        # Highlight the epsilon-delta connection with pulsing
        self.play(
            delta_interval.animate.set_stroke(width=12),
            epsilon_top_line.animate.set_stroke(width=6),
            epsilon_bottom_line.animate.set_stroke(width=6)
        )
        self.wait(0.5)

        # Final dramatic box around the answer
        box = SurroundingRectangle(step_text, color=GREEN, buff=0.3)
        self.play(Create(box))
        self.wait(2)