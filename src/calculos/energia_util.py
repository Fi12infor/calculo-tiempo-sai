"""
    Calcula la energía útil disponible.

    Fórmula:
        Wh_utiles = Wh × η

    Donde:
        Wh       : energía total de la batería (Wh)
        η        : eficiencia del SAI (0-1)
        Wh_utiles: energía aprovechable (Wh)

    Parámetros:
        wh (float): energía total.
        eficiencia (float): eficiencia del SAI.

    Retorna:
        float: energía útil.
"""