"""Clases base del modelo orientado a objetos."""
from abc import ABC, abstractmethod

class Entidad(ABC):
    """Representa una entidad general del sistema."""

    def __init__(self, identificador: str, nombre: str):
        if not identificador or not identificador.strip():
            raise ValueError("El identificador es obligatorio.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre es obligatorio.")
        self._identificador = identificador.strip()
        self._nombre = nombre.strip()

    @property
    def identificador(self):
        return self._identificador

    @property
    def nombre(self):
        return self._nombre

    @abstractmethod
    def describir(self):
        """Cada entidad concreta debe proporcionar una descripción."""
        raise NotImplementedError
