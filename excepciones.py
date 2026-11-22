"""Excepciones personalizadas del sistema Software FJ."""

class ErrorSistema(Exception):
    """Clase base para los errores controlados de la aplicación."""

class DatoInvalidoError(ErrorSistema):
    """Se genera cuando un dato no cumple las validaciones."""

class ServicioNoDisponibleError(ErrorSistema):
    """Se genera cuando un servicio no está disponible."""

class ReservaInvalidaError(ErrorSistema):
    """Se genera cuando una reserva no puede procesarse."""

class OperacionNoPermitidaError(ErrorSistema):
    """Se genera cuando el estado no permite una operación."""
