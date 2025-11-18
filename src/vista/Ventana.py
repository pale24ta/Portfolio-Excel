from tkinter import Tk,Frame,StringVar
from tkinter import Checkbutton,Label,messagebox,filedialog,Entry,Button,Event
import enum


# clase para el frame de seleccion
class Seleccion(Frame):
    def __init__(self,root,texto,lista_selecciones):
        super().__init__(root)
        Label(root,text = texto).pack()
        for option in lista_selecciones:
            Checkbutton(self,text=option).pack()
        self.pack()

# Clase para escribir la direccion del archivo deseado
class Directorio(Frame):
    def __init__(self,root,texto,tipo_entrada):
        super().__init__(root)  # instancia de la clase frame
        Label(root,text=texto).pack() # el nombre del objeto

        self.directorio = StringVar()
        # La barra de texto para cargar la informacion
        self.barra = Entry(self,textvariable=self.directorio,width=80).pack()
        
        def accion_boton():
            if tipo_entrada:
                direccion = filedialog.askopenfile(title='archivo.dat')
            else:
                direccion = filedialog.askdirectory(title='Donde desea guardarlo')
            if direccion:
                if type(direccion) == str: self.directorio.set(direccion)
                else: self.directorio(direccion.name)

                if tipo_entrada:
                    direccion.close()

        # boton para navegar por la computadora
        self.botton_search = Button(self,text='...',command=accion_boton).pack()
        self.pack()
    
    
# clase de la ventana principial

class Ventana(Tk):
    def __init__(self,title,heigh = None, weigh = None,reazible = True):
        super().__init__()
        self.title(title)
        self.config(height=heigh,weigh = weigh)
        self.config(background="#28C522")
        Directorio(self,'Buscar archivo.dat',True)

        options = ['Agregar numero','Eliminar numero']
        Seleccion(self,'Opciones',options)

        Directorio(self,'Salida',False)
    
        self.mainloop()
    