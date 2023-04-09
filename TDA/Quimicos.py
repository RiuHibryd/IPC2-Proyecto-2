import xml.etree.ElementTree as ET
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class ElementoQuimico:
    def __init__(self, numeroAtomico=None, simbolo=None, nombre=None):
        self.numeroAtomico = numeroAtomico
        self.simbolo = simbolo
        self.nombre = nombre
    def __str__(self):
        return "Numero atomico: " + str(self.numeroAtomico) + " Simbolo: " + self.simbolo + " Nombre: " + self.nombre
class Compuesto:
    def __init__(self, nombre=None, elementos=None):
        self.nombre = nombre
        self.elementos = elementos
    def __str__(self):
        elements_str = ", ".join([elemento.simbolo for elemento in self.elementos])
        return "Nombre: " + self.nombre + " Elementos: " + elements_str
class Pin:
    def __init__(self, nombre=None, numeroPines=None, elementos=None):
        self.nombre = nombre
        self.numeroPines = numeroPines
        self.elementos = elementos if elementos is not None else Lista()

class Maquina:
    def __init__(self, nombre=None, numeroPines=None, numeroElementos=None, pines=None, numeroPines2=None):
        self.nombre = nombre
        self.numeroPines = numeroPines
        self.numeroElementos = numeroElementos
        self.pines = pines
        self.numeroPines2 = numeroPines2
    def __str__(self):
        return "Nombre: " + self.nombre + " Numero de pines: " + str(self.numeroPines) + " Numero de elementos: " + str(self.numeroElementos) + " Pines: " + str(self.pines)
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
    def __len__(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count
#-------------------------------------------------------
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            if isinstance(current_node.data, Compuesto):
                print(current_node.data.nombre)
            else:
                print(current_node.data)
            current_node = current_node.next

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next
#------------------------------------------------------

#-------------------------------------------------------
    def bubble_sorting(self):
        if self.head is None or self.head.next  is None:
            return
        bubble_list = False
        while not bubble_list:
            bubble_list = True
            current_node = self.head
            while current_node.next is not None:
                if current_node.data.numeroAtomico > current_node.next.data.numeroAtomico:
                    bubble_list = False
                    current_node.data, current_node.next.data = current_node.next.data, current_node.data
                current_node = current_node.next        
#------------------------------------------------------

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
            if nombre not in [q.nombre for q in Quimicos] and simbolo not in [q.simbolo for q in Quimicos] and numeroAtomico not in [q.numeroAtomico for q in Quimicos]:
             Quimicos.insert(ElementoQuimico(numeroAtomico, simbolo, nombre))



       
        for maquina in root.findall("listaMaquinas/Maquina"):
            nombre = maquina.find("nombre").text
            numeroPines = maquina.find("numeroPines").text
            numeroElementos = maquina.find("numeroElementos").text
            pines = Lista()
            for pin in maquina.findall("pin"):
                elementos = Lista()
                for e in pin.findall("elementos/elemento"):
                    for elemento in Quimicos:
                        if elemento.simbolo == e.text:
                            elementos.insert(elemento)
                            break
                # Chorradas criminales que hacen que funke
                pines.insert(Pin(None, len(elementos), elementos))
            if nombre not in [m.nombre for m in Maquinas]:
                Maquinas.insert(Maquina(nombre, numeroPines, numeroElementos, pines))

   

        for compuesto in root.findall("listaCompuestos/compuesto"):
            nombre = compuesto.find("nombre").text
            elementos = Lista()
            for e in compuesto.findall("elementos/elemento"):
                for elemento in Quimicos:
                    if elemento.simbolo == e.text:
                        elementos.insert(elemento)
                        break
            if nombre not in [c.nombre for c in Compuestos]:
                Compuestos.insert(Compuesto(nombre, elementos))
           
    except Exception as e:
        print("Error loading XML file:", e)

  
        # Print the contents of each list for verification

    
