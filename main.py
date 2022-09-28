import xml.etree.ElementTree as ET
from ListaEmpresa import ListaEmpresa
#from NodoCabeza import Nodo_Cabecera
from NodoEmpresa import NodoEmpresa
from NodoEscritorio import NodoEscritorio
#from ListaEscritorio import ListaEscritorio
from NodoPuntosAtencion import NodoPuntosAtencion
from NodoTransaccion import NodoTransaccion
#from ListaTransaccion import ListaTransaccion

def menu():
    listaempresa=ListaEmpresa()
   # listaescritorio=ListaEscritorio()
    #listatransaccion=ListaTransaccion()

    while True:
        
        print('|***************** Menú ****************|')
        print()
        print(' → 1. Limpiar sistema.')
        print(' → 2. Cargar archivos.')
        print(' → 3. Crear nueva empresa.')
        print(' → 4. Salir.')
        
        print()
        
        n = input('Digite la opción a realizar: ')
        print()
        print()
        if n=="1":
            listaempresa=ListaEmpresa()
        if n == '2':
            n2 = -1
            try:

                while n2 != 3:
                    
                    while n2 == -1:
                        print('|------------------- Cargar de Archivos -------------------|')
                        print()
                        print(' → Ingrese la ruta de su archivo, si desea regresar al menú principal ingrese "1":')
                        
                        ruta = input('\t →  ')
                        
                        if ruta != '1':
                            tree=ET.parse(ruta)
                            root=tree.getroot()
                            for emp in root:
                              #  print(emp)
           #                     for empresa in emp:
            #                        if empresa.tag.lower()=="listaEmpresas":
                      #                  for idemp in empresa:
                                            
                                            if emp.tag=="empresa":
                                        #        print(emp.tag)

                                                idempresa=emp.get("id")
                              #                  print(emp)
                                                
                                                for name in emp:
                                                    if name.tag.lower()=="nombre":
                                                        nombre=str(name.text)
                                                    elif name.tag.lower()=="abreviatura":
                                                        abreviatura=str(name.text)
                                                        nuevaempresa=NodoEmpresa(idempresa,nombre,abreviatura)
                                                        listaempresa.append(nuevaempresa)
                                                        buscar=listaempresa.buscarempresa(idempresa)




                                                    elif name.tag=="listaPuntosAtencion":
                                                        for pantencion in name:
                                                            if pantencion.tag=="puntoAtencion":
                                                                puntoatencion=pantencion.attrib["id"]
                                                                for datopunto in pantencion:
                                                                    if datopunto.tag.lower()=="nombre":
                                                                        nombrepunto=str(datopunto.text)
                                                                    elif datopunto.tag.lower()=="direccion":
                                                                        print(datopunto.tag)
                                                                        direccionpunto=str(datopunto.text)
                                                                        nuevopuntoatencion=NodoPuntosAtencion(puntoatencion,nombrepunto,direccionpunto)
                                                                        buscar.ListaPuntosAtencion.append(nuevopuntoatencion)
                                                                        
                                                                    elif datopunto.tag=="listaEscritorios":
                                                                        for datoecri in datopunto:
                                                                            if datoecri.tag.lower()=="escritorio":
                                                                                idescritorio=datoecri.attrib["id"]
                                                                                buscar2=buscar.ListaPuntosAtencion.buscarempresa(idescritorio)
                                                                            elif datoecri.tag.lower()=="identificacion":
                                                                                identificacionescri=str(datoecri.text)
                                                                            elif datoecri.tag.lower()=="encargado":
                                                                                encargadoescri=str(datoecri.text)
                                                                                nuevoescritorio=NodoEscritorio(idescritorio,identificacionescri,encargadoescri)
                                                                          #      listaescritorio.append(nuevoescritorio)
                                                                                buscar2.listaEsc.append(nuevoescritorio)
                                                                                
                                                    elif name.tag=="listaTransacciones":
                                                        for trans in name:
                                                            if trans.tag.lower()=="transaccion":
                                                                transaccion=trans.attrib["id"]
                                                            elif trans.tag.lower()=="nombre":
                                                                transnombre=str(trans.text)
                                                            elif trans.tag=="tiempoAtencion":
                                                                tiempoatencion=str(trans.text)
                                                                nuevatransaccion=NodoTransaccion(transaccion,transnombre,tiempoatencion)
                                                                buscar.ListaTransiccion.append(nuevatransaccion)
                                                               # listatransaccion.append(nuevatransaccion)

                                                            

                            
                        else:
                            
                            n2 = 3
                            print('|----------------------------------------------------------|')
                            print("f")
                            print()
                            break
                        
                        print('|----------------------------------------------------------|')
                        print("f")
                        listaempresa.print()
                        print()
                        n2 = 2

                
                    
            except:
                
                print(' ha ingresado un digito no númerico, por favor vuelve a intentar.')









        if n== "4":
            return False
                  
menu()