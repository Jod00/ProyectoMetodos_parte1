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
    et2= Label(ventana, text="")
    try: 
        numero= entrada.get()
        nu= int(numero)
        #obtiene el tamanno que debe tener el arreglo
        tamano=0
        while nu>=1:
            tamano=tamano+1
            nu=nu/2
        
        nu=int(numero)
        ordenbin = zeros(tamano)
        cont=tamano-1
        
        while nu >= 1 :
            ordenbin[cont]= nu%2
            cont=cont-1
            nu=nu/2

        et2= Label(ventana, text=str(ordenbin))
        et2.grid(column=0,row=6)
    except:
        et2= Label(ventana, text="Solo es permitido numeros Enteros")
        et2.grid(column=1,row=8)

#convierte numeros decimales a octal
def octal():
    try:
        cadenaordenada=""
        numero= entrada.get()
        n = int(numero)
        ordenoctal = []
        while n>=1:
            ordenoctal.append(str(n%8))
            n= n/8
        
        cadenaordenada="".join(ordenoctal[::-1])

        et3=Label(ventana, text=cadenaordenada,font="Arial 10" )
        et3.grid(column=1,row=6)
    except:
        et3= Label(ventana, text="Solo es permitido numeros Enteros")
        et3.grid(column=1,row=8)


#convierte numeros decimales a hexadecimal
def hexadecimal():
        print("f")


etiq= Label(ventana,text="Convertir a:",font="Arial 13")
etiq.grid(column=1,row=3)

boton1= Button(ventana,text="Binario",fg="Blue", command=binario)
boton1.grid(column=0,row=4)

boton2= Button(ventana,text="octal",fg="Blue", command=octal) #cambiar
boton2.grid(column=1,row=4)

boton3= Button(ventana,text="hexadecimal",fg="Blue", command=hexadecimal) #cambiar
boton3.grid(column=2,row=4)

ventana.mainloop()