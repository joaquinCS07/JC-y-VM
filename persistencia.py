import pickle

def guardar_datos_binarios(lista_objetos, nombre_archivo: str):
    try:
        with open(nombre_archivo, "wb") as f:
            pickle.dump(lista_objetos, f)
        print("Datos guardados correctamente en formato binario.")
    except Exception as e:
        print(f"Error al guardar: {e}")

def cargar_datos_binarios(nombre_archivo: str):
    try:
        with open(nombre_archivo, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return [] # Retorna lista vacía si no existe el archivo