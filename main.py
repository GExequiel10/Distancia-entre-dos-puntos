print ('Calcula la distancia entre dos puntos')
import math


def calculate_distence ():
  x1 = int(input('Ingrese X1:'))
  y1 = int(input('Ingrese Y1:'))
  x2 = int(input('Ingrese X2:'))
  y2 = int(input('Ingrese Y2:'))

  lista_1 = [x1,y1]
  lista_2 = [x2,y2]
  points_1 = tuple(lista_1)
  points_2 = tuple(lista_2)

  distance = math.sqrt(((points_2[0])-(points_1[0]))**2+((points_2[1])-(points_1[1]))**2)
  return print(distance)

calculate_distence()
