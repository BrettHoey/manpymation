from manim import *
import numpy as np

class IntermediateValueTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("This Proves Two PLACES Have the SAME Temperature", font_size=38, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Hook steps
        steps = [
            r"\text{Right now, somewhere on Earth...}",
            r"\text{Two places have the EXACT same temperature}",
            r"\text{This isn't a guess - it's mathematically CERTAIN}",
            r"\text{Meet: The Intermediate Value Theorem}",
            r"\text{If } f \text{ is continuous on } [a,b] \text{ and } k \text{ is between } f(a) \text{ and } f(b)",
            r"\text{Then } \exists c \text{ where } f(c) = k",
            r"\text{Why this proves the temperature claim:}",
            r"\text{Temperature is continuous around Earth}",
        ]

        # Step 1: The hook - show Earth with temperature gradient
        step_text = MathTex(steps[0], font_size=40, color=BLUE).next_to(watermark, DOWN, buff=1.2)
        self.play(Write(step_text))
        
        # Create Earth representation with temperature visualization (smaller to fit labels)
        earth_circle = Circle(radius=1.5, color=BLUE, fill_opacity=0.1).shift(DOWN * 1.2)
        
        # Create temperature gradient visualization
        temp_colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        temp_bands = VGroup()
        
        for i, color in enumerate(temp_colors):
            band = Annulus(
                inner_radius=0.25 * i, 
                outer_radius=0.25 * (i + 1), 
                color=color, 
                fill_opacity=0.4
            ).shift(DOWN * 1.2)
            temp_bands.add(band)
        
        # Add equator line
        equator = Line(LEFT * 1.5, RIGHT * 1.5, color=WHITE, stroke_width=3).shift(DOWN * 1.2)
        
        # Temperature labels (better positioned)
        hot_label = Text("HOT", font_size=24, color=RED).next_to(earth_circle, UP, buff=0.2)
        cold_label = Text("COLD", font_size=24, color=BLUE).next_to(earth_circle, DOWN, buff=0.2)
        
        self.play(
            Create(earth_circle),
            Create(temp_bands, lag_ratio=0.2),
            Create(equator),
            Write(hot_label), 
            Write(cold_label)
        )
        self.wait(2)

        # Step 2: The bold claim
        new_step = MathTex(steps[1], font_size=40, color=RED).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step))
        
        # Highlight two points on Earth
        point1 = Dot(earth_circle.point_at_angle(PI/4), color=YELLOW, radius=0.15)
        point2 = Dot(earth_circle.point_at_angle(5*PI/4), color=YELLOW, radius=0.15)
        
        # Add pulsing effect to points
        self.play(
            Create(point1), Create(point2),
            point1.animate.scale(1.5).set_color(GOLD),
            point2.animate.scale(1.5).set_color(GOLD)
        )
        self.wait(2)

        # Step 3: Mathematical certainty
        new_step = MathTex(steps[2], font_size=40, color=PURPLE).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step))
        
        # Add "PROOF" stamp effect
        proof_stamp = Text("MATHEMATICAL\nPROOF", font_size=32, color=GOLD, weight=BOLD)
        proof_stamp.rotate(PI/6)
        proof_stamp.move_to(earth_circle.get_center() + UP * 0.5 + RIGHT * 2)
        
        stamp_rect = RoundedRectangle(
            width=proof_stamp.width + 0.4,
            height=proof_stamp.height + 0.3,
            corner_radius=0.1,
            color=GOLD,
            stroke_width=4,
            fill_opacity=0.1
        ).move_to(proof_stamp.get_center())
        
        self.play(
            FadeIn(stamp_rect, scale=0.5),
            Write(proof_stamp),
            run_time=1
        )
        self.wait(1)

        # Clear the Earth visualization
        earth_group = VGroup(earth_circle, temp_bands, equator, hot_label, cold_label, 
                           point1, point2, proof_stamp, stamp_rect)
        self.play(FadeOut(earth_group))

        # Step 4: Introduce the theorem
        new_step = MathTex(steps[3], font_size=40, color=ORANGE).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step))
        self.wait(1)

        # Show the classic IVT visualization
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE, "stroke_width": 2},
        ).shift(DOWN * 2)

        # Create a continuous curve that clearly shows IVT
        def sample_function(x):
            return 2 + 1.5*np.sin(x) + 0.3*x

        curve = axes.plot(sample_function, x_range=[1, 5], color=GREEN, stroke_width=4)
        
        # Mark the endpoints
        a_point = Dot(axes.c2p(1, sample_function(1)), color=RED, radius=0.12)
        b_point = Dot(axes.c2p(5, sample_function(5)), color=RED, radius=0.12)
        
        # Labels for endpoints
        a_label = MathTex("f(a)", font_size=28, color=RED).next_to(a_point, LEFT)
        b_label = MathTex("f(b)", font_size=28, color=RED).next_to(b_point, RIGHT)
        
        self.play(Create(axes))
        self.play(Create(curve, run_time=2))
        self.play(Create(a_point), Create(b_point), Write(a_label), Write(b_label))
        self.wait(1.5)

        # Step 5: The formal theorem statement
        new_step = MathTex(steps[4], font_size=32, color=GREEN).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step))
        
        # Show the k value between f(a) and f(b) - positioned to not block labels
        k_value = 2.9  # Choose a value between f(a) and f(b)
        k_line = DashedLine(
            axes.c2p(0.2, k_value), 
            axes.c2p(5.8, k_value), 
            color=YELLOW, 
            stroke_width=3
        )
        k_label = MathTex("k", font_size=32, color=YELLOW).move_to(axes.c2p(0.5, k_value + 0.3))
        
        self.play(Create(k_line), Write(k_label))
        self.wait(1)

        # Step 6: Show the conclusion
        new_step = MathTex(steps[5], font_size=32, color=PURPLE).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step))
        
        # Find and show the c value where f(c) = k
        # Approximate where curve intersects k_line
        c_x = 3.2  # Approximate solution
        c_point = Dot(axes.c2p(c_x, k_value), color=PURPLE, radius=0.12)
        c_line = DashedLine(axes.c2p(c_x, 0), axes.c2p(c_x, k_value), color=PURPLE, stroke_width=2)
        c_label = MathTex("c", font_size=28, color=PURPLE).next_to(c_line, DOWN)
        
        # Dramatic reveal of the c point
        self.play(
            Create(c_line),
            Create(c_point, run_time=1.5),
            Write(c_label),
            c_point.animate.scale(1.5)
        )
        self.wait(1)

        # Clear the graph
        graph_group = VGroup(axes, curve, a_point, b_point, a_label, b_label, 
                           k_line, k_label, c_point, c_line, c_label)
        self.play(FadeOut(graph_group))

        # Step 7: Back to the temperature example
        new_step = MathTex(steps[6], font_size=40, color=GOLD).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Step 8: Explain the temperature logic
        new_step = MathTex(steps[7], font_size=36, color=BLUE).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step))
        
        # Show Earth again with temperature path
        earth_circle2 = Circle(radius=1.5, color=BLUE, fill_opacity=0.1).shift(DOWN * 1.5)
        
        # Show a path around Earth with temperature function
        temp_path = ParametricFunction(
            lambda t: earth_circle2.get_center() + 1.5 * np.array([np.cos(t), np.sin(t), 0]),
            t_range=[0, 2*PI],
            color=GREEN,
            stroke_width=4
        )
        
        # Temperature values at different points
        temp_high = Text("30°C", font_size=24, color=RED).move_to(earth_circle2.get_center() + UP * 2)
        temp_low = Text("10°C", font_size=24, color=BLUE).move_to(earth_circle2.get_center() + DOWN * 2)
        temp_mid = Text("20°C", font_size=24, color=YELLOW).move_to(earth_circle2.get_center() + RIGHT * 2.2)
        
        self.play(
            Create(earth_circle2),
            Create(temp_path, run_time=2),
            Write(temp_high), Write(temp_low), Write(temp_mid)
        )
        self.wait(1.5)

        # Final dramatic conclusion
        conclusion_steps = [
            r"\text{Since temperature changes continuously...}",
            r"\text{And we go from 30°C to 10°C...}",
            r"\text{We MUST hit every temperature in between!}",
            r"\text{Including the SAME temperature twice!}",
        ]

        for i, conclusion in enumerate(conclusion_steps):
            new_step = MathTex(conclusion, font_size=34, color=[ORANGE, PURPLE, GREEN, GOLD][i]).next_to(watermark, DOWN, buff=1.2)
            self.play(Transform(step_text, new_step))
            self.wait(1)

        # Final mind-blown effect
        final_group = VGroup(step_text, earth_circle2, temp_path, temp_high, temp_low, temp_mid)
        final_frame = RoundedRectangle(
            width=final_group.width + 1.5,
            height=final_group.height + 1,
            corner_radius=0.3,
            color=GOLD,
            stroke_width=5,
            fill_opacity=0.1
        ).move_to(final_group.get_center())
        
        # Add "MIND = BLOWN" text - positioned to not block content
        mind_blown = Text("MIND = BLOWN ", font_size=32, color=GOLD, weight=BOLD)
        mind_blown.move_to(UP * 2.2)  # Position at very top, above everything
        
        self.play(
            Create(final_frame),
            Write(mind_blown, run_time=2),
            final_frame.animate.set_stroke(width=8)
        )
        self.wait(1.5)