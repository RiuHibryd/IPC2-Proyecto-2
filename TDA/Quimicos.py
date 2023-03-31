import xml.etree.ElementTree as ET
from tkinter import filedialog

class Element:
    def __init__(self, numeroAtomico, simbolo, nombre):
        self.numeroAtomico = numeroAtomico
        self.simbolo = simbolo
        self.nombre = nombre

class Maquina:
    def __init__(self, nombre, numeroPines, numeroElementos, elementos):
        self.nombre = nombre
        self.numeroPines = numeroPines
        self.numeroElementos = numeroElementos
        self.elementos = elementos

class Compuesto:
    def __init__(self, nombre, elementos):
        self.nombre = nombre
        self.elementos = elementos

class DataContainer:
    def __init__(self):
        self.listaElementos = []
        self.listaMaquinas = []
        self.listaCompuestos = []

def load_xml_file(data_container):
    try:
        # Open file dialog to select XML file
        filename = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])
        
        # Parse XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Process XML data and create instances of classes
        for element in root.findall("listaElementos/elemento"):
            numeroAtomico = element.find("numeroAtomico").text
            simbolo = element.find("simbolo").text
            nombre = element.find("nombreElemento").text
            data_container.listaElementos.append(Element(numeroAtomico, simbolo, nombre))
        
        for maquina in root.findall("listaMaquinas/Maquina"):
            nombre = maquina.find("nombre").text
            numeroPines = maquina.find("numeroPines").text
            numeroElementos = maquina.find("numeroElementos").text
            elementos = [e.text for e in maquina.find("pin/elementos/elemento")]
            data_container.listaMaquinas.append(Maquina(nombre, numeroPines, numeroElementos, elementos))
            
        for compuesto in root.findall("listaCompuestos/compuesto"):
            nombre = compuesto.find("nombre").text
            elementos = [e.text for e in compuesto.find("elementos/elemento")]
            data_container.listaCompuestos.append(Compuesto(nombre, elementos))
        
    except Exception as e:
        print("Error loading XML file:", e)