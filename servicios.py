"""Servicios abstractos y especializados de Software FJ."""
from abc import abstractmethod
from entidades import Entidad
from excepciones import DatoInvalidoError, ServicioNoDisponibleError

class Servicio(Entidad):
    def __init__(self, identificador: str, nombre: str, tarifa: float, disponible: bool = True):
        super().__init__(identificador, nombre)
        if not isinstance(tarifa, (int, float)) or isinstance(tarifa, bool) or tarifa <= 0:
            raise DatoInvalidoError("La tarifa debe ser un número mayor que cero.")
        self._tarifa = float(tarifa)
        self._disponible = bool(disponible)

    @property
    def tarifa(self):
        return self._tarifa

    @property
    def disponible(self):
        return self._disponible

    def validar_disponibilidad(self):
        if not self._disponible:
            raise ServicioNoDisponibleError(f"El servicio '{self.nombre}' no está disponible.")

    def calcular_costo(self, duracion: float, impuesto: float = 0.0, descuento: float = 0.0):
        """Variantes de cálculo: básico, con impuesto y/o con descuento."""
        self.validar_disponibilidad()
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatoInvalidoError("La duración debe ser mayor que cero.")
        if not 0 <= impuesto <= 1:
            raise DatoInvalidoError("El impuesto debe expresarse entre 0 y 1.")
        if not 0 <= descuento <= 1:
            raise DatoInvalidoError("El descuento debe expresarse entre 0 y 1.")
        subtotal = self.tarifa * duracion
        total = subtotal * (1 + impuesto) * (1 - descuento)
        return round(total, 2)

    @abstractmethod
    def describir(self):
        raise NotImplementedError

    @abstractmethod
    def validar_parametros(self, duracion: float):
        raise NotImplementedError

class ReservaSala(Servicio):
    def __init__(self, identificador, nombre, tarifa, capacidad: int, disponible=True):
        super().__init__(identificador, nombre, tarifa, disponible)
        if not isinstance(capacidad, int) or isinstance(capacidad, bool) or capacidad <= 0:
            raise DatoInvalidoError("La capacidad de la sala debe ser un entero positivo.")
        self.capacidad = capacidad

    def validar_parametros(self, duracion):
        self.validar_disponibilidad()
        if duracion < 1:
            raise DatoInvalidoError("La sala debe reservarse por al menos una hora.")

    def describir(self):
        return f"Sala '{self.nombre}' para {self.capacidad} personas. Tarifa/hora: ${self.tarifa:.2f}"

class AlquilerEquipo(Servicio):
    def __init__(self, identificador, nombre, tarifa, cantidad: int, disponible=True):
        super().__init__(identificador, nombre, tarifa, disponible)
        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
            raise DatoInvalidoError("La cantidad de equipos debe ser un entero positivo.")
        self.cantidad = cantidad

    def validar_parametros(self, duracion):
        self.validar_disponibilidad()
        if duracion < 1:
            raise DatoInvalidoError("El alquiler debe ser de al menos una hora.")

    def describir(self):
        return f"Equipo '{self.nombre}', unidades: {self.cantidad}. Tarifa/hora: ${self.tarifa:.2f}"

class Asesoria(Servicio):
    def __init__(self, identificador, nombre, tarifa, especialidad: str, disponible=True):
        super().__init__(identificador, nombre, tarifa, disponible)
        if not especialidad or not especialidad.strip():
            raise DatoInvalidoError("La especialidad de la asesoría es obligatoria.")
        self.especialidad = especialidad.strip()

    def validar_parametros(self, duracion):
        self.validar_disponibilidad()
        if duracion < 0.5:
            raise DatoInvalidoError("La asesoría debe durar al menos media hora.")

    def describir(self):
        return f"Asesoría en {self.especialidad}: {self.nombre}. Tarifa/hora: ${self.tarifa:.2f}"
