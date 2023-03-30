import tkinter as tk

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

        # Ayuda
        self.help_button = tk.Button(self)
        self.help_button["text"] = "Ayudame"
        self.help_button.pack(side="bottom")

root = tk.Tk()
app = Application(master=root)
app.mainloop()