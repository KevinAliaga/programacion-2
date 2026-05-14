class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrarInfo(self):
        print(f"autor es {self.nombre} ({self.nacionalidad})")

class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrarInfo(self):
        print(f"estudiante es {self.nombre} - SIS: {self.codigo}")

class Pagina:
    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido

    def mostrarContenido(self):
        print(f"Pagina {self.numero} y {self.contenido}")

class Libro:
    def __init__(self, titulo, isbn, contenidos):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = []
        contador = 1
        for i in contenidos:
            nueva_pagina = Pagina(contador, i)
            self.paginas.append(nueva_pagina)
            contador = contador + 1

    def leer(self):
        print(f"leyendo {self.titulo}")
        for j in self.paginas:
            j.mostrarContenido()

class Prestamo:
    def __init__(self, fecha_prestamo, fecha_devolucion, estudiante, libro):
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estudiante = estudiante
        self.libro = libro

    def mostrarInfo(self):
        print(f"prestamo {self.libro.titulo} a {self.estudiante.nombre}")
        print(f"desde {self.fecha_prestamo} hasta {self.fecha_devolucion}")

class Horario:
    def __init__(self, dias, hora_apertura, hora_cierre):
        self.dias = dias
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre

    def mostrarHorario(self):
        print(f"horario: {self.dias} de {self.hora_apertura} a {self.hora_cierre}")

class Biblioteca:
    def __init__(self, nombre, dias, hora_apertura, hora_cierre):
        self.nombre = nombre
        self.libros = []
        self.autores = []
        self.prestamos = []
        self.horario = Horario(dias, hora_apertura, hora_cierre)

    def agregarLibro(self, libro):
        self.libros.append(libro)

    def agregarAutor(self, autor):
        self.autores.append(autor)

    def prestarLibro(self, estudiante, libro, fecha_prestamo, fecha_devolucion):
        nuevo_prestamo = Prestamo(fecha_prestamo, fecha_devolucion, estudiante, libro)
        self.prestamos.append(nuevo_prestamo)

    def mostrarEstado(self):
        print(f"biblioteca {self.nombre} ")
        self.horario.mostrarHorario()
        print("autores ")
        for a in self.autores:
            a.mostrarInfo()
        print("libros")
        for b in self.libros:
            print(f"{b.titulo} (ISBN: {b.isbn})")
        print("prestamos ")
        for c in self.prestamos:
            c.mostrarInfo()

    def cerrarBiblioteca(self):
        print(f"cerrando la biblioteca {self.nombre} prestamos cancelados ")
        self.prestamos = []

biblio_central = Biblioteca("biblioteca de UMSA", " de Lunes a Viernes", "08:00", "20:00")
autor1 = Autor("franz tamayo", "boliviana")
libro1 = Libro("pedagogia nacional", "97899905", ["prologo", "capitulo 1", "fin"])
autor2 = Autor("alcides arguedas", "boliviana")
libro2 = Libro("raza de bronce", "97884206", ["inicio", "desarrollo", "fin"])
biblio_central.agregarAutor(autor1)
biblio_central.agregarAutor(autor2)
biblio_central.agregarLibro(libro1)
biblio_central.agregarLibro(libro2)
estudiante1 = Estudiante("1705643", "juanito")
biblio_central.prestarLibro(estudiante1, libro1, "10/05/2026", "15/05/2026")
biblio_central.mostrarEstado()
libro1.leer()
biblio_central.cerrarBiblioteca()