import random
import matplotlib.pyplot as plt
#existen 30 trabajos, del 0 al 29
#existen 3 máquinas del 0 a al 2
#la matriz Tiempos tiene los tiempos que demora cada máquina en hacer cada trabajo
#Tiempos[maquina][trabajo] = tiempo que demora la maquina en hacer el trabajo
#por ejemplo, Tiempos[0][5] = 0.13 significa que la máquina 0 demora 0.13 en hacer el trabajo 5
#la matriz Tiempos es la siguiente:
Tiempos = [
    [4.52, 5.13, 6.29, 2.31, 1.89, 3.77, 5.60, 2.99, 4.45, 3.87,
     2.48, 5.32, 6.08, 4.01, 3.21, 7.25, 6.66, 5.97, 3.42, 2.73,
     4.88, 6.41, 3.96, 5.17, 4.60, 3.84, 4.72, 5.06, 3.59, 2.17],

    [0.13, 0.23, 0.67, 1.42, 15.81, 0.88, 2.30, 3.10, 1.14, 0.73,
     1.99, 0.56, 2.52, 1.60, 0.49, 1.31, 0.20, 2.71, 0.35, 0.92,
     1.44, 2.99, 0.08, 1.76, 0.38, 2.25, 1.22, 9.61, 0.17, 1.55],

    [0.32, 0.15, 3.42, 0.64, 0.88, 0.49, 0.28, 0.91, 7.35, 0.73,
     0.25, 0.56, 8.79, 0.61, 0.13, 0.96, 0.47, 0.38, 0.53, 0.84,
     0.33, 0.59, 22.45, 0.67, 4.12, 0.77, 0.92, 0.36, 0.68, 0.58]
]

#la funcion recibirá el nombre de una de las listas que tienen los trabajos 
#, la maquina (0,1,2) y la matriz de tiempos (esta siempre es "Tiempos") 
#La funcion devolverá un valor, que corresponde al tiempo que demora tal maquina
#en terminar todos sus trabajos asignados
def calcular_tiempo_maquina(lista,maquina,t):
  total = 0.0
  for costo in lista:
    total = total + t[maquina][costo]
  return total

maquina1=[]
maquina2=[]
maquina3=[]

SolucionAceptada = 10000
historial = []  # Para guardar la evolución
iteraciones = []    # Para guardar en qué iteración mejoró
#aqui debe encontrar una solucion inicial factible

##################################################

#aqui debe desarrollar la mejora de la solucion
#la cantidad de réplicas debe elegirlas usted

replicas = 1000
for i in range(replicas):
   maquina1_auxiliar = []
   maquina2_auxiliar = []
   maquina3_auxiliar = []
   #aqui debe generar una solucion aleatoria factible
   for j in range(30):
       trabajo = random.randint(0, 29)
       if j % 3 == 0:
           maquina1_auxiliar.append(trabajo)
       elif j % 3 == 1:
           maquina2_auxiliar.append(trabajo)
       else:
           maquina3_auxiliar.append(trabajo)
   #aqui debe calcular el tiempo de cada maquina
   tiempo_maquina1 = calcular_tiempo_maquina(maquina1_auxiliar, 0, Tiempos)
   tiempo_maquina2 = calcular_tiempo_maquina(maquina2_auxiliar, 1, Tiempos)
   tiempo_maquina3 = calcular_tiempo_maquina(maquina3_auxiliar, 2, Tiempos)
   #aqui debe calcular el tiempo total de la solucion
   tiempo_total = max(tiempo_maquina1, tiempo_maquina2, tiempo_maquina3)
   #aqui debe guardar la mejor solucion encontrada
   # y su valor     
   # si la solucion es mejor que la mejor aceptada, se guarda
   if tiempo_total < SolucionAceptada:
       SolucionAceptada = tiempo_total
       maquina1 = maquina1_auxiliar
       maquina2 = maquina2_auxiliar
       maquina3 = maquina3_auxiliar
       historial.append(SolucionAceptada)
       iteraciones.append(i)
   pass        

##############################################
#aqui debe mostrar la mejor solucion encontrada y su valor

print("Mejor solución encontrada:")
print("Máquina 1:", maquina1)
print("Máquina 2:", maquina2)
print("Máquina 3:", maquina3)
print("Tiempo total:", SolucionAceptada)
print("Historial de soluciones:", historial)

##############################################

# Crear gráfica de evolución
if historial:  # Solo si hubo mejoras
    plt.figure(figsize=(12, 6))
    plt.plot(iteraciones, historial, 'b-o', linewidth=2, markersize=4)
    plt.title('Evolución de la Mejor Solución', fontsize=14, fontweight='bold')
    plt.xlabel('Iteración', fontsize=12)
    plt.ylabel('Makespan (minutos)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.yscale('log')  # Escala logarítmica para mejor visualización
    
    # Anotar la mejor solución
    plt.annotate(f'Mejor: {round(SolucionAceptada, 2)} min', 
                xy=(iteraciones[-1], historial[-1]), 
                xytext=(10, 10), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    
    plt.tight_layout()
    plt.show()
else:
    print("No se encontraron mejoras durante la búsqueda")