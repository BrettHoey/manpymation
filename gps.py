from manim import *
import numpy as np

class GPSCalculusTikTok(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Your GPS is Solving Calculus in Real-Time", font_size=46, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Create a simple city grid/map - smaller and positioned better
        grid_size = 2
        grid = VGroup()
        
        # Create street grid
        for i in range(4):
            # Horizontal lines (streets)
            h_line = Line(
                start=[-grid_size, -1 + i*0.6, 0],
                end=[grid_size, -1 + i*0.6, 0],
                color=GREY,
                stroke_width=2
            )
            grid.add(h_line)
            
            # Vertical lines (avenues)
            v_line = Line(
                start=[-grid_size + i*1.33, -1, 0],
                end=[-grid_size + i*1.33, 0.8, 0],
                color=GREY,
                stroke_width=2
            )
            grid.add(v_line)

        grid.shift(DOWN * 1.5)  # Move grid lower
        self.play(Create(grid))

        # Add some buildings as simple rectangles - smaller and adjusted positions
        buildings = VGroup()
        building_positions = [
            [-1.3, -0.7], [-0.3, -0.7], [0.7, -0.7],
            [-1.3, -1.7], [0, -1.7], [1.3, -1.7]
        ]
        
        for pos in building_positions:
            building = Rectangle(width=0.3, height=0.4, color=DARK_GREY, fill_opacity=0.5)
            building.move_to([pos[0], pos[1], 0])
            buildings.add(building)
        
        self.play(Create(buildings))

        # Start and end points - adjusted positions for smaller grid
        start_dot = Dot([-1.8, -0.4, 0], color=GREEN, radius=0.08)
        end_dot = Dot([1.8, -2.2, 0], color=RED, radius=0.08)
        
        start_label = Text("You", font_size=16, color=GREEN).next_to(start_dot, UP, buff=0.05)
        end_label = Text("Target", font_size=16, color=RED).next_to(end_dot, DOWN, buff=0.05)
        
        self.play(Create(start_dot), Create(end_dot), Write(start_label), Write(end_label))

        # Steps to show
        steps = [
            r"\text{You just ask for directions...}",
            r"\text{But GPS finds the SHORTEST path!}",
            r"\text{This is a calculus problem:}",
            r"\text{Minimize: } F = \int_a^b \sqrt{1 + (y')^2} \, dx",
            r"\text{Subject to obstacles \& traffic}",
            r"\text{Euler-Lagrange equation:}",
            r"\frac{d}{dx}\frac{\partial L}{\partial y'} - \frac{\partial L}{\partial y} = 0",
            r"\text{Your phone solves this 1000x/second!}",
        ]

        # Step 1: Show simple request
        step_text = MathTex(steps[0], font_size=36, color=BLUE).next_to(watermark, DOWN, buff=0.3)
        self.play(Write(step_text))
        
        # Show naive straight line path (impossible due to buildings)
        naive_path = Line(start_dot.get_center(), end_dot.get_center(), color=YELLOW, stroke_width=6)
        self.play(Create(naive_path))
        self.wait(1)
        
        # Make it flash red to show it's blocked
        self.play(naive_path.animate.set_color(RED))
        self.play(FadeOut(naive_path))

        # Step 2: The reveal
        new_step = MathTex(steps[1], font_size=36, color=ORANGE).next_to(watermark, DOWN, buff=0.3)
        self.play(Transform(step_text, new_step))
        
        # Show the actual optimal path around buildings - adjusted for smaller grid
        optimal_path_points = [
            [-1.8, -0.4, 0],   # start
            [-1.8, -0.5, 0],   # go down a bit
            [-1.0, -0.5, 0],   # go right
            [-1.0, -1.0, 0],   # go down
            [0.3, -1.0, 0],    # go right
            [0.3, -1.9, 0],    # go down
            [1.8, -1.9, 0],    # go right
            [1.8, -2.2, 0]     # reach target
        ]
        
        optimal_path = VMobject()
        optimal_path.set_points_smoothly([np.array(p) for p in optimal_path_points])
        optimal_path.set_color(GREEN)
        optimal_path.set_stroke(width=6)
        
        self.play(Create(optimal_path, run_time=2))
        self.wait(1.5)

        # Step 3: This is calculus
        new_step = MathTex(steps[2], font_size=36, color=PURPLE).next_to(watermark, DOWN, buff=0.3)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Step 4: The calculus of variations formula
        new_step = MathTex(steps[3], font_size=30, color=YELLOW).next_to(watermark, DOWN, buff=0.3)
        self.play(Transform(step_text, new_step))
        
        # Highlight the path while showing the equation
        self.play(optimal_path.animate.set_stroke(width=8, color=GOLD))
        self.wait(2)

        # Step 5: Constraints
        new_step = MathTex(steps[4], font_size=32, color=WHITE).next_to(watermark, DOWN, buff=0.3)
        self.play(Transform(step_text, new_step))
        
        # Flash buildings red to show they're obstacles
        self.play(buildings.animate.set_color(RED))
        self.wait(1)
        self.play(buildings.animate.set_color(DARK_GREY))
        self.wait(1)

        # Step 6: Euler-Lagrange equation
        new_step = MathTex(steps[5], font_size=32, color=BLUE).next_to(watermark, DOWN, buff=0.3)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Step 7: The actual differential equation
        new_step = MathTex(steps[6], font_size=28, color=PINK).next_to(watermark, DOWN, buff=0.3)
        self.play(Transform(step_text, new_step))
        self.wait(2)

        # Step 8: Mind-blown finale
        new_step = MathTex(steps[7], font_size=36, color=GREEN).next_to(watermark, DOWN, buff=0.3)
        self.play(Transform(step_text, new_step))
        
        # Show MANY more path calculations happening rapidly - like phone is calculating
        for round in range(4):  # Multiple rounds of calculations
            paths_to_show = VGroup()
            
            for i in range(6):  # 6 paths per round
                # Create more varied path attempts
                variation_points = [[p[0], p[1], p[2]] for p in optimal_path_points]
                
                # Add more randomness to show different "attempts"
                for j in range(1, len(variation_points)-1):
                    variation_points[j][0] += np.random.uniform(-0.4, 0.4)
                    variation_points[j][1] += np.random.uniform(-0.3, 0.3)
                
                # Some paths try to go through buildings (bad solutions)
                if i < 2:
                    variation_points[2][0] += np.random.uniform(-0.8, 0.8)
                    variation_points[3][1] += np.random.uniform(-0.5, 0.5)
                
                variation_path = VMobject()
                variation_path.set_points_smoothly([np.array(p) for p in variation_points])
                
                # Color-code the paths: red for bad, blue for okay, green for good
                if i < 2:
                    variation_path.set_color(RED)  # Bad paths
                elif i < 4:
                    variation_path.set_color(BLUE)  # Okay paths
                else:
                    variation_path.set_color(GREEN)  # Better paths
                    
                variation_path.set_stroke(width=2)
                paths_to_show.add(variation_path)
            
            # Show all paths at once, then fade them
            self.play(Create(paths_to_show, run_time=0.4))
            self.play(FadeOut(paths_to_show, run_time=0.3))
        
        # Show final "convergence" - multiple good paths getting closer to optimal
        final_paths = VGroup()
        for i in range(8):
            variation_points = [[p[0], p[1], p[2]] for p in optimal_path_points]
            
            # Very small variations around the optimal path
            for j in range(1, len(variation_points)-1):
                variation_points[j][0] += np.random.uniform(-0.1, 0.1)
                variation_points[j][1] += np.random.uniform(-0.08, 0.08)
            
            variation_path = VMobject()
            variation_path.set_points_smoothly([np.array(p) for p in variation_points])
            variation_path.set_color(YELLOW)
            variation_path.set_stroke(width=2)
            final_paths.add(variation_path)
        
        # Show the convergence
        self.play(Create(final_paths, run_time=0.6))
        self.wait(0.5)
        
        # All paths converge to the optimal solution
        self.play(
            FadeOut(final_paths),
            optimal_path.animate.set_stroke(width=10, color=GOLD),
            run_time=1
        )

        # Final box around the answer
        box = SurroundingRectangle(step_text, color=GREEN, buff=0.3)
        self.play(Create(box))
        self.wait(2)

        # Add final "calculation speed" indicator
        speed_text = Text("Processing: 1000 calculations/sec", font_size=24, color=YELLOW)
        speed_text.next_to(box, DOWN, buff=0.3)
        self.play(Write(speed_text))
        
        # Make it "blink" like a computer processing
        for _ in range(3):
            self.play(speed_text.animate.set_opacity(0.3), run_time=0.2)
            self.play(speed_text.animate.set_opacity(1), run_time=0.2)
        
        self.wait(1)