from sqlalchemy.orm import Session
from schema import engine, Autor, Libro, Socio, Prestamo

with Session(engine) as session:
    
    autores = [ 
        Autor(nombre="Franz", apellido="Kafka", nacionalidad="Checa"),  
        Autor(nombre="Jane", apellido="Austen", nacionalidad="Británica"),  
        Autor(nombre="Albert", apellido="Camus", nacionalidad="Francesa"), 
        Autor(nombre="Marjane", apellido="Satrapi", nacionalidad="Iraní"),  
        Autor(nombre="Neil", apellido="Gaiman", nacionalidad="Británica"),  
        Autor(nombre="Gabriel", apellido="García Márquez", nacionalidad="Colombiana"), 
        Autor(nombre="Julio", apellido="Cortázar", nacionalidad="Argentina"),   
        Autor(nombre="Jorge Luis", apellido="Borges", nacionalidad="Argentina"), 
        Autor(nombre="Isabel", apellido="Allende", nacionalidad="Chilena"),     
        Autor(nombre="Stephen", apellido="King", nacionalidad="Estadounidense") 
    ]
    session.add_all(autores)
    session.flush() 
    
    libros = [ 
        Libro(titulo="La Metamorfosis", isbn="6001", stock=5, anio=1915, autor_id=1),  
        Libro(titulo="Mujercitas", isbn="6000", stock=12, anio=1868, autor_id=2),  
        Libro(titulo="Persepolis", isbn="6002", stock=13, anio=2000, autor_id=4),  
        Libro(titulo="Coraline", isbn="6003", stock=10, anio=2002, autor_id=5), 
        Libro(titulo="Orgullo y prejuicio", isbn="6004", stock=20, anio=1813, autor_id=2), 
        Libro(titulo="El extranjero", isbn="6005", stock=54, anio=1942, autor_id=3),  
        Libro(titulo="Cien años de soledad", isbn="6006", stock=15, anio=1967, autor_id=6),  
        Libro(titulo="Rayuela", isbn="6007", stock=8, anio=1963, autor_id=7),  
        Libro(titulo="El Aleph", isbn="6008", stock=11, anio=1949, autor_id=8),  
        Libro(titulo="The Shining", isbn="6009", stock=7, anio=1977, autor_id=10)  
    ]
    session.add_all(libros)
    session.flush() 
    
    socios = [ 
        Socio(nombre="Faustino", apellido="Pérez", email="faustino@email.com", activo=True),    
        Socio(nombre="Jorge", apellido="Gómez", email="jorge@email.com", activo=True),          
        Socio(nombre="Lucas", apellido="Díaz", email="lucas@email.com", activo=False),          
        Socio(nombre="Martina", apellido="Rodríguez", email="martina@email.com", activo=True),  
        Socio(nombre="Frederick", apellido="Smith", email="frederick@email.com", activo=True),  
        Socio(nombre="Valeria", apellido="Fernández", email="valeria@email.com", activo=True),  
        Socio(nombre="Andrés", apellido="López", email="andres@email.com", activo=True),        
        Socio(nombre="Sofía", apellido="Martínez", email="sofia@email.com", activo=False),      
        Socio(nombre="Tomás", apellido="Sánchez", email="tomas@email.com", activo=True),        
        Socio(nombre="Camila", apellido="Romero", email="camila@email.com", activo=True)        
    ]
    session.add_all(socios)
    session.flush() 
    
    prestamos = [ 
        Prestamo(fecha_inicio="2026-09-01", fecha_devolucion="2026-09-08", devuelto=True, libro_id=1, socio_id=1),  
        Prestamo(fecha_inicio="2026-09-05", fecha_devolucion="2026-09-12", devuelto=True, libro_id=2, socio_id=2),  
        Prestamo(fecha_inicio="2026-09-10", fecha_devolucion="2026-09-17", devuelto=True, libro_id=3, socio_id=4),  
        Prestamo(fecha_inicio="2026-09-12", fecha_devolucion=None, devuelto=False, libro_id=4, socio_id=5), 
        Prestamo(fecha_inicio="2026-09-14", fecha_devolucion=None, devuelto=False, libro_id=5, socio_id=6),
        Prestamo(fecha_inicio="2026-09-15", fecha_devolucion=None, devuelto=False, libro_id=6, socio_id=7),  
        Prestamo(fecha_inicio="2026-09-15", fecha_devolucion="2026-09-16", devuelto=True, libro_id=7, socio_id=9),  
        Prestamo(fecha_inicio="2026-09-16", fecha_devolucion=None, devuelto=False, libro_id=8, socio_id=10),  
        Prestamo(fecha_inicio="2026-09-16", fecha_devolucion=None, devuelto=False, libro_id=9, socio_id=1),  
        Prestamo(fecha_inicio="2026-09-17", fecha_devolucion=None, devuelto=False, libro_id=10, socio_id=2)  
    ]
    session.add_all(prestamos)
    
    session.commit()
