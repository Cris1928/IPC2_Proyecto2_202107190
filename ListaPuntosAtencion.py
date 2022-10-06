from django.forms import PasswordInput
from AtencionCliente import NodoAtencionCliente
from CalcularMax import ListMax
from CalcularMax import nodoMax
from os import system
from NodoClientesDef import NodoListadoClientesD
from NodoPuntosAtencion import NodoPuntosAtencion
from NodoUltimaTrans import NodoUlitmaTras
class ListaPuntosAntecnion:
    def __init__(self) -> None:
        self.primero=NodoPuntosAtencion()
        self.ultimo=NodoPuntosAtencion()
        self.size=0

    def append(self, nuevoPunto):
        if self.primero.id is None:
            self.primero=nuevoPunto
            self.ultimo=nuevoPunto
            self.size += 1
        elif self.primero.siguiente is None:
            self.primero.siguiente=nuevoPunto
            nuevoPunto.anterior=self.primero
            self.ultimo=nuevoPunto
            self.size += 1
        else:
            self.ultimo.siguiente=nuevoPunto
            nuevoPunto.anterior=self.ultimo
            self.ultimo=nuevoPunto
            self.size += 1
    def buscarescritorio(self,id):

        nodoaux=self.primero
        while nodoaux.id != id:
            if nodoaux.siguiente is not None:
                nodoaux=nodoaux.siguiente
            else:
                return None
     #   print(nodoaux.id)
        return nodoaux

    def printnuevo(self):



        nodoaux=self.primero
        cadena= ""
        num=1
        while True:

            if nodoaux.id is not None:



                cadena +=str(num)+". ("+str(nodoaux.nombrepuntoservicio)+")"
                if nodoaux.siguiente is not None:
                    nodoaux=nodoaux.siguiente
                    cadena+="\n"
                    num=num+1
                else:
                    break
            else:
                break
        print(cadena)





    def print(self):
        nodoaux=self.primero
        cadena= ""
        num=1
        while True:
            if nodoaux.id is not None and nodoaux.estado==1:
                cadena +=str(num)+". ("+str(nodoaux.nombrepuntoservicio)+")"
                if nodoaux.siguiente is not None:
                    nodoaux=nodoaux.siguiente
                    cadena+="\n"
                    num=num+1
                else:
                    break
            else:
                break
        print(cadena)

    def returnEvaluarEscritorio(self, numero):
            
        actual = self.primero
        i = 1
        
        while actual is not None:
            if actual.estado==1:
                if i == numero:
                    return actual.listaEsc
                else:
                    pass
                i += 1 
            else:
                pass
            actual = actual.siguiente  
    def returnEvaluarEscritorios(self, numero):
            
        actual = self.primero
        i = 1
        
        while actual is not None:
        
            if i == numero:
                return actual.listaEsc
            else:
                pass
            i += 1 
           
            actual = actual.siguiente   


    def returnEmpresa(self, numero):
            
        actual = self.primero
        i = 1
        
        while actual is not None:

        
            if i == numero:
                 #   returnpasciente = actual.ListaPuntosAtencion
                  #  return returnpasciente
                  actual.listaEsc.print()
                  
    
            actual = actual.siguiente
            i += 1        


    def CambiarEstado(self,ide):

 #       escAc=ListaEscritoriosActivos()
        actual=self.primero
        while actual is not None:

            if actual.id==ide:

                actual.estado=1
      #          print(actual.nombrepuntoservicio)
            else:
                pass
            actual=actual.siguiente
    def printEstado(self):
        nodoaux=self.primero
        cadena= ""
        num=1
        while nodoaux is not None:
            if nodoaux.estado == 1:
                cadena +=str(num)+". ("+str(nodoaux.nombrepuntoservicio)+")"
                cadena+="\n"
                num=num+1
            else:
                pass
            nodoaux=nodoaux.siguiente

        print(cadena)
    def calculo(self):
        actual=self.primero.listadoclientes.primero
        print("CLIENTES EN ESPERA")
        while actual is not None:
            if actual.estado==0:

                print(actual.nombre)
            else:
                pass
            actual=actual.siguiente


    def cantidaddetrans(self):
        actual=self.primero.listadoclientes.primero.listaTransacciones.primero
        cont=0
        while actual is not None:
            cont=cont+1
            actual =actual.siguiente
        return(cont)



    def CantidaddeClientes(self):
        actual=self.primero.listadoclientes.primero
        contador=0
        while actual is not None:
            contador=contador+1
            #print(actual.nombre)
            actual=actual.siguiente
        return contador

    def EscritoriosInactivos(self):
        actual=self.primero.listaEsc.primero
        
    def tiempopromedioatencion(self):
        a=self.primero.listadoclientes.primero
        sumat=0
        cantidaddeclientes=0
        while a is not None:
            if a.estado==2:
                actual=a.listaTransacciones.primero
            #   actual=self.primero.listadoclientes.primero.listaTransacciones.primero float
                suma=0
                while actual is not None:
            #      print(actual.tiempo)
            #       print(actual.cantidad)
                    if actual.tiempo !=None and actual.cantidad!=None:
                        suma=suma+(int(actual.tiempo))*(int(actual.cantidad))
                    else:
                        pass
                    actual=actual.siguiente

                sumat=sumat+suma
                cantidaddeclientes=cantidaddeclientes+1
            else:
                pass


            a=a.siguiente         
        if cantidaddeclientes !=0:
            promedio=sumat/cantidaddeclientes
            return promedio
        else:
            return 0
    def buscarcliente(self,dpi):

        actual=self.primero.listadoclientes.primero
        while actual is not None:


            if actual.dpi == dpi:
                return actual
            else:
                pass
            actual=actual.siguiente
        print(" no se encontro el cliente")

    def agregarcliente(self,cliente,nombre):
        self.primero.listadoclientes.append(NodoListadoClientesD(cliente,nombre,0))


    
    def agregarletrasacciones(self,dpi,nombre,id,cantidad,tiempo):        
        actual=self.primero.listadoclientes.primero
        while actual is not None:
            

            if actual.dpi==dpi:

            
                actual.listaTransacciones.append(NodoUlitmaTras(id,nombre,cantidad,tiempo))
            else:
                pass


            actual =actual.siguiente
                
    def tiempomaximoatencion(self):

        a=self.primero.listadoclientes.primero
        aux=0

        while a is not None:
            if a.estado==2:
                actual=a.listaTransacciones.primero
                suma=0
                while actual is not None:
                    if actual.tiempo !=None and actual.cantidad!=None:
                        suma=suma+(int(actual.tiempo))*(int(actual.cantidad))
                    else:
                        pass
                    actual=actual.siguiente
                if suma >aux:
                    aux=suma
            else:
                pass

            a=a.siguiente         
        return aux

    def tiempomaximoClientesEnatencion(self):
        actual=self.primero.listaEsc.primero
        aux=0
        while actual is not None:
            if actual.estado==2:
                actual2=actual.listadoAtencionClientes.primero
                suma=0
                while actual2 is not None:
                    suma=suma+(int(actual2.tiempo))
                    actual2=actual2.siguiente
                if suma >aux:
                    aux=suma
            else:
                pass
            actual=actual.siguiente
        return aux
