from ListaEscritorio import ListaEscritorio
class NodoPuntosAtencion:
    def __init__(self,id=None,nombrepuntoservicio=None,direccionpuntoservicio=None):
        self.id=id
        self.nombrepuntoservicio=nombrepuntoservicio
        self.direccionpuntoservicio=direccionpuntoservicio
        self.listaEsc=ListaEscritorio()
        self.siguiente=None
        self.anterior=None