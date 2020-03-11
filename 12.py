class direccion:
    def __init__(self):
        self.__calle = ''
        self.__piso = ''
        self.__ciudad = ''
        self.__cp = ''
    def getCalle(self):
        return self.__calle
    def getPiso(self):
        return self.__piso
    def getCiudad(self):
        return self.__ciudad
    def getCp(self):
        return self.__cp
    def setCalle(self,calle):
        self.__calle = calle
    def setPiso(self,piso):
        self.__piso = piso
    def setCiudad(self,ciudad):
        self.__ciudad = ciudad
    def setCp(self,cp):
        self.__cp = cp

class persona:
    def __init__(self):
        self.__nombre = ''
        self.__apellidos = ''
        self.__fechaNac = ''
    def getNombre(self):
        return self.__nombre
    def getApellidos(self):
        return self.__apellidos
    def getFechaNac(self):
        return self.__fechaNac
    def setNombre(self,nombre):
        self.__nombre = nombre
    def setApellidos(self,apellidos):
        self.__apellidos = apellidos
    def setFechaNac(self,fecha):
        self.__fechaNac = fecha

class telefono:
    def __init__(self):
        self.__movil = ''
        self.__fijo = ''
        self.__trabajo = ''
    def getMovil(self):
        return self.__movil
    def getFijo(self):
        return self.__fijo
    def getTrabajo(self):
        return self.__trabajo
    def setMovil(self,movil):
        self.__movil = movil
    def setFijo(self,fijo):
        self.__fijo = fijo
    def setTrabajo(self,trabajo):
        self.__trabajo = trabajo

class Contacto(direccion,persona,telefono):
    def __init__(self):
        self.__email = ''
    def getEmail(self):
        return self.__email
    def setEmail(self,mail):
        self.__email = mail
    def showContacto(self):
        print('---CONTACTO---')
        print('Nombre:',self.getNombre())
        print('Apellidos:',self.getApellidos())
        print('Fecha de nacimiento:',self.getFechaNac())
        print('Teléfono móvil:',self.getMovil())
        print('Teléfono fijo:',self.getFijo())
        print('Teléfono trabajo:',self.getTrabajo())
        print('Calle:',self.getCalle())
        print('Piso:',self.getPiso())
        print('Ciudad:',self.getCiudad())
        print('C.P.:',self.getCp())
        print('Email:',self.getEmail())

class agenda:
    
    def __init__(self,path):
        self.__listaContactos = []
        self.__path = path
        
    def cargarContactos(self):
        try:
            fichero = open(self.__path,'r')
        except:
            print('ERROR: El fichero no existe')
        else:
            contactos = fichero.readlines()
            fichero.close()
            if(len(contactos)>0):
                for contacto in contactos:
                    datos = contacto.split('#')
                    if(len(datos)==11):
                        nuevoContacto = Contacto()
                        nuevoContacto.setNombre(datos[0])
                        nuevoContacto.setApellidos(datos[1])
                        nuevoContacto.setFechaNac(datos[2])
                        nuevoContacto.setMovil(datos[3])
                        nuevoContacto.setFijo(datos[4])
                        nuevoContacto.setTrabajo(datos[5])
                        nuevoContacto.setCalle(datos[6])
                        nuevoContacto.setPiso(datos[7])
                        nuevoContacto.setCiudad(datos[8])
                        nuevoContacto.setCp(datos[9])
                        nuevoContacto.setEmail(datos[10])
                        self.__listaContactos = self.__listaContactos + [nuevoContacto]
                print('INFO: Cargados',len(self.__listaContactos),'contactos')
                
    def crearContacto(self,contacto):
        self.__listaContactos = self.__listaContactos + [contacto]

    def guardarContacto(self):
        try:
            fichero = open(self.__path,'w')
        except:
            print('ERROR: El fichero no se puede guardar')
        else:
            for contacto in self.__listaContactos:
                texto = contacto.getNombre() + '#'
                texto = texto + contacto.getApellidos() + '#'
                texto = texto + contacto.getFechaNac() + '#'
                texto = texto + contacto.getMovil() + '#'
                texto = texto + contacto.getFijo() + '#'
                texto = texto + contacto.getTrabajo() + '#'
                texto = texto + contacto.getCalle() + '#'
                texto = texto + contacto.getPiso() + '#'
                texto = texto + contacto.getCiudad() + '#'
                texto = texto + contacto.getCp() + '#'
                texto = texto + contacto.getEmail() + '\n'
                fichero.write(texto)
            fichero.close()

    def mostrarAgenda(self):
        print('### Agenda ###')
        print('Numero de contactos:',len(self.__listaContactos),'\n')
        for contacto in self.__listaContactos:
            contacto.showContacto()
        print('######')

    def buscarContacto(self,tipo,dato):
        listaEncontrados = []
        for contacto in self.__listaContactos:
            if tipo == 1:
                if contacto.getNombre() == dato:
                    listaEncontrados = listaEncontrados + [contacto]  
            elif tipo == 2:
                if contacto.getMovil() == dato:
                    listaEncontrados = listaEncontrados + [contacto]
            elif tipo == 3:
                if contacto.getFijo() == dato:
                    listaEncontrados = listaEncontrados + [contacto]
            elif tipo == 4:
                if contacto.getTrabajo() == dato:
                    listaEncontrados = listaEncontrados + [contacto]
        return listaEncontrados

    def borrarContacto(self,tipo,dato):
        listaFinal = []
        for contacto in self.__listaContactos:
            if tipo == 1:
                if contacto.getNombre() != dato:
                    listaFinal = listaFinal + [contacto]  
            elif tipo == 2:
                if contacto.getMovil() != dato:
                    listaFinal = listaFinal + [contacto]
            elif tipo == 3:
                if contacto.getFijo() != dato:
                    listaFinal = listaFinal + [contacto]
            elif tipo == 4:
                if contacto.getTrabajo() != dato:
                    listaFinal = listaFinal + [contacto]
        print('INFO:',len(self.__listaContactos)-len(listaFinal),'contactos han sido borrados')
        self.__listaContactos = listaFinal

