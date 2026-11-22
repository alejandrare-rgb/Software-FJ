"""Punto de entrada y demostración de 12 operaciones de Software FJ."""
import logging
from pathlib import Path

from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reservas import Reserva
from gestor import GestorSistema
from excepciones import ErrorSistema

RUTA_LOG = Path(__file__).parent / "logs" / "sistema.log"
RUTA_LOG.parent.mkdir(exist_ok=True)
logging.basicConfig(
    filename=RUTA_LOG,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)
logger = logging.getLogger("SoftwareFJ")

gestor = GestorSistema()

def ejecutar(numero, descripcion, operacion):
    """Ejecuta una operación sin detener las demás si ocurre un error."""
    print(f"\\n[{numero}] {descripcion}")
    try:
        resultado = operacion()
    except ErrorSistema as error:
        logger.exception("Error controlado en operación %s: %s", numero, error)
        print(f"ERROR CONTROLADO: {error}")
    except (TypeError, ValueError) as error:
        logger.exception("Dato o parámetro incorrecto en operación %s: %s", numero, error)
        print(f"ERROR DE VALIDACIÓN: {error}")
    except Exception as error:
        logger.exception("Error inesperado en operación %s: %s", numero, error)
        print(f"ERROR INESPERADO: {error}")
    else:
        logger.info("Operación %s exitosa: %s", numero, resultado)
        print(resultado)
    finally:
        print("Operación finalizada; el sistema continúa.")

def registrar_cliente_valido():
    cliente = Cliente("C001", "Laura Pérez", "laura@email.com", "3001234567")
    gestor.registrar_cliente(cliente)
    return cliente.describir()

def registrar_cliente_invalido():
    cliente = Cliente("C002", "Carlos Ruiz", "correo-no-valido", "3001234567")
    gestor.registrar_cliente(cliente)
    return cliente.describir()

def registrar_cliente_duplicado():
    cliente = Cliente("C001", "Laura Pérez", "laura2@email.com", "3011234567")
    gestor.registrar_cliente(cliente)
    return "Cliente duplicado registrado."

def crear_sala():
    servicio = ReservaSala("S001", "Sala de reuniones", 50000, 12)
    gestor.registrar_servicio(servicio)
    return servicio.describir()

def crear_equipo():
    servicio = AlquilerEquipo("S002", "Proyector", 20000, 3)
    gestor.registrar_servicio(servicio)
    return servicio.describir()

def crear_asesoria():
    servicio = Asesoria("S003", "Asesoría de software", 80000, "desarrollo de software")
    gestor.registrar_servicio(servicio)
    return servicio.describir()

def crear_servicio_invalido():
    servicio = ReservaSala("S004", "Sala inválida", -1000, 10)
    gestor.registrar_servicio(servicio)
    return servicio.describir()

def reserva_exitosa():
    reserva = Reserva("R001", gestor.clientes[0], gestor.servicios[0], 2)
    gestor.registrar_reserva(reserva)
    reserva.confirmar()
    total = reserva.procesar(impuesto=0.19, descuento=0.10)
    return f"{reserva.describir()} | Total con impuesto y descuento: ${total:,.2f}"

def reserva_sin_cliente():
    reserva = Reserva("R002", None, gestor.servicios[0], 1)
    gestor.registrar_reserva(reserva)
    return reserva.describir()

def reserva_duracion_invalida():
    reserva = Reserva("R003", gestor.clientes[0], gestor.servicios[0], 0)
    gestor.registrar_reserva(reserva)
    return reserva.describir()

def servicio_no_disponible():
    servicio = ReservaSala("S005", "Sala ocupada", 40000, 8, disponible=False)
    gestor.registrar_servicio(servicio)
    # Se intenta utilizar el servicio para comprobar su disponibilidad.
    servicio.validar_parametros(1)
    return servicio.describir()

def cancelar_reserva():
    reserva = Reserva("R004", gestor.clientes[0], gestor.servicios[1], 1)
    gestor.registrar_reserva(reserva)
    reserva.confirmar()
    return reserva.cancelar()

def main():
    print("=" * 62)
    print("SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
    print("=" * 62)

    operaciones = [
        ("Registrar cliente válido", registrar_cliente_valido),
        ("Intentar registrar cliente con correo inválido", registrar_cliente_invalido),
        ("Intentar registrar cliente duplicado", registrar_cliente_duplicado),
        ("Crear servicio de reserva de sala", crear_sala),
        ("Crear servicio de alquiler de equipo", crear_equipo),
        ("Crear servicio de asesoría especializada", crear_asesoria),
        ("Intentar crear servicio con tarifa negativa", crear_servicio_invalido),
        ("Crear, confirmar y procesar una reserva", reserva_exitosa),
        ("Intentar crear reserva sin cliente", reserva_sin_cliente),
        ("Intentar crear reserva con duración inválida", reserva_duracion_invalida),
        ("Intentar utilizar un servicio no disponible", servicio_no_disponible),
        ("Confirmar y cancelar una reserva", cancelar_reserva),
    ]

    for numero, (descripcion, operacion) in enumerate(operaciones, start=1):
        ejecutar(numero, descripcion, operacion)

    print("\\n" + "=" * 62)
    print("RESUMEN")
    print(f"Clientes registrados: {len(gestor.clientes)}")
    print(f"Servicios registrados: {len(gestor.servicios)}")
    print(f"Reservas registradas: {len(gestor.reservas)}")
    print(f"Registro de eventos y errores: {RUTA_LOG}")
    print("El programa terminó sin detenerse por los errores controlados.")
    print("=" * 62)

if __name__ == "__main__":
    main()
