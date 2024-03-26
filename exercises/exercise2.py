"""Lógica Simple y Cortocircuito"""


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si al menos una de las variables es True.
"""

esta_lloviendo = True
riego_activado = True

# COMPLETAR - INICIO
if (esta_lloviendo == True) or (riego_activado == True):
    piso_mojado = True
else:
    piso_mojado = False
# COMPLETAR - FIN

assert piso_mojado


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el área es mayor a 5.
Restricción: Usar NOT.
"""

lado_cuadrado = 5
area_cuadrado = pow(lado_cuadrado, 2)

# COMPLETAR - INICIO
if not (area_cuadrado > 5) and (lado_cuadrado > 0):
    area_mayor_a_cinco = False
else:
    area_mayor_a_cinco = True
# COMPLETAR - FIN

assert area_mayor_a_cinco


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el número 1 es divisible por 7 y al mismo tiempo el número 2 no lo es.
"""

numero_1 = 49
numero_2 = 50

# COMPLETAR - INICIO
if (numero_1 % 7 == 0) and (numero_2 % 7 != 0):
    resultado = True
else:
    resultado = False
# COMPLETAR - FIN

assert resultado


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
el mismo valor de la variable 3.
Restricción: sólo usar OR, NOT y el mecanismo de cortocircuito.
"""

variable_01 = False
variable_02 = True
variable_03 = 80
variable_04 = "90"
variable_05 = 100

# COMPLETAR - INICIO
if not {(variable_01 == False) or (variable_02 == False) 
        or (variable_03 == 34) or (variable_04 == "90") 
        or (variable_05 == 54)}:
    resultado = False
else:
    resultado = variable_03

# COMPLETAR - FIN

assert resultado == 80