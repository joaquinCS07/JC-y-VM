
# Importamos los módulos
from sede import Sede
from evento import Evento
from artista import Artista
from cliente import Cliente
from entradaGeneral import EntradaGeneral
from entradaVip import EntradaVIP
from entradaPromocional import EntradaPromocional
from persona import Persona


def main():
    print("--- SISTEMA DE GESTIÓN DE EVENTOS MUSICALES ---\n")

    # 1. Creación de una Sede y un Evento
    print("[1] Creando la sede y el evento...")
    wizink = Sede("WiZink Center", "Av. Felipe II, Madrid", 15000)
    concierto_reggaeton = Evento("Reggaeton Beach Festival", "2026-05-20", wizink)
    print(f"-> Evento creado: {concierto_reggaeton._nombre_evento} en {wizink._nombre}\n")

    # 2. Creación de un Artista y uso de su Agenda
    print("[2] Registrando artista y añadiendo evento a su agenda...")
    cantante = Artista("Bad Bunny", "12345678A", "badbunny@gmail.es", "Reggaeton")
    cantante.agregar_a_agenda(concierto_reggaeton)
    print(cantante)
    print("Agenda del artista:")
    print(cantante.ver_agenda())
    print()

    # 3. Creación de un Cliente
    print("[3] Registrando un nuevo cliente...")
    cliente_fan = Cliente("Pablo gonzalez", "87654321B", "pablogon@gmail.com", "600123456")
    print(cliente_fan.mostrar_info())
    print()

    # 4. Creación de diferentes tipos de Entradas
    print("[4] Generando entradas para el evento...")
    entrada1 = EntradaGeneral(1001, 40.0)
    entrada2 = EntradaVIP(1002, 40.0, "Front Stage")
    entrada3 = EntradaPromocional(1003, 40.0, "Black Friday", 15.0)

    # Lista de entradas
    entradas_disponibles = [entrada1, entrada2, entrada3]

    for entrada in entradas_disponibles:
        precio = entrada.calcular_precio_final()
        tipo = type(entrada).__name__
        print(f"-> {tipo} calculada: {precio}€")
    print()

    # 5. Simulando una compra
    print("[5] Simulando la compra de la entrada promocional por parte del cliente...")
    entrada3.marcar_como_vendida()
    cliente_fan.nueva_compra(entrada3)

    print("\nEstado de la entrada tras la compra:")
    print(entrada3)

    print("\nInformación actualizada del cliente:")
    print(cliente_fan.mostrar_info())
    print()

    # 6. Estadísticas finales
    print("[6] Estadísticas del sistema...")
    print(f"-> Total de personas registradas en el sistema (Artistas + Clientes): {Persona.total_registrados()}")


if __name__ == "__main__":
    main()