import pickle


ARCHIVO = "eventos.bin"



def guardar_datos(eventos):
    with open(ARCHIVO, "wb") as fichero:
        pickle.dump(eventos, fichero)



def cargar_datos():
    try:
        with open(ARCHIVO, "rb") as fichero:
            return pickle.load(fichero)

    except FileNotFoundError:
        return []