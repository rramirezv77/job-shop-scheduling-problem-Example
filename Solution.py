#existen 30 trabajos, del 0 al 29
#existen 3 máquinas del 0 a al 2

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
#aqui debe encontrar una solucion inicial factible

##################################################

#aqui debe desarrollar la mejora de la solucion
#la cantidad de réplicas debe elegirlas usted
replicas=1
for _ in range(replicas):
  pass

##############################################
#aqui debe mostrar la mejor solucion encontrada y su valor

#este es un ejemplo de cómo usar la funcion que calcula el tiempo.
#En este caso calculamos cuánti tiempo demorará la maquina 2 en hacer
#los trabajos 5,2,3,6,0,9,4
#siempre debe ir el parámetro Tiempo. La lista "a" corresponde a al vector de trabajos
#y el numero 2 indica que es la maquina 2 que estamos evaluando
a=[5,2,3,6,0,9,4]
print(calcular_tiempo_maquina(a,2,Tiempos))
