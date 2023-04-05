import tkinter as tk
from TDA.Quimicos import Maquinas, load_xml_file, Compuestos, Quimicos
from graphviz import Digraph
import graphviz
import io
import tkinter.ttk as ttk
from tkinter import *


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()



    def create_widgets(self):
        # Boton de inicializacion
        self.init_button = tk.Button(self)
        self.init_button["text"] = "Inicializar"
        self.init_button.pack(side="top")

        # Boton de carga de archivo de entrada
        self.load_input_button = tk.Button(self)
        self.load_input_button["text"] = "Cargar archivo de entrada"
        self.load_input_button.pack(side="top")
        self.load_input_button["command"] = load_xml_file 
        
        # Generar archivo de salida
        self.generate_output_button = tk.Button(self)
        self.generate_output_button["text"] = "Generar archivo de salida"
        self.generate_output_button.pack(side="top")

        # Manejo de elementos quimicos frame
        self.chem_frame = tk.LabelFrame(self, text="Manejo de elementos quimicos")
        self.chem_frame.pack(side="left")

        # Mirar elementos quimicos 
        self.view_elements_button = tk.Button(self.chem_frame)
        self.view_elements_button["text"] = "Ver elementos quimicos por numero atomico"
        self.view_elements_button.pack(side="top")
   
        # Agregar elemento quimico
        self.add_element_button = tk.Button(self.chem_frame)
        self.add_element_button["text"] = "Agregar elemento quimico"
        self.add_element_button.pack(side="top")
        # Manejo de compuestos frame
        self.comp_frame = tk.LabelFrame(self, text="Manejo de compuestos")
        self.comp_frame.pack(side="left")

        # Ver compuestos y sus formulas
        self.view_compounds_button = tk.Button(self.comp_frame)
        self.view_compounds_button["text"] = "Compuestos y sus formulas"
        self.view_compounds_button.pack(side="top")
        self.view_compounds_button["command"] = lambda: self.display_compounds()
        # Analizar compuesto
        self.analyze_compound_button = tk.Button(self.comp_frame)
        self.analyze_compound_button["text"] = "Analizar compuesto"
        self.analyze_compound_button.pack(side="top")

        # Manejo de maquinas frame
        self.mach_frame = tk.LabelFrame(self, text="Manejo de maquinas")
        self.mach_frame.pack(side="left")

        # Ver maquinas
        self.view_machines_button = tk.Button(self.mach_frame)
        self.view_machines_button["text"] = "Ver maquinas"
        self.view_machines_button.pack(side="top")
        self.view_machines_button["command"] = lambda: self.display_maquinas()


        # Ayuda
        self.help_button = tk.Button(self)
        self.help_button["text"] = "Ayudame"
        self.help_button.pack(side="bottom")
    def display_maquinas(self):
        # crear una nueva ventana
        machines_window = tk.Toplevel(self.master)
        for machine in Maquinas:
            machine_frame = tk.Frame(machines_window)
            machine_frame.pack()
            # desplegar el nombre de la maquina
            name_label = tk.Label(machine_frame, text=machine["Nombre"])
            name_label.pack()
            # desplegar la formula de la maquina
            elements_label = tk.Label(machine_frame, text="Elementos: " + ", ".join(machine["Elementos"]))
            elements_label.pack()
       
    def display_compounds(self):
        # crear una nueva ventana
        compounds_window = tk.Toplevel(self.master)

        # loop entre los compuestos y mostrarlos en la ventana
        for compound in Compuestos:
            compound_frame = tk.Frame(compounds_window)
            compound_frame.pack()

            # desplegar el nombre del compuesto
            name_label = tk.Label(compound_frame, text=compound["Nombre"])
            name_label.pack()

            # desplegar la formula del compuesto
            elements_label = tk.Label(compound_frame, text="Elementos: " + ", ".join(compound["Elementos"]))
            elements_label.pack()

        # poner el tamaño de la ventana
        compounds_window.geometry("400x400")

root = tk.Tk()
app = Application(master=root)
app.mainloop()