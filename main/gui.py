from tkinter import *
from tkinter import font
from generate_stack import *
from convert_str_to_int import convert_str_to_int

import random


class MyWindow:
    
    def __init__(self, win):
        
        win.title('Single Molecule Image Generator')
        helv36 = font.Font(size=11, weight='bold')
        information = font.Font(size=10, slant="italic")
        
        
        
        ### SIMULATIONS PARAMETERS ###
        self.simulation_parameters = LabelFrame(win, text=" SIMULATION PARAMETERS ")
        self.simulation_parameters['font'] = helv36
        self.simulation_parameters.grid(row=0, columnspan=1, sticky='NW', padx=8, pady=5, ipady=15, ipadx=8)
        self.space = Label(self.simulation_parameters, text="")
        self.space.grid(row=0, column=0, sticky='W', padx=5, pady=3)
        
        # Molecules number
        self.number_of_mol_text = Label(self.simulation_parameters, text=" Number of molecules")
        self.number_of_mol_text.grid(row=1, column=0, sticky='W', padx=5, pady=10)
        self.number_of_mol = Entry(self.simulation_parameters)
        self.number_of_mol.grid(row=1, column=1, columnspan=7, sticky="WE", pady=3)


        # Frames
        self.number_of_frames_text = Label(self.simulation_parameters, text=" Number of frames")
        self.number_of_frames_text.grid(row=2, column=0, sticky='W', padx=5, pady=10)
        self.number_of_frames = Entry(self.simulation_parameters)
        self.number_of_frames.grid(row=2, column=1, columnspan=10, sticky="WE", pady=3)

        # Filename
        self.filename_text = Label(self.simulation_parameters, text=" Filename")
        self.filename_text.grid(row=3, column=0, sticky='W', padx=5, pady=10)
        self.file_name = Entry(self.simulation_parameters)
        self.file_name.grid(row=3, column=1, columnspan=10, sticky="WE", pady=3)
        
        
        # Edge size
        self.edge_text = Label(self.simulation_parameters, text=" Edge added size")
        self.edge_text.grid(row=4, column=0, sticky='W', padx=5, pady=10)
        self.edge = Entry(self.simulation_parameters)
        self.edge.grid(row=4, column=1, columnspan=10, sticky="WE", pady=0)



        ### BLIKING ###
        self.bliking = LabelFrame(win, text=" BLINKING PARAMETERS ")
        self.bliking['font'] = helv36
        self.bliking.grid(row=2, columnspan=4, sticky='NW', padx=5, pady=5, ipadx=5, ipady=15)
        self.space1 = Label(self.bliking, text="")
        self.space1.grid(row=0, column=0, sticky='W', padx=5, pady=0)
        
        
        # Number of blinks per molecule
        self.number_of_blink_text = Label(self.bliking, text="Number of blinks per molecule")
        self.number_of_blink_text['font'] = information
        self.number_of_blink_text.grid(row=1, column=0, sticky='W', padx=5, pady=10)
        
        self.minimum_value_blink_text = Label(self.bliking, text="Min.")
        self.minimum_value_blink_text.grid(row=1, column=1, sticky='W', padx=5, pady=0)
        self.minimum_value_blink = Entry(self.bliking)
        self.minimum_value_blink.grid(row=1, column=2, columnspan=1, sticky="W", pady=3, ipadx=0)
        self.minimum_value_blink_text = Label(self.bliking, text="Max.")
        self.minimum_value_blink_text.grid(row=1, column=3, sticky='W', padx=5, pady=10)
        self.maximum_value_blink = Entry(self.bliking)
        self.maximum_value_blink.grid(row=1, column=4, columnspan=1, sticky="W", pady=10, ipadx=1)
        

        self.state_random_range_blink = BooleanVar()
        self.state_random_range_blink.set(False)
        self.button_random_range_blink = Button(self.bliking, text="Generate random range", command=self.generate_random_range_bliking_number)
        self.button_random_range_blink.grid(row=2, column=0, sticky='W', padx=5, pady=3)
        
        self.state_random_value_blink = BooleanVar()
        self.state_random_value_blink.set(False)
        self.button_random_value_blink = Button(self.bliking, text="Generate random unique value", command=self.generate_random_unique_bliking_number)#, var=self.check_button_random_value_blink)
        self.button_random_value_blink.grid(row=3, column=0, sticky='W', padx=5, pady=3)
        self.random_unique_blink_text = Label(self.bliking, text="Value:")
        self.random_unique_blink_text.grid(row=3, column=1, sticky='W', padx=5, pady=10)
        self.random_unique_blink_value = Entry(self.bliking)
        self.random_unique_blink_value.insert(0, '')
        self.random_unique_blink_value.grid(row=3, column=2, columnspan=1, sticky="W", pady=10, ipadx=1)
        
        
    
        self.space5 = Label(self.bliking, text="")
        self.space5.grid(row=4, column=0, sticky='W', padx=5, pady=10)
        # Range for on time length
        self.on_time_text = Label(self.bliking, text="On time duration (in frame number)")
        self.on_time_text['font'] = information
        self.on_time_text.grid(row=5, column=0, sticky='W', padx=5, pady=10)
        
        self.min_on_time_text= Label(self.bliking, text="Min.")
        self.min_on_time_text.grid(row=5, column=1, sticky='W', padx=5, pady=0)
        self.min_on_time_value = Entry(self.bliking)
        self.min_on_time_value.grid(row=5, column=2, columnspan=7, sticky="W", pady=3)
        self.max_on_time_text = Label(self.bliking, text="Max.")
        self.max_on_time_text.grid(row=5, column=3, sticky='W', padx=5, pady=10)
        self.max_on_time_value = Entry(self.bliking)
        self.max_on_time_value.grid(row=5, column=4, columnspan=7, sticky="W", pady=3)
        
        self.check_button_random_range_blink_on = BooleanVar()
        self.check_button_random_range_blink_on.set(False)
        self.button_random_range_blink_on = Button(self.bliking, text="Generate random range", command=self.generate_random_range_on_number)
        self.button_random_range_blink_on.grid(row=6, column=0, sticky='W', padx=5, pady=3)
        
        self.check_toggle_value_unique_on = BooleanVar()
        self.check_toggle_value_unique_on.set(False)
        self.toggle_unique_value_on = Button(self.bliking, text="Generate random unique value", command=self.generate_random_unique_on_number)#, var=self.check_button_random_range_blink_on)
        self.toggle_unique_value_on.grid(row=7, column=0, sticky='W', padx=5, pady=3)
        self.random_unique_on = Label(self.bliking, text="Value:")
        self.random_unique_on.grid(row=7, column=1, sticky='W', padx=5, pady=10)
        self.random_unique_value_on = Entry(self.bliking)
        self.random_unique_value_on.insert(0, '')
        self.random_unique_value_on.grid(row=7, column=2, columnspan=1, sticky="W", pady=10, ipadx=1)
        
        
        
        # OWN BLINKING SEQUENCE
        self.sequence = LabelFrame(win, text="Sequence of blinks to enter")
        self.sequence['font'] = information
        self.sequence.grid(row=2, column=3, sticky='NW', padx=5, pady=10)
        
        self.text = Text(self.sequence, height = 10, width = 55)
        self.text.grid(row=2, column=0, sticky='W', padx=5, pady=10)
        self.text.insert(1.0,'Sequence structure\n\nThe separator between value is a comma (eg: 2, 3, 4)\nA sequence can be created using a - (eg: 2, 3, 4-10)\nDelete this before entering a sequence\nKeep in mind your number of frames\nDon\'t forget to validate')
        
        self.check_use_perso = BooleanVar()
        self.check_use_perso.set(False)
        self.use_perso = Button(self.sequence, text="Validate", command=self.use_own_sequence)
        self.use_perso.grid(row=3, column=0, sticky='WE', padx=5, pady=3)
        
        
        
        
        ### RUN SIMULATION ###
        self.simu = LabelFrame(win, text=" RUN SIMULATION ")
        self.simu['font'] = helv36
        self.simu.grid(row=3, column=0, columnspan=7, sticky='NW', padx=5, pady=5, ipadx=21, ipady=15)
        self.run = Button(self.simu, text='Generate TIF stack', command=self.set)
        self.run.grid(row=1, column=0, sticky='NW', padx=103, pady=5)
        
        self.text_sim = StringVar(name=" ")
        self.state_simulation=Label(self.simu, text=self.text_sim)
        self.state_simulation.grid(row=4, column=0, sticky='W', padx=5, pady=0)
        
        
        
        
        
        ### OTHERS PARAMETERS ###
        self.others = LabelFrame(win, text=" OTHER PARAMETERS ")
        self.others['font'] = helv36
        self.others.grid(row=0, column=3, columnspan=1, sticky='NW', padx=5, pady=5, ipadx=5, ipady=5)
        self.space1 = Label(self.others, text="")
        self.space1.grid(row=0, column=0, sticky='W', padx=5, pady=3)

        self.predifined = BooleanVar()
        self.predifined.set(False)
        self.check_predifined = Button(self.others, text='Use predifined parameters', command=self.check_predifined_parameters)
        self.check_predifined.grid(row=8, column=0, columnspan=7, sticky="WE", pady=3, padx=5)

        self.delete = BooleanVar()
        self.delete.set(False)
        self.delete_check = Button(self.others, text='Delete all settings', command=self.check_delete)
        self.delete_check.grid(row=9, column=0, columnspan=7, sticky="WE", pady=3, ipadx=1, padx=5)
        
        self.ssss = Label(self.others, text=" ")
        self.ssss.grid(row=10, column=0, sticky='W', padx=5, pady=10)
        self.avg_intensity = Label(self.others, text="Molecules Integrated Intensity")
        self.avg_intensity.grid(row=11, column=0, sticky='W', padx=5, pady=10)
        self.intensity = Entry(self.others)
        self.intensity.grid(row=11, column=1, sticky="WE", pady=3)
        
        self.sd_avg_intensity = Label(self.others, text="Integrated Intensity s.d.")
        self.sd_avg_intensity.grid(row=12, column=0, sticky='W', padx=5, pady=10)
        self.sd_intensity = Entry(self.others)
        self.sd_intensity.grid(row=12, column=1, sticky="WE", pady=3)



        ### CAMERA PARAMETERS ###
        self.camera = LabelFrame(win, text=" CAMERA SIMULATION ")
        self.camera['font'] = helv36
        self.camera.grid(row=0, column=2, columnspan=1, sticky='NW', padx=5, pady=5, ipadx=5, ipady=15)
        self.space1 = Label(self.camera, text="Background")
        self.space1['font'] = information
        self.space1.grid(row=0, column=0, sticky='W', padx=5, pady=8)
        
        # Background range
        self.background = Label(self.camera, text=" Background mean value")
        self.background.grid(row=1, column=0, sticky='W', padx=5, pady=10)
        self.background_value = Entry(self.camera)
        self.background_value.grid(row=1, column=1, columnspan=7, sticky="WE", pady=3)

        # Background sd
        self.sd_bg = Label(self.camera, text=" Standard deviation")
        self.sd_bg.grid(row=2, column=0, sticky='W', padx=5, pady=10)
        self.sd_bg_value = Entry(self.camera)
        self.sd_bg_value.grid(row=2, column=1, columnspan=7, sticky="WE", pady=3)

       
        
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
        self.minimum_value_blink.delete(0, "end")
        tmp.append(random.choice(list(range(1, int(self.number_of_frames.get())))))
        tmp.append(random.choice(list(range(1, int(self.number_of_frames.get())))))
        self.maximum_value_blink.insert(0, str(min(tmp)))
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
        self.text.delete(1.0,END)
        self.text.insert(1.0,'Sequence structure\n\nThe separator between value is a comma (eg: 2, 3, 4)\nA sequence can be created using a - (eg: 2, 3, 4-10)\nDelete this before entering a sequence\nKeep in mind your number of frames\nDon\'t forget to validate')
        self.predifined.set(False)
        self.check_use_perso.set(False)



    def check_predifined_parameters(self):
        self.number_of_mol.insert(0, "100")
        self.number_of_frames.insert(0, "30")
        self.file_name.insert(0, "sim01")
        self.edge.insert(0, "0")
        self.minimum_value_blink.insert(0, "2")
        self.maximum_value_blink.insert(0, "3")
        self.min_on_time_value.insert(0, "1")
        self.max_on_time_value.insert(0, "2")
        self.background_value.insert(0, '498')
        self.sd_bg_value.insert(0, '100')
        self.intensity.insert(0, '11000')
        self.sd_intensity.insert(0,'0')
        self.delete.set(False)


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
        
        
        generate_stack(frames, molecules, filename+'.tif', 
                       randomize=True, 
                       intensity=int(self.intensity.get()),
                       ii_sd=int(self.sd_intensity.get()),
                       x_image=2500, 
                       y_image=2500,
                       length_min=lgt_min, 
                       length_max=lgt_max, 
                       blink_min=blk_min, 
                       blink_max=blk_max, 
                       background_value=bkg_value,
                       sd_bckg_value=sd_bkg_value, 
                       blinking_seq=blink_seq,
                       edge=edge)
        
        self.state_simulation.config(text='Done!')