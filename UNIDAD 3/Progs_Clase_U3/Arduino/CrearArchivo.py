def guardar (nombrearchivo, datos):
    archivo = open ("../../ Progs_Clase_U3"+nombrearchivo+"txt","w")

    for i in datos:
        archivo.write(str(i))
        archivo.flush()
        archivo.close()


d = [10, 20, 30]
#d = ["10, 4,5,8", "1,2,3,5", "4,7,3,2"]
guardar("prueba",d)

