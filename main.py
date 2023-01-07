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
            "Ennek a segítségével felírhatjuk a következő két egyenlőséget\\\\ a sajátvektorok kiszámításához"
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

        # Example part

        ex_title1 = Tex(
            "Oldjuk meg a feladatot a következő példára:"
        ).scale(0.90).to_edge(UP)

        self.play(Write(ex_title1))
        self.wait()

        ex_mtext1 = MathTex(
            "x' = 2x + 2y"
        ).scale(0.75)
        ex_mtext2 = MathTex(
            "y' = x + 3y"
        ).scale(0.75).next_to(ex_mtext1, DOWN)

        self.play(Write(VGroup(ex_mtext1, ex_mtext2)), run_time=2)
        self.wait(2)

        ex_vecXDer = Matrix(
            [["x'"], ["y'"]],
            left_bracket="(",
            right_bracket=")"
        )#.set_color(RED)
        ex_matA = IntegerMatrix(
            [[2, 2], [1, 3]],
            left_bracket="(",
            right_bracket=")"
        )#.set_color(YELLOW)
        ex_vecX = Matrix(
            [["x"], ["y"]],
            left_bracket="(",
            right_bracket=")"
        )#.set_color(GREEN)
        ex_txt_equal = MathTex("=")
        ex_txt_times = MathTex("\\times")

        ex_txt_equal.next_to(ex_matA, LEFT)
        ex_vecXDer.next_to(ex_txt_equal, LEFT)
        ex_txt_times.next_to(ex_matA, RIGHT)
        ex_vecX.next_to(ex_txt_times, RIGHT)

        ex_matrix_eq1 = VGroup(ex_vecXDer, ex_txt_equal, ex_matA, ex_txt_times, ex_vecX).scale(0.75)

        self.play(
            ReplacementTransform(
                VGroup(ex_mtext1, ex_mtext2),
                ex_matrix_eq1
            ), run_time=2
        )
        self.wait()
        self.play(ex_matrix_eq1.animate.shift(UP*2))
        self.wait(2)

        ex_eigenvalues = MathTex(
            "det(A - \\lambda I_{2}) = 0"
        )

        self.play(Create(ex_eigenvalues))
        self.wait(2)

        ex_det = Matrix(
            [["2 - \\lambda", "2  "], ["1  ", "3 - \\lambda"]],
            left_bracket="|",
            right_bracket="|"
        ).shift(LEFT * 0.4)
        ex_txt_equal_zero = MathTex("=0").next_to(ex_det, RIGHT)

        self.play(ReplacementTransform(ex_eigenvalues, VGroup(ex_det, ex_txt_equal_zero)))
        self.wait(3)

        ex_det_calc1 = MathTex(
            "(2 - \\lambda)(3 - \\lambda) - 2"
        ).next_to(ex_txt_equal_zero, LEFT)

        self.play(ReplacementTransform(ex_det, ex_det_calc1))
        self.wait(3)

        ex_det_calc2 = MathTex(
            "\\lambda^2 -5 \\lambda + 4"
        ).next_to(ex_txt_equal_zero, LEFT)

        self.play(ReplacementTransform(ex_det_calc1, ex_det_calc2))
        self.wait(3)

        ex_det_calc3 = MathTex(
            "(\\lambda - 1) (\\lambda -4)"
        ).next_to(ex_txt_equal_zero, LEFT)

        self.play(ReplacementTransform(ex_det_calc2, ex_det_calc3))
        self.wait(3)

        ex_text_lambda1 = MathTex(
            "\\lambda_{1}=1"
        ).scale(0.90).next_to(ex_det_calc3, DL).shift(DL)
        ex_text_lambda2 = MathTex(
            "\\lambda_{2}=4"
        ).scale(0.90).next_to(ex_det_calc3, DR).shift(DR)

        ex_arrow1 = Line(
            start=ex_det_calc3.get_bottom(), end=ex_text_lambda1.get_top(), buff=0.2
        ).add_tip().scale(0.75)
        ex_arrow2 = Line(
            start=ex_det_calc3.get_bottom(), end=ex_text_lambda2.get_top(), buff=0.2
        ).add_tip().scale(0.75)

        self.play(Create(VGroup(ex_text_lambda1, ex_arrow1, ex_text_lambda2, ex_arrow2)), run_time=2)
        self.wait(2)
        self.play(
            Uncreate(VGroup(ex_arrow1, ex_arrow2, ex_text_lambda2, ex_det_calc3, ex_txt_equal_zero))
        )
        self.play(ex_text_lambda1.animate.shift(UP * 2.3))
        self.wait()

        ex_matA1 = IntegerMatrix(
            [[1, 2], [1, 2]],
            left_bracket="(",
            right_bracket=")"
        )
        ex_vecX1 = Matrix(
            [["x_1"], ["x_2"]],
            left_bracket="(",
            right_bracket=")"
        ).next_to(ex_matA1, RIGHT)
        ex_txt_equal1 = MathTex("=").next_to(ex_vecX1, RIGHT)
        ex_vec_zero1 = IntegerMatrix(
            [[0], [0]],
            left_bracket="(",
            right_bracket=")"
        ).next_to(ex_txt_equal1, RIGHT)

        ex_eigenvector_eq1 = VGroup(ex_matA1, ex_vecX1, ex_txt_equal1, ex_vec_zero1).scale(0.75).shift(LEFT * 1.5 + DOWN)

        self.play(Create(ex_eigenvector_eq1), run_time=3)
        self.wait()
        self.play(ex_eigenvector_eq1.animate.shift(LEFT * 2))

        ex_ar1 = Arrow(
            LEFT, RIGHT
        ).next_to(ex_eigenvector_eq1, RIGHT)

        ex_ev_sys11 = MathTex(
            "x_1 + 2 x_2 = 0"
        ).scale(0.75)
        ex_ev_sys12 = MathTex(
            "x_1 + 2 x_2 = 0"
        ).scale(0.75).next_to(ex_ev_sys11, DOWN)
        ex_ev_sys1 = VGroup(ex_ev_sys11, ex_ev_sys12).next_to(ex_ar1, RIGHT)

        self.play(Create(VGroup(ex_ar1, ex_ev_sys1)), run_time=2)
        self.wait(2)

        ex_ev_txt1 = MathTex(
            "x_1 = -2 x_2"
        ).scale(0.75).next_to(ex_ar1, RIGHT)

        self.play(ReplacementTransform(ex_ev_sys1, ex_ev_txt1))
        self.wait()

        ex_ev_res1 = MathTex("X_1 = ").scale(0.75).next_to(ex_matA1, DOWN * 2.5)

        ex_vecX1_res1 = Matrix(
            [["x_1"], ["x_2"]],
            left_bracket="(",
            right_bracket=")"
        ).next_to(ex_ev_res1, RIGHT).scale(0.75)

        self.play(Create(VGroup(ex_ev_res1, ex_vecX1_res1)))
        self.wait()

        ex_vecX1_res2 = Matrix(
            [["-2 x_2"], ["x_2"]],
            left_bracket="(",
            right_bracket=")"
        ).next_to(ex_ev_res1, RIGHT).scale(0.75)

        self.play(ReplacementTransform(ex_vecX1_res1, ex_vecX1_res2))
        self.wait()

        ex_vecX1_res3 = IntegerMatrix(
            [[-2], [1]],
            left_bracket="(",
            right_bracket=")"
        ).next_to(ex_ev_res1, RIGHT).scale(0.75)

        self.play(ReplacementTransform(ex_vecX1_res2, ex_vecX1_res3))
        self.wait(2)

        ex_text_lambda2 = MathTex(
            "\\lambda_{2}=4"
        ).scale(0.90).next_to(ex_text_lambda1, ORIGIN)

        self.play(
            Uncreate(VGroup(ex_eigenvector_eq1, ex_ar1, ex_ev_txt1, ex_ev_res1, ex_vecX1_res3))
        )
        self.play(ReplacementTransform(ex_text_lambda1, ex_text_lambda2))
        self.wait(2)

        ex_matA2 = IntegerMatrix(
            [[-2, 2], [1, -1]],
            left_bracket="(",
            right_bracket=")"
        )
        ex_vecX2 = Matrix(
            [["x_3"], ["x_4"]],
            left_bracket="(",
            right_bracket=")"
        ).next_to(ex_matA2, RIGHT)
        ex_txt_equal2 = MathTex("=").next_to(ex_vecX2, RIGHT)
        ex_vec_zero2 = IntegerMatrix(
            [[0], [0]],
            left_bracket="(",
            right_bracket=")"
        ).next_to(ex_txt_equal2, RIGHT)

        ex_eigenvector_eq2 = VGroup(ex_matA2, ex_vecX2, ex_txt_equal2, ex_vec_zero2).scale(0.75).shift(
            LEFT * 1.5 + DOWN)

        self.play(Create(ex_eigenvector_eq2), run_time=3)
        self.wait()
        self.play(ex_eigenvector_eq2.animate.shift(LEFT * 2))

        ex_ar2 = Arrow(
            LEFT, RIGHT
        ).next_to(ex_eigenvector_eq2, RIGHT)

        ex_ev_sys21 = MathTex(
            "-2 x_3 + 2 x_4 = 0"
        ).scale(0.75)
        ex_ev_sys22 = MathTex(
            "x_3 - x_4 = 0"
        ).scale(0.75).next_to(ex_ev_sys21, DOWN)
        ex_ev_sys2 = VGroup(ex_ev_sys21, ex_ev_sys22).next_to(ex_ar2, RIGHT)

        self.play(Create(VGroup(ex_ar2, ex_ev_sys2)), run_time=2)
        self.wait(2)

        ex_ev_txt2 = MathTex(
            "x_3 = x_4"
        ).scale(0.75).next_to(ex_ar2, RIGHT)

        self.play(ReplacementTransform(ex_ev_sys2, ex_ev_txt2))
        self.wait()

        ex_ev_res2 = MathTex("X_2 = ").scale(0.75).next_to(ex_matA2, DOWN * 2.5)

        ex_vecX2_res1 = Matrix(
            [["x_3"], ["x_4"]],
            left_bracket="(",
            right_bracket=")"
        ).next_to(ex_ev_res2, RIGHT).scale(0.75)

        self.play(Create(VGroup(ex_ev_res2, ex_vecX2_res1)))
        self.wait()

        ex_vecX2_res2 = Matrix(
            [["x_4"], ["x_4"]],
            left_bracket="(",
            right_bracket=")"
        ).next_to(ex_ev_res2, RIGHT).scale(0.75)

        self.play(ReplacementTransform(ex_vecX2_res1, ex_vecX2_res2))
        self.wait()

        ex_vecX2_res3 = IntegerMatrix(
            [[1], [1]],
            left_bracket="(",
            right_bracket=")"
        ).next_to(ex_ev_res2, RIGHT).scale(0.75)

        self.play(ReplacementTransform(ex_vecX2_res2, ex_vecX2_res3))
        self.wait(2)

        self.play(
            Uncreate(VGroup(ex_eigenvector_eq2, ex_ar2, ex_ev_txt2, ex_ev_res2, ex_vecX2_res3, ex_text_lambda2))
        )
        self.wait(2)

        ex_sol_text_template = MathTex(
            "X = c_{1} e^{\\lambda_{1} t} X_{1} + c_{2} e^{\\lambda_{2} t} X_{2}"
        )

        self.play(Create(ex_sol_text_template), run_time=2)
        self.wait(2)

        ex_sol_vecX = Matrix(
            [["x"], ["y"]],
            left_bracket="(",
            right_bracket=")"
        ).scale(0.8)

        ex_sol_text1 = MathTex(
            "= c_{1} e^{t}"
        ).next_to(ex_sol_vecX, RIGHT)

        ex_sol_vecX1 = IntegerMatrix(
            [[-2], [1]],
            left_bracket="(",
            right_bracket=")"
        ).next_to(ex_sol_text1, RIGHT).scale(0.8)

        ex_sol_text2 = MathTex(
            "c_{2} e^{4t}"
        ).next_to(ex_sol_vecX1, RIGHT)

        ex_sol_vecX2 = IntegerMatrix(
            [[1], [1]],
            left_bracket="(",
            right_bracket=")"
        ).next_to(ex_sol_text2, RIGHT).scale(0.8)

        ex_sol1 = VGroup(ex_sol_vecX, ex_sol_text1, ex_sol_vecX1, ex_sol_text2, ex_sol_vecX2).shift(LEFT * 2.6)

        self.play(ReplacementTransform(ex_sol_text_template, ex_sol1), run_time=2)
        self.wait(3)

        ex_sol_x = MathTex(
            "x = -2 c_1 e^{t} + c_2 e^{4t}"
        ).scale(0.75)
        ex_sol_y = MathTex(
            "y = c_1 e^{t} + c_2 e^{4t}"
        ).scale(0.75).next_to(ex_sol_x, DOWN)

        self.play(
            ReplacementTransform(
                ex_sol1,
                VGroup(ex_sol_x, ex_sol_y)
            ), run_time=2
        )
        self.wait(2)


