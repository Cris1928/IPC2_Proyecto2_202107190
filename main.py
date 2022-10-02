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
from NodoClientesDef import NodoListadoClientesD
from NodoUltimaTrans import NodoUlitmaTras
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
                                print(' → Ingrese la ruta de su archivo, si desea regresar al menú principal ingrese "salir":')
                                
                                ruta = input(' →  ')
                                
                                if ruta.upper() != 'salir'.upper():
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
                                                                nuevaempresa=NodoEmpresa(idempresa,nombre,abreviatura,0)
                                                                listaempresa.append(nuevaempresa)
                                                                buscar=listaempresa.buscarPunto(idempresa)
                                                                

                                                            elif name.tag=="listaPuntosAtencion":
                                                                for pantencion in name:
                                                                    if pantencion.tag=="puntoAtencion":
                                                                        puntoatencion=pantencion.attrib["id"]
                                                                        for datopunto in pantencion:
                                                                            if datopunto.tag.lower()=="nombre":
                                                                                nombrepunto=str(datopunto.text)
                                                                            elif datopunto.tag.lower()=="direccion":
                                                                                #print(datopunto.tag)
                                                                                direccionpunto=str(datopunto.text)
                                                                                nuevopuntoatencion=NodoPuntosAtencion(puntoatencion,nombrepunto,direccionpunto,0)
                                                                                buscar.ListaPuntosAtencion.append(nuevopuntoatencion)
                                                                                buscar2=buscar.ListaPuntosAtencion.buscarescritorio(puntoatencion)
                                                                                
                                                                                
                                                                            elif datopunto.tag=="listaEscritorios":
                                                                                for datoecri in datopunto:
                                                                                    if datoecri.tag=="escritorio":
                                                                                        idescritorio=datoecri.attrib["id"]
                                                                                        for n in datoecri:
                                                            #                            print(idescritorio)
                                                                  #                      buscar2=buscar.ListaPuntosAtencion.buscarescritorio(idescritorio)
                                                                                            if n.tag.lower()=="identificacion":
                                                                                                identificacionescri=str(n.text)
                                                                                            elif n.tag.lower()=="encargado":
                                                                                                encargadoescri=str(n.text)
                                                                                                nuevoescritorio=NodoEscritorio(idescritorio,identificacionescri,encargadoescri,0)
                                                                                        #      listaescritorio.append(nuevoescritorio)
                                                                                                buscar2.listaEsc.append(nuevoescritorio)
                                                                                        
                                                            elif name.tag=="listaTransacciones":
                                                                for trans in name:
                                                                    if trans.tag.lower()=="transaccion":
                                                                        transaccion=trans.attrib["id"]
                                                                       # print(transaccion)
                                                                    for re in trans:

                                                                        if re.tag.lower()=="nombre":
                                                                            transnombre=str(re.text)
                                                                         #   print(transnombre)
                                                                            
                                                                        elif re.tag=="tiempoAtencion":
                                                                            tiempoatencion=str(re.text)
                                                                            nuevatransaccion=NodoTransaccion(transaccion,transnombre,tiempoatencion)
                                                                            buscar.ListaTransiccion.append(nuevatransaccion)
                                                                    #        buscar.ListaTransiccion.print()
                                                                            
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
                    listaempresa3=NodoEmpresa(idEmpresa3,nombreEmpresa3,abreviatura3,0)
                    listaempresa.append(listaempresa3)
                    buscar3=listaempresa.buscarPunto(idEmpresa3)
                    print("---------------- LISTA PUNTO ATENCION----------------")
                    cantidaddepuntos=int(input("¿cuantos puntos de atencion desea?: "))
                    contador=0
                    while contador <= cantidaddepuntos:
                        idatencion3=str(input("ingrese el id de el punto de atencion: "))
                        nombreatencion3=str(input("ingrese el nombre del punto de servicio: "))
                        dereccionatencion3=str(input("ingrese la direccion del punto de servicio: "))
                        puntodeatencion3=NodoPuntosAtencion(idatencion3,nombreatencion3,dereccionatencion3,0)
                        buscar3.ListaPuntosAtencion.append(puntodeatencion3)
                        buscarescritorio3=buscar3.ListaPuntosAtencion.buscarescritorio(idatencion3)
                        numescritorios=int(input("¿cuantos escritorios desea?: "))
                        contador1=0
                        while contador1<= numescritorios:
                            idescritorio3=str(input("ingrese el id de el escritorio: "))
                            identificacion3=str(input("ingrese la identificacion del escritorio: "))
                            nombreencargado3=str(input("ingrese el nombre del encargado del escritorio: "))
                            nuevoescritorio3=NodoEscritorio(idescritorio3,identificacion3,nombreencargado3,0)
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

