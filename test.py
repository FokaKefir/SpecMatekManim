from manim import *
"""
    run in terminal
    > manim -pql test.py CreateCircle
    > manim -pql test.py Pith -r 1920,1080
    > manim -pql test.py Testing -r 1280,720
    > manim -pql test.py Testing -r 1280,720 --fps 30
    > manim -pqm test.py Testing 
        (720p30)
    > manim -pqh test.py Testing 
        (1080p60)
    
"""
# manim options: https://3b1b.github.io/manim/getting_started/configuration.html


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class Pith(Scene):
    def construct(self):
        sq = Square(side_length=5, stroke_color=GREEN, fill_color=BLUE, fill_opacity=0.75)
        self.play(Create(sq), run_time=3)
        self.wait()


class Testing(Scene):
    def construct(self):
        name = Tex("Babos David").to_edge(UL, buff=0.5)
        sq = Square(side_length=0.5, fill_color=GREEN, fill_opacity=0.75).shift(LEFT*3)
        tri = Triangle().scale(0.6).to_edge(DR)

        self.play(Write(name))
        self.play(DrawBorderThenFill(sq), run_time=2)
        self.play(Create(tri))
        self.wait()

        self.play(name.animate.to_edge(UR), run_time=2)
        self.play(sq.animate.scale(2), tri.animate.to_edge(DL), run_time=3)
        self.wait()


class Getters(Scene):
    def construct(self):
        rect = Rectangle(color=WHITE, height=3, width=2.5).to_edge(UL)
        circ = Circle().to_edge(DOWN)
        arrow = always_redraw(
            lambda: Line(
                start=rect.get_bottom(), end=circ.get_top(), buff=0.2
            ).add_tip()
        )

        self.play(Create(VGroup(rect, circ, arrow)))
        self.wait()
        self.play(rect.animate.to_edge(UR), circ.animate.scale(0.5), run_time=4)


class Updaters(Scene):
    def construct(self):
        num = MathTex("ln(2)")
        box = always_redraw(
            lambda: SurroundingRectangle(
                num, color=BLUE, fill_opacity=0.4, fill_color=RED, buff=0.5
            )
        )
        name = always_redraw(lambda: Tex("Babi").next_to(box, DOWN, buff=0.25))

        self.play(Create(VGroup(num, box, name)))
        self.play(num.animate.shift(RIGHT * 2), run_time=2)
        self.wait()


class ValueTrackers(Scene):
    def construct(self):
        k = ValueTracker(5)

        num = always_redraw(lambda: DecimalNumber().set_value(k.get_value()))

        self.play(FadeIn(num))
        self.wait()
        self.play(k.animate.set_value(0), run_time=5, rate_func=smooth)
        self.wait()


class Graphing(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-4, 4, 2], x_length=7, y_range=[0, 16, 4], y_length=5
        ).to_edge(DOWN).add_coordinates()

        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")

        parab = plane.plot(lambda x: x ** 2, x_range=[-4, 4], color=GREEN)
        func_label = MathTex("f(x)={x}^{2}").scale(0.6).next_to(parab, UR, buff=0.5).set_color(GREEN)

        area = plane.get_riemann_rectangles(graph=parab, x_range=[-2, 3], dx=0.2, stroke_width=0.1, stroke_color=WHITE)

        self.play(DrawBorderThenFill(plane))
        self.play(Create(VGroup(labels, parab, func_label)))
        self.wait()
        self.play(Create(area))
        self.wait()


class UpdateGraphing(Scene):
    def construct(self):
        k = ValueTracker(-4)

        ax = Axes(
            x_range=[-4, 4, 1], y_range=[-2, 16, 2], x_length=10, y_length=6
        ).to_edge(DOWN).add_coordinates().set_color(WHITE)

        func = ax.plot(lambda x: x ** 2, x_range=[-4, 4], color=BLUE)

        slope = always_redraw(
            lambda: ax.get_secant_slope_group(
                x=k.get_value(), graph=func, dx=0.01, secant_line_color=GREEN, secant_line_length=3
            )
        )

        pt = always_redraw(
            lambda: Dot().move_to(
                ax.c2p(k.get_value(), func.underlying_function(k.get_value()))
            )
        )

        self.add(ax, func, slope, pt)
        self.wait()
        self.play(k.animate.set_value(4), run_time=3)
