

from homework_16.Figures.Figure import Figure


class Rectange(Figure):

    __rectange_a: int
    __rectange_b: int

    def __init__(self, rectange_a: int, rectange_b: int):
        self.__rectange_a = rectange_a
        self.__rectange_b = rectange_b


    def calculate_perimetr(self) -> int:
        return (self.__rectange_a * 2) + (self.__rectange_b * 2)


    def calculate_square(self):
        return  self.__rectange_a * self.__rectange_b