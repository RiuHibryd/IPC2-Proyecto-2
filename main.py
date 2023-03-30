import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Initialization button
        self.init_button = tk.Button(self)
        self.init_button["text"] = "Initialization"
        self.init_button.pack(side="top")

        # Load input file button
        self.load_input_button = tk.Button(self)
        self.load_input_button["text"] = "Load input XML file"
        self.load_input_button.pack(side="top")

        # Generate output file button
        self.generate_output_button = tk.Button(self)
        self.generate_output_button["text"] = "Generate output XML file"
        self.generate_output_button.pack(side="top")

        # Chemical element management frame
        self.chem_frame = tk.LabelFrame(self, text="Chemical element management")
        self.chem_frame.pack(side="left")

        # View chemical elements button
        self.view_elements_button = tk.Button(self.chem_frame)
        self.view_elements_button["text"] = "View chemical elements sorted by atomic number"
        self.view_elements_button.pack(side="top")

        # Add new chemical element button
        self.add_element_button = tk.Button(self.chem_frame)
        self.add_element_button["text"] = "Add new chemical element"
        self.add_element_button.pack(side="top")

        # Compound management frame
        self.comp_frame = tk.LabelFrame(self, text="Compound management")
        self.comp_frame.pack(side="left")

        # View compounds button
        self.view_compounds_button = tk.Button(self.comp_frame)
        self.view_compounds_button["text"] = "View compounds and their formulas"
        self.view_compounds_button.pack(side="top")

        # Analyze compound button
        self.analyze_compound_button = tk.Button(self.comp_frame)
        self.analyze_compound_button["text"] = "Analyze compound"
        self.analyze_compound_button.pack(side="top")

        # Machine management frame
        self.mach_frame = tk.LabelFrame(self, text="Machine management")
        self.mach_frame.pack(side="left")

        # View machines button
        self.view_machines_button = tk.Button(self.mach_frame)
        self.view_machines_button["text"] = "View machines"
        self.view_machines_button.pack(side="top")

        # Help button
        self.help_button = tk.Button(self)
        self.help_button["text"] = "Help"
        self.help_button.pack(side="bottom")

root = tk.Tk()
app = Application(master=root)
app.mainloop()