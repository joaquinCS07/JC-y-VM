
from sede import Sede
from evento import Evento
from entradaVip import EntradaVIP
from entradaGeneral import EntradaGeneral
from entradaPromocional import EntradaPromocional
from persistencia import guardar_datos, cargar_datos

# Lista principal de eventos
eventos = []


# =========================
# FUNCIONES DEL MENÚ
# =========================

def crear_evento():
    print("\n===== CREAR EVENTO =====")

    nombre = input("Nombre del evento: ")
    fecha = input("Fecha (YYYY-MM-DD): ")

    nombre_sede = input("Nombre de la sede: ")
    direccion = input("Dirección: ")
    aforo = int(input("Aforo máximo: "))

    sede = Sede(nombre_sede, direccion, aforo)
    evento = Evento(nombre, fecha, sede)

    eventos.append(evento)

    print("✅ Evento creado correctamente")



def mostrar_eventos():
    print("\n===== LISTA DE EVENTOS =====")

    if not eventos:
        print("No hay eventos registrados")
        return

    for i, evento in enumerate(eventos, start=1):
        print(f"{i}. {evento}")



def vender_entrada():
    print("\n===== VENDER ENTRADA =====")

    if not eventos:
        print("No hay eventos disponibles")
        return

    mostrar_eventos()

    indice = int(input("Seleccione el número del evento: ")) - 1

    if indice < 0 or indice >= len(eventos):
        print("❌ Evento inválido")
        return

    evento = eventos[indice]

    print("\nTipos de entrada:")
    print("1. VIP")
    print("2. General")
    print("3. Promocional")

    tipo = input("Seleccione el tipo: ")

    id_entrada = int(input("ID de la entrada: "))
    precio = float(input("Precio base: "))

    try:
        if tipo == "1":
            zona = input("Zona exclusiva: ")
            entrada = EntradaVIP(id_entrada, precio, zona)

        elif tipo == "2":
            entrada = EntradaGeneral(id_entrada, precio)

        elif tipo == "3":
            descuento = float(input("Descuento (%): "))
            entrada = EntradaPromocional(id_entrada, precio, descuento4)

        else:
            print("❌ Tipo inválido")
            return

        evento.agregar_venta(entrada)
        print("✅ Entrada vendida correctamente")

    except Exception as e:
        print(f"❌ Error: {e}")



def mostrar_ingresos():
    print("\n===== INGRESOS POR EVENTO =====")

    if not eventos:
        print("No hay eventos registrados")
        return

    for evento in eventos:
        print(f"{evento.nombre}: {evento.calcular_ingresos_totales()} €")



def guardar():
    guardar_datos(eventos)
    print("✅ Datos guardados correctamente")



def cargar():
    global eventos
    eventos = cargar_datos()
    print("✅ Datos cargados correctamente")


# =========================
# MENÚ PRINCIPAL
# =========================

def menu():

    while True:

        print("\n===============================")
        print(" SISTEMA DE GESTIÓN DE EVENTOS")
        print("===============================")
        print("1. Crear evento")
        print("2. Mostrar eventos")
        print("3. Vender entrada")
        print("4. Mostrar ingresos")
        print("5. Guardar datos")
        print("6. Cargar datos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                crear_evento()

            elif opcion == "2":
                mostrar_eventos()

            elif opcion == "3":
                vender_entrada()

            elif opcion == "4":
                mostrar_ingresos()

            elif opcion == "5":
                guardar()

            elif opcion == "6":
                cargar()

            elif opcion == "7":
                print("👋 Saliendo del sistema...")
                break

            else:
                print("❌ Opción inválida")

        except ValueError:
            print("❌ Error: introduzca un valor válido")

        except Exception as e:
            print(f"❌ Error inesperado: {e}")


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

if __name__ == "__main__":
    menu()


