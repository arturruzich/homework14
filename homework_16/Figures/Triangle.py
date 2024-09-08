

from homework_16.Figures.Figure import Figure


class Triangle(Figure):

    __trianlge_a: int
    __trianlge_b: int
    __trianlge_c: int
    __height: int

    def __init__(self, trianlge_a: int,trianlge_b: int,trianlge_c: int, height: int):
        self.__height = height
        self.__trianlge_a = trianlge_a
        self.__trianlge_b = trianlge_b
        self.__trianlge_c = trianlge_c


    def calculate_perimetr(self) -> int:
        return self.__trianlge_a + self.__trianlge_b + self.__trianlge_c


    def calculate_square(self) -> float:
        return 0.5 * self.__trianlge_a * self.__height