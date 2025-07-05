from itertools import product

def generar_tabla_verdad(n):
    return list(product([0, 1], repeat=n))

def construir_sop(variables, salidas):
    tabla = generar_tabla_verdad(len(variables))
    términos = []

    for i, fila in enumerate(tabla):
        if salidas[i] == 1:
            término = []
            for j, bit in enumerate(fila):
                if bit == 1:
                    término.append(variables[j])
                else:
                    término.append(f"¬{variables[j]}")
            términos.append("(" + " ∧ ".join(término) + ")")

    return " ∨ ".join(términos)

def main():
    print("Ingrese número de variables (2 o 3):")
    n = int(input("> "))
    variables = ["A", "B", "C"][:n]

    print(f"\nVariables: {variables}")
    tabla = generar_tabla_verdad(n)

    print("\nIngrese los valores de salida (0 o 1) para cada fila:")
    salidas = []
    for fila in tabla:
        valores = ", ".join(f"{var}={val}" for var, val in zip(variables, fila))
        salida = int(input(f"{valores} => "))
        salidas.append(salida)

    print("\nTabla de Verdad:")
    for fila, salida in zip(tabla, salidas):
        print(" | ".join(map(str, fila)) + f" => {salida}")

    expresion = construir_sop(variables, salidas)
    print("\nExpresión SOP generada:")
    print(expresion)

if __name__ == "__main__":
    main()
