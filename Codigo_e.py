# CLASE USUARIO
# Aqui se utliza el encapsulamiento para proteger los atributos
class Usuario:
    def __init__(self, id_usuario, nombre, direccion, telefono, correo_electronico):
        self.__id_usuario = id_usuario  # Aqui es en donde se encapsula el ID del usuario
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__correo_electronico = correo_electronico

    # Métodos getters ( valor de un atributo encapsulado) y setters (modificar el valor  del atributo encapsulado)
    def get_id_usuario(self):
        return self.__id_usuario

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo_electronico

    def set_direccion(self, nueva_direccion):
        self.__direccion = nueva_direccion

    def set_telefono(self, nuevo_telefono):
        self.__telefono = nuevo_telefono


# CLASE LIBRO
# Aqui tambien se hace aplica elEncapsulamiento 
class Libro:
    def __init__(self, isbn, titulo, autor, genero, año, ubicacion, estado="disponible"):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__año = año
        self.__ubicacion = ubicacion
        self.__estado = estado

    # Estos son los métodos encapsulados
    def get_titulo(self):
        return self.__titulo

    def get_estado(self):
        return self.__estado

    def set_estado(self, nuevo_estado):
        self.__estado = nuevo_estado


# CLASE CATALOGO 
# Aqui se hace uso de la herencia y el polimorfismo
class Catalogo:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.get_titulo().lower() == titulo.lower():
                return libro
        return None

    def obtener_libros_disponibles(self):
        return [libro for libro in self.libros if libro.get_estado() == "disponible"]

    def eliminar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            self.libros.remove(libro)
            return f"El libro '{titulo}' ha sido eliminado del catálogo."
        return "Libro no encontrado."


# CLASE PRESTAMO
# Aqui tambien se aplica la herencia 
class Prestamo:
    def __init__(self, id_prestamo, id_usuario, libro, fecha_prestamo, fecha_vencimiento):
        self.id_prestamo = id_prestamo
        self.id_usuario = id_usuario  # Cambiado a ID del usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_vencimiento = fecha_vencimiento  # Cambiado a fecha de vencimiento

    def detalles_prestamo(self):
        return (f"Préstamo ID: {self.id_prestamo}, ID Usuario: {self.id_usuario}, "
                f"Libro: {self.libro.get_titulo()}, Fecha de préstamo: {self.fecha_prestamo}, "
                f"Fecha de vencimiento: {self.fecha_vencimiento}")


# Clase derivada SistemaPrestamos 
# Aqui se emplea el polimorfismo y manejo de errores
class SistemaPrestamos(Catalogo):
    def __init__(self):
        super().__init__()
        self.prestamos = []

    def registrar_prestamo(self, id_usuario, titulo_libro, fecha_prestamo, fecha_vencimiento):
        try:  # Manejo de errores con try-except
            libro = self.buscar_libro(titulo_libro)
            if libro and libro.get_estado() == "disponible":
                libro.set_estado("prestado")
                nuevo_prestamo = Prestamo(len(self.prestamos) + 1, id_usuario, libro, fecha_prestamo, fecha_vencimiento)
                self.prestamos.append(nuevo_prestamo)
                return f"Préstamo registrado exitosamente: {nuevo_prestamo.detalles_prestamo()}"
            else:
                return "Libro no disponible o no encontrado."
        except Exception as e:
            return f"Error al registrar préstamo: {str(e)}"

    def devolver_libro(self, titulo_libro):
        try:  # Manejo de errores con try-except
            libro = self.buscar_libro(titulo_libro)
            if libro and libro.get_estado() == "prestado":
                libro.set_estado("disponible")
                return f"El libro '{titulo_libro}' ha sido devuelto exitosamente."
            else:
                return "El libro no está en préstamo o no existe."
        except Exception as e:
            return f"Error al devolver libro: {str(e)}"


# Ejemplo de uso
if __name__ == "__main__":
    sistema = SistemaPrestamos()

    # Crear usuarios y libros
    usuario1 = Usuario(1, "Joselyn Aguirre", "Calle Argentina", "5551234568", "joselynaguirre@gmail.com")
    libro1 = Libro("123456", "El Principito", "Antoine de Saint-Exupéry", "Ficción", 1943, "Estante A")
    libro2 = Libro("789101", "Cien años de soledad", "Gabriel García Márquez", "Ficción", 1967, "Estante B")

    # Agregar libros al catálogo
    sistema.agregar_libro(libro1)
    sistema.agregar_libro(libro2)

    # Registrar un préstamo
    print(sistema.registrar_prestamo(usuario1.get_id_usuario(), "El Principito", "2024-12-05", "2024-12-12"))

    # Intentar devolver el libro
    print(sistema.devolver_libro("El Principito"))

    # Eliminar un libro del catálogo
    print(sistema.eliminar_libro("Cien años de soledad"))
