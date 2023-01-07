from manim import *
"""
    > manim -pqm main.py SystemOfDiffEquation
"""


class SystemOfDiffEquation(Scene):
    def construct(self):
        title = Tex("Állandó együtthatójú lineáris differenciálegyenlet-rendszer")

        self.play(Create(title), run_time=2)
        self.wait(2)
        self.play(FadeOut(title))
        self.wait()

        sub_title1 = Tex("Általános alakja:").scale(0.90)

        self.play(Create(sub_title1))
        self.wait()
        self.play(sub_title1.animate.to_edge(UL))

        mtext1 = MathTex(
            "x'(t) = a_{11} \cdot x(t) + a_{12} \cdot y(t)"
        ).scale(0.75)
        mtext1[0][0:5].set_fill(RED)
        mtext1[0][6:9].set_fill(YELLOW)
        mtext1[0][10:14].set_fill(BLUE)
        mtext1[0][15:18].set_fill(YELLOW)
        mtext1[0][19:23].set_fill(BLUE)

        mtext2 = MathTex(
                "y'(t) = a_{21} \cdot x(t) + a_{22} \cdot y(t)"
            ).scale(0.75).next_to(mtext1, DOWN)
        mtext2[0][0:5].set_fill(RED)
        mtext2[0][6:9].set_fill(YELLOW)
        mtext2[0][10:14].set_fill(BLUE)
        mtext2[0][15:18].set_fill(YELLOW)
        mtext2[0][19:23].set_fill(BLUE)

        self.play(Write(VGroup(mtext1, mtext2)))
        self.wait(2)

        sub_title2 = Tex(
            "Ezt felírhatjuk matrixok szorzataként is"
        ).scale(0.90).to_edge(UL)

        self.play(ReplacementTransform(sub_title1, sub_title2))
        self.wait()

        vecXDer = Matrix(
            [["x'"], ["y'"]],
            left_bracket="(",
            right_bracket=")"
        ).set_color(RED)
        matA = Matrix(
            [["a_{11}", "a_{12}"], ["a_{21}", "a_{22}"]],
            left_bracket="(",
            right_bracket=")"
        ).set_color(YELLOW)
        vecX = Matrix(
            [["x"], ["y"]],
            left_bracket="(",
            right_bracket=")"
        ).set_color(BLUE)
        txt_equal = MathTex("=")
        txt_times = MathTex("\\times")

        txt_equal.next_to(matA, LEFT)
        vecXDer.next_to(txt_equal, LEFT)
        txt_times.next_to(matA, RIGHT)
        vecX.next_to(txt_times, RIGHT)

        matrix_eq1 = VGroup(vecXDer, txt_equal, matA, txt_times, vecX).scale(0.75)

        self.play(
            ReplacementTransform(
                VGroup(mtext1, mtext2),
                matrix_eq1
            ), run_time=2
        )
        self.wait()

        sub_title3 = Tex(
            "Amit a következőképpen fogunk jelölni"
        ).scale(0.90).to_edge(UL)

        self.play(ReplacementTransform(sub_title2, sub_title3))

        self.wait()

        matrix_eq2 = MathTex(
            "X' = A \\times X"
        ).scale(1.20)
        matrix_eq2[0][0:2].set_fill(RED)
        matrix_eq2[0][3].set_fill(YELLOW)
        matrix_eq2[0][5].set_fill(BLUE)

        self.play(ReplacementTransform(matrix_eq1, matrix_eq2))
        self.wait()

        sub_title4 = Tex(
            "Az egyenlet megoldásához meg kell oldjuk a következő sajátérték és sajátvektor rendszert"
        ).scale(0.90).to_edge(UL)

        self.play(ReplacementTransform(sub_title3, sub_title4))
        self.wait()

        matrix_eq3 = MathTex(
            "(A - \\lambda I_{2})X = 0"
        ).scale(1.20)
        matrix_eq3[0][1].set_fill(YELLOW)
        matrix_eq3[0][3].set_fill(BLUE)
        matrix_eq3[0][7].set_fill(BLUE)

        self.play(ReplacementTransform(matrix_eq2, matrix_eq3))
        self.wait()


