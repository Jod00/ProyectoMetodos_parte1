#PROYECTO Metodos Convertir numeros decimales a binarios, Octal y Hexadecimal
from Tkinter import *
from numpy import *

ventana=Tk()
ventana.geometry("450x400") 
ventana.title("Proyecto_Parte1")

etiqueta= Label(ventana,text="Ingrese un numero Entero:",font="Arial 13")
etiqueta.grid(column=1,row=0)

entrada= Entry(ventana, font="Arial 12")
entrada.grid(column=1,row=2)

#convierte numeros decimales a binarios
def binario():
    numero= entrada.get()
    nu= int(numero)
    ordenbin = zeros(10)
    cont=9
    
    while nu >= 1 :
        ordenbin[cont]= nu%2
        cont=cont-1
        nu=nu/2

    et2= Label(ventana, text=str(ordenbin))
    et2.grid(column=0,row=6)

#convierte numeros decimales a octal


#convierte numeros decimales a hexadecimal


et3= Label(ventana,text="Convertir a:",font="Arial 13")
et3.grid(column=1,row=3)

boton1= Button(ventana,text="Binario",fg="Blue", command=binario)
boton1.grid(column=0,row=4)

boton2= Button(ventana,text="octal",fg="Blue", command=binario) #cambiar
boton2.grid(column=1,row=4)

boton3= Button(ventana,text="hexadecimal",fg="Blue", command=binario) #cambiar
boton3.grid(column=2,row=4)

ventana.mainloop()