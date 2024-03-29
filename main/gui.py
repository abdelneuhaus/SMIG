from tkinter import *					
from tkinter import ttk
from ttkthemes import ThemedStyle
from generate_stack import *
from convert_str_to_int import convert_str_to_int
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog as fd
from binary_mask_utils import get_polygons, generate_coordinates_poly, get_all_coordinates

import matplotlib.pyplot as plt 
import random
import json


class MyWindow:
    
    def __init__(self, root):
        window = ttk.Notebook(root)
        style = ThemedStyle(root)
        style.theme_use('equilux')

        tab1 = ttk.Frame(window)
        tab1bis = ttk.Frame(window)
        tab2 = ttk.Frame(window)
        tab3 = ttk.Frame(window)
        tab4 = ttk.Frame(window)
        tab4bis = ttk.Frame(window)
        tab5 = ttk.Frame(window)

        window.add(tab1, text ='Options & Parameters')
        window.add(tab1bis, text ='Image settings')
        window.add(tab2, text ='Photophysics')
        window.add(tab3, text ='Custom blinking')
        window.add(tab4, text ='Previzualise Image')
        window.add(tab4bis, text='Pattern & Diffusion')
        window.add(tab5, text ='Run simulation')
        window.pack(expand = 1, fill ="both")


        # ------- IMAGES PARAMETERS TAB -------
        self.predifined = BooleanVar()
        self.predifined.set(False)
        self.check_predifined = Button(tab1, text='Use predifined parameters', command=self.check_predifined_parameters, activebackground='#464646', bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.check_predifined.grid(row=5, column=0, columnspan=7, sticky="WE", pady=3, padx=5)

        self.delete = BooleanVar()
        self.delete.set(False)
        self.delete_check = Button(tab1, text='Delete all settings', command=self.check_delete, activebackground='#464646', bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.delete_check.grid(row=6, column=0, columnspan=7, sticky="WE", pady=3, ipadx=1, padx=5)

        self.load_data_bool = BooleanVar()
        self.load_data_bool.set(False)
        self.load_data = Button(tab1, text='Load molecules data', command=self.load_molecule_data, activebackground='#464646', bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.load_data.grid(row=7, column=0, columnspan=7, sticky="WE", pady=3, ipadx=1, padx=5)
        self.data_loaded = None

        # Frames
        self.number_of_frames_text = Label(tab1, text=" Number of frames", bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.number_of_frames_text.grid(row=1, column=0, sticky='W', padx=5, pady=10)
        self.number_of_frames = Entry(tab1, width=7, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.number_of_frames.grid(row=1, column=1, columnspan=10, sticky="WE", pady=3)

        # Filename
        self.filename_text = Label(tab1, text=" Filename", bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.filename_text.grid(row=3, column=0, sticky='W', padx=5, pady=10)
        self.file_name = Entry(tab1, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.file_name.grid(row=3, column=1, columnspan=10, sticky="WE", pady=3)

        # Edge size
        self.edge_text = Label(tab1, text=" Edge added size", bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.edge_text.grid(row=4, column=0, sticky='W', padx=5, pady=10)
        self.edge = Entry(tab1, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.edge.grid(row=4, column=1, columnspan=10, sticky="WE", pady=0)



        # ------- MOLECULES TAB -------
        # Molecules number
        self.number_of_mol_text = Label(tab1bis, text="Number of molecules ", bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.number_of_mol_text.grid(row=0, column=0, sticky='W', padx=5, pady=10)
        self.number_of_mol = Entry(tab1bis, width=7, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.number_of_mol.grid(row=0, column=1, sticky="WE", pady=3)
        

        self.avg_intensity = Label(tab1bis, text="Molecules Integrated Intensity", bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.avg_intensity.grid(row=1, column=0, sticky='W', padx=5, pady=10)
        self.intensity = Entry(tab1bis, width=7, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.intensity.grid(row=1, column=1, sticky="WE", pady=3)
        
        self.sd_avg_intensity = Label(tab1bis, text="Integrated Intensity s.d.", bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.sd_avg_intensity.grid(row=2, column=0, sticky='W', padx=5, pady=10)
        self.sd_intensity = Entry(tab1bis, width=7, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.sd_intensity.grid(row=2, column=1, sticky="WE", pady=3)

        # Background range
        self.background = Label(tab1bis, text="Background mean value", bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.background.grid(row=3, column=0, sticky='W', padx=5, pady=10)
        self.background_value = Entry(tab1bis, width=7, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.background_value.grid(row=3, column=1, sticky="WE", pady=3)

        # Background sd
        self.sd_bg = Label(tab1bis, text="Background s.d.", bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.sd_bg.grid(row=4, column=0, sticky='W', padx=5, pady=10)
        self.sd_bg_value = Entry(tab1bis, width=7, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.sd_bg_value.grid(row=4, column=1, sticky="WE", pady=3)

        # Density
        self.density_text = Label(tab1bis, text='Density', bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.density_text.grid(row=6, column=0, sticky='W', padx=5, pady=3)
        self.density = Entry(tab1bis, width=7, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.density.grid(row=6, column=1, columnspan=1, sticky="W", pady=10, ipadx=1)
        self.use_density = BooleanVar()
        self.use_density.set(False)
        self.checkme = Checkbutton(tab1bis, text='Use density', variable=self.use_density, fg='#edebeb', onvalue=True, offvalue=False, bg='#464646', highlightcolor='#464646', selectcolor='#464646', activebackground='#464646', highlightthickness=0, highlightbackground="#edebeb")#, width=20, height=5)
        self.checkme.grid(row=6, column=2, sticky='W', padx=10, pady=3)
        
        self.space2 = Label(tab1bis, text=" ", bg='#464646').grid(row=5, column=0, sticky='W')

        self.tracking_text = Label(tab1bis, text='Displacement', bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.tracking_text.grid(row=7, column=0, sticky='W', padx=5, pady=3)
        
        self.use_tracking = BooleanVar()
        self.use_tracking.set(False)
        self.checktrack = Checkbutton(tab1bis, text='Add displacement (in pixel)', variable=self.use_tracking, fg='#edebeb', onvalue=True, offvalue=False, bg='#464646', highlightcolor='#464646', selectcolor='#464646', activebackground='#464646', highlightthickness=0, highlightbackground="#edebeb")
        self.checktrack.grid(row=7, column=2, sticky='W', padx=10, pady=3)
        self.pixel_track = Entry(tab1bis, width=7, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.pixel_track.grid(row=7, column=1, sticky="W", pady=0)#, ipadx=1)



        # ------- BLIKING TAB -------
        # Number of blinks per molecule
        self.number_of_blink_text = Label(tab2, text="Number of blinks per molecule", bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.number_of_blink_text.grid(row=0, column=0, sticky='W', padx=5, pady=10)

        self.minimum_value_blink_text = Label(tab2, text="Min.", bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.minimum_value_blink_text.grid(row=1, column=1, sticky='E', padx=5, pady=0)
        self.minimum_value_blink = Entry(tab2, width=5, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.minimum_value_blink.grid(row=1, column=2, columnspan=1, sticky="W", pady=3, ipadx=0)
        self.minimum_value_blink_text = Label(tab2, text="Max.", bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.minimum_value_blink_text.grid(row=1, column=3, sticky='W', padx=5, pady=10)
        self.maximum_value_blink = Entry(tab2, width=5, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.maximum_value_blink.grid(row=1, column=4, columnspan=1, sticky="W", pady=10, ipadx=1)
        
        self.state_random_range_blink = BooleanVar()
        self.state_random_range_blink.set(False)
        self.button_random_range_blink = Button(tab2, text="Generate random range", command=self.generate_random_range_bliking_number, activebackground='#464646',bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.button_random_range_blink.grid(row=1, column=0, sticky='W', padx=5, pady=3)

        self.state_random_value_blink = BooleanVar()
        self.state_random_value_blink.set(False)
        self.button_random_value_blink = Button(tab2, text="Generate random unique value", command=self.generate_random_unique_bliking_number, bg='#464646', activebackground='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")#, var=check_button_random_value_blink)
        self.button_random_value_blink.grid(row=2, column=0, sticky='W', padx=5, pady=3)
        self.random_unique_blink_text = Label(tab2, text="Value:", bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.random_unique_blink_text.grid(row=2, column=1, sticky='W', padx=5, pady=10)
        self.random_unique_blink_value = Entry(tab2, width=5, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.random_unique_blink_value.insert(0, '')
        self.random_unique_blink_value.grid(row=2, column=2, columnspan=1, sticky="W", pady=10, ipadx=1)


        # Range for on time length
        self.space = Label(tab2, text=" ", bg='#464646').grid(row=3, column=0, sticky='W')
        self.on_time_text = Label(tab2, text="On time duration (in frame number)", bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.on_time_text.grid(row=4, column=0, sticky='W', padx=5, pady=10)

        self.min_on_time_text= Label(tab2, text="Min.", bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.min_on_time_text.grid(row=5, column=1, sticky='W', padx=5, pady=0)
        self.min_on_time_value = Entry(tab2, width=5, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.min_on_time_value.grid(row=5, column=2, columnspan=7, sticky="W", pady=3)
        self.max_on_time_text = Label(tab2, text="Max.", bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.max_on_time_text.grid(row=5, column=3, sticky='W', padx=5, pady=10)
        self.max_on_time_value = Entry(tab2, width=5, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.max_on_time_value.grid(row=5, column=4, columnspan=7, sticky="W", pady=3)

        self.check_button_random_range_blink_on = BooleanVar()
        self.check_button_random_range_blink_on.set(False)
        self.button_random_range_blink_on = Button(tab2, text="Generate random range", command=self.generate_random_range_on_number, activebackground='#464646', bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.button_random_range_blink_on.grid(row=5, column=0, sticky='W', padx=5, pady=3)

        self.check_toggle_value_unique_on = BooleanVar()
        self.check_toggle_value_unique_on.set(False)
        self.toggle_unique_value_on = Button(tab2, text="Generate random unique value", command=self.generate_random_unique_on_number, activebackground='#464646', bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")#, var=check_button_random_range_blink_on)
        self.toggle_unique_value_on.grid(row=6, column=0, sticky='W', padx=5, pady=3)
        self.random_unique_on = Label(tab2, text="Value:", bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.random_unique_on.grid(row=6, column=1, sticky='W', padx=5, pady=10)
        self.random_unique_value_on = Entry(tab2, width=5, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.random_unique_value_on.insert(0, '')
        self.random_unique_value_on.grid(row=6, column=2, columnspan=1, sticky="W", pady=10, ipadx=1)



        # ------- OWN BLINKING SEQUENCE -------
        self.text = Text(tab3, height = 7, width = 60, bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.text.grid(row=0, column=0, sticky='WE', padx=10, pady=10)
        self.text.insert(1.0,'Sequence structure\n\nThe separator between value is a comma (eg: 2, 3, 4)\nA sequence can be created using a - (eg: 2, 3, 4-10)\nDelete this before entering a sequence\nKeep in mind your number of frames\nDon\'t forget to validate')

        self.check_use_perso = BooleanVar()
        self.check_use_perso.set(False)
        self.use_perso = Button(tab3, text="Validate", command=self.use_own_sequence, bg='#464646', fg='#edebeb', activebackground='#464646', highlightthickness=0, highlightbackground="#edebeb")
        self.use_perso.grid(row=1, column=0, sticky='WE', padx=10, pady=3)
        self.space1 = Label(tab3, text=" ", bg='#464646').grid(row=2, column=0, sticky='W')

        # SMLM setup
        self.photophysics_text = Label(tab3, text='SMLM METHODS', bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb", font='bold')
        self.photophysics_text.grid(row=3, column=0, sticky='W', padx=5)
        self.use_palm = BooleanVar()
        self.use_palm.set(False)
        self.check_me_for_palm = Checkbutton(tab3, text='Use PALM photophysic', variable=self.use_palm, fg='#edebeb', onvalue=True, offvalue=False, bg='#464646', highlightcolor='#464646', selectcolor='#464646', activebackground='#464646', highlightthickness=0, highlightbackground="#edebeb")
        self.check_me_for_palm.grid(row=4, column=0, sticky='W', padx=5, pady=3)
        self.use_dnapaint = BooleanVar()
        self.use_dnapaint.set(False)
        self.check_me_for_dnapaint = Checkbutton(tab3, text='Use DNA-PAINT photophysic (NOT DONE)', variable=self.use_dnapaint, fg='#edebeb', onvalue=True, offvalue=False, bg='#464646', highlightcolor='#464646', selectcolor='#464646', activebackground='#464646', highlightthickness=0, highlightbackground="#edebeb")
        self.check_me_for_dnapaint.grid(row=6, column=0, sticky='W', padx=5, pady=3)
        self.use_storm = BooleanVar()
        self.use_storm.set(False)
        self.check_me_for_storm = Checkbutton(tab3, text='Use dSTORM photophysic', variable=self.use_storm, fg='#edebeb', onvalue=True, offvalue=False, bg='#464646', highlightcolor='#464646', selectcolor='#464646', activebackground='#464646', highlightthickness=0, highlightbackground="#edebeb")
        self.check_me_for_storm.grid(row=5, column=0, sticky='W', padx=5, pady=3)        

        # ------- RUN SIMULATION SEQUENCE -------
        self.run = Button(tab5, text='Generate TIF stack', command=self.set, bg='#464646', fg='#edebeb', activebackground='#464646', highlightthickness=0, highlightbackground="#edebeb", width=20, height=5)
        self.run.pack(pady=80)
        
        
        # ------- TEST TAB SEQUENCE -------
        self.image = Canvas(tab4, width=0, height=0, bg='#464646', highlightthickness=0, highlightbackground="#edebeb")
        self.image.pack()
        self.show = Button(tab4, text='Show previzualisation', command=self.press_to_show, bg='#464646', fg='#edebeb', activebackground='#464646', highlightthickness=0, highlightbackground="#edebeb", width=20, height=1)
        self.show.pack()
        
        
        # ------- OPTIONS TAB -------
        # Grid coordinates
        self.use_grille = BooleanVar()
        self.use_grille.set(False)
        self.checkgrille = Checkbutton(tab4bis, text='Set points as a grid', variable=self.use_grille, fg='#edebeb', onvalue=True, offvalue=False, bg='#464646', highlightcolor='#464646', selectcolor='#464646', activebackground='#464646', highlightthickness=0, highlightbackground="#edebeb")
        self.checkgrille.grid(row=1, column=1, sticky='W', padx=10, pady=3)

        # Circle coordinates
        self.use_circle = BooleanVar()
        self.use_circle.set(False)
        self.checkcircle = Checkbutton(tab4bis, text='Create circle of single molecule', variable=self.use_circle, fg='#edebeb', onvalue=True, offvalue=False, bg='#464646', highlightcolor='#464646', selectcolor='#464646', activebackground='#464646', highlightthickness=0, highlightbackground="#edebeb")
        self.checkcircle.grid(row=2, column=1, sticky='W', padx=10, pady=3)
        self.num_circle = Entry(tab4bis, width=7, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.num_circle.grid(row=2, column=2, sticky="W", pady=10, ipadx=1)
        
        # Load binary image
        self.use_mask_button = Button(tab4bis, text='Load binary image', command=self.load_binary_mask, activebackground='#464646', bg='#464646', fg='#edebeb', highlightthickness=0, highlightbackground="#edebeb")
        self.use_mask_button.grid(row=3, column=1,  sticky="W", padx=10, pady=3)
        self.binary_image = None
        self.polygons = None
        self.polygons_coordinates = None
        
        self.space3 = Label(tab1bis, text=" ", bg='#464646').grid(row=4, column=0, sticky='W')
        
        # Use Brownian motion
        self.use_brownian = BooleanVar()
        self.use_brownian.set(False)
        self.checkbrownian = Checkbutton(tab4bis, text='Diffusion coefficient (brownian motion)', variable=self.use_brownian, fg='#edebeb', onvalue=True, offvalue=False, bg='#464646', highlightcolor='#464646', selectcolor='#464646', activebackground='#464646', highlightthickness=0, highlightbackground="#edebeb")
        self.checkbrownian.grid(row=5, column=1, sticky='W', padx=10, pady=3)
        self.brown_value = Entry(tab4bis, width=7, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.brown_value.grid(row=5, column=2, sticky="W", pady=10, ipadx=1)
        
        # Use random walk 
        self.use_rw = BooleanVar()
        self.use_rw.set(False)
        self.checkrw = Checkbutton(tab4bis, text='Max jump for random walk (pixel)', variable=self.use_rw, fg='#edebeb', onvalue=True, offvalue=False, bg='#464646', highlightcolor='#464646', selectcolor='#464646', activebackground='#464646', highlightthickness=0, highlightbackground="#edebeb")
        self.checkrw.grid(row=6, column=1, sticky='W', padx=10, pady=3)
        self.rw_value = Entry(tab4bis, width=7, bg='#464646', fg='#edebeb', highlightthickness=1, highlightbackground="#edebeb")
        self.rw_value.grid(row=6, column=2, sticky="W", pady=10, ipadx=1)
        

    
    def load_molecule_data(self):
        filetypes = (('JSON files', '*.json'), ('All files', '*.*'))
        try:
            self.load_data = fd.askopenfilename(
                title='Open a file',
                initialdir='.',
                filetypes=filetypes)
            with open(self.load_data, 'r') as f:
                self.data_loaded = json.load(f)
            self.load_data_bool.set(True)
            self.data_loaded = {int(k):v for k,v in self.data_loaded.items()}
            if '_diffusion' in self.load_data:
                for i in range(len(self.data_loaded)):
                    self.data_loaded[i]['on_times'] = [self.data_loaded[i]['frame']]
                    self.data_loaded[i]['shift'] = 0
            print("Done")
        except:
            print("No JSON loaded")
        
    
    def load_binary_mask(self):
        filetypes = (
            ('JPG files', '*.jpg'),
            ('PNG files', '*.png'),
            ('TIF files', '*.tif'),
            ('All files', '*.*'))
        try:
            self.binary_image = fd.askopenfilename(
                title='Open a file',
                initialdir='.',
                filetypes=filetypes)
            
            polygons = get_polygons(self.binary_image)
            otp = get_all_coordinates(polygons)
            tmp = [generate_coordinates_poly(otp[i]) for i in range(len(polygons))]
            self.polygons_coordinates = [j for i in tmp for j in i]
            print("Done")
        except:
            print("No file loaded")
        
        
    def use_own_sequence(self):
        self.check_use_perso.set(True)

        
    def generate_random_unique_bliking_number(self):
        self.random_unique_blink_value.delete(0, "end")
        self.random_unique_blink_value.insert(0, str(random.choice(list(range(1, int(self.number_of_frames.get()))))))   
        
    def generate_random_unique_on_number(self):
        self.random_unique_value_on.delete(0, "end")
        self.random_unique_value_on.insert(0, str(random.choice(list(range(1, int(self.number_of_frames.get()))))))
        

    def generate_random_range_bliking_number(self):
        tmp = []
        self.minimum_value_blink.delete(0, "end")
        self.maximum_value_blink.delete(0, "end")
        tmp.append(random.choice(list(range(1, int(self.number_of_frames.get())))))
        tmp.append(random.choice(list(range(1, int(self.number_of_frames.get())))))
        self.minimum_value_blink.insert(0, str(min(tmp)))
        self.maximum_value_blink.insert(0, str(max(tmp)))


    def generate_random_range_on_number(self):
        tmp = []
        self.min_on_time_value.delete(0, "end")
        self.max_on_time_value.delete(0, "end")
        tmp.append(random.choice(list(range(1, int(self.number_of_frames.get())))))
        tmp.append(random.choice(list(range(1, int(self.number_of_frames.get())))))
        self.min_on_time_value.insert(0, str(min(tmp)))
        self.max_on_time_value.insert(0, str(max(tmp)))


    def check_delete(self):
        self.number_of_mol.delete(0, "end")
        self.use_density.set(False)
        self.number_of_frames.delete(0, "end")
        self.file_name.delete(0, "end")
        self.edge.delete(0, "end")
        self.minimum_value_blink.delete(0, "end")
        self.maximum_value_blink.delete(0, "end")
        self.min_on_time_value.delete(0, "end")
        self.max_on_time_value.delete(0, "end")
        self.background_value.delete(0, 'end')
        self.sd_bg_value.delete(0, 'end')
        self.random_unique_value_on.delete(0, "end")
        self.random_unique_blink_value.delete(0, "end")
        self.intensity.delete(0, "end")
        self.sd_intensity.delete(0, "end")
        self.density.delete(0, "end")
        self.text.delete(1.0,END)
        self.text.insert(1.0,'Sequence structure\n\nThe separator between value is a comma (eg: 2, 3, 4)\nA sequence can be created using a - (eg: 2, 3, 4-10)\nDelete this before entering a sequence\nKeep in mind your number of frames\nDon\'t forget to validate')
        self.predifined.set(False)
        self.check_use_perso.set(False)
        self.use_circle.set(False)
        self.use_grille.set(False)
        self.use_brownian.set(False)
        self.use_rw.set(False)
        self.brown_value.delete(0, "end")
        self.rw_value.delete(0, "end")
        self.num_circle.delete(0, "end")
        try:
            self.clear_plot()
        except AttributeError:
            pass
        self.polygons = None
        self.polygons_coordinates = None
        self.binary_image = None
        self.load_data_bool.set(False)
        self.load_data = None
        self.data_loaded = None
        self.pixel_track.delete(0, "end")
        self.use_tracking.set(False)
        self.use_palm.set(False)
        self.use_dnapaint.set(False)
        self.use_storm.set(False)



    def check_predifined_parameters(self):
        self.number_of_mol.insert(0, "100")
        self.density.insert(0, "None")
        self.number_of_frames.insert(0, "30")
        self.file_name.insert(0, "sim01")
        self.edge.insert(0, "0")
        self.minimum_value_blink.insert(0, "2")
        self.maximum_value_blink.insert(0, "3")
        self.min_on_time_value.insert(0, "1")
        self.max_on_time_value.insert(0, "2")
        self.background_value.insert(0, '498')
        self.sd_bg_value.insert(0, '50')
        self.intensity.insert(0, '11000')
        self.sd_intensity.insert(0,'0')
        self.num_circle.insert(0,'0')
        self.delete.set(False)
        self.pixel_track.insert(0, "0")
        self.use_tracking.set(False)
        self.rw_value.insert(0, "0")
        self.use_rw.set(False)
        self.brown_value.insert(0, "0")
        self.use_brownian.set(False)
   
   
    def press_to_show(self):
        global output, fig
        for child in self.image.winfo_children():
                child.destroy()
        output = None
        image = self.previzualize()
        fig = plt.figure()
        fig.patch.set_facecolor('#464646')
        ax = fig.add_subplot(111)
        ax.axis('off')
        output = FigureCanvasTkAgg(fig, master=self.image)
        output.draw()
        output.get_tk_widget().pack()
        ax.imshow(image, cmap='gray')
        plt.close(fig)


    def previzualize(self):
        molecules = int(self.number_of_mol.get())
        filename = str(self.file_name.get())
        edge = int(self.edge.get())
        if self.check_use_perso.get() == False:
            blink_seq = None
        else:
            blink_seq = convert_str_to_int(self.text.get(1.0, "end-1c"))
        bkg_value = int(self.background_value.get())
        sd_bkg_value = int(self.sd_bg_value.get())
        if (self.use_density.get() == True) and (self.density.get() != 'None'):
            edge_ = int(self.edge.get())
            size_image = 500 - edge_
            if self.use_circle.get() == True:
                size_image=60*int(self.num_circle.get())
            molecules = int((size_image*0.16)*float(self.density.get()))*int((size_image*0.16)*float(self.density.get()))

        image = generate_stack(1, molecules, filename+'.tif', 
                    randomize=True, 
                    intensity=int(self.intensity.get())/6,
                    ii_sd=int(self.sd_intensity.get())/6,
                    x_image=500, 
                    y_image=500,
                    length_min=1, 
                    length_max=1, 
                    blink_min=1, 
                    blink_max=1, 
                    background_value=bkg_value,
                    sd_bckg_value=sd_bkg_value, 
                    blinking_seq=blink_seq,
                    edge=edge,
                    save=False,
                    grid=self.use_grille.get(),
                    circle=self.use_circle.get(), 
                    num_circle=int(self.num_circle.get()),
                    binary_file=self.binary_image,
                    coordinates_binary=self.polygons_coordinates, 
                    use_density = self.use_density.get(),
                    is_loaded=self.load_data_bool.get(), 
                    loaded_data=self.data_loaded, 
                    use_palm=self.use_palm.get(),
                    use_storm=self.use_storm.get(),
                    shift=False, 
                    shift_value=0)
        return image
        

    def set(self):
        molecules = int(self.number_of_mol.get())
        frames = int(self.number_of_frames.get())
        filename = str(self.file_name.get())
        edge = int(self.edge.get())
        
        if (str(self.random_unique_blink_value.get()) != ''):
            blk_min = int(self.random_unique_blink_value.get())
            blk_max = int(self.random_unique_blink_value.get())
        else:
            blk_min = int(self.minimum_value_blink.get())
            blk_max = int(self.maximum_value_blink.get())
            
        if self.check_use_perso.get() == False:
            blink_seq = None
        else:
            blink_seq = convert_str_to_int(self.text.get(1.0, "end-1c"))
            
        if (str(self.random_unique_value_on.get()) != ''):
            lgt_min = int(self.random_unique_value_on.get())
            lgt_max = int(self.random_unique_value_on.get())
        else:
            lgt_min = int(self.min_on_time_value.get())
            lgt_max = int(self.max_on_time_value.get())
        bkg_value = int(self.background_value.get())
        sd_bkg_value = int(self.sd_bg_value.get())
        
        if (self.use_density.get() == True) and (self.density.get() != 'None'):
            edge_ = int(self.edge.get())
            size_image = 500 - edge_
            molecules = int((size_image*0.16)*float(self.density.get()))*int((size_image*0.16)*float(self.density.get()))
            
        generate_stack(frames, molecules, filename+'.tif', 
                    randomize=True, 
                    intensity=int(self.intensity.get())/6,
                    ii_sd=int(self.sd_intensity.get())/6,
                    x_image=500, 
                    y_image=500,
                    length_min=lgt_min, 
                    length_max=lgt_max, 
                    blink_min=blk_min, 
                    blink_max=blk_max, 
                    background_value=bkg_value,
                    sd_bckg_value=sd_bkg_value, 
                    blinking_seq=blink_seq,
                    edge=edge,
                    grid=self.use_grille.get(),
                    circle=self.use_circle.get(), 
                    num_circle=int(self.num_circle.get()),
                    binary_file=self.binary_image,
                    coordinates_binary=self.polygons_coordinates,
                    use_density = self.use_density.get(),
                    is_loaded=self.load_data_bool.get(), 
                    loaded_data=self.data_loaded, 
                    use_palm=self.use_palm.get(),
                    use_storm=self.use_storm.get(),
                    shift=self.use_tracking.get(), 
                    shift_value=float(self.pixel_track.get()),
                    brownian_value=float(self.brown_value.get()), 
                    use_brownian=self.use_brownian.get(),
                    randomwalk_value=float(self.rw_value.get()),
                    use_randomwalk=self.use_rw.get())