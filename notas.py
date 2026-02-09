def pedir_notas():
    """Pide notas al usuario hasta que introduzca -1"""
    notas = []
    print("Introduce las notas (escribe -1 para terminar):")

    while True:
        nota = float(input("Nota: "))
        if nota == -1:
            break
        notas.append(nota)

    return notas


def mostrar_resumen(notas):
    """Muestra el resumen de las notas"""
    if len(notas) == 0:
        print("No se han introducido notas.")
    else:
        print("\nResumen de notas:")
        print("Número de notas:", len(notas))
        print("Nota máxima:", max(notas))
        print("Nota mínima:", min(notas))
        print("Nota media:", sum(notas) / len(notas))


def main():
    notas = pedir_notas()


main()
