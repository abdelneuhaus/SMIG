from tkinter import *
from tkinter import font
from generate_stack import *

import random


class MyWindow:
    
    def __init__(self, win):
        
        win.title('Single Molecule Image Generator')
        helv36 = font.Font(size=12, weight='bold')
        information = font.Font(size=10, slant="italic")
        
        
        
        ### SIMULATIONS PARAMETERS ###
        self.simulation_parameters = LabelFrame(win, text=" SIMULATION PARAMETERS ")
        self.simulation_parameters['font'] = helv36
        self.simulation_parameters.grid(row=0, columnspan=1, sticky='NW', padx=8, pady=5, ipady=40 ,ipadx=8)
        self.space = Label(self.simulation_parameters, text="")
        self.space.grid(row=0, column=0, sticky='W', padx=5, pady=3)
        
        # Molecules number
        self.mol_label = Label(self.simulation_parameters, text=" Number of molecules")
        self.mol_label.grid(row=1, column=0, sticky='W', padx=5, pady=10)
        self.mol_number = Entry(self.simulation_parameters)
        self.mol_number.grid(row=1, column=1, columnspan=7, sticky="WE", pady=3)

        # Frames
        self.frame_label = Label(self.simulation_parameters, text=" Number of frames")
        self.frame_label.grid(row=2, column=0, sticky='W', padx=5, pady=10)
        self.frame_number = Entry(self.simulation_parameters)
        self.frame_number.grid(row=2, column=1, columnspan=10, sticky="WE", pady=3)

        # Filename
        self.file_label = Label(self.simulation_parameters, text=" Filename")
        self.file_label.grid(row=3, column=0, sticky='W', padx=5, pady=10)
        self.file_name = Entry(self.simulation_parameters)
        self.file_name.grid(row=3, column=1, columnspan=10, sticky="WE", pady=3)
        


        ### BLIKING ###
        self.bliking = LabelFrame(win, text=" BLINKING PARAMETERS ")
        self.bliking['font'] = helv36
        self.bliking.grid(row=2, columnspan=4, sticky='NW', padx=5, pady=5, ipadx=5, ipady=15)
        self.space1 = Label(self.bliking, text="")
        self.space1.grid(row=0, column=0, sticky='W', padx=5, pady=0)
        
        
        # Number of blinks per molecule
        self.blink_label = Label(self.bliking, text="Number of blinks per molecule")
        self.blink_label['font'] = information
        self.blink_label.grid(row=1, column=0, sticky='W', padx=5, pady=10)
        
        self.min_blink = Label(self.bliking, text="Min.")
        self.min_blink.grid(row=1, column=1, sticky='W', padx=5, pady=0)
        self.min_blk = Entry(self.bliking)
        self.min_blk.grid(row=1, column=2, columnspan=1, sticky="W", pady=3, ipadx=0)
        self.max_blink = Label(self.bliking, text="Max.")
        self.max_blink.grid(row=1, column=3, sticky='W', padx=5, pady=10)
        self.max_blk = Entry(self.bliking)
        self.max_blk.grid(row=1, column=4, columnspan=1, sticky="W", pady=10, ipadx=1)
        

        self.check_toggle_random_range_blink = BooleanVar()
        self.check_toggle_random_range_blink.set(False)
        self.toggle_random_range = Button(self.bliking, text="Generate random range", command=self.generate_random_range_bliking_number)
        self.toggle_random_range.grid(row=2, column=0, sticky='W', padx=5, pady=3)
        
        self.check_toggle_unique_value_blink = BooleanVar()
        self.check_toggle_unique_value_blink.set(False)
        self.toggle_random_value_blink = Button(self.bliking, text="Generate random unique value", command=self.generate_random_unique_bliking_number)#, var=self.check_toggle_random_value_blink)
        self.toggle_random_value_blink.grid(row=3, column=0, sticky='W', padx=5, pady=3)
        self.random_unique_blink = Label(self.bliking, text="Value:")
        self.random_unique_blink.grid(row=3, column=1, sticky='W', padx=5, pady=10)
        self.random_unique_value_blink = Entry(self.bliking)
        self.random_unique_value_blink.insert(0, '')
        self.random_unique_value_blink.grid(row=3, column=2, columnspan=1, sticky="W", pady=10, ipadx=1)
        
        
    
        self.space5 = Label(self.bliking, text="")
        self.space5.grid(row=4, column=0, sticky='W', padx=5, pady=10)
        # Range for on time length
        self.on_label = Label(self.bliking, text="On time duration (in frame number)")
        self.on_label['font'] = information
        self.on_label.grid(row=5, column=0, sticky='W', padx=5, pady=10)
        
        self.min_on= Label(self.bliking, text="Min.")
        self.min_on.grid(row=5, column=1, sticky='W', padx=5, pady=0)
        self.min_on_lgt = Entry(self.bliking)
        self.min_on_lgt.grid(row=5, column=2, columnspan=7, sticky="W", pady=3)
        self.max_on = Label(self.bliking, text="Max.")
        self.max_on.grid(row=5, column=3, sticky='W', padx=5, pady=10)
        self.max_on_lgt = Entry(self.bliking)
        self.max_on_lgt.grid(row=5, column=4, columnspan=7, sticky="W", pady=3)
        
        self.check_toggle_random_range_on = BooleanVar()
        self.check_toggle_random_range_on.set(False)
        self.toggle_random_range_on = Button(self.bliking, text="Generate random range", command=self.generate_random_range_on_number)
        self.toggle_random_range_on.grid(row=6, column=0, sticky='W', padx=5, pady=3)
        
        self.check_toggle_value_unique_on = BooleanVar()
        self.check_toggle_value_unique_on.set(False)
        self.toggle_unique_value_on = Button(self.bliking, text="Generate random unique value", command=self.generate_random_unique_on_number)#, var=self.check_toggle_random_range_on)
        self.toggle_unique_value_on.grid(row=7, column=0, sticky='W', padx=5, pady=3)
        self.random_unique_on = Label(self.bliking, text="Value:")
        self.random_unique_on.grid(row=7, column=1, sticky='W', padx=5, pady=10)
        self.random_unique_value_on = Entry(self.bliking)
        self.random_unique_value_on.insert(0, '')
        self.random_unique_value_on.grid(row=7, column=2, columnspan=1, sticky="W", pady=10, ipadx=1)
        
        
        
        # PERSONALIZE SEQUENCE
        # TO DO
        self.sequence = LabelFrame(win, text="Sequence of blinks to enter")
        self.sequence['font'] = information
        self.sequence.grid(row=2, column=3, sticky='NW', padx=5, pady=10)
        
        self.text = Text(self.sequence, height = 10, width = 55)
        self.text.grid(row=2, column=0, sticky='W', padx=5, pady=10)
        self.text.insert(1.0,'Sequence structure\n\nThe separator between value is a comma (eg: 2, 3, 4)\nA sequence can be created using a - (eg: 2, 3, 4-10)\nDelete this before entering a sequence\nKeep in mind your number of frames\nDon\'t forget to validate')
        
        self.check_use_perso = BooleanVar()
        self.check_use_perso.set(False)
        self.use_perso = Button(self.sequence, text="Validate", command=None)
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
        self.avg_intensity = Label(self.others, text="Molecules Intensity")
        self.avg_intensity['font'] = information
        self.avg_intensity.grid(row=11, column=0, sticky='W', padx=5, pady=10)
        self.intensity = 11000



        ### CAMERA PARAMETERS ###
        self.camera = LabelFrame(win, text=" CAMERA SIMULATION ")
        self.camera['font'] = helv36
        self.camera.grid(row=0, column=2, columnspan=1, sticky='NW', padx=5, pady=5, ipadx=5, ipady=15)
        self.space1 = Label(self.camera, text="Background range")
        self.space1['font'] = information
        self.space1.grid(row=0, column=0, sticky='W', padx=5, pady=8)
        
        # Background range
        self.background = Label(self.camera, text=" Background mean")
        self.background.grid(row=1, column=0, sticky='W', padx=5, pady=10)
        self.background_value = Entry(self.camera)
        self.background_value.grid(row=1, column=1, columnspan=7, sticky="WE", pady=3)

        # Background sd
        self.sd_bg = Label(self.camera, text=" Background sd")
        self.sd_bg.grid(row=2, column=0, sticky='W', padx=5, pady=10)
        self.sd_bg_value = Entry(self.camera)
        self.sd_bg_value.grid(row=2, column=1, columnspan=7, sticky="WE", pady=3)

       
        
        
        
        
    def generate_random_unique_bliking_number(self):
        self.random_unique_value_blink.delete(0, "end")
        self.random_unique_value_blink.insert(0, str(random.choice(list(range(1, int(self.frame_number.get()))))))   
        
    def generate_random_unique_on_number(self):
        self.random_unique_value_on.delete(0, "end")
        self.random_unique_value_on.insert(0, str(random.choice(list(range(1, int(self.frame_number.get()))))))
        

    def generate_random_range_bliking_number(self):
        tmp = []
        self.min_blk.delete(0, "end")
        self.max_blk.delete(0, "end")
        tmp.append(random.choice(list(range(1, int(self.frame_number.get())))))
        tmp.append(random.choice(list(range(1, int(self.frame_number.get())))))
        self.min_blk.insert(0, str(min(tmp)))
        self.max_blk.insert(0, str(max(tmp)))


    def generate_random_range_on_number(self):
        tmp = []
        self.min_on_lgt.delete(0, "end")
        self.max_on_lgt.delete(0, "end")
        tmp.append(random.choice(list(range(1, int(self.frame_number.get())))))
        tmp.append(random.choice(list(range(1, int(self.frame_number.get())))))
        self.min_on_lgt.insert(0, str(min(tmp)))
        self.max_on_lgt.insert(0, str(max(tmp)))


    def check_delete(self):
        self.mol_number.delete(0, "end")
        self.frame_number.delete(0, "end")
        self.file_name.delete(0, "end")
        self.min_blk.delete(0, "end")
        self.max_blk.delete(0, "end")
        self.min_on_lgt.delete(0, "end")
        self.max_on_lgt.delete(0, "end")
        self.background_value.delete(0, 'end')
        self.sd_bg_value.delete(0, 'end')
        self.random_unique_value_on.delete(0, "end")
        self.random_unique_value_blink.delete(0, "end")
        self.predifined.set(False)


    def check_predifined_parameters(self):
        self.mol_number.insert(0, "100")
        self.frame_number.insert(0, "30")
        self.file_name.insert(0, "sim01")
        self.min_blk.insert(0, "2")
        self.max_blk.insert(0, "3")
        self.min_on_lgt.insert(0, "1")
        self.max_on_lgt.insert(0, "2")
        self.background_value.insert(0, '498')
        self.sd_bg_value.insert(0, '100')
        self.delete.set(False)


    def set(self):
        molecules = int(self.mol_number.get())
        frames = int(self.frame_number.get())
        filename = str(self.file_name.get())
        if (str(self.random_unique_value_blink.get()) != ''):
            blk_min = int(self.random_unique_value_blink.get())
            blk_max = int(self.random_unique_value_blink.get())
        else:
            blk_min = int(self.min_blk.get())
            blk_max = int(self.max_blk.get())
        if (str(self.random_unique_value_on.get()) != ''):
            lgt_min = int(self.random_unique_value_on.get())
            lgt_max = int(self.random_unique_value_on.get())
        else:
            lgt_min = int(self.min_on_lgt.get())
            lgt_max = int(self.max_on_lgt.get())
        bkg_value = int(self.background_value.get())
        sd_bkg_value = int(self.sd_bg_value.get())
        
        
        generate_stack(frames, molecules, filename+'.tif', 
                       randomize=True, 
                       intensity=self.intensity, 
                       x_image=2500, 
                       y_image=2500,
                       length_min=lgt_min, 
                       length_max=lgt_max, 
                       blink_min=blk_min, 
                       blink_max=blk_max, 
                       background_value=bkg_value,
                       sd_bckg_value=sd_bkg_value, 
                       max_value=65535)
        
        self.state_simulation.config(text='Done!')