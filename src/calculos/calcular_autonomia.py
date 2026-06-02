def calcular_autonomia(energia_util, consumo_total):
    """
    Calcula la autonomía estimada del SAI.
    Fórmula:
        t = Wh_utiles / P_total
    Donde:
        t         : tiempo de autonomía (h)
        Wh_utiles : energía útil disponible (Wh)
        P_total   : consumo total (W)
    Parámetros:
        energia_util (float): energía disponible.
        consumo_total (float): consumo total.
    Retorna:
        float: autonomía en horas.
    """
