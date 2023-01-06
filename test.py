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
