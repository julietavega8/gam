from tkinter import *
 
 
 
 
 
ventana=Tk()
ventana.title("CALCULADORA")
ventana.geometry("392x600")
ventana.config(bg="black")
color_boton=("gray77")
 
ancho_boton=11
alto_boton=3
 
 
 
Salida=Entry(ventana,font=('arial',20,'bold'),width=22,bd=20,insertwidth=4,bg="light grey",justify="right")
Salida.place(x=10,y=60)
 
 
Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton).place(x=17,y=180)
Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton).place(x=107,y=180)
Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton).place(x=197,y=180)
Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton).place(x=287,y=180)
Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton).place(x=17,y=240)
Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton).place(x=107,y=240)
Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton).place(x=197,y=240)
Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton).place(x=287,y=240)
Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton).place(x=17,y=300)
Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton).place(x=107,y=300)
Button(ventana,text=".",bg=color_boton,width=ancho_boton,height=alto_boton).place(x=197,y=300)
Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton).place(x=287,y=300)
Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton).place(x=17,y=360)
Button(ventana,text="*",bg=color_boton,width=ancho_boton,height=alto_boton).place(x=107,y=360)
Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton).place(x=197,y=360)
Button(ventana,text="C",bg=color_boton,width=ancho_boton,height=alto_boton).place(x=17,y=420)
Button(ventana,text="=",bg=color_boton,width=ancho_boton,height=alto_boton).place(x=287,y=360)
 
 
 
ventana.mainloop()

