from manim import *
import numpy as np

class IntegralTypesTikTok(ThreeDScene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Your Calculus Class Only Taught You ONE Integral", font_size=42, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Steps to show
        steps = [
            r"\text{You learned this in Calc 1...}",
            r"\text{But there are MANY types!}",
            r"\text{Riemann: } \int_a^b f(x) \, dx",
            r"\text{Line: } \int_C \mathbf{F} \cdot d\mathbf{r}",
            r"\text{Surface: } \iint_S f(x,y,z) \, dS",
            r"\text{Volume: } \iiint_V f(x,y,z) \, dV",
            r"\text{Contour: } \oint_C f(z) \, dz",
            r"\text{Path: } \int_C P \, dx + Q \, dy",
            r"\text{Each one unlocks different physics!}",
        ]

        # Create main text area
        step_text = MathTex(steps[0], font_size=40, color=BLUE).next_to(watermark, DOWN, buff=1.2)
        self.play(Write(step_text))
        self.wait(1.5)

        # Show basic Riemann integral first
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 3, 1],
            x_length=5,
            y_length=3,
            axis_config={"color": DARK_GREY, "stroke_width": 2},
        ).shift(DOWN * 2)

        # Simple curve for Riemann integral
        func = axes.plot(lambda x: 1 + 0.5*np.sin(2*x) + 0.3*x, color=BLUE, stroke_width=4)
        area = axes.get_area(func, x_range=[1, 3], color=BLUE, opacity=0.3)
        
        self.play(Create(axes), Create(func))
        self.play(Create(area))
        self.wait(1.5)

        # Step 2: Reveal there are many types
        new_step = MathTex(steps[1], font_size=40, color=ORANGE).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step))
        self.wait(1.5)

        # Clear the basic example
        self.play(FadeOut(axes), FadeOut(func), FadeOut(area))

        # Step 3: Riemann Integral
        new_step = MathTex(steps[2], font_size=36, color=GREEN).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step))
        
        # Show Riemann sum visualization
        riemann_axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 2, 1],
            x_length=4,
            y_length=2.5,
            axis_config={"color": DARK_GREY, "stroke_width": 1},
        ).shift(DOWN * 2)
        
        riemann_func = riemann_axes.plot(lambda x: 1 + 0.3*np.sin(3*x), color=BLUE, stroke_width=3)
        rectangles = riemann_axes.get_riemann_rectangles(riemann_func, x_range=[0.5, 3.5], dx=0.3, color=GREEN, fill_opacity=0.5)
        
        self.play(Create(riemann_axes), Create(riemann_func))
        self.play(Create(rectangles))
        self.wait(1.5)
        self.play(FadeOut(riemann_axes), FadeOut(riemann_func), FadeOut(rectangles))

        # Step 4: Line Integral - improved visibility
        new_step = MathTex(steps[3], font_size=36, color=PURPLE).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step))
        
        # Show vector field and path with better visibility
        line_axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=4.5,
            y_length=4.5,
            axis_config={"color": WHITE, "stroke_width": 2},
        ).shift(DOWN * 1.8)
        
        # Create a cleaner vector field with better spacing
        vector_field = VGroup()
        for x in np.arange(-1.6, 2.0, 0.6):
            for y in np.arange(-1.6, 2.0, 0.6):
                start_point = line_axes.c2p(x, y)
                # Simple vector field F = (0.3*y, -0.3*x) - smaller for visibility
                end_point = line_axes.c2p(x + 0.3*y, y - 0.3*x)
                arrow = Arrow(
                    start_point, end_point, 
                    buff=0, 
                    stroke_width=3, 
                    max_tip_length_to_length_ratio=0.25, 
                    color=BLUE,
                    tip_length=0.15
                )
                vector_field.add(arrow)
        
        # Path curve - make it stand out more
        t_vals = np.linspace(0, 2*PI, 100)
        path_points = [line_axes.c2p(0.8*np.cos(t), 0.8*np.sin(t)) for t in t_vals]
        path_curve = VMobject()
        path_curve.set_points_smoothly(path_points)
        path_curve.set_color(PURPLE)
        path_curve.set_stroke(width=6)
        
        # Add glow effect to path
        path_glow = VMobject()
        path_glow.set_points_smoothly(path_points)
        path_glow.set_color(PURPLE)
        path_glow.set_stroke(width=12)
        path_glow.set_stroke(opacity=0.3)
        
        self.play(Create(line_axes))
        self.play(Create(vector_field))
        self.play(Create(path_glow), Create(path_curve, run_time=2))
        self.wait(1.5)
        self.play(FadeOut(line_axes), FadeOut(vector_field), FadeOut(path_curve), FadeOut(path_glow))

        # Step 5: Surface Integral - true 3D with fixed text positioning
        new_step = MathTex(steps[4], font_size=36, color=RED).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step))
        
        # Show beautiful 3D surface (moved down to not block text)
        surface_axes = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            z_range=[0, 2, 1],
            x_length=4,
            y_length=4,
            z_length=2.5,
            axis_config={"color": WHITE, "stroke_width": 2}
        ).shift(DOWN * 2.2)  # Moved further down
        
        # Create a beautiful wavy surface
        surface = surface_axes.plot_surface(
            lambda u, v: 1 + 0.4*np.sin(u)*np.cos(v) + 0.2*np.cos(2*u),
            u_range=[-1.5, 1.5],
            v_range=[-1.5, 1.5],
            resolution=(15, 15),
            color=RED,
            fill_opacity=0.7,
            stroke_color=RED,
            stroke_width=1
        )
        
        # IMPORTANT: Add text to fixed frame AFTER creating 3D objects
        self.add_fixed_in_frame_mobjects(step_text, title, watermark)
        
        # Set 3D camera angle
        self.set_camera_orientation(phi=65 * DEGREES, theta=45 * DEGREES)
        self.play(Create(surface_axes, run_time=1), Create(surface, run_time=2))
        
        # Rotate the surface slightly for better view
        self.play(Rotate(surface, angle=PI/6, axis=UP), run_time=1.5)
        self.wait(1)
        
        # Clean up 3D objects BEFORE resetting camera
        self.play(FadeOut(surface_axes), FadeOut(surface))
        
        # CRITICAL: Reset camera and remove fixed frame together
        self.remove_fixed_in_frame_mobjects(step_text, title, watermark)
        self.set_camera_orientation(phi=0, theta=0)
        self.wait(0.3)  # Brief pause to ensure reset

        # Step 6: Volume Integral - beautiful 3D with fixed text
        new_step = MathTex(steps[5], font_size=36, color=YELLOW).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step))
        
        # Show proper 3D volume with internal structure (moved down)
        volume_axes = ThreeDAxes(
            x_range=[-1.5, 1.5, 1],
            y_range=[-1.5, 1.5, 1],
            z_range=[-1.5, 1.5, 1],
            x_length=3.5,
            y_length=3.5,
            z_length=3.5,
            axis_config={"color": WHITE, "stroke_width": 2}
        ).shift(DOWN * 2)  # Moved further down
        
        # Create a semi-transparent cube
        volume_cube = Cube(
            side_length=2.5, 
            color=YELLOW, 
            fill_opacity=0.2,
            stroke_color=GOLD,
            stroke_width=3
        ).move_to(volume_axes.get_origin())
        
        # Add internal grid to show volume elements
        internal_grid = VGroup()
        spacing = 0.6
        for i in np.arange(-1, 1.5, spacing):
            for j in np.arange(-1, 1.5, spacing):
                for k in np.arange(-1, 1.5, spacing):
                    small_cube = Cube(
                        side_length=0.3,
                        color=YELLOW,
                        fill_opacity=0.1,
                        stroke_color=GOLD,
                        stroke_width=1
                    ).move_to(volume_axes.c2p(i, j, k))
                    internal_grid.add(small_cube)
        
        # Add text to fixed frame AFTER creating 3D objects
        self.add_fixed_in_frame_mobjects(step_text, title, watermark)
        
        # Set 3D view
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        self.play(Create(volume_axes, run_time=1))
        self.play(Create(volume_cube, run_time=1.5))
        self.play(Create(internal_grid, run_time=2), rate_func=rush_from)
        
        # Rotate for better visualization
        self.play(
            Rotate(VGroup(volume_cube, internal_grid), angle=PI/4, axis=UP),
            run_time=1.5
        )
        self.wait(1)
        
        # Clean up 3D objects BEFORE resetting camera
        self.play(FadeOut(volume_axes), FadeOut(volume_cube), FadeOut(internal_grid))
        
        # CRITICAL: Reset camera and remove fixed frame together
        self.remove_fixed_in_frame_mobjects(step_text, title, watermark)
        self.set_camera_orientation(phi=0, theta=0)
        self.wait(0.3)  # Brief pause to ensure reset

        # Step 7: Contour Integral
        new_step = MathTex(steps[6], font_size=36, color=PINK).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step))
        
        # Show complex plane with contour
        contour_axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=4,
            y_length=4,
            axis_config={"color": DARK_GREY, "stroke_width": 1},
        ).shift(DOWN * 1.8)
        
        # Add labels for complex plane
        real_label = MathTex(r"\text{Re}", font_size=20).next_to(contour_axes.get_x_axis(), RIGHT)
        imag_label = MathTex(r"\text{Im}", font_size=20).next_to(contour_axes.get_y_axis(), UP)
        
        # Closed contour (circle)
        contour_circle = Circle(radius=1, color=PINK, stroke_width=4).move_to(contour_axes.get_origin())
        
        # Add arrow to show direction
        arrow_on_contour = Arrow(
            contour_circle.point_at_angle(0),
            contour_circle.point_at_angle(0.5),
            color=PINK,
            buff=0,
            stroke_width=3
        )
        
        self.play(Create(contour_axes), Write(real_label), Write(imag_label))
        self.play(Create(contour_circle))
        self.play(Create(arrow_on_contour))
        self.wait(1.5)
        self.play(FadeOut(contour_axes), FadeOut(real_label), FadeOut(imag_label), 
                 FadeOut(contour_circle), FadeOut(arrow_on_contour))

        # Step 8: Path Integral (Green's theorem style)
        new_step = MathTex(steps[7], font_size=36, color=TEAL).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step))
        
        # Show 2D region with boundary
        path_axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=4,
            y_length=4,
            axis_config={"color": DARK_GREY, "stroke_width": 1},
        ).shift(DOWN * 1.8)
        
        # Create a closed path (irregular shape)
        path_points = []
        for t in np.linspace(0, 2*PI, 50):
            r = 1 + 0.3*np.sin(3*t)
            x = r * np.cos(t)
            y = r * np.sin(t)
            path_points.append(path_axes.c2p(x, y))
        
        closed_path = VMobject()
        closed_path.set_points_smoothly(path_points + [path_points[0]])  # Close the path
        closed_path.set_color(TEAL)
        closed_path.set_stroke(width=4)
        
        # Fill the region
        region_fill = VMobject()
        region_fill.set_points_smoothly(path_points + [path_points[0]])
        region_fill.set_fill(color=TEAL, opacity=0.2)
        region_fill.set_stroke(width=0)
        
        self.play(Create(path_axes))
        self.play(Create(region_fill), Create(closed_path))
        self.wait(1.5)
        self.play(FadeOut(path_axes), FadeOut(region_fill), FadeOut(closed_path))

        # Final step: Physics revelation
        new_step = MathTex(steps[8], font_size=40, color=GOLD).next_to(watermark, DOWN, buff=1.2)
        self.play(Transform(step_text, new_step))
        self.wait(1)

        # Show quick montage of physics applications
        physics_text = VGroup(
            Text("• Riemann → Areas & Volumes", font_size=24, color=WHITE),
            Text("• Line → Work & Circulation", font_size=24, color=WHITE),
            Text("• Surface → Flux & Flow", font_size=24, color=WHITE),
            Text("• Contour → Residue Theory", font_size=24, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(step_text, DOWN, buff=0.7)
        
        self.play(Write(physics_text, run_time=3))
        self.wait(2)

        # Final dramatic frame
        everything_group = VGroup(step_text, physics_text)
        final_frame = RoundedRectangle(
            width=everything_group.width + 1.2,
            height=everything_group.height + 0.8,
            corner_radius=0.3,
            color=GOLD,
            stroke_width=4,
            fill_opacity=0.1
        ).move_to(everything_group.get_center())
        
        self.play(Create(final_frame))
        self.play(final_frame.animate.set_stroke(width=6).set_fill(opacity=0.2))
        self.wait(2)