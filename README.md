# Calculadora de autonomía para SAI

Aplicación desarrollada en Python para estimar el tiempo aproximado de
funcionamiento de un **Sistema de Alimentación Ininterrumpida (SAI)** en
función de los datos introducidos por el usuario.

El proyecto está planteado con una estructura modular para facilitar el
trabajo en equipo, el mantenimiento del código y la incorporación de nuevas
funcionalidades.

## Objetivo

El objetivo principal es proporcionar una estimación orientativa de la
autonomía de un SAI ante una carga determinada.

La aplicación solicitará al usuario los datos necesarios, realizará las
conversiones de unidades correspondientes y calculará el tiempo aproximado
de funcionamiento.

## Estructura del proyecto

```text
calculadora_tiempo_sai/
|-- main.py
|-- src/
|   |-- calculos/
|   |   `-- calcular_autonomia.py
|   |-- convercion/
|   |   `-- convertir_unidades.py
|   `-- menu/
`-- README.md
```

### Responsabilidad de cada módulo

| Ruta | Responsabilidad |
| --- | --- |
| `main.py` | Punto de entrada de la aplicación. |
| `src/menu/` | Interacción con el usuario y recogida de datos. |
| `src/convercion/convertir_unidades.py` | Conversión de las unidades necesarias para realizar los cálculos. |
| `src/calculos/calcular_autonomia.py` | Estimación de la autonomía aproximada del SAI. |

## Flujo previsto

1. El usuario inicia la aplicación.
2. El programa solicita los datos necesarios del SAI y de la carga.
3. Los valores introducidos se validan y se convierten a las unidades
   requeridas.
4. El módulo de cálculo estima la autonomía.
5. El programa muestra al usuario el tiempo aproximado de funcionamiento.

## Requisitos

- Python 3.10 o superior.
- No se requieren dependencias externas en la versión inicial.

## Ejecución

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

## Estado del proyecto

El proyecto se encuentra en una fase inicial de desarrollo. La estructura
modular ya está preparada para implementar progresivamente:

- El menú de entrada de datos.
- La validación de valores introducidos por el usuario.
- Las conversiones de unidades.
- La fórmula de estimación de autonomía.
- La presentación del resultado final.
- Las pruebas de funcionamiento.

## Consideraciones

El resultado obtenido será una **estimación aproximada**. La autonomía real
de un SAI puede variar según factores como la eficiencia del equipo, el
estado de la batería, su antigüedad, la temperatura y el comportamiento de
la carga conectada.

## Uso académico

Este proyecto ha sido creado con fines educativos como ejercicio de
programación modular en Python.
