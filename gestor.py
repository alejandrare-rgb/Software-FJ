"""Listas en memoria para administrar clientes, servicios y reservas."""
from excepciones import DatoInvalidoError

class GestorSistema:
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, cliente):
        if any(c.identificador == cliente.identificador for c in self.clientes):
            raise DatoInvalidoError("Ya existe un cliente con ese identificador.")
        self.clientes.append(cliente)
        return cliente

    def registrar_servicio(self, servicio):
        if any(s.identificador == servicio.identificador for s in self.servicios):
            raise DatoInvalidoError("Ya existe un servicio con ese identificador.")
        self.servicios.append(servicio)
        return servicio

    def registrar_reserva(self, reserva):
        if any(r.identificador == reserva.identificador for r in self.reservas):
            raise DatoInvalidoError("Ya existe una reserva con ese identificador.")
        self.reservas.append(reserva)
        return reserva
