

Este programa tiene como objetivo **generar una expresión booleana en forma SOP (Suma de Productos)** a partir de una **tabla de verdad definida por el usuario**, utilizando los conceptos de álgebra booleana.

### 🔧 Módulo utilizado

```python
from itertools import product
```

* Se importa `product` desde el módulo `itertools` para generar todas las combinaciones posibles de 0 y 1 para las variables booleanas (es decir, la **tabla de verdad**).

---

### 📚 Funciones principales

#### 1. `generar_tabla_verdad(n)`

```python
def generar_tabla_verdad(n):
    return list(product([0, 1], repeat=n))
```

* **Entrada:** Número de variables booleanas (`n` = 2 o 3).
* **Salida:** Lista con todas las combinaciones binarias posibles para `n` variables.
* **Ejemplo:** Si `n = 2`, devuelve: `[(0,0), (0,1), (1,0), (1,1)]`.

---

#### 2. `construir_sop(variables, salidas)`

```python
def construir_sop(variables, salidas):
    ...
```

* **Entrada:** Lista de nombres de variables (ej. `["A", "B", "C"]`) y salidas de la tabla de verdad (lista de 0 y 1).
* **Proceso:**

  * Recorre cada fila de la tabla de verdad.
  * Si la **salida es 1**, construye un término producto (`AND`) basado en los valores de entrada:

    * Si la variable vale 1 ➝ se incluye directamente (ej. `A`)
    * Si la variable vale 0 ➝ se niega (ej. `¬A`)
  * Une los términos con el operador OR (`∨`) para formar la expresión completa en formato SOP.
* **Salida:** Cadena de texto con la expresión booleana en forma SOP.
* **Ejemplo:**
  Entrada → `A=0 B=1 C=0` con salida `1`
  Término generado → `(¬A ∧ B ∧ ¬C)`

---

### 🧠 Función principal

```python
def main():
    ...
```

* Pide al usuario el número de variables (2 o 3).
* Genera automáticamente la tabla de verdad para esas variables.
* Solicita al usuario la **salida deseada (0 o 1)** para cada combinación.
* Imprime la tabla de verdad completa junto con las salidas ingresadas.
* Construye y muestra la **expresión SOP final**.

---

### 🧪 Ejecución

```python
if __name__ == "__main__":
    main()
```

* Permite ejecutar el programa directamente si se ejecuta el archivo `.py`.

---

### 🧾 Ejemplo de salida del programa

```bash
Ingrese número de variables (2 o 3):
> 3

Variables: ['A', 'B', 'C']

Ingrese los valores de salida (0 o 1) para cada fila:
A=0, B=0, C=0 => 0
A=0, B=0, C=1 => 1
A=0, B=1, C=0 => 1
A=0, B=1, C=1 => 0
A=1, B=0, C=0 => 1
A=1, B=0, C=1 => 0
A=1, B=1, C=0 => 0
A=1, B=1, C=1 => 0

Tabla de Verdad:
0 | 0 | 0 => 0
0 | 0 | 1 => 1
0 | 1 | 0 => 1
0 | 1 | 1 => 0
1 | 0 | 0 => 1
1 | 0 | 1 => 0
1 | 1 | 0 => 0
1 | 1 | 1 => 0

Expresión SOP generada:
(¬A ∧ ¬B ∧ C) ∨ (¬A ∧ B ∧ ¬C) ∨ (A ∧ ¬B ∧ ¬C)
```
