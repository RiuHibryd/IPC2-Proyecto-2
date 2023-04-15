import tkinter as tk
from TDA.Quimicos import Maquinas, load_xml_file, Compuestos, Quimicos, Lista, ElementoQuimico, Compuesto, Maquina
import TDA.Quimicos
from TDA.Quimicos import *
from graphviz import Digraph
import graphviz
import io
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tempfile
import time

#Codigo hecho por Riu
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.output_text = tk.Text(self, wrap=tk.WORD, width=10, height=10 )
        self.output_text.pack()

    # Funcion para crear lainterfaz grafica
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
        self.generate_output_button["command"] = lambda: self.generate_xml_output(self.compound, self.maquina, "output.xml")
        # Manejo de elementos quimicos frame
        self.chem_frame = tk.LabelFrame(self, text="Manejo de elementos quimicos")
        self.chem_frame.pack(side="left")

        # Mirar elementos quimicos 
        self.view_elements_button = tk.Button(self.chem_frame)
        self.view_elements_button["text"] = "Ver elementos quimicos por numero atomico"
        self.view_elements_button.pack(side="top")
        self.view_elements_button["command"] = lambda: (self.display_elements())
   
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
        self.analyze_compound_button["command"] = lambda: self.display_compound_analisys()

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
    
    def display_maquinas(self):  #Despliega las maquinas y sus elementos
        machines_window = tk.Toplevel(self.master)
        for machine in Maquinas:
            machine_frame = tk.Frame(machines_window)
            machine_frame.pack()
            name_label = tk.Label(machine_frame, text=machine.nombre)
            name_label.pack()
            for pin in machine.pines:
                if len(pin.elementos) == 0:
                    elements_label = tk.Label(machine_frame, text="No elements found.")
                else:
                    elements_label = tk.Label(machine_frame, text="Elementos: " + ", ".join([element.simbolo for element in pin.elementos])) #Despliega los elementos de la maquina
                elements_label.pack()
        machines_window.geometry("400x400")
    def display_compounds(self):    #Despliega los compuestos y sus elementos
        compounds_window = tk.Toplevel(self.master)
        for compound in Compuestos:
            compound_frame = tk.Frame(compounds_window)
            compound_frame.pack()
            name_label = tk.Label(compound_frame, text=compound.nombre)
            name_label.pack()
            elements_label = tk.Label(compound_frame, text="Elementos: " + ", ".join([element.simbolo for element in compound.elementos])) #Despliega los elementos de los compuestos
            elements_label.pack()
        compounds_window.geometry("400x400")
    def display_elements(self): #Despliega los elementos quimicos
        elementos_window = tk.Toplevel(self.master)
        columns = ('Numero atomico', 'Simbolo', 'Nombre')   #Columnas de la tabla
        tree = ttk.Treeview(elementos_window, columns=columns, show='headings')
        tree.heading('Nombre', text='Nombre')
        tree.heading('Simbolo', text='Simbolo')
        tree.heading('Numero atomico', text='Numero atomico')
        tree.pack()

        for element in Quimicos:  # Itera sobre los elementos quimicos
            tree.insert('', 'end', values=(element.numeroAtomico, element.simbolo, element.nombre))
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
            if chemical.numeroAtomico == atomic_number or chemical.simbolo == atomic_symbol or chemical.nombre == chemical_name:
                messagebox.showerror("Error", "El elemento químico ya existe")
                return

        new_chemical = ElementoQuimico(atomic_number, atomic_symbol, chemical_name)
        Quimicos.insert(new_chemical)
    
    def display_compound_analisys(self):
        display_compound_analisys_window = tk.Toplevel(self.master)
        #Crear campos
        compound_name_label = tk.Label(display_compound_analisys_window, text="Nombre del compuesto")
        compound_name_label.grid(row=0, column=0)
        compound_name_entry = tk.Entry(display_compound_analisys_window)
        compound_name_entry.grid(row=0, column=1)
        #Agregar elemento a la base de datos
        add_compound_button = tk.Button(display_compound_analisys_window, text="Analizar compuesto", command=lambda: self.analyze_compound(compound_name_entry.get()))
        add_compound_button.grid(row=4, column=0, columnspan=2)
    def analyze_compound(self, compound_name):
        found = False
        for compound in Compuestos:
            if compound.nombre == compound_name:
                found = True
                analyze_compound_window = tk.Toplevel(self.master)
                compound_frame = tk.Frame(analyze_compound_window)
                compound_frame.pack()
                name_label = tk.Label(compound_frame, text=compound.nombre)
                name_label.pack()
                elements_label = tk.Label(compound_frame, text="Elementos: " + ", ".join([element.simbolo for element in compound.elementos]))
                elements_label.pack()
                for machine in Maquinas:
                    name_label = tk.Label(compound_frame, text=machine.nombre)
                    name_label.pack()
                    for pin in machine.pines:
                        elements_label = tk.Label(compound_frame, text="Elementos: " + ", ".join([element.simbolo for element in pin.elementos]))
                        elements_label.pack()
                    add_analisys_button = tk.Button(analyze_compound_window, text="Analizar Maquina", command=lambda machine=machine: self.add_analisys(compound, machine))
                    add_analisys_button.pack()
                    break
        if not found:
            messagebox.showerror("Error", "El compuesto no existe")
    def add_analisys(self, compound, maquina):
        images = self.display_animated_process(compound)

        # Create a new window to display the image
        image_window = tk.Toplevel(self.master)
        # Create a label to display the image
        image_label = tk.Label(image_window)
        image_label.pack()

        for image in images:
            photo = ImageTk.PhotoImage(image)
            image_label.image = photo  # Save a reference to the image
            image_label.configure(image=photo)
            image_label.update()
            time.sleep(1)

        elements_str = ", ".join([element.simbolo for element in compound.elementos])
        self.output_text.insert(tk.END, f"{compound.nombre}: {elements_str}\n")
        self.output_text.see(tk.END)
        self.compound = compound
        output_file = "output.xml"
        self.generate_xml_output(compound, maquina, output_file)
      
        self.generate_xml_output(compound, maquina, output_file)
    def visualize_process(self, compound, current_pin_index, current_element_index):
        g = Digraph('G', filename='process.gv', format='png')
        g.attr(rankdir='LR', size='8,5')

        for machine_index, machine in enumerate(Maquinas):
            # Crear una tabla para mostrar los pines de la maquina
            table = '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                        <TR><TD COLSPAN="2" BGCOLOR="lightblue">''' + machine.nombre + '''</TD></TR>'''

            for pin_index, pin in enumerate(machine.pines):
                elements_str = ""
                for element_index, element in enumerate(pin.elementos):
                    color = ""
                    if machine_index == 0 and pin_index == current_pin_index and element_index == current_element_index:
                        color = ' COLOR="blue"'
                        if element in compound.elementos:  #Si el elemento esta en el compuesto
                            color = ' COLOR="green"' #Como podria dejarlo estatico
                    elements_str += '<FONT' + color + '>' + element.simbolo + '</FONT>, '
                elements_str = elements_str.rstrip(', ')

                table += '''<TR><TD BGCOLOR="lightblue">Pin ''' + str(pin.numeroPines) + '''</TD><TD>''' + elements_str + '''</TD></TR>'''

            table += "</TABLE>>"

            g.node(machine.nombre, label=table, shape='plaintext')

        return g.pipe(format='png')

    def display_animated_process(self, compound):
            images = Lista()
            machine = Maquinas.head.data
            delay = 1  # Ajustar el tiempo de espera entre cada imagen
            for pin_index, pin in enumerate(machine.pines):
                for element_index, _ in enumerate(pin.elementos):
                    image_data = self.visualize_process(compound, pin_index, element_index)
                    image = Image.open(io.BytesIO(image_data))
                    images.insert(image)
                    time.sleep(delay)

            return images

 #---------------------XML---------------------
    def generate_xml_output(self, compuesto, maquina, output_file):
        root = ET.Element("RESPUESTA")
        lista_compuestos = ET.SubElement(root, "listaCompuestos")
        compuesto_element = ET.SubElement(lista_compuestos, "compuesto")

        nombre_element = ET.SubElement(compuesto_element, "nombre")
        nombre_element.text = compuesto.nombre

        maquina_element = ET.SubElement(compuesto_element, "maquina")
        maquina_element.text = maquina.nombre

        tiempo_optimo_element = ET.SubElement(compuesto_element, "tiempoOptimo")
        tiempo_optimo_element.text = str(compuesto.tiempo_optimo)

        instrucciones_element = ET.SubElement(compuesto_element, "instrucciones")

        instructions = Lista()  

        index = 0
        for instruction in instructions:
            tiempo_element = ET.SubElement(instrucciones_element, "tiempo")
            numero_segundo_element = ET.SubElement(tiempo_element, "numeroSegundo")
            numero_segundo_element.text = str(index)
            index += 1

            acciones_element = ET.SubElement(tiempo_element, "acciones")

            for action in instruction.elementos:
                accion_pin_element = ET.SubElement(acciones_element, "accionPin")
                numero_pin_element = ET.SubElement(accion_pin_element, "numeroPin")
                numero_pin_element.text = str(action.numeroPines)
                accion_element = ET.SubElement(accion_pin_element, "accion")
                accion_element.text = action.accion

        # Salida
        tree = ET.ElementTree(root)
        tree.write(output_file, encoding='utf-8', xml_declaration=True)
root = tk.Tk()
app = Application(master=root)
app.mainloop()