#C:\Users\USER\Downloads\prueba1.xml
#C:\Users\USER\Downloads\prueba2.xml
                elif np=="4":
                    n22 = -1
           #         try:

                    while n22 != 3:
                        
                        while n22 == -1:
                            print('|------------------- Cargar archivo con configuración inicial -------------------|')
                            print()
                            print(' → Ingrese la ruta de su archivo, si desea regresar al menú principal ingrese "salir":')   
                            ruta2 = input(' →  ')           
                            if ruta2.upper() != 'salir'.upper():
                                treee=ET.parse(ruta2)
                                root2=treee.getroot()
                                for empc in root2:
                                    if empc.tag=="configInicial":
                                        idconfig=empc.get("id")
                                        idempresaconfig=empc.get("idEmpresa")
                                        #-----------------------------------------
    #                                    listaempresa.CambiarEstado(idempresaconfig)
     #                                   buscarconfigesc=listaempresa.buscarempresa(idempresaconfig)
                                    



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
#---------------------------
       #                                                 buscaesccon=buscarconfigesc.ListaPuntosAtencion.buscarescritorio(idescritorioconfig)
        #                                                if buscaesccon is not None:
         #                                                   buscaesccon.listaEsc.CambiarEstado(idescritorioconfig)
          #                                              else:
           #                                                 pass


                                                        

                                            if escAc.tag=="listadoClientes":
                                                for cli in escAc:
                                                    if cli.tag.lower()=="cliente":
                                                        dpiconfig=cli.get("dpi")
                                                        for clireg in cli:
                                                            if clireg.tag.lower()=="nombre":
                                                                nombreclienteconfig=str(clireg.text)
                                                                nuevaclienteconfig=NodoListadoClientes(dpiconfig,nombreclienteconfig)
                                                                buscarconfig.ListadoClientes.append(nuevaclienteconfig)
                            #------------------------------------
         #                                                       buscaesccon.listadoclientes.append(nuevaclienteconfig)
          #                                                      buscarcliente2=buscaesccon.listadoclientes.buscarcliente(buscaesccon)
                                                                buscarcliente=buscarconfig.ListadoClientes.buscarcliente(dpiconfig)
                                                            elif clireg.tag=="listadoTransacciones":
                                                                for transaccionreg in clireg:
                                                                    if transaccionreg.tag.lower()=="transaccion":
                                                                        idtransreg=transaccionreg.get("idTransaccion")
                                                                        cantidadtranreg=transaccionreg.get("cantidad")
                                                                        nuevatransaccionconfig=NodoTrasaccionesConfig(idtransreg,cantidadtranreg)
                            #-----------------------------------------
           #                                                             buscarcliente2.listaTransaccionesConfig.append(nuevatransaccionconfig)
                                                                        buscarcliente.listaTransaccionesConfig.append(nuevatransaccionconfig)
                                #listaconfig.print()
                                                                        
                                    
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
    #        buscarescritorio                
     #               except:
      #                  
       #                 print(' ha ingresado un digito no númerico, por favor vuelve a intentar.')
                elif np=="5":
                    verificador1=False
                    verificador=True
#C:\Users\USER\Downloads\prueba1.xml
#C:\Users\USER\Downloads\prueba2.xml

        elif n=="2":
            actual=listaempresa.primero
            actual2=listaconfig.primero
            while actual2 is not None:
                listaempresa.CambiarEstado(actual2.idempresa)

                busqueda=listaempresa.buscarPunto(actual2.idempresa)

                if busqueda is not None:
                    actual22=listaconfig.primero
                    while actual22 is not None:
                        busqueda.ListaPuntosAtencion.CambiarEstado(actual22.idpunto)
                        

                        actual222=actual22.ListaEscritoriosActivos.primero
                        
                        busqueda2=busqueda.ListaPuntosAtencion.buscarescritorio(actual22.idpunto)
                        while actual222 is not None:
                            

                            if busqueda2 is not None:

                                busqueda2.listaEsc.CambiarEstados(actual222.idEscritorioActivo)
                                
                            
                                #busqueda2.listaEsc.printt()
                             #   print(actual222.idEscritorioActivo)
                            else:
                                pass
                            actual222=actual222.siguiente
                        
                        actualcli=actual22.ListadoClientes.primero
                        while actualcli is not None:
                            

                            if busqueda2 is not None:
     #                           print(busqueda2.nombrepuntoservicio)
                                if busqueda2.listadoclientes.buscarcliente(actualcli.dpi) == None:
                                    
                 #                   print("el punto es:",busqueda2.nombrepuntoservicio)
                                    busqueda2.listadoclientes.append(NodoListadoClientesD(actualcli.dpi,actualcli.nombre))


                                    busqueda3=busqueda2.listadoclientes.buscarcliente(actualcli.dpi)
                   #                 if busqueda3 is not None:
                     #                   print(busqueda3.nombre)
                                    if actualcli.listaTransaccionesConfig.primero is not None:
                                        
                                        
                                        a=actualcli.listaTransaccionesConfig.primero
                                        while a is not None:
                                            e=busqueda.ListaTransiccion.buscarTrans(a.idTransaccion)
                                         #   busqueda.ListaTransiccion.print
                                            
                                            if e is not None:
                                                if busqueda3 is not None:
                                                    
                                        
                                                    busqueda3.listaTransacciones.append(NodoUlitmaTras(a.idTransaccion,e.nombreTransaccion,a.cantidad,e.minutosAtencion))
