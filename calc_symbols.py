from manim import *
import numpy as np

class CalculusSymbolRanking(Scene):
    def construct(self):
        # Title and watermark (persistent)
        title = Text("Ranking Calculus Symbols by TRAUMA Level", font_size=42, color=BLUE).to_edge(UP)
        watermark = Text("@calc4dumb", font_size=24, color=GREY).next_to(title, DOWN, buff=0.1)
        self.add(title, watermark)

        # Create tier boxes on the right side
        tier_boxes = self.create_tier_system()
        
        # Symbols to rank with their trauma explanations
        symbols_data = [
            (r"x", "Basic variable", GREEN, "HARMLESS"),
            (r"+", "Addition", GREEN, "HARMLESS"), 
            (r"\frac{dy}{dx}", "Basic derivative", YELLOW, "ANNOYING"),
            (r"\int", "Integration", ORANGE, "SCARY"),
            (r"\lim_{x \to 0}", "Limits", ORANGE, "SCARY"),
            (r"\partial", "Partial derivatives", RED, "NIGHTMARE"),
            (r"\nabla", "Del operator", PURPLE, "FINAL BOSS"),
        ]
        
        # Show tier system immediately (no hook text)
        self.play(Create(tier_boxes), run_time=1.5)
        
        # Show symbols one by one and rank them
        self.rank_symbols(symbols_data, tier_boxes)
        
        # Final dramatic reveal
        self.final_reveal()

    def create_tier_system(self):
        # Create tier list on the right side
        tier_labels = ["FINAL BOSS", "NIGHTMARE", "SCARY", "ANNOYING", "HARMLESS"]
        tier_colors = [PURPLE, RED, ORANGE, YELLOW, GREEN]
        
        tier_boxes = VGroup()
        
        for i, (label, color) in enumerate(zip(tier_labels, tier_colors)):
            # Create tier box (wider to accommodate symbols)
            box = Rectangle(
                width=4.5, height=1.2,
                fill_color=color, fill_opacity=0.2,
                stroke_color=color, stroke_width=3
            )
            
            # Tier label - centered in the box
            tier_text = Text(label, font_size=14, color=color, weight=BOLD)
            tier_text.move_to(box.get_center())
            
            # Position boxes vertically - moved down to avoid overlap with title
            box.move_to(RIGHT * 3.5 + UP * (1.8 - i * 1.1))
            tier_text.move_to(box.get_center())
            
            tier_group = VGroup(box, tier_text)
            tier_boxes.add(tier_group)
            
        return tier_boxes

    def rank_symbols(self, symbols_data, tier_boxes):
        placed_symbols = VGroup()
        
        for i, (symbol_tex, description, color, tier_name) in enumerate(symbols_data):
            # Create the symbol (smaller size)
            symbol = MathTex(symbol_tex, font_size=32, color=WHITE)
            symbol.move_to(LEFT * 4 + UP * (1 - i * 0.3))
            
            # Show symbol with dramatic entrance
            self.play(
                Write(symbol, run_time=0.8),
                symbol.animate.scale(1.5).set_color(YELLOW),
                rate_func=rush_from
            )
            self.play(symbol.animate.scale(1/1.5).set_color(WHITE))
            
            # Show description (smaller text)
            desc_text = Text(f'"{description}"', font_size=20, color=GREY)
            desc_text.next_to(symbol, DOWN, buff=0.2)
            self.play(Write(desc_text), run_time=0.6)
            self.wait(0.5)
            
            # Find target tier box
            tier_index = ["HARMLESS", "ANNOYING", "SCARY", "NIGHTMARE", "FINAL BOSS"].index(tier_name)
            target_box = tier_boxes[4 - tier_index]  # Reverse order since we start from top
            
            # Move to tier with dramatic effect - position in the symbol area of the box
            target_pos = target_box[0].get_center() + LEFT * 1.2
            
            # Trauma level announcement (smaller text)
            trauma_announcement = Text(f"TRAUMA LEVEL: {tier_name}!", 
                                     font_size=22, color=color, weight=BOLD)
            trauma_announcement.next_to(symbol, UP, buff=0.5)
            
            self.play(Write(trauma_announcement), run_time=0.6)
            self.wait(0.3)
            
            # Move symbol to tier
            self.play(
                symbol.animate.move_to(target_pos).set_color(color),
                FadeOut(desc_text),
                FadeOut(trauma_announcement),
                run_time=1
            )
            
            # Add horizontal spacing for multiple symbols in same tier
            existing_in_tier = len([s for s in placed_symbols if abs(s.get_center()[1] - target_pos[1]) < 0.1])
            if existing_in_tier > 0:
                symbol.shift(LEFT * 0.6 * existing_in_tier)  # Side by side spacing
            
            placed_symbols.add(symbol)
            self.wait(0.3)
        
        # Special dramatic moment for the final boss
        final_boss = placed_symbols[-1]  # ∇ should be last
        self.play(
            final_boss.animate.scale(1.5).set_color(PURPLE),
            rate_func=there_and_back,
            run_time=1
        )

    def final_reveal(self):
        # Clear everything except title, watermark, and ranked symbols
        
        # Final commentary - smaller font and better positioning
        final_steps = [
            "The tier list that haunts math students!",
            "If you see del operator, RUN!",
            "Comment your calculus trauma below!",
        ]
        
        # Position final text in center-left area - moved further left and smaller
        final_text = Text(final_steps[0], font_size=28, color=GOLD).move_to(LEFT * 3.5 + DOWN * 2)
        self.play(Write(final_text), run_time=0.8)
        self.wait(1)
        
        for i in range(1, 3):
            color = [PURPLE, RED][i-1]
            new_step = Text(final_steps[i], font_size=28, color=color).move_to(LEFT * 3.5 + DOWN * 2)
            self.play(Transform(final_text, new_step), run_time=0.8)
            self.wait(1)
        
        # Add some floating trauma symbols for effect
        trauma_symbols = VGroup()
        for _ in range(5):
            scary_symbol = MathTex(r"\nabla", font_size=60, color=PURPLE)
            scary_symbol.move_to([
                np.random.uniform(-3, 1),
                np.random.uniform(-3, 1),
                0
            ])
            scary_symbol.set_opacity(0.2)
            trauma_symbols.add(scary_symbol)
        
        self.play(
            LaggedStart(*[FadeIn(s, scale=2) for s in trauma_symbols], lag_ratio=0.1),
            run_time=1.5
        )
        
        # Final frame effect - remove the problematic VGroup line
        final_frame = RoundedRectangle(
            width=14, height=8,
            corner_radius=0.3,
            color=PURPLE,
            stroke_width=6,
            fill_opacity=0.05
        )
        
        # Add final text overlay
        overlay_text = Text("CALCULUS TRAUMA TIER LIST", 
                          font_size=28, color=GOLD, weight=BOLD)
        overlay_text.to_edge(DOWN, buff=0.5)
        
        self.play(
            Create(final_frame),
            Write(overlay_text),
            run_time=1.2
        )
        
        # Quick pulse effect
        self.play(
            final_frame.animate.set_stroke(width=10).set_fill(opacity=0.1),
            rate_func=there_and_back,
            run_time=0.8
        )
        
        self.wait(1.5)