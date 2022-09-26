"""Properties"""


import string
from tokenize import String


class Article:
    """Re-Escribir el ejercicio anterior utilizando una property en vez de un
    método de instancia.

    Restricciones:
        - Utilizar 3 variables de instancia
        - Utilizar 1 property
        - Utilizar 1 variable de clase
        - Utilizar 1 método de clase
        - No utilizar métodos de instancia
        - No utilizar Dataclasses
        - Utilizar Type Hints en todos los métodos y variables
    """
    _iva = 0.21
    def __init__(self, nombre):
        self.nombre: string = nombre

    def __init__(self, descuento):
        self.descuento: int = descuento

    def __init__(self, costo):
        self.costo: int = costo

    @classmethod
    def actualizar_iva(self):
        return self._iva
    
    @property
    def dosdecimales(self):
        return round(self.costo, 2)

    @dosdecimales.setter
    def precio(self, costo):
        self.costo = costo

    def preciofinal(self):
        self.precio = (self.costo - self.descuento)+((self.costo - self.descuento)*self._iva)
        return self.precio

# NO MODIFICAR - INICIO
# Test parámetro obligatorio
try:
    article = Article()
    assert False, "No se puede instanciar sin nombre ni costo"
except TypeError:
    assert True

try:
    article = Article("Auto")
    assert False, "No se puede instanciar sin costo"
except TypeError:
    assert True

try:
    article = Article(nombre="Auto", costo=1)
    assert True
except TypeError:
    assert False, "El descuento es opcional"

try:
    article = Article(nombre="Auto", costo=1)
    article.precio = 2
    assert False, "No se puede modificar el precio"
except AttributeError:
    assert True


# Test básico
article = Article("Auto", 1)
assert article.nombre == "Auto"
assert article.precio == 1.21


article = Article("Auto", 1, 0.21)
assert article.nombre == "Auto"
assert article.precio == 0.96


# Test palabra clave
article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.precio == 1.21

article = Article(costo=1, nombre="Auto", descuento=0.21)
assert article.nombre == "Auto"
assert article.precio == 0.96


# Test de método de clase
Article.actualizar_iva(0.25)

article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.precio == 1.25
# NO MODIFICAR - FIN
