import random

def mostrar_matriz(estudiantes,materias,matriz):
    
    for i in range(len(materias)):
        print(f"{materias[i]:<15} ",end="")
        
    print()
    print("-"*90)
        
    for j in range(len(estudiantes)):
        print(f"{estudiantes[j]}",end=" ")
        for h in range(len(materias)-1):
            print(f"{matriz[j][h]:^15}",end=" ")
        print()
        
def calcular_promedio_estudiantes(estudiantes,materias,matriz):
    
    for i in range(len(estudiantes)):
        sum_notas=0
        prom=0
        for j in range(len(materias)-1):
            sum_notas+=matriz[i][j]
        prom=sum_notas/(len(materias)-1)
        print(f"El promedio del Estudiante {i+1} es: {prom}")    
        
def calcular_promedio_materias(estudiantes,materias,matriz):
    
    for i in range(len(materias)-1):
        sum_notas=0
        prom=0
        for j in range(len(estudiantes)):
            sum_notas+=matriz[j][i]
        prom=sum_notas/(len(estudiantes))
        print(f"El promedio de la Materia {i+1} es : {prom}")

estudiantes=["Estudiante1","Estudiante2","Estudiante3","Estudiante4","Estudiante5"] #Filas
materias=["Estudiantes","Materia1","Materia2","Materia3","Materia4","Materia5"] #Columnas
matriz=[]

for i in range(len(estudiantes)):
    matriz.append([])
    for j in range(len(materias)-1):
        matriz[i].append(random.randint(1,10))
        
mostrar_matriz(estudiantes,materias,matriz)
print()
calcular_promedio_estudiantes(estudiantes,materias,matriz)
print()
calcular_promedio_materias(estudiantes,materias,matriz)