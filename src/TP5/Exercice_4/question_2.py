from ..Exercice_3.point import Point
from .rectangle import Rectangle

r1: Rectangle = Rectangle(1, 2, 3, 4)
r2: Rectangle = r1
print(f"r1 : {r1}, r2 : {r2}")
r1.coin_no = Point(0, 0)
print(f"r1 : {r1}, r2 : {r2}")
r1.coin_se.homothetie(2)
print(f"r1 : {r1}, r2 : {r2}")
