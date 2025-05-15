#VITAE CONSOLE
#Registrar
#Actualizar
#COnsultar hojas de vida con multiples secciones

#registro datos personales, educativos, profesional
#de referencia y otros 
#visualizar , actualizar, exportar cada hoja de vida

#REGISTRO HOJA DE VIDA COMPLETA

hojadevida = {}

def registrarhoja(): #DATOS BASICOS
    cedula = int(input("Ingrese numero cedula: "))
    if cedula in hojadevida:
        print("ya existe una hoja de vida")
        return
    
    nombre = input("Nombre completo : ")
    correo = input("Correo electronico: ")
    telefono = input("Telefono: ")
    direccion = input("Direccion: ")

    educacion = input("Nivel educativo: ")
    institucion = input("Institucion Educativa: ")
    titulo = input("Titulo obtenido")

    empresa = input("Ultima empresa donde trabajo: ")
    cargo = input("Cargo desempeñado: ")
    tiempo = int(input("Tiempo en empresa: "))
    
    referencia_nombre= input("Nombre referencia personal: ")
    referencia_contacto=input("numero referencia personal")
    referencia_familiar = input("Nombre referencia familiar: ")
    referencia_contactoFa=input("Numero contacto familiar")

    habilidades_especificas = input("Habilidades separadas por (,): ")

    hoja = {
        "nombre": nombre,
        "correo": correo,
        "telefono": telefono,
        "direccion": direccion,
        "educacion": educacion,
        "institucion": institucion,
        "titulo": titulo,
        
    }