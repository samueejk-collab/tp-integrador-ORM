from sqlalchemy import or_
from sqlalchemy.orm import Session
from schema import engine, Autor, Libro, Socio, Prestamo

with Session(engine) as session:

    libros_recientes = session.query(Libro).filter(Libro.anio >= 1950).all()
    for l in libros_recientes: 
        print(l.titulo, l.anio) 
        
    email_socio = session.query(Socio).filter(Socio.nombre == "Faustino").all() 
    for c in email_socio: 
        print(c.nombre, c.email)

    prestamos_activos = session.query(Prestamo).filter(Prestamo.devuelto == False).all()
    for p in prestamos_activos:
        print(p.id, p.fecha_inicio)

    socios_busqueda = session.query(Socio).filter(or_(Socio.apellido == "Pérez", Socio.activo == False)).all()
    for s in socios_busqueda:
        print(s.nombre, s.apellido, s.activo)

    autores_filtro = session.query(Autor).filter(Autor.nacionalidad.startswith("Argen")).all()
    for a in autores_filtro:
        print(a.nombre, a.apellido, a.nacionalidad)

    libro_mas_antiguo = session.query(Libro).order_by(Libro.anio.asc()).first()
    if libro_mas_antiguo:
        print(libro_mas_antiguo.titulo, libro_mas_antiguo.anio)
