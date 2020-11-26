import os
import re
import sys


def registro():
    codigo = input("IngresÃ¡ el codigo del producto: ")
    nombre = input("IngresÃ¡ el nombre del producto: ")
    precio = int(input("Precio Actual: "))
    unidades = int(input("Unidades Adqueridas: "))

    total = precio*unidades

    return codigo+" "+nombre+" "+str(precio)+" "+str(unidades)+" | Total: "+str(total)+"\n"

while True:
    
    print("""
    1. Registrar Productos                
    2. Imprimir el Total y productos comprados
    3. Buscar Productos                   
    4. Eliminar Productos                 
    6. Ver Total
    9. Salir                           
    """)
    
    
    opcion = int(input("Escoga una opcion:"))

    if opcion == 1:
        os.system('cls')
        row_data=registro()
        file = open("registroCarga.txt", "a+")
        file.write(row_data)
        file.close()
        print("Datos agregados exitosamente")

        nuevo_registro=input("Desea insertar otro registro?(s/n)")

        while nuevo_registro == "s":
            os.system('cls')
            row_data=registro()
            file = open("registroCarga.txt", "a+")
            file.write(row_data)
            file.close()
            print("Datos agregados exitosamente \n")
            print("")
            nuevo_registro = input("Desea insertar otro registro?(s/n): ")
           
    elif opcion == 2:
        os.system('cls')
        print("Codigo Nombre Precio Cantidad Total")
        open_file = open("registroCarga.txt","r")
        for linea in open_file.readlines():
            print(linea)
        open_file.close()
        print("<---------------FIN----------------->")

    elif opcion == 3:
        os.system('cls')
        busqueda=input("IngresÃ¡ el codigo que quisiera encontrar: ")
        with open("registroCarga.txt", "r") as file:
            for line in file:
                palabra = re.match(busqueda, line)
                if palabra:
                    print(line)

    elif opcion == 4:
        os.system('cls')
        dato_eliminar = input("IngresÃ¡ el codigo del dato que quisiera eliminar: ")

        f = open("registroCarga.txt","r")
        lineas = f.readlines()
        f.close()

        with open("registroCarga.txt", "r") as file:
            for line in file:
                palabra = re.match(dato_eliminar, line)

                if palabra:
                    valor=line
                    
        file = open("registroCarga.txt", "w")
        for linea in lineas:
                
            if linea != valor:                
                file.write(linea)
        
        file.close()
        print("<---------------Datos Eliminados----------------->")




    elif opcion == 6:
        os.system('cls')
     
        open_file = open("registroCarga.txt","r")
        for linea in open_file.readlines():
            lin = linea
            print(lin.lstrip("| "))
        open_file.close()
        print("<---------------FIN----------------->")


    elif opcion == 9:
        os.system('cls')
        sys.exit() 
    else:
        os.system('cls')
        print(">>>>>Reintente <<<<<")
        print("<---------------FIN----------------->")