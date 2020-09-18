#manejador_archivo = open("mbox.txt" ,"r")
#print (manejador_archivo)
#mensaje = manejador_archivo.read()
#print (mensaje)
#manejador_archivo.close()


with open("maravillas_antiguas.csv", "r") as archivo:
    for linea in archivo:
        if (linea.find ("Grecia")! = -1):
        print(linea, end='')

