# Eventos y entradas
El proyecto consiste en un sistema de venta de entradas 
para diferentes eventos, guardando datos sobre las entradas y todos sus tipos, 
o toda la información para gestionar los datos de los clientes. 


## Objetivo del proyecto: 

El objetivo de nuestro proyecto es gestionar de manera eficiente 
la relación entre sedes, eventos, artistas y clientes, permitiendo 
la venta de diferentes tipos de entradas con lógicas de precio dinámicas.

## Instalación:

Primeramente, clonar el repositorio y asegurarse de tener Python 3.x instalado
Puedes hacer lo siguiente: 

python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip pytest

Instala dependencias si las hubiera: 

pip install -r requirements.txt

## Características técnicas: 

Todo nuestro código ha sido diseñado siguiendo los siguientes aspectos: 

- **Encapsulamiento:**  uso de atributos protegidos y decoradores property para asegurar 
la integridad de los datos en clases como Sede y Cliente. 

- **Herencia y Polimorfismo:** Implementación de una jerarquía de clases para Persona (Artista/
Cliente) y Entrada (VIP/General/Promocional). También, el cálculo de ingresos en la clase Evento es totalmente
polimófico

- **Clases abstractas:** La clase base Entrada actúa como una interfaz abstracta para definir 
el comportamiento obligatorio de sus clases hijas.

- **Modularidad:** El proyecto está dividido en múltiples módulos según su funcionalidad para facilitar el mantenimiento.

## Estructura del proyecto: 
1. persona.py, cliente.py, artista.py: Gestión de usuarios y perfiles.

2. sede.py, evento.py: Gestión de infraestructuras y logística de eventos.

3. entrada.py, entradaVip.py, entradaGeneral.py, entradaPromocional.py: Lógica de precios y tipos de acceso.

4. promocion.py: Mixin para aplicar descuentos a entradas promocionales.

## Arquitectura y Responsabilidades:

El proyecto sigue una estructura modular con dependencias dirigidas para asegurar la mantenibilidad:

**Dominio (`persona.py`, `entrada.py`, `sede.py`, etc.)**: Contiene las entidades, sus estados e invariantes de negocio (ej. validación de aforo o cálculo de precios).
**Lógica de Orquestación (`evento.py`)**: Coordina la relación entre sedes, entradas y ventas.
**Mixins (`promocion.py`)**: Proporciona comportamientos específicos reutilizables de forma transversal.

## Ejemplo rápido de uso: 

from sede import Sede
from evento import Evento
from entradaVip import EntradaVIP

# 1. Definir infraestructura
sede_madrid = Sede("WiZink Center", "Av. Felipe II", 15000)

# 2. Crear evento
concierto = Evento("Concierto Rock", "2026-05-20", sede_madrid)

# 3. Venta polimórfica (El evento no necesita saber que es VIP para calcular el total)
vip = EntradaVIP(id_entrada="V-001", precio_base=80, zona_exclusiva="Front Stage")
concierto.agregar_venta(vip)

print(f"Total recaudado: {concierto.calcular_ingresos_totales()}€")