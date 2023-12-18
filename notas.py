"""
PROGRAMA PARA CALCULAR LAS NOTAS DE N ESTUDIANTES..
"""
import os
alumnos =[]
isActive = True
menu = "1. Registrar Alumno\n2. Registrar Notas\n3. Buscar estudiante\n4. Salir\n:)"
subMenuNotas = ["Parciales","Quices","Trabajos","Regresar al menu principal"]
opMenu=0
while (isActive) :
    os.system("cls")
    try:
        opMenu = int(input(menu))
    except ValueError:
        print("Error en el dato de de ingreso")
        os.system("pause")
    else:
        if (opMenu == 1):
            rta = "S"
            while (rta in ["S","s"]):
                codigo = input("Ingrese el Codigo del Estudiante: ")
                nombre = input("Ingrese el Nombre del Estudiante: ")
                edad = int(input(f"Ingrese la edad del Estudiante {nombre}: "))
                alumno = [codigo,nombre,edad,[],[],[]]
                alumnos.append(alumno)
                os.system("pause")
                rta = input("Desea registrar otro Alumno S(si) o N(No): ").upper()
        elif (opMenu == 2):
            opNotas = 0
            isActiveGrades = True
            codigo = input("Ingrese el codigo del Estudiante del cual va a registrar las notas: ")
            for item in alumnos:
                if codigo in item:
                    indice=alumnos.index(item)
                    print(f"{alumnos[indice][0]}\t{alumnos[indice][1]}")                    
            os.system("pause")
            print("Seleccione cual nota desea ingresar: ")
            while (isActiveGrades):
                for i,item in enumerate(subMenuNotas):
                    print(f"{i+1}. {item}")
                try:
                    opNotas = int(input(":)"))
                except ValueError:
                    print("Error en el dato de de ingreso")
                    os.system("pause")
                else:
                    if (opNotas == 1):
                        rta = "S"
                        while (rta in ["S","s"]):
                            nota=float(input("Ingrese la nota: "))
                            alumnos[indice][3].append(nota)
                            os.system("pause")
                            rta = input("Desea registrar otra nota S(si) o N(No): ").upper()
                    elif (opNotas == 2):
                        rta = "S"
                        while (rta in ["S","s"]):
                            nota=float(input("Ingrese la nota del Parcial: "))
                            alumnos[indice][4].append(nota)
                            os.system("pause")
                            rta = input("Desea registrar otra nota S(si) o N(No): ").upper()
                    elif (opNotas == 3):
                        rta = "S"
                        while (rta in ["S","s"]):
                            nota=float(input("Ingrese la nota del Quis: "))
                            alumnos[indice][5].append(nota)
                            os.system("pause")
                            rta = input("Desea registrar otra nota S(si) o N(No): ").upper()
                    elif (opNotas == 4):
                        isActiveGrades = False                        
                    else:
                        rta = "S"
                        while (rta in ["S","s"]):
                            nota=input("Ingrese la nota del trabajo: ")
                            alumnos[indice][5].append(nota)
                            os.system("pause")
                            rta = input("Desea registrar otra nota S(si) o N(No): ").upper()
        elif (opMenu == 3):
            codigo = input("Ingrese el codigo del Estudiante: ")
            for item in alumnos:
                if codigo in item:
                    print(item)
            os.system("pause")
        elif (opMenu == 4):
            os.system("cls")
            print("Gracias por usar nuestro sistema")
            isActive = False
        else:
            os.system("cls")
            print("Opcion invalida")
    os.system("pause")
        