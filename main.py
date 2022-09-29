import xml.etree.ElementTree as ET
from ListaEmpresa import ListaEmpresa
#from NodoCabeza import Nodo_Cabecera
from NodoEmpresa import NodoEmpresa
from NodoEscritorio import NodoEscritorio
#from ListaEscritorio import ListaEscritorio
from NodoPuntosAtencion import NodoPuntosAtencion
from NodoTransaccion import NodoTransaccion
#from ListaTransaccion import ListaTransaccion
from NodoTransaccionesConfig import NodoTrasaccionesConfig
from NodoConfiguracionInicial import NodoConfiguracionInicial
from NodoEscritoriosActivos import NodoEscritoriosActivos
from NodoListadoClientes import NodoListadoClientes
from ListaConfiguracionInicial import ListaConfiguracionInicial

#from N


def menu():
    listaempresa=ListaEmpresa()
    listaconfig=ListaConfiguracionInicial()
   # listaescritorio=ListaEscritorio()
    #listatransaccion=ListaTransaccion()
    verificador=True

    while verificador==True:
        
        print('|***************** Menú ****************|')
        print()
        print(' → 1. Configuracion de empresas.')
        print(' → 2. Selección de empresa y punto de atención.')
        print(' → 3. Manejo de puntos de atención:.')
        print(' → 4. Salir.')
        
        print()
        
        n = input('Digite la opción a realizar: ')
        print()
        print()
        if n=="1":
            verificador1=True
            while verificador1 == True:
                print('|***************** CONFIGURACION DE EMPRESAS ****************|')
                print()
                print(' → 1. Limpiar sistema.')
                print(' → 2. Cargar archivos.')
                print(' → 3. Crear nueva empresa.')
                print(' → 4. Cargar archivo con configuracion inicial.')
                print(' → 5. Salir.')
                        
                print()
                        
                np = input('Digite la opción a realizar: ')
                print()
                print()
                if np=="1":
                    listaempresa=ListaEmpresa()
                elif np == '2':
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

                                                    if emp.tag=="empresa":
    
                                                        idempresa=emp.get("id")

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
                                                                                        buscar2=buscar.ListaPuntosAtencion.buscarescritorio(idescritorio)
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
                          #      print("f")
                           #     listaempresa.print()
                                print()
                                n2 = 2

                            while n2 == 2:
                                print("¿Desea seguir?")
                                print(' → 1. Si')
                                print(' → 2. No.')
                                
                                
                                n2 = int(input('Digite la opción a realizar: '))
                                print()
                                
                                if n2 == 1:
                                    
                                    n2 = -1
                                    
                                elif n2 == 2:

                                    n2 = 3
                                else:                        
                                    print()
                                    print('Digito no valido')
                                    print()
                                    n2 = 2
                            
                    except:
                        
                        print(' ha ingresado un digito no númerico, por favor vuelve a intentar.')



                elif np=="3":
                    print("--------------------- NUEVA EMPRESA-------------------")
                    idEmpresa3=str(input("ingrese el id de la empresa: "))
                    nombreEmpresa3=str(input("ingrese el nombre de la empresa: "))
                    abreviatura3=str(input("ingrese la abreviatura de la empresa: "))
                    listaempresa3=NodoEmpresa(idEmpresa3,nombreEmpresa3,abreviatura3)
                    listaempresa.append(listaempresa3)
                    buscar3=listaempresa.buscarempresa(idEmpresa3)
                    print("---------------- LISTA PUNTO ATENCION----------------")
                    cantidaddepuntos=int(input("¿cuantos puntos de atencion desea?: "))
                    contador=0
                    while contador <= cantidaddepuntos:
                        idatencion3=str(input("ingrese el id de el punto de atencion: "))
                        nombreatencion3=str(input("ingrese el nombre del punto de servicio: "))
                        dereccionatencion3=str(input("ingrese la direccion del punto de servicio: "))
                        puntodeatencion3=NodoPuntosAtencion(idatencion3,nombreatencion3,dereccionatencion3)
                        buscar3.ListaPuntosAtencion.append(puntodeatencion3)
                        buscarescritorio3=buscar3.ListaPuntosAtencion.buscarescritorio(idatencion3)
                        numescritorios=int(input("¿cuantos escritorios desea?: "))
                        contador1=0
                        while contador1<= numescritorios:
                            idescritorio3=str(input("ingrese el id de el escritorio: "))
                            identificacion3=str(input("ingrese la identificacion del escritorio: "))
                            nombreencargado3=str(input("ingrese el nombre del encargado del escritorio: "))
                            nuevoescritorio3=NodoEscritorio(idescritorio3,identificacion3,nombreencargado3)
                            buscarescritorio3.listaEsc.append(nuevoescritorio3)
                            contador1=contador1+1
                        contador=contador+1
                    cantidaddetransacciones3=int(input("¿cuantas trasacciones necesita?: "))
                    contadort=0
                    while contadort<= cantidaddetransacciones3:
                        idtransaccion3=str(input("ingrese el id de la transaccion: "))
                        nombretransaccion3=str(input("ingrese el nombre de la transaccion: "))
                        minutordetransaccion3=float(input("ingrese los minutos de atencion: "))
                        nuervatransaccion3=NodoTransaccion(idtransaccion3,nombretransaccion3,minutordetransaccion3)
                        buscar3.ListaTransiccion.append(nuervatransaccion3)
                    print("  ")
                    print(" Listo ")

           #     elif np=="3":


                elif np=="4":
                    n22 = -1
                    try:

                        while n22 != 3:
                            
                            while n22 == -1:
                                print('|------------------- Cargar archivo con configuración inicial -------------------|')
                                print()
                                print(' → Ingrese la ruta de su archivo, si desea regresar al menú principal ingrese "1":')   
                                ruta2 = input('\t →  ')           
                                if ruta2 != '1':
                                    treee=ET.parse(ruta2)
                                    root2=treee.getroot()
                                    for empc in root2:
                                        if empc.tag=="configInicial":
                                            idconfig=empc.get("id")
                                            idempresaconfig=empc.get("idEmpresa")
                                            idpuntoconfig=empc.get("idPunto")
                                            print(idpuntoconfig)
                                            nuevaconfiginicial=NodoConfiguracionInicial(idconfig,idempresaconfig,idpuntoconfig)
                                            listaconfig.append(nuevaconfiginicial)
                                            buscarconfig=listaconfig.buscarconfig(idconfig)
                                            for escAc in empc:
                                                if escAc.tag=="escritoriosActivos":
                                                    for esca in escAc:
                                                        if esca.tag.lower()=="escritorio":
                                                            idescritorioconfig=esca.get("idEscritorio")
                                                            nuevoescritorioconfig=NodoEscritoriosActivos(idescritorioconfig)
                                                            buscarconfig.ListaEscritoriosActivos.append(nuevoescritorioconfig)
                                                if escAc.tag=="listadoClientes":
                                                    for cli in escAc:
                                                        if cli.tag.lower()=="cliente":
                                                            dpiconfig=cli.get("dpi")
                                                            for clireg in cli:
                                                                if clireg.tag.lower()=="nombre":
                                                                    nombreclienteconfig=str(clireg.text)
                                                                    nuevaclienteconfig=NodoListadoClientes(dpiconfig,nombreclienteconfig)
                                                                    buscarconfig.ListadoClientes.append(nuevaclienteconfig)
                                                                    buscarcliente=buscarconfig.ListadoClientes.buscarcliente(dpiconfig)
                                                                elif clireg.tag=="listadoTransacciones":
                                                                    for transaccionreg in clireg:
                                                                        if transaccionreg.tag.lower()=="transaccion":
                                                                            idtransreg=transaccionreg.get("idTransaccion")
                                                                            cantidadtranreg=transaccionreg.get("cantidad")
                                                                            nuevatransaccionconfig=NodoTrasaccionesConfig(idtransreg,cantidadtranreg)
                                                                            buscarcliente.listaTransaccionesConfig.append(nuevatransaccionconfig)
                                                                                                       

                                        
                                else:
                                    
                                    n22 = 3
                                    print('|----------------------------------------------------------|')
                                    print("f")
                                    print()
                                    break
                                    
                                print('|----------------------------------------------------------|')
                                print()
                                n22 = 2
                            while n22 == 2:
                                print("¿Desea seguir?")
                                
                                print(' → 1. Si')
                                print(' → 2. No.')
                                
                                n22 = int(input('Digite la opción a realizar: '))
                                print()
                                
                                if n22 == 1:
                                    
                                    n22 = -1
                                    
                                elif n22 == 2:

                                    n22 = 3
                                else:                        
                                    print()
                                    print('Digito no valido')
                                    print()
                                    n22 = 2
                            
                    except:
                        
                        print(' ha ingresado un digito no númerico, por favor vuelve a intentar.')
                elif np=="5":
                    verificador1=False
                    verificador=True


        elif n=="2":
            if int(listaempresa.returnTamano()) != 0:
                listaempresa.print()
                print(" ")
                decision=int(input("ingrese la empresa: "))
                print("--- PUNTOS DE ATENCION---")
                print(" ")
                listaempresa.returnEmpresa(decision)
                print(" ")
                decision2=int(input("ingrese el punto de atencion: "))

            else:
                print(" ")
                print("No hay empresas registradas en el sistema")
                print(" ")


        elif n== "4":
            verificador= False
                  
menu()
"""

"""