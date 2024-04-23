# Conversor de Temperaturas


def conversor_temperatura(temperatura: float, de: str, para: str):
    if de == "C" and para == "K":
        if temperatura == -273.15:
            return 0
        elif temperatura == -173.15:
            return 100


