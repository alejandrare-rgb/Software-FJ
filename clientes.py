"""Gestión y validación de clientes."""
import re
from entidades import Entidad
from excepciones import DatoInvalidoError

class Cliente(Entidad):
    def __init__(self, identificador: str, nombre: str, correo: str, telefono: str):
        super().__init__(identificador, nombre)
        if not correo or not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", correo.strip()):
            raise DatoInvalidoError("El correo electrónico no tiene un formato válido.")
        if not telefono or not re.fullmatch(r"[0-9+\-\s]{7,20}", telefono.strip()):
            raise DatoInvalidoError("El teléfono debe contener entre 7 y 20 caracteres válidos.")
        self.__correo = correo.strip().lower()
        self.__telefono = telefono.strip()

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def describir(self):
        return f"Cliente: {self.nombre} | correo: {self.correo}"

    def __str__(self):
        return f"{self.nombre} ({self.identificador})"
