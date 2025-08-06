from manim import *

class IntegrationBee(Scene):
    def construct(self):
        # Set up the scene with title and watermark
        self.setup_scene()
        
        # Show the integral problem
        self.show_problem()
        
        # Solve step by step
        self.solve_step_by_step()
        
        # Show final answer
        self.show_final_answer()

    def setup_scene(self):
        # Create title
        title = Text("MIT Integration Bee", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.3)
        
        # Create watermark directly below title
        watermark = Text("@calc4dumb", font_size=20, color=GRAY, opacity=0.7)
        watermark.next_to(title, DOWN, buff=0.2)
        
        # Animate title and watermark
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(watermark), run_time=0.5)
        self.wait(0.5)
        
        # Store for later use
        self.title = title
        self.watermark = watermark

    def show_problem(self):
        # Create the integral problem (smaller size)
        problem = MathTex(
            r"\int \frac{x^3}{(x^2 + 1)^2} \, dx",
            font_size=35
        )
        problem.next_to(self.watermark, DOWN, buff=0.5)
        
        # Animate the problem appearance
        self.play(Write(problem), run_time=1)
        self.wait(1)
        
        # Add a box around it for emphasis
        box = SurroundingRectangle(problem, color=YELLOW, buff=0.2)
        self.play(Create(box), run_time=0.8)
        self.wait(0.5)
        
        self.problem = problem
        self.problem_box = box

    def solve_step_by_step(self):
        # Step 1: Rewrite the integrand
        step1_text = Text("Step 1: Rewrite the integrand", font_size=24, color=GREEN)
        step1_text.next_to(self.problem_box, DOWN, buff=0.3)
        
        step1_math = MathTex(
            r"\frac{x^3}{(x^2 + 1)^2} = \frac{x \cdot x^2}{(x^2 + 1)^2} = \frac{x(x^2 + 1 - 1)}{(x^2 + 1)^2}",
            font_size=35
        )
        step1_math.next_to(step1_text, DOWN, buff=0.3)
        
        self.play(Write(step1_text), run_time=0.8)
        self.play(Write(step1_math), run_time=1.2)
        self.wait(1)
        
        # Step 2: Simplify
        step2_math = MathTex(
            r"= \frac{x(x^2 + 1)}{(x^2 + 1)^2} - \frac{x}{(x^2 + 1)^2} = \frac{x}{x^2 + 1} - \frac{x}{(x^2 + 1)^2}",
            font_size=35
        )
        step2_math.next_to(step1_math, DOWN, buff=0.3)
        
        self.play(Write(step2_math), run_time=1.2)
        self.wait(1)
        
        # Clear previous steps and show the split integral
        self.play(FadeOut(step1_text), FadeOut(step1_math), FadeOut(step2_math), run_time=0.8)
        
        # Step 3: Split the integral
        step3_text = Text("Step 2: Split the integral", font_size=24, color=GREEN)
        step3_text.next_to(self.problem_box, DOWN, buff=0.4)
        
        step3_math = MathTex(
            r"\int \frac{x^3}{(x^2 + 1)^2} dx = \int \frac{x}{x^2 + 1} dx - \int \frac{x}{(x^2 + 1)^2} dx",
            font_size=35
        )
        step3_math.next_to(step3_text, DOWN, buff=0.3)
        
        self.play(Write(step3_text), run_time=0.8)
        self.play(Write(step3_math), run_time=1.2)
        self.wait(1)
        
        # Step 4: Solve first integral
        step4_text = Text("Step 3: Solve first integral using substitution", font_size=27, color=GREEN)
        step4_text.next_to(step3_math, DOWN, buff=0.4)
        
        step4_math1 = MathTex(
            r"\int \frac{x}{x^2 + 1} dx \quad \text{Let } u = x^2 + 1, \text{ then } du = 2x \, dx",
            font_size=31
        )
        step4_math1.next_to(step4_text, DOWN, buff=0.25)
        
        step4_math2 = MathTex(
            r"= \frac{1}{2} \int \frac{1}{u} du = \frac{1}{2} \ln|u| = \frac{1}{2} \ln(x^2 + 1)",
            font_size=31
        )
        step4_math2.next_to(step4_math1, DOWN, buff=0.25)
        
        self.play(Write(step4_text), run_time=0.8)
        self.play(Write(step4_math1), run_time=1)
        self.wait(0.5)
        self.play(Write(step4_math2), run_time=1)
        self.wait(1)
        
        # Clear and move to second integral
        self.play(FadeOut(step3_text), FadeOut(step3_math), 
                 FadeOut(step4_text), FadeOut(step4_math1), FadeOut(step4_math2), run_time=0.8)
        
        # Step 5: Solve second integral
        step5_text = Text("Step 4: Solve second integral using substitution", font_size=27, color=GREEN)
        step5_text.next_to(self.problem_box, DOWN, buff=0.4)
        
        step5_math1 = MathTex(
            r"\int \frac{x}{(x^2 + 1)^2} dx \quad \text{Let } u = x^2 + 1, \text{ then } du = 2x \, dx",
            font_size=31
        )
        step5_math1.next_to(step5_text, DOWN, buff=0.25)
        
        step5_math2 = MathTex(
            r"= \frac{1}{2} \int \frac{1}{u^2} du = \frac{1}{2} \int u^{-2} du = \frac{1}{2} \cdot \frac{u^{-1}}{-1} = -\frac{1}{2u}",
            font_size=29
        )
        step5_math2.next_to(step5_math1, DOWN, buff=0.25)
        
        step5_math3 = MathTex(
            r"= -\frac{1}{2(x^2 + 1)}",
            font_size=31
        )
        step5_math3.next_to(step5_math2, DOWN, buff=0.25)
        
        self.play(Write(step5_text), run_time=0.8)
        self.play(Write(step5_math1), run_time=1)
        self.wait(0.5)
        self.play(Write(step5_math2), run_time=1)
        self.wait(0.5)
        self.play(Write(step5_math3), run_time=1)
        self.wait(1)
        
        # Clear for final combination
        self.play(FadeOut(step5_text), FadeOut(step5_math1), 
                 FadeOut(step5_math2), FadeOut(step5_math3), run_time=0.8)

    def show_final_answer(self):
        # Final step: Combine results
        final_text = Text("Step 5: Combine the results", font_size=31, color=GREEN)
        final_text.next_to(self.problem_box, DOWN, buff=0.4)
        
        final_math1 = MathTex(
            r"\int \frac{x^3}{(x^2 + 1)^2} dx = \frac{1}{2} \ln(x^2 + 1) - \left(-\frac{1}{2(x^2 + 1)}\right)",
            font_size=31
        )
        final_math1.next_to(final_text, DOWN, buff=0.3)
        
        final_math2 = MathTex(
            r"= \frac{1}{2} \ln(x^2 + 1) + \frac{1}{2(x^2 + 1)} + C",
            font_size=33
        )
        final_math2.next_to(final_math1, DOWN, buff=0.3)
        
        # Animate final answer
        self.play(Write(final_text), run_time=0.8)
        self.play(Write(final_math1), run_time=1.2)
        self.wait(1)
        self.play(Write(final_math2), run_time=1.2)
        
        # Create a box around the final answer
        answer_box = SurroundingRectangle(final_math2, color=GOLD, buff=0.2)
        self.play(Create(answer_box), run_time=0.8)
        
        # Add celebration text
        celebration = Text("Solution Complete! 🎉", font_size=28, color=GOLD)
        celebration.next_to(answer_box, DOWN, buff=0.5)
        self.play(Write(celebration), run_time=1)
        
        # Final pause to appreciate the solution
        self.wait(2)
        
        # Fade out everything except watermark
        elements_to_fade = [
            self.title, self.problem, self.problem_box,
            final_text, final_math1, final_math2, answer_box, celebration
        ]
        self.play(*[FadeOut(element) for element in elements_to_fade], run_time=0.8)