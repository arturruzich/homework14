from homework_16.Figures.Figure import Figure
from homework_16.Figures.Rectange import Rectange
from homework_16.Figures.Square import Square
from homework_16.Figures.Triangle import Triangle

square_f: Square = Square(10)

rectange: Rectange = Rectange(10, 5)

triangle: Triangle = Triangle(5, 6, 9,3)

figures_list: list[Figure] = [square_f, rectange,triangle]

list_tuple_perimetr_and_square: list[tuple[int, object]] = [(figure.calculate_perimetr(), figure.calculate_square()) for
                                                            figure in figures_list]

for item in list_tuple_perimetr_and_square:
    print(item[0], item[1])