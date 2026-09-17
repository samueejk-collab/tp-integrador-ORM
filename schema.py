from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase):
    pass

class Autor(Base):
    __tablename__ = "Autor"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    nacionalidad = Column(String)
    libros = relationship("Libro", back_populates="autor")

class Libro(Base):
    __tablename__ = "Libro"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    isbn = Column(String, unique=True)
    anio = Column(Integer)
    stock = Column(Integer, default=0)
    autor_id = Column(Integer, ForeignKey("Autor.id"), nullable=False)
    autor = relationship("Autor", back_populates="libros")
    prestamos = relationship("Prestamo", back_populates="libro")

class Socio(Base):
    __tablename__ = "Socio"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, unique=True)
    activo = Column(Boolean, default=True)
    prestamos = relationship("Prestamo", back_populates="socio")

class Prestamo(Base):
    __tablename__ = "Prestamo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_inicio = Column(String, nullable=False)     
    fecha_devolucion = Column(String)                 
    devuelto = Column(Boolean, default=False)         
    libro_id = Column(Integer, ForeignKey("Libro.id"), nullable=False)
    socio_id = Column(Integer, ForeignKey("Socio.id"), nullable=False)
    libro = relationship("Libro", back_populates="prestamos")
    socio = relationship("Socio", back_populates="prestamos")

engine = create_engine("sqlite:///biblioteca.db")
Base.metadata.create_all(engine)
