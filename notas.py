"""
PROGRAMA PARA CALCULAR LAS NOTAS DE N ESTUDIANTES..
"""
import os
alumnos =[]
isActive = True
menu = "1. Registrar Alumno\n2. Registrar Notas\n3. Buscar estudiante\n4. Ver definitivas del curso\n5. Salir\n:)"
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
                codigo = input("Ingrese el Codigo del Estudiante : ")
                nombre = input("Ingrese el Nombre del Estudiante : ")
                edad = int(input(f"Ingrese la edad del Estudiante :  {nombre}"))
                alumno = [codigo,nombre,edad,[],[],[]]
                alumnos.append(alumno)
                os.system("pause")
                rta = input("Desea registrar otro Alumno S(si) o N(No)").upper()
        elif (opMenu == 2):
            if (len(alumnos)>0):
                opNotas = 0
                isActiveGrades = True
                while (isActiveGrades):
                    os.system("cls")
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
                            isAddGrades = True
                            while isAddGrades:
                                codigo = input("Ingrese el codigo del Estudiante: ")
                                for item in alumnos:
                                    if codigo in item:
                                        indice=alumnos.index(item)
                                while (rta in ["S","s"]):
                                    nota=float(input("Ingrese la nota del parcial: "))
                                    alumnos[indice][3].append(nota)
                                    print(alumnos)
                                    os.system("pause")
                                    rta = input("Desea registrar otro parcial S(si) o N(No)").upper()
                                if bool(input("Desea registrar otro estudiante S(si) o Enter(No)")):
                                    rta = "S"
                                    isAddGrades = True
                                else:
                                    isAddGrades = False                           
                        elif (opNotas == 2):
                            rta = "S"
                            isAddGrades = True
                            while isAddGrades:
                                codigo = input("Ingrese el codigo del Estudiante: ")
                                for item in alumnos:
                                    if codigo in item:
                                        indice=alumnos.index(item)
                                while (rta in ["S","s"]):
                                    nota=float(input("Ingrese la nota del Quiz: "))
                                    alumnos[indice][4].append(nota)
                                    print(alumnos)
                                    os.system("pause")
                                    rta = input("Desea registrar otro Quiz S(si) o N(No)").upper()
                                if bool(input("Desea registrar otro estudiante S(si) o Enter(No)")):
                                    rta = "S"
                                    isAddGrades = True
                                else:
                                    isAddGrades = False                           
                        elif (opNotas == 3):
                            rta = "S"
                            isAddGrades = True
                            while isAddGrades:
                                codigo = input("Ingrese el codigo del Estudiante: ")
                                for item in alumnos:
                                    if codigo in item:
                                        indice=alumnos.index(item)
                                while (rta in ["S","s"]):
                                    nota=float(input("Ingrese la nota del Trabajo: "))
                                    alumnos[indice][5].append(nota)
                                    print(alumnos)
                                    os.system("pause")
                                    rta = input("Desea registrar otro Trabajo S(si) o N(No)").upper()
                                if bool(input("Desea registrar otro estudiante S(si) o Enter(No)")):
                                    rta = "S"
                                    isAddGrades = True
                                else:
                                    isAddGrades = False                           
                        elif (opNotas == 4):
                            isActiveGrades = False
                        else:
                            pass
            opNotas = 0
            isActiveGrades = True
            if len(alumnos)==0:
                isActiveGrades=False
                print("No se cuenta con registros de estudiantes, por favor registre un estudiante para poder ingresar las notas")
                os.system("pause")
            else:
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
            definitiva=[[],[]]
            print("Las definitivas del curso son las siguientes: ")
            print(f"Nombre\t\tDefinitiva")
            for i in range(len(alumnos)):
                nomTemp=alumnos[i][1]
                notaParc=0
                notaQuiz=0
                notaTrab=0
                for j in range(len(alumnos[i][3])):
                    notaParc=notaParc+alumnos[i][3][j]
                notaParc=(notaParc/len(alumnos[i][3]))*0.6
                for j in range(len(alumnos[i][4])):
                    notaQuiz=notaQuiz+alumnos[i][4][j]
                notaQuiz=(notaQuiz/len(alumnos[i][4]))*0.25              
                for j in range(len(alumnos[i][5])):
                    notaTrab=notaTrab+alumnos[i][5][j]
                notaTrab=(notaTrab/len(alumnos[i][5]))*0.15              
                notaDef=round(notaParc+notaQuiz+notaTrab,2)
                definitiva[0].append(nomTemp)
                definitiva[1].append(notaDef)
            for i in range(len(alumnos)):            
                print(f"{definitiva[0][i]}\t\t{definitiva[1][i]}")
        elif (opMenu == 5):
            os.system("cls")
            print("Gracias por usar nuestro sistema")
            isActive = False
        else:
            os.system("cls")
            print("Opcion invalida")
    os.system("pause")
        