def obtenerOpcion(texto):
    leido = False
    while not leido:
        try:
            numero = int(input(texto))
        except ValueError:
            print('El valor debe ser un numero')
        else:
            leido = True
    return numero

def mostrarMenu():
    print('########## MENÚ PRINCIPAL ####################')
    print('1 - Mostrar contactos')
    print('2 - Buscar contactos')
    print('3 - Crear nuevo contacto')
    print('4 - Borrar contactos')
    print('5 - Guardar contactos')
    print('6 - Salir')

def buscarContactos(agenda):
    print('Buscar contactos')
    print('1 - Nombre')
    print('2 - Movil')
    print('3 - Fijo')
    print('4 - Trabajo')
    print('5 - Salir')
    finBuscar = False
    while not finBuscar:
        opcion = obtenerOpcion('Opción de búsqueda:')
        if opcion == 5:
            finBuscar = True
        encontrados = agenda.buscarContacto(opcion,input('Introduce el valor:'))
        if len(encontrados) > 0:
            print('### CONTACTOS ENCONTRADOS ###')
            for item in encontrados:
                item.showContacto()
            print('######')
        else:
            print('INFO: No se han encontrado contactos')

def procesoCrearContacto(agenda):
    nuevoContacto = Contacto()
    nuevoContacto.setNombre(input('Introduce el nombre:'))
    nuevoContacto.setApellidos(input('Introduce los apellidos:'))
    nuevoContacto.setFechaNac(input('Introduce la fecha de nacimiento:'))
    nuevoContacto.setMovil(input('Introduce el movil:'))
    nuevoContacto.setFijo(input('Introduce el fijo:'))
    nuevoContacto.setTrabajo(input('Introduce el teléfono del trabajo:'))
    nuevoContacto.setCalle(input('Introduce la calle:'))
    nuevoContacto.setPiso(input('Introduce el piso:'))
    nuevoContacto.setCiudad(input('Introduce la ciudad:'))
    nuevoContacto.setCp(input('Introduce el C.P.:'))
    nuevoContacto.setEmail(input('Introduce el email:'))
    agenda.crearContacto(nuevoContacto)

def borrarContacto(agenda):
    print('Borrar contacto')
    print('1 - Nombre')
    print('2 - Movil')
    print('3 - Fijo')
    print('4 - Trabajo')
    print('5 - Salir')
    finBuscar = False
    while not finBuscar:
        opcion = obtenerOpcion('Opción de borrado:')
        if opcion == 5:
            finBuscar = True
        else:
            encontrados = agenda.borrarContacto(opcion,input('Introduce el valor:'))
            finBuscar = True

def Main():
    nuevaAgenda = agenda('./files/agenda.txt')
    nuevaAgenda.cargarContactos()
    fin = False
    while not fin:
        mostrarMenu()
        opcion = obtenerOpcion('Opción:')
        if(opcion==1):
            nuevaAgenda.mostrarAgenda()
        elif(opcion==2):
            buscarContactos(nuevaAgenda)
        elif(opcion==3):
            procesoCrearContacto(nuevaAgenda)
        elif(opcion==4):
            borrarContacto(nuevaAgenda)
        elif(opcion==5):
            nuevaAgenda.guardarContacto()
        elif(opcion==6):
            fin = True

Main()
        
