from enum import StrEnum
from tablero import TableroAjedrez
class Pieza:
    def __init__(self,color):
        self.color=color
    def can_move(self,tablero:TableroAjedrez,casilla_inicial,casilla_final):
        fila, columna=casilla_final
        if tablero.tablero[fila][columna].color==self.color==self.color:
            return False
        return True


class Color(StrEnum):
    BLANCO="blanco"
    NEGRO="negro"

class Peon(Pieza):
    def can_move(self,tablero:TableroAjedrez,casilla_inicial,casilla_final):
        super().can_move(tablero,casilla_inicial,casilla_final)

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

