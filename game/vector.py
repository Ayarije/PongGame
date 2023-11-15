from math import sqrt, acos
from random import random
import pygame


class Vector:
    def __init__(self, x, y=None) -> None:
        if type(x) == type((0, 0)):
            if len(x) == 2:
                try:
                    x = list(x)
                    x[0] = float(x[0])
                    x[1] = float(x[1])
                except TypeError as error:
                    raise error
                self.x, self.y = x
            else:
                raise TypeError('tuple too short or too long')
        else:
            self.x = float(x)
            self.y = float(y)

    # Vector operator functions
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x + other.x, self.y + other.y)
        return Vector(self.x + other, self.y + other)
    
    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x - other.x, self.y - other.y)
        return Vector(self.x - other, self.y - other)
    
    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x * other.x, self.y * other.y)
        return Vector(self.x * other, self.y * other)
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x / other.x, self.y / other.y)
        return Vector(self.x / other, self.y / other)
    
    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        return self.x == other and self.y == other

    def __str__(self) -> str:
        return f'v({self.x}, {self.y})'
    
    def get_content(self) -> tuple[int, int]:
        return int(self.x), int(self.y)

    def apply(self, rect: pygame.Rect) -> pygame.Rect:
        return pygame.Rect(rect.x+self.x, rect.y+self.y, rect.width, rect.height)

def dot(vec1: Vector, vec2: Vector) -> float:
    return vec1.x * vec2.x + vec1.y * vec2.y

def angle_between(vec1: Vector, vec2: Vector) -> float:
    return acos(dot(vec1, vec2))

def length_sqr(vec: Vector) -> float:
    return vec.x**2 + vec.y**2

def dist_sqr(vec1: Vector, vec2: Vector):
    return length_sqr(vec1 - vec2)

def length(vec: Vector) -> float:
    return sqrt(length_sqr(vec))

def dist(vec1: Vector, vec2: Vector) -> float:
    return sqrt(dist(vec1, vec2))

def normalize(vec: Vector) -> Vector:
    vec_length = length(vec)
    if vec_length < 0.00001:
        Vector(0, 0)
    return Vector(vec.x / vec_length, vec.y / vec_length)

def reflect(incident: Vector, normal: Vector) -> Vector:
    return incident - dot(normal, incident) * 2.0 * normal

def negate(vec: Vector) -> Vector:
    return Vector(-vec.x, -vec.y)

def right(vec: Vector) -> Vector:
    return Vector(-vec.y, vec.x)

def left(vec: Vector) -> Vector:
    return negate(right(vec))

def random_vector() -> Vector:
    return Vector(random() * 2.0 - 1.0, random() * 2.0 - 1.0)

def random_direction() -> Vector:
    return normalize(random_vector())

def copy(vec: Vector) -> Vector:
    return Vector(vec.x, vec.y)
