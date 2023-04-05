import xml.etree.ElementTree as ET
from tkinter import filedialog

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None
class Lista:
    def __init__(self):
        self.head = None
#-------------------------------------------------------

    def insert(self, data):
        new_node = Nodo(data)

        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
#-------------------------------------------------------
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next
#-------------------------------------------------------
    def bubble_sorting(self):
        if self.head is None or self.head.next  is None:
            return
        bubble_list = False
        while not bubble_list:
            bubble_list = True
            current_node = self.head
            while current_node.next is not None:
                if current_node.data["numeroAtomico"] > current_node.next.data["numeroAtomico"]:
                    bubble_list = False
                    current_node.data, current_node.next.data = current_node.next.data, current_node.data
                current_node = current_node.next        
#-------------------------------------------------------

Quimicos = Lista()
Compuestos = Lista()
Maquinas = Lista()
def load_xml_file():
    try:
        # Obteniendo el archivo XML
        filename = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])
        
        # Parseando el XML
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Procesando la data del XML
        for element in root.findall("listaElementos/elemento"):
            numeroAtomico = element.find("numeroAtomico").text
            simbolo = element.find("simbolo").text
            nombre = element.find("nombreElemento").text
            if nombre not in [q["Nombre"] for q in Quimicos]and simbolo not in [q["Simbolo"] for q in Quimicos] and numeroAtomico not in [q["NumeroAtomico"] for q in Quimicos]:   
             Quimicos.insert({"NumeroAtomico": numeroAtomico, "Simbolo": simbolo, "Nombre": nombre})

        for maquina in root.findall("listaMaquinas/Maquina"):
            nombre = maquina.find("nombre").text
            numeroPines = maquina.find("numeroPines").text
            numeroElementos = maquina.find("numeroElementos").text
            elementos = [e.text for pin in maquina.findall("pin") for e in pin.find("elementos").findall("elemento")]
            num_pines = len(maquina.findall("pin"))
            if nombre not in [m["Nombre"] for m in Maquinas]:
                Maquinas.insert({"Nombre": nombre, "NumeroPines": numeroPines, "NumeroElementos": numeroElementos, "Elementos": elementos, "Numero pines": num_pines})

        for compuesto in root.findall("listaCompuestos/compuesto"):
           nombre = compuesto.find("nombre").text
           elementos = [e.text for e in compuesto.findall("elementos/elemento")]
           if nombre not in [c["Nombre"] for c in Compuestos]:
            Compuestos.insert({"Nombre": nombre, "Elementos": elementos})
           
    except Exception as e:
        print("Error loading XML file:", e)
    Quimicos.print_list()
    Maquinas.print_list()
    Compuestos.print_list()
    if len(Maquinas.head.data["Elementos"]) > 0:
        print("Maquinas has elements")
    else:
        print("Maquinas does not have elements")

    if len(Compuestos.head.data["Elementos"]) > 0:
        print("Compuestos has elements")
    else:
        print("Compuestos does not have elements")
    
