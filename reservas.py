"""Creación y procesamiento de reservas."""
from entidades import Entidad
from excepciones import ReservaInvalidaError, OperacionNoPermitidaError

class Reserva(Entidad):
    ESTADOS = ("PENDIENTE", "CONFIRMADA", "CANCELADA")

    def __init__(self, identificador, cliente, servicio, duracion):
        super().__init__(identificador, f"Reserva {identificador}")
        if cliente is None or servicio is None:
            raise ReservaInvalidaError("La reserva requiere un cliente y un servicio.")
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ReservaInvalidaError("La duración de la reserva debe ser positiva.")
        servicio.validar_parametros(duracion)
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = float(duracion)
        self.estado = "PENDIENTE"

    def confirmar(self):
        if self.estado != "PENDIENTE":
            raise OperacionNoPermitidaError("Solo se pueden confirmar reservas pendientes.")
        self.servicio.validar_parametros(self.duracion)
        self.estado = "CONFIRMADA"
        return f"Reserva {self.identificador} confirmada."

    def cancelar(self):
        if self.estado == "CANCELADA":
            raise OperacionNoPermitidaError("La reserva ya está cancelada.")
        self.estado = "CANCELADA"
        return f"Reserva {self.identificador} cancelada."

    def procesar(self, impuesto=0.19, descuento=0.0):
        if self.estado != "CONFIRMADA":
            raise OperacionNoPermitidaError("La reserva debe estar confirmada para procesarse.")
        try:
            return self.servicio.calcular_costo(self.duracion, impuesto, descuento)
        except Exception as error:
            # Encadenamiento: conserva la causa original del fallo.
            raise ReservaInvalidaError(
                "No fue posible calcular el costo de la reserva."
            ) from error

    def describir(self):
        return (f"{self.identificador}: {self.cliente.nombre} - "
                f"{self.servicio.nombre} - {self.duracion} horas - {self.estado}")
