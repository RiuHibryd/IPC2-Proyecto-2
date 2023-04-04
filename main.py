import tkinter as tk
from TDA.Quimicos import Maquinas, load_xml_file
from graphviz import Digraph
import graphviz
import io
from PIL import ImageTk, Image
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
        self.view_machines_button["command"] = lambda: self.display_maquinas(Maquinas)


        # Ayuda
        self.help_button = tk.Button(self)
        self.help_button["text"] = "Ayudame"
        self.help_button.pack(side="bottom")
    def display_maquinas(self, maquinas):
        # Create a new window
        self.maquinas_root = tk.Toplevel(self.master)
        self.maquinas_root.title("Máquinas")

        # Create a string in the graphviz language that describes the graph
        graphviz_string = "digraph G {\n"
        graphviz_string += "\trankdir=LR;\n"
        for i, maquina in enumerate(maquinas):
            graphviz_string += "\tM{} [shape=box, style=filled, color=lightgrey, label=<".format(i)
            graphviz_string += "<table border='0' cellspacing='0'>"
            graphviz_string += "<tr><td colspan='{}' bgcolor='black'></td></tr>".format(len(maquina['Elementos']) + 1)
            graphviz_string += "<tr><td colspan='{}' bgcolor='grey' align='center'><font color='white'>{}</font></td></tr>".format(len(maquina['Elementos']) + 1, maquina['Nombre'])
            for elemento in maquina['Elementos']:
                graphviz_string += "<tr><td bgcolor='white' align='left'>{}</td>".format(elemento.data['Nombre'])
                graphviz_string += "<td bgcolor='white' align='right'>{}</td></tr>".format(elemento['Cantidad'])
            graphviz_string += "</table>>];\n"
            if i > 0:
                graphviz_string += f"\tM{i-1} -> M{i};\n"
        graphviz_string += "}"

        # Use the Graphviz module to display the graph directly in the popup window
        graph = graphviz.Source(graphviz_string)
        graph.format = "png"

        # Convert the graph image to a Tkinter PhotoImage object
        img = Image.open(io.BytesIO(graph.pipe())).convert('RGBA')
        photo = ImageTk.PhotoImage(img)

        # Create a label to display the graph image
        self.graph_label = tk.Label(self.maquinas_root, image=photo, bg="white")
        self.graph_label.image = photo
        self.graph_label.pack()

        # Add a scrollbar for horizontal scrolling
        scrollbar = tk.Scrollbar(self.maquinas_root, orient="horizontal", command=self.graph_label.xview)
        scrollbar.pack(side="bottom", fill="x")
        self.graph_label.configure(xscrollcommand=scrollbar.set)
root = tk.Tk()
app = Application(master=root)
app.mainloop()