#        a=self.primero.listadoclientes.primero
 #       aux=0

  #      while a is not None:
   #         if a.estado==2:
    #            actual=a.listaTransacciones.primero
     #           suma=0
      #          while actual is not None:
       #             suma=suma+(int(actual.tiempo))*(int(actual.cantidad))
        #            actual=actual.siguiente
         #       if suma >aux:
          #          aux=suma
           # else:
            #    pass



    #        a=a.siguiente         
     #   return aux






    def tiempominimoClienteEnatencion(self):
        actual=self.primero.listaEsc.primero
        mayor=self.tiempomaximoClientesEnatencion()
       # print(mayor)
        while actual is not None:
            if actual.estado==2:
                actual2=actual.listadoAtencionClientes.primero
                suma=0
                while actual2 is not None:
                    suma=suma+actual2.tiempo
                    actual2=actual2.siguiente

                if suma<mayor:
                    mayor=suma
                else:
                    pass
            else:
                pass
            actual=actual.siguiente
        return mayor




  #  def tiempominimoClienteEnatencion(self):
   #   #  a=self.primero.listaEsc.primero.listadoAtencionClientes.primero
    #    a=self.primero.listadoclientes.primero
   # #    acu=int(a.listaTransacciones.primero.cantidad)*int(a.listaTransacciones.primero.tiempo)
    #    aux=self.tiempomaximoClientesEnatencion()

     #   while a is not None:
      #      if a.estado==2:
       #         actual=a.listaTransacciones.primero
        #        suma=0
         #       while actual is not None:
          #          suma=suma+(int(actual.tiempo))*(int(actual.cantidad))
           #         actual=actual.siguiente
            #    if suma <aux:
             #       aux=suma
              #  else:
               #     pass
      #             
       #     else:
        #        pass
         #   a=a.siguiente 

        #return aux




    def tiempominimoatencion(self):
        a=self.primero.listadoclientes.primero
    #    acu=int(a.listaTransacciones.primero.cantidad)*int(a.listaTransacciones.primero.tiempo)
        aux=self.tiempomaximoatencion()

        while a is not None:
            if a.estado==2:
                actual=a.listaTransacciones.primero
                suma=0
                while actual is not None:
                    if actual.tiempo !=None and actual.cantidad!=None:
                        suma=suma+(int(actual.tiempo))*(int(actual.cantidad))
                    else:
                        pass
                    actual=actual.siguiente
                if suma <aux:
                    aux=suma
                else:
                    pass
            else:
                pass
            a=a.siguiente         
        return aux


    def tiempopromediodeespera(self):
        instancia=ListMax()
        actual=self.primero.listadoclientes.primero
        sumat=0
        while actual is not None:
            a=actual.listaTransacciones.primero
            suma=0
            while a is not None:
                suma=suma+(int(a.tiempo))*(int(a.cantidad))
                a=a.siguiente
            sumat=sumat+suma
            instancia.append(nodoMax(sumat))
            actual=actual.siguiente
        return instancia.calcularProm()

    def tiempomaximoespera(self):
        instancia=ListMax()
        actual=self.primero.listadoclientes.primero
        sumat=0
        while actual is not None:
            a=actual.listaTransacciones.primero
            suma=0
            while a is not None:
                suma=suma+(int(a.tiempo))*(int(a.cantidad))
                a=a.siguiente
            sumat=sumat+suma
            instancia.append(nodoMax(sumat))
            actual=actual.siguiente
     #   print("listo")
        return instancia.calcularMax()
    def tiempominimoespera(self):
        instancia=ListMax()
        actual=self.primero.listadoclientes.primero
        sumat=0
        while actual is not None:
            a=actual.listaTransacciones.primero
            suma=0
            while a is not None:
                suma=suma+(int(a.tiempo))*(int(a.cantidad))
                a=a.siguiente
            sumat=sumat+suma
            instancia.append(nodoMax(sumat))
            actual=actual.siguiente

        return instancia.calcularminimo()

    def tiempominimodeesperadefinitivo(self):
        instancia=ListMax()
        tamano=self.primero.listaEsc.CantidaddeEstados()
        iterador=0
        actual=self.primero.listadoclientes.primero

    def Atender(self):
        tamano=self.primero.listaEsc.CantidaddeEstados()
        iterador=0
      #  while iterador != tamano:
        actual1=self.primero.listaEsc.primero
        
        while actual1 is not None or iterador!=int(tamano):

            comrobante=False
            actual2=self.primero.listadoclientes.primero
            while actual2 is not None:
                if actual2.estado ==0:
                    time=0
                    actual3=actual2.listaTransacciones.primero
                    while actual3 is not None:
                        time =time +(int(actual3.tiempo))*(int(actual3.cantidad))
                        actual3=actual3.siguiente



                    actual1.listadoAtencionClientes.append(actual2.dpi,actual2.nombre,time)
                    actual2.estado=2
                    actual1.estado=2
                    iterador=iterador+1
                    break
                else:
                    pass
                actual2=actual2.siguiente
            actual1=actual1.siguiente
            
           # iterador=iterador+1

    def cantidaddeclientes(self):
        actual=self.primero.listadoclientes.primero
        suma=0
        while actual is not None:
            suma=suma+1
            actual=actual.siguiente
        return suma
            
        #    inerador=iterador+1

    def atender1(self):
        
        ulitomocliente=self.primero.listadoclientes.ultimo.estado
        tamano=self.primero.listaEsc.CantidaddeEstados()
        comprobante1=False
      #  graphviz = 'digraph Patron{ \n node[shape=box fillcolor="#FFEDBB" style=filled];  \n subgraph cluster_p{ \n label ='+ '"periodo-{}"'.format(p)+'\n bgcolor="#398D9C" \n raiz[label="0,0"]\n edge[dir="none" style=invisible] \n '

        while True:
            actual1=self.primero.listadoclientes.primero
            while actual1 is not None:
                #aqui calculo el timepo que tardara en atenderse 
                time=0
                actualtrans= actual1.listaTransacciones.primero
                while actualtrans is not None:
                    time = time +(int(actualtrans.tiempo))*(int(actualtrans.cantidad))
                    actualtrans=actualtrans.siguiente
                #veo si el cliente no ha sido atendido
                if actual1.estado==0:
                    actual=self.primero.listaEsc.primero
                    #busco un escritorio que sea activo 
                    comprobante=False
                    while actual is not None:
                        
                        if actual.estado ==1:
                       #     print("si hay estado")
                       #     print(actual1.dpi)
                            if actual1.dpi != None and actual1.nombre != None and time != None:
                                actual.listadoAtencionClientes.append(NodoAtencionCliente(actual1.dpi,actual1.nombre,time))

                                print("------------------------------------------------------------------------")
                              #  print("tiene que haber 4 de estas")
                                print(" El cliente"+str(actual1.nombre)+" esta siendo atendido en el escritorio con ID: "+str(actual.id))
                                print("------------------------------------------------------------------------")
                                print(" ")
                                print(" ")



                                #graficar................................................................................................
                                



                            #le indico que esta siendo atendido
                                actual1.estado=2
                            #desactivio momentaniamente el escritorio
                                actual.estado=2







                                break
                        elif actual.estado==0:
                            actual.estado=0
                        else:
                            pass


                        actual=actual.siguiente
                 #   print("tienen que haber 3")
                else:
                    pass
                actual1=actual1.siguiente
            actualescritorioenespera=self.primero.listaEsc.primero
            tiempominimo=self.tiempominimoClienteEnatencion()
     #       print(tiempominimo)
            while actualescritorioenespera is not None:
                if actualescritorioenespera.estado==2:
                    a=actualescritorioenespera.listadoAtencionClientes.primero
                #    if a.tiempo is not None:
                 #       a.tiempo=a.tiempo - int(tiempominimo)
                    while a is not None:
                        if a.tiempo is not None:
                            a.tiempo=a.tiempo - int(tiempominimo)
                        else:
                            pass
                        a=a.siguiente



                 #   actualescritorioenespera.listadoAtencionClientes.primero.tiempo=actualescritorioenespera.listadoAtencionClientes.primero.tiempo - int(tiempominimo)
                  #  print(actualescritorioenespera.listadoAtencionClientes.primero.tiempo)
                elif  actualescritorioenespera.estado==0:

                    actualescritorioenespera.estado=0


                else:

                    pass
                actualescritorioenespera=actualescritorioenespera.siguiente


            actualescritorioenespera2=self.primero.listaEsc.primero
            while actualescritorioenespera2 is not None:
                if actualescritorioenespera2.estado==1 or actualescritorioenespera2.estado==2:


                    a=actualescritorioenespera2.listadoAtencionClientes.primero
                    suma=0
                    while a is not None:
                        if a.tiempo is not None:
                            suma =suma + int(a.tiempo)
                        else:
                            pass
                        a=a.siguiente
                    if suma <=0:
                        actualescritorioenespera2.estado=1

                        e=actualescritorioenespera2.listadoAtencionClientes.primero
                        while e is not None:

                            e.tiempo=0
                            e=e.siguiente
                    else:
                        pass
                else:
                    pass



                actualescritorioenespera2=actualescritorioenespera2.siguiente


            clientes=self.primero.listadoclientes.primero
            sumatoria=0
            totaldeclientesatendidos=int(self.cantidaddeclientes())
            while clientes is not None:
                if clientes.estado==2:
                    sumatoria=sumatoria+1
                else:
                    pass

                clientes=clientes.siguiente
            if sumatoria == totaldeclientesatendidos:
                return False
            else:
             #   print(sumatoria)
             #   print(totaldeclientesatendidos)
              #  print("nou")
                pass


    def graficar(self):
        graphviz = 'digraph Patron{ \n node[shape=box fillcolor="#FFEDBB" style=filled];  \n subgraph cluster_p{ \n label ='+ '"Atencio al Cliente \n|Activos/Desocupado: Verdes|\n|Ocupados: Amarillo| \n|Inactivos:grises|  "  \n bgcolor="#398D9C" \n edge[dir="none" style=invisible] \n '
        actualf=self.primero.listaEsc.primero
        filas=1

        graphviz += 'Fila1'+'[label="Escritorios",group=1];\n'
        while actualf is not None:
            filas=filas+1
            if actualf.estado==1:
                graphviz += 'Fila{}'.format(filas)+'[label="{}"'.format(actualf.id)+',group=1,fillcolor=green];\n'
            elif actualf.estado==2:
                graphviz += 'Fila{}'.format(filas)+'[label="{}"'.format(actualf.id)+',group=1,fillcolor=yellow];\n'
            elif actualf.estado==0:
                graphviz += 'Fila{}'.format(filas)+'[label="{}"'.format(actualf.id)+',group=1,fillcolor=gray];\n'
            else:
                pass

            actualf=actualf.siguiente

        tamanof=filas+1
     #   for n in range(1,tamanof):
      #      graphviz += 'Fila{}'.format(n)+'[label="{}"'.format(n)+',group=1];\n'

        for n in range(1,tamanof-1):
            graphviz += 'Fila{}'.format(n)+'->Fila{};\n'.format(n+1)
        
        actual=self.primero.listadoclientes.primero
        columnas=0

        while actual is not None:
            columnas=columnas+1
            if actual.estado==0:
                graphviz += 'Columna{}'.format(columnas)+'[label="{}"'.format(actual.dpi)+',group={}'.format(columnas+1)+',fillcolor=blue];\n'
            actual=actual.siguiente

        graphviz += '} }'
        miArchivo=open("graphviz.dot","w")
        miArchivo.write(graphviz)
        miArchivo.close()
        system("dot -Tpng graphviz.dot -o graphviz.png")

        #for n in range(1,tamano):
         #   graphviz += 'Columna{}'.format(n)+'[label="{}"'.format(n)+',group={}'.format(n+1)+',fillcolor=yellow];\n'
        #for n in range(1,tamano-1):
         #   graphviz += 'Columna{}'.format(n)+'-> Columna{};\n'.format(n+1)





#        graphviz += 'raiz -> Fila1;\n'
 #       graphviz += 'raiz -> Columna1;\n'
  #      graphviz += '{rank=same;raiz;'






        #for n in range(1,tamano):
         #   graphviz += 'Columna{};'.format(n)
        #graphviz += '}'






        


     #   self.primero.listaEsc.analizarescritorioenespera(self.tiempominimoClienteEnatencion())

     #   self.primero.listaEsc.librarescritorio()


   
      #  tiempominimo=self.tiempomaximoClientesEnatencion()
       # actualescritoiro=self.primero.listaEsc.primero
        #while actualescritoiro is not None:
         #   if actualescritoiro.listadoAtencionClientes.primero.tiempo==0:         


    def atenderprueba(self):
        
        ulitomocliente=self.primero.listadoclientes.ultimo.estado
        tamano=self.primero.listaEsc.CantidaddeEstados()
        comprobante1=False
      #  graphviz = 'digraph Patron{ \n node[shape=box fillcolor="#FFEDBB" style=filled];  \n subgraph cluster_p{ \n label ='+ '"periodo-{}"'.format(p)+'\n bgcolor="#398D9C" \n raiz[label="0,0"]\n edge[dir="none" style=invisible] \n '

       # while True:
        actual1=self.primero.listadoclientes.primero
        while actual1 is not None:
            #aqui calculo el timepo que tardara en atenderse 
            time=0
            actualtrans= actual1.listaTransacciones.primero
            while actualtrans is not None:
                time = time +(int(actualtrans.tiempo))*(int(actualtrans.cantidad))
                actualtrans=actualtrans.siguiente
            #veo si el cliente no ha sido atendido
            if actual1.estado==0:
                actual=self.primero.listaEsc.primero
                #busco un escritorio que sea activo 
                comprobante=False
                while actual is not None:
                    
                    if actual.estado ==1:
                    #     print("si hay estado")
                    #     print(actual1.dpi)
                        if actual1.dpi != None and actual1.nombre != None and time != None:
                            actual.listadoAtencionClientes.append(NodoAtencionCliente(actual1.dpi,actual1.nombre,time))

                            print("------------------------------------------------------------------------")
                            #  print("tiene que haber 4 de estas")
                            print(" El cliente"+str(actual1.nombre)+" esta siendo atendido en el escritorio con ID: "+str(actual.id))
                            print("------------------------------------------------------------------------")
                            print(" ")
                            print(" ")



                            #graficar................................................................................................
                            



                        #le indico que esta siendo atendido
                            actual1.estado=2
                        #desactivio momentaniamente el escritorio
                            actual.estado=2







                            break
                    elif actual.estado==0:
                        actual.estado=0
                    else:
                        pass


                    actual=actual.siguiente
                #   print("tienen que haber 3")
            else:
                pass
            actual1=actual1.siguiente
        actualescritorioenespera=self.primero.listaEsc.primero
        tiempominimo=self.tiempominimoClienteEnatencion()
    #       print(tiempominimo)
        while actualescritorioenespera is not None:
            if actualescritorioenespera.estado==2:
                a=actualescritorioenespera.listadoAtencionClientes.primero
            #    if a.tiempo is not None:
                #       a.tiempo=a.tiempo - int(tiempominimo)
                while a is not None:
                    if a.tiempo is not None:
                        a.tiempo=a.tiempo - int(tiempominimo)
                    else:
                        pass
                    a=a.siguiente



                #   actualescritorioenespera.listadoAtencionClientes.primero.tiempo=actualescritorioenespera.listadoAtencionClientes.primero.tiempo - int(tiempominimo)
                #  print(actualescritorioenespera.listadoAtencionClientes.primero.tiempo)
            elif  actualescritorioenespera.estado==0:

                actualescritorioenespera.estado=0


            else:

                pass
            actualescritorioenespera=actualescritorioenespera.siguiente


        actualescritorioenespera2=self.primero.listaEsc.primero
        while actualescritorioenespera2 is not None:
            if actualescritorioenespera2.estado==1 or actualescritorioenespera2.estado==2:


                a=actualescritorioenespera2.listadoAtencionClientes.primero
                suma=0
                while a is not None:
                    if a.tiempo is not None:
                        suma =suma + int(a.tiempo)
                    else:
                        pass
                    a=a.siguiente
                if suma <=0:
                    actualescritorioenespera2.estado=1

                    e=actualescritorioenespera2.listadoAtencionClientes.primero
                    while e is not None:

                        e.tiempo=0
                        e=e.siguiente
                else:
                    pass
            else:
                pass



            actualescritorioenespera2=actualescritorioenespera2.siguiente


        clientes=self.primero.listadoclientes.primero
        sumatoria=0
        totaldeclientesatendidos=int(self.cantidaddeclientes())
        while clientes is not None:
            if clientes.estado==2:
                sumatoria=sumatoria+1
            else:
                pass

            clientes=clientes.siguiente
        if sumatoria == totaldeclientesatendidos:

            print("clientes atendidos")
        else:

            pass


            #   print(sumatoria)
            #   print(totaldeclientesatendidos)
            #  print("nou")



    def comportamientoatencion(self):
        actual=self.primero.listaEsc.primero
        contador=1
        while actual is not None:
            if actual is not None:
                print("\t Escritorio No.{}".format(contador))
                print("Engargado: "+str(actual.encargado)+"  ID: "+str(actual.id))
                actual.listadoAtencionClientes.mostrar()
                contador=contador+1
            else:
                pass
            actual=actual.siguiente
