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
        self.play(sub_title1.animate.to_edge(UP))

        mtext1 = MathTex(
            "x'(t) = a_{11} \cdot x(t) + a_{12} \cdot y(t)"
        ).scale(0.75)
        mtext1[0][0:5].set_fill(RED)
        mtext1[0][6:9].set_fill(YELLOW)
        mtext1[0][10:14].set_fill(GREEN)
        mtext1[0][15:18].set_fill(YELLOW)
        mtext1[0][19:23].set_fill(GREEN)

        mtext2 = MathTex(
                "y'(t) = a_{21} \cdot x(t) + a_{22} \cdot y(t)"
            ).scale(0.75).next_to(mtext1, DOWN)
        mtext2[0][0:5].set_fill(RED)
        mtext2[0][6:9].set_fill(YELLOW)
        mtext2[0][10:14].set_fill(GREEN)
        mtext2[0][15:18].set_fill(YELLOW)
        mtext2[0][19:23].set_fill(GREEN)

        self.play(Write(VGroup(mtext1, mtext2)))
        self.wait(2)

        sub_title2 = Tex(
            "Ezt felírhatjuk matrixok szorzataként is"
        ).scale(0.90).to_edge(UP)

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
        ).set_color(GREEN)
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
        ).scale(0.90).to_edge(UP)

        self.play(ReplacementTransform(sub_title2, sub_title3))

        self.wait()

        matrix_eq2 = MathTex(
            "X' = A \\times X"
        ).scale(1.20)
        matrix_eq2[0][0:2].set_fill(RED)
        matrix_eq2[0][3].set_fill(YELLOW)
        matrix_eq2[0][5].set_fill(GREEN)

        self.play(ReplacementTransform(matrix_eq1, matrix_eq2), run_time=2)
        self.wait()

        sub_title4 = Tex(
            "Az egyenlet megoldásához meg kell oldjuk a következő sajátérték és sajátvektor rendszert"
        ).scale(0.90).to_edge(UP)

        self.play(ReplacementTransform(sub_title3, sub_title4))
        self.wait(2)

        matrix_eq3 = MathTex(
            "(A - \\lambda I_{2})X = 0"
        ).scale(1.20)
        matrix_eq3[0][1].set_fill(YELLOW)
        matrix_eq3[0][3].set_fill(BLUE)
        matrix_eq3[0][7].set_fill(BLUE)

        self.play(ReplacementTransform(matrix_eq2, matrix_eq3), run_time=2)
        self.wait()

        hint = MathTex(
            "\\text{Ahol } \\lambda \\text{ jelöli a rendszer sajátértékeit és } X \\text{ a sajátvektorait}", color=BLUE
        ).to_edge(DOWN).shift(UP * 2).scale(0.75)

        self.play(FadeIn(hint))
        self.wait(2)
        self.play(FadeOut(hint))
        self.wait()

        sub_title5 = Tex(
            "Sajátérték kíszámításához a következő egyenlőséget kell meghatározzuk"
        ).scale(0.90).to_edge(UP)

        self.play(ReplacementTransform(sub_title4, sub_title5))
        self.wait(2)

        eigenvalues = MathTex(
            "det(A - \\lambda I_{2}) = 0"
        ).scale(1.20)
        eigenvalues[0][4].set_fill(YELLOW)
        eigenvalues[0][6].set_fill(BLUE)

        self.play(ReplacementTransform(matrix_eq3, eigenvalues), run_time=2)
        self.wait(2)

        sub_title6 = MathTex(
            "\\text{Az egyenlet megoldásával kapunk két } \\lambda_{1}, \\lambda_{2} \\text{ értéket}"
        ).scale(0.90).to_edge(UP)

        self.play(ReplacementTransform(sub_title5, sub_title6))
        self.wait(2)

        text_lambda1 = MathTex(
            "\\lambda_{1}", color=BLUE
        ).scale(0.90).next_to(eigenvalues, DL).shift(DL)
        text_lambda2 = MathTex(
            "\\lambda_{2}", color=BLUE
        ).scale(0.90).next_to(eigenvalues, DR).shift(DR)

        arrow1 = Line(
            start=eigenvalues.get_bottom(), end=text_lambda1.get_top(), buff=0.2
        ).add_tip().scale(0.75)
        arrow2 = Line(
            start=eigenvalues.get_bottom(), end=text_lambda2.get_top(), buff=0.2
        ).add_tip().scale(0.75)

        self.play(Create(VGroup(text_lambda1, arrow1, text_lambda2, arrow2)), run_time=2)
        self.wait(2)

        sub_title7 = Tex(
            "Ennek a segítségével felírhatjuk a következő két egyenlőséget\\\\ a sajátvektor kiszámításához"
        ).scale(0.90).to_edge(UP)

        self.play(ReplacementTransform(sub_title6, sub_title7))
        self.wait(2)

        eigenvectors_eq1 = MathTex(
            "(A - \\lambda_{1} I_{2})X_{1} = 0"
        ).scale(1.20)
        eigenvectors_eq1[0][1].set_fill(YELLOW)
        eigenvectors_eq1[0][3:5].set_fill(BLUE)
        eigenvectors_eq1[0][8:10].set_fill(BLUE)

        eigenvectors_eq2 = MathTex(
            "(A - \\lambda_{2} I_{2})X_{2} = 0"
        ).scale(1.20).next_to(eigenvectors_eq1, DOWN)
        eigenvectors_eq2[0][1].set_fill(YELLOW)
        eigenvectors_eq2[0][3:5].set_fill(BLUE)
        eigenvectors_eq2[0][8:10].set_fill(BLUE)

        self.play(
            ReplacementTransform(
                VGroup(eigenvalues, text_lambda1, arrow1, text_lambda2, arrow2),
                VGroup(eigenvectors_eq1, eigenvectors_eq2)
            ), run_time=2
        )
        self.wait(2)

        sub_title8 = Tex(
            "Miután meghatároztuk a sajátértékeket és sajátvektorokat\\\\Felírhatjuk a megoldást"
        ).scale(0.90).to_edge(UP)

        self.play(ReplacementTransform(sub_title7, sub_title8))
        self.wait(2)

        sol_text = MathTex(
            "X = c_{1} e^{\\lambda_{1} t} X_{1} + c_{2} e^{\\lambda_{2} t} X_{2}"
        ).scale(1.2)
        sol_text[0][0].set_fill(GREEN)
        sol_text[0][5:7].set_fill(BLUE)
        sol_text[0][8:10].set_fill(BLUE)
        sol_text[0][14:16].set_fill(BLUE)
        sol_text[0][17:19].set_fill(BLUE)

        self.play(ReplacementTransform(VGroup(eigenvectors_eq1, eigenvectors_eq2), sol_text), run_time=2)
        self.wait(3)

        sol_text1 = MathTex(
            "x(t) = c_{1} e^{\\lambda_{1} t} x_{11} + c_{2} e^{\\lambda_{2} t} x_{21}"
        ).scale(1.1)
        sol_text2 = MathTex(
            "y(t) = c_{2} e^{\\lambda_{1} t} x_{12} + c_{2} e^{\\lambda_{2} t} x_{22}"
        ).scale(1.1).next_to(sol_text1, DOWN)
        sol_text1[0][0:4].set_fill(GREEN)
        sol_text1[0][8:10].set_fill(BLUE)
        sol_text1[0][11:14].set_fill(BLUE)
        sol_text1[0][18:20].set_fill(BLUE)
        sol_text1[0][21:24].set_fill(BLUE)
        sol_text2[0][0:4].set_fill(GREEN)
        sol_text2[0][8:10].set_fill(BLUE)
        sol_text2[0][11:14].set_fill(BLUE)
        sol_text2[0][18:20].set_fill(BLUE)
        sol_text2[0][21:24].set_fill(BLUE)

        self.play(ReplacementTransform(sol_text, VGroup(sol_text1, sol_text2)), run_time=2)
        self.wait(3)

        self.play(Uncreate(VGroup(sol_text1, sol_text2)), FadeOut(sub_title8))

