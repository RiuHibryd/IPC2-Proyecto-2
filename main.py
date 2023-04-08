import tkinter as tk
from TDA.Quimicos import Maquinas, load_xml_file, Compuestos, Quimicos
from graphviz import Digraph
import graphviz
import io
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox


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
        self.view_elements_button["command"] = lambda: (Quimicos.bubble_sorting ,self.display_elements())
   
        # Agregar elemento quimico
        self.add_element_button = tk.Button(self.chem_frame)
        self.add_element_button["text"] = "Agregar elemento quimico"
        self.add_element_button.pack(side="top")
        self.add_element_button["command"] = lambda: self.add_Chemical()
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
    def display_elements(self):
        
        elementos_window = tk.Toplevel(self.master)
        columns = ('Numero atomico', 'Simbolo', 'Nombre')
        tree = ttk.Treeview(elementos_window, columns=columns, show='headings')
        tree.heading('Nombre', text='Nombre')
        tree.heading('Simbolo', text='Simbolo')
        tree.heading('Numero atomico', text='Numero atomico')
        tree.pack()
        #Insertar elementos

        for element in Quimicos:
            tree.insert('', 'end', values=(element["NumeroAtomico"], element["Simbolo"], element["Nombre"]))
        elementos_window.geometry("610x280")
    def add_Chemical(self):
        add_chemical_window = tk.Toplevel(self.master)
        #Crear campos
        atomic_number_label = tk.Label(add_chemical_window, text="Numero atomico")
        atomic_number_label.grid(row=0, column=0)
        atomic_number_entry = tk.Entry(add_chemical_window)
        atomic_number_entry.grid(row=0, column=1)

        atomic_symbol_label = tk.Label(add_chemical_window, text="Simbolo")
        atomic_symbol_label.grid(row=1, column=0)
        atomic_symbol_entry = tk.Entry(add_chemical_window)
        atomic_symbol_entry.grid(row=1, column=1)

        chemical_name_label = tk.Label(add_chemical_window, text="Nombre")
        chemical_name_label.grid(row=2, column=0)
        chemical_name_entry = tk.Entry(add_chemical_window)
        chemical_name_entry.grid(row=2, column=1)

        #Crear boton

        add_chemical_button = tk.Button(add_chemical_window, text="Agregar elemento quimico", command=lambda: self.add_chemical(atomic_number_entry.get(), atomic_symbol_entry.get(), chemical_name_entry.get()))
        add_chemical_button.grid(row=4, column=0, columnspan=2)
    def add_chemical(self, atomic_number, atomic_symbol, chemical_name):
        
        for chemical in Quimicos:
            if chemical["NumeroAtomico"] == atomic_number or chemical["Simbolo"] == atomic_symbol or chemical["Nombre"] == chemical_name:
                messagebox.showerror("Error", "El elemento quimico ya existe")
                return
        
        #Agregar elemento a la lista
        Quimicos.insert({
            "NumeroAtomico": atomic_number,
            "Simbolo": atomic_symbol,
            "Nombre": chemical_name
        })
       
        #Agregar elemento a la base de datos
    
root = tk.Tk()
app = Application(master=root)
app.mainloop()