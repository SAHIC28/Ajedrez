from enum import StrEnum

class Pieza:
    def __init__(self,color):
        self.color=color

class Color(StrEnum):
    BLANCO="blanco"
    NEGRO="negro"

class Peon(Pieza):
    ...

class Alfil(Pieza):
    ...

class Caballo(Pieza):
    ...

class Torre(Pieza):
    ...

class Reina(Pieza):
    ...

class Rey(Pieza):
    ...

