# Software FJ – Sistema Integral de Gestión

Proyecto académico del curso Programación (213023), Ingeniería de Sistemas – UNAD.

## Descripción
Aplicación de consola desarrollada en Python para gestionar clientes, servicios y reservas de una empresa ficticia. No utiliza bases de datos: la información se mantiene en listas y objetos durante la ejecución. Los eventos y errores se registran en `logs/sistema.log`.

## Requisitos
- Python 3.9 o superior.
- No requiere instalar paquetes externos.

## Ejecución
Desde la carpeta del proyecto, ejecutar:

```bash
python main.py
```

El programa simula 12 operaciones válidas e inválidas. Los resultados se muestran en consola y se registran en el archivo de logs.

## Estructura
- `entidades.py`: clase abstracta Entidad.
- `clientes.py`: clase Cliente y validaciones.
- `servicios.py`: clase abstracta Servicio y tres servicios especializados.
- `reservas.py`: creación, confirmación, cancelación y procesamiento de reservas.
- `excepciones.py`: excepciones personalizadas.
- `gestor.py`: administración mediante listas en memoria.
- `main.py`: ejecución de las pruebas.
- `logs/sistema.log`: registro de eventos y errores.

## Conceptos de POO aplicados
- **Abstracción:** Entidad y Servicio son clases abstractas.
- **Herencia:** Cliente y los servicios especializados heredan de sus clases base.
- **Encapsulación:** los datos del cliente se almacenan en atributos privados y se exponen mediante propiedades.
- **Polimorfismo:** los servicios implementan sus propias versiones de `describir()` y `validar_parametros()`.
- **Sobrecarga simulada:** `calcular_costo()` admite diferentes combinaciones de parámetros opcionales (duración, impuesto y descuento), ya que Python no implementa sobrecarga tradicional por firma.

## Manejo de excepciones
Se utilizan excepciones personalizadas y bloques `try/except/else/finally`. Los errores se registran con el módulo `logging`. La instrucción `raise ... from ...` puede utilizarse para encadenar excepciones cuando una operación de nivel superior necesite conservar la causa original.

## Consideraciones
La aplicación mantiene los datos en memoria y, por tanto, estos se pierden al cerrar el programa. El archivo de logs sí permanece guardado.
