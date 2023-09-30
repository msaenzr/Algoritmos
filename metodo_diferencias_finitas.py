#Librerias importadas
import matplotlib.pyplot as plt
import numpy as np

#Dimensiones de la grafica
l_x = 10
l_y = 10

#Condiciones de frontera
b = 5
y_0 = 0
x_0 = x_1 = 0


#Creación de grilla
g = 0.1*100
x, y = np.meshgrid(np.linspace(0,g,l_x),np.linspace(0,g,l_y))


#Se fija el valor de interes en todas las celdas
V = np.empty((l_x,l_y))
V.fill(0)

#Evaluacion de condiciones de frontera
V[(l_y-1):, :] = b
V[:1, :]=y_0
V[:, (l_x-1):]=x_1
V[:, :1]=x_0

#Cálculo de potencial
for n in range(1000):
    for i in range(1,l_x-1):
        for j in range(1,l_y-1):
            V[i,j]= (1/4)*(V[i+1][j]+ V[i][j+1]+ V[i-1][j]+ V[i][j-1])

#Configuración de gráfica
plt.contourf(x,y,V,50,cmap='plasma')
plt.colorbar()
plt.title("V(x,y) (Volts)",fontname="cambria",size =16)
plt.xlabel("X(cm)",fontname="cambria",size =12)
plt.ylabel("Y(cm)",fontname="cambria",size =12)
plt.show()