#                                                print(e.nombreTransaccion)



                                    
                                        
 #                                           print(a.idTransaccion)
                                            a=a.siguiente
  #                                      print(" cambio ")
                                    

                               #     actu=busqueda3.listaTransaccionesConfig.primero
                         #           while actu is not None:
                          #              print(actu.idTransaccion)
                           #             actu=actu.siguiente
                                    




                    #                print("el nombre del cliente es: ",actualcli.nombre)
                                    
                                else:
                                    pass                      
                            else:
                                pass

                            actualcli=actualcli.siguiente

                 #       print(" cambio")


                        

                        actual22=actual22.siguiente                    
                   # busqueda2=busqueda.ListaPuntosAtencion.buscarescritorio()


                actual2=actual2.siguiente
            

               
            if int(listaempresa.returnTamano()) != 0:


                listaempresa.print()
                print(" ")
                decision=int(input("ingrese la empresa: "))
                print("--- PUNTOS DE ATENCION---")
                print(" ")
                listaempresa.returnEmpresa(decision)

                b=listaempresa.returnEvaluarEmpresas(decision)
           #     print("-------name--------")
               # b.calculo()
                print(" ")
                decision2=int(input("ingrese el punto de atencion: "))
                b2=b.returnEvaluarEscritorios(decision2)




#                listaempresa.printEstados()
 #               print(" ")
  #              decision=int(input("ingrese la empresa: "))
   #             print("--- PUNTOS DE ATENCION---")
    #            print(" ")
     #           listaempresa.returnEmpresaEstado(decision)
      #          b=listaempresa.returnEvaluarEmpresa(decision)
       #    #     print("-------name--------")
        #       # b.calculo()
         #       print(" ")
          #      decision2=int(input("ingrese el punto de atencion: "))
           #     b2=b.returnEvaluarEscritorio(decision2)
                
                
                
            
                

                
                

#calculo
   #         else:
    #            print(" ")
     #           print("No hay empresas registradas en el sistema")
      #          print(" ")

        elif n=="3":
            verificador2=True
            while verificador2 == True:
                print("-------- MANEJO PUNTOS DE ATENCION--------")
                print("→ 1. Ver estado de punto de atencion.")
                print("→ 2. Activar escritorio de servicio.")
                print("→ 3. Desactivar escritorio.")
                print("→ 4. Atender cliente.")
                print("→ 5. Solicitud de atencion.")
                print("→ 6. Simular actividad del punto de atencion.")
                print(" ")
                print(" ")
                decisionPatencion=int(input("ingrese el numero: "))
                if decisionPatencion==1:
                    print("cantidad de escritorios activos: ",b2.CantidaddeEstados())
                    print("Cantidad de escritorios inactivos: ",b2.CantidaddeEstadosInactivos())
                    #print("Cantidad de clientes en espera: ",b.CantidaddeClientes())
                    print("Clientes en espera: ")
                    b.calculo()
                    
            
             #       b2.Escritoriosinactivos()
                    print(" ")
                elif decisionPatencion==2:
                   b2.Escritoriosinactivos()
                   print(" ")
                   cambiarestado=int(input("ingrese el escritorio que desea cambiar de estado: "))
                   b2.reevaluaresc(cambiarestado)
                   print(" ")
                   print("LISTO")
                elif decisionPatencion==3:
                    b2.Escritoriosactivos()
                    print(" ")
                    cambiarestad2=int(input("ingrese el escritorio que desea cambiar de estado: "))
                    b2.reevaluaresc2(cambiarestad2)
                elif decisionPatencion ==4:
                    print(b.cantidaddetrans())

                    



        elif n== "4":

        
            verificador= False
                  
menu()
"""

"""