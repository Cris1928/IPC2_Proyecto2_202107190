from ListaEscritorio import ListaEscritorio
from ListaClientesDef import ListadoClientes
class NodoPuntosAtencion:
    def __init__(self,id=None,nombrepuntoservicio=None,direccionpuntoservicio=None,estado=None):
        self.id=id
        self.estado=estado
        self.nombrepuntoservicio=nombrepuntoservicio
        self.direccionpuntoservicio=direccionpuntoservicio
        self.listaEsc=ListaEscritorio()
        self.listadoclientes=ListadoClientes()
        self.siguiente=None
        self.anterior=None