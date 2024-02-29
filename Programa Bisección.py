def funcion_cuadratica(x, a, b, c):
    return a * x**2 + b * x + c


def metodo_biseccion(a, b, c, xi, xu, tolerancia=1e-6, max_iteraciones=100, Es=1e-4, valor_verdadero=None):
    if funcion_cuadratica(xi, a, b, c) * funcion_cuadratica(xu, a, b, c) > 0:
        print("Error: La función no cumple con el cambio de signo en efl intervalo dado.")
        return None

    # Si no se proporciona el valor verdadero, calcularlo a partir de la función
    if valor_verdadero is None or valor_verdadero == 0:
        valor_verdadero = funcion_cuadratica(xi, a, b, c)

    # Imprimir encabezado de la tabla
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
        "Iteración", "xi", "xu", "XR", "f(xi)*f(XR)", "EA", "ET", "EA < ES"))

    iteracion = 1
    xr = (xi + xu) / 2

    while abs(funcion_cuadratica(xr, a, b, c)) > tolerancia and iteracion <= max_iteraciones:
        fxixr = funcion_cuadratica(xi, a, b, c) * \
            funcion_cuadratica(xr, a, b, c)
        ea = abs((xr - xi) / xr) * 100
        et = abs((valor_verdadero - xr) / valor_verdadero) * 100
        ea_menor_es = ea < Es

        print("{:<10} {:<20.10f} {:<20.10f} {:<20.10f} {:<20.10f} {:<20.10f} {:<20.10f} {:<20}".format(
            iteracion, xi, xu, xr, fxixr, ea, et, ea_menor_es))

        if ea_menor_es:
            print(f"\nEA es menor que ES en la iteración {iteracion}.")
            break

        if fxixr < 0:
            xu = xr
        else:
            xi = xr

        xr = (xi + xu) / 2
        iteracion += 1

    if iteracion > max_iteraciones:
        print("Error: Se alcanzó el número máximo de iteraciones.")
        return None

    return xr


# Solicitar coeficientes de la ecuación cuadrática
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c:"))

# Solicitar límites inferior y superior
xi = float(input("Ingrese el límite inferior (xi): "))
xu = float(input("Ingrese el límite superior (xu): "))

# Solicitar el valor verdadero o calcularlo a partir de la función
valor_verdadero = float(
    input("Ingrese el valor verdadero (o ingrese 0 para calcularlo): "))

# Solicitar el margen de error (Es)
Es = float(input("Ingrese el margen de error (Es): "))

# Aplicar el método de bisección
raiz = metodo_biseccion(
    a, b, c, xi, xu, valor_verdadero=valor_verdadero, Es=Es)

# Imprimir resultado
if raiz is not None:
    print(f"\nLa raíz aproximada es: {raiz}")
