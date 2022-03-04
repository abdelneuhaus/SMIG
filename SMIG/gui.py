from tkinter import *
from tkinter import font
from generate_stack import *


class MyWindow:
    
    def __init__(self, win):
        
        win.title('Single Molecule Image Generator')
        helv36 = font.Font(size=11, weight='bold')
        italic = font.Font(size=10, slant="italic")
        
        ### SIMULATIONS PARAMETERS ###
        self.simulation_parameters = LabelFrame(win, text=" SIMULATION PARAMETERS ")
        self.simulation_parameters['font'] = helv36
        self.simulation_parameters.grid(row=0, columnspan=7, sticky='NW', padx=5, pady=5, ipadx=48, ipady=40)
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
        self.bliking.grid(row=2, columnspan=7, sticky='NW', padx=5, pady=5, ipadx=5, ipady=15)
        self.space1 = Label(self.bliking, text="")
        self.space1.grid(row=0, column=0, sticky='W', padx=5, pady=0)
        
        # Number of blinks per molecule
        self.blink_label = Label(self.bliking, text="Number of blinks per molecule")
        self.blink_label['font'] = italic
        self.blink_label.grid(row=1, column=0, sticky='W', padx=5, pady=10)
        
        self.min_blink = Label(self.bliking, text="Min.")
        self.min_blink.grid(row=2, column=0, sticky='W', padx=5, pady=0)
        self.min_blk = Entry(self.bliking)
        self.min_blk.grid(row=2, column=1, columnspan=7, sticky="W", pady=3)
        
        self.max_blink = Label(self.bliking, text="Max.")
        self.max_blink.grid(row=3, column=0, sticky='W', padx=5, pady=10)
        self.max_blk = Entry(self.bliking)
        self.max_blk.grid(row=3, column=1, columnspan=7, sticky="W", pady=3)
        
        
        # Range for off time length
        self.off_label = Label(self.bliking, text="Off time duration (in frame number)")
        self.off_label['font'] = italic
        self.off_label.grid(row=5, column=0, sticky='W', padx=5, pady=10)
        
        self.min_off= Label(self.bliking, text="Min.")
        self.min_off.grid(row=6, column=0, sticky='W', padx=5, pady=0)
        self.min_off_lgt = Entry(self.bliking)
        self.min_off_lgt.grid(row=6, column=1, columnspan=7, sticky="W", pady=3)
        
        self.max_off = Label(self.bliking, text="Max.")
        self.max_off.grid(row=7, column=0, sticky='W', padx=5, pady=10)
        self.max_off_lgt = Entry(self.bliking)
        self.max_off_lgt.grid(row=7, column=1, columnspan=7, sticky="W", pady=3)
        
        self.checkVal = BooleanVar()
        self.checkVal.set(False)
        self.check = Checkbutton(self.bliking, text='Activate random bliking parameters', command=self.check_value_random_bliking_on, var=self.checkVal) 
        self.check.grid(row=8, column=0, columnspan=7, sticky="W", pady=30)
        
        
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
        self.others.grid(row=2, column=7, columnspan=7, sticky='NW', padx=5, pady=5, ipadx=5, ipady=15)
        self.space1 = Label(self.others, text="")
        self.space1.grid(row=0, column=0, sticky='W', padx=5, pady=3)

        self.predifined = BooleanVar()
        self.predifined.set(False)
        self.check_predifined = Checkbutton(self.others, text='Use predifined parameters', command=self.check_predifined_parameters, var=self.predifined) 
        self.check_predifined.grid(row=8, column=0, columnspan=3, sticky="W", pady=3)


        self.delete = BooleanVar()
        self.delete.set(False)
        self.delete_check = Checkbutton(self.others, text='Delete all settings', command=self.check_delete, var=self.delete) 
        self.delete_check.grid(row=9, column=0, columnspan=3, sticky="W", pady=3)
        
        self.ssss = Label(self.others, text=" ")
        self.ssss.grid(row=10, column=0, sticky='W', padx=5, pady=10)
        
        
        self.avg_intensity = Label(self.others, text="Molecules Intensity")
        self.avg_intensity['font'] = italic
        self.avg_intensity.grid(row=11, column=0, sticky='W', padx=5, pady=10)
        self.intensity = 100000
        
        self.avg_int_bool = BooleanVar()
        self.avg_int_bool.set(False)
        self.check_avg_int_bool = Checkbutton(self.others, text='Use average intensity (typical DNA-PAINT grey value)', command=self.set_avg_intensity, var=self.avg_int_bool) 
        self.check_avg_int_bool.grid(row=12, column=0, columnspan=3, sticky="W", pady=3)


        self.beads_int_bool = BooleanVar()
        self.beads_int_bool.set(False)
        self.check_beads_int_bool = Checkbutton(self.others, text='Use beads-like intensity', command=self.set_beads_like_intensity, var=self.beads_int_bool) 
        self.check_beads_int_bool.grid(row=13, column=0, columnspan=3, sticky="W", pady=3)


        ### CAMERA PARAMETERS ###
        self.camera = LabelFrame(win, text=" CAMERA PARAMETERS ")
        self.camera['font'] = helv36
        self.camera.grid(row=0, column=7, columnspan=7, sticky='NW', padx=5, pady=5, ipadx=33, ipady=15)
        self.space1 = Label(self.camera, text="Further tests needed")
        self.space1['font'] = italic
        self.space1.grid(row=0, column=0, sticky='W', padx=5, pady=8)
        
        # Camera baseline
        self.baseline = Label(self.camera, text=" Camera baseline")
        self.baseline.grid(row=1, column=0, sticky='W', padx=5, pady=10)
        self.baseline_value = Entry(self.camera)
        self.baseline_value.grid(row=1, column=1, columnspan=7, sticky="WE", pady=3)

        # Electrons per ADU
        self.epadu = Label(self.camera, text=" Electrons per ADU")
        self.epadu.grid(row=2, column=0, sticky='W', padx=5, pady=10)
        self.epadu_value = Entry(self.camera)
        self.epadu_value.grid(row=2, column=1, columnspan=7, sticky="WE", pady=3)
        
        # EM Gain
        self.emgain = Label(self.camera, text=" EM Gain")
        self.emgain.grid(row=3, column=0, sticky='W', padx=5, pady=10)
        self.emgain_value = Entry(self.camera)
        self.emgain_value.grid(row=3, column=1, columnspan=7, sticky="WE", pady=3)
        
        # Quantum efficiency
        self.qe = Label(self.camera, text=" Quantum efficiency")
        self.qe.grid(row=4, column=0, sticky='W', padx=5, pady=10)
        self.qe_value = Entry(self.camera)
        self.qe_value.grid(row=4, column=1, columnspan=7, sticky="WE", pady=3)
        
        

    def set_avg_intensity(self):
        self.beads_int_bool.set(False)
        self.intensity = 100000
        
        
    def set_beads_like_intensity(self):
        self.avg_int_bool.set(False)        
        self.intensity = 500000


    def check_delete(self):
        self.mol_number.delete(0, "end")
        self.frame_number.delete(0, "end")
        self.file_name.delete(0, "end")
        self.min_blk.delete(0, "end")
        self.max_blk.delete(0, "end")
        self.min_off_lgt.delete(0, "end")
        self.max_off_lgt.delete(0, "end")
        self.baseline_value.delete(0, 'end')
        self.emgain_value.delete(0, 'end')
        self.qe_value.delete(0, 'end')
        self.epadu_value.delete(0, 'end')
        self.checkVal.set(False)
        self.predifined.set(False)
        self.avg_int_bool.set(False)        
        self.beads_int_bool.set(False)


    def check_predifined_parameters(self):
        self.mol_number.insert(0, "100")
        self.frame_number.insert(0, "30")
        self.file_name.insert(0, "sim01")
        self.min_blk.insert(0, "2")
        self.max_blk.insert(0, "3")
        self.min_off_lgt.insert(0, "1")
        self.max_off_lgt.insert(0, "2")
        self.baseline_value.insert(0, '750')
        self.epadu_value.insert(0, '6')
        self.qe_value.insert(0, '1')
        self.emgain_value.insert(0, '100')
        self.checkVal.set(True)
        self.avg_int_bool.set(True)        
        self.delete.set(False)

        
    def check_value_random_bliking_on(self):
        return self.checkVal.get()
    
    def set(self):
        molecules = int(self.mol_number.get())
        frames = int(self.frame_number.get())
        filename = str(self.file_name.get())
        blk_min = int(self.min_blk.get())
        blk_max = int(self.max_blk.get())
        lgt_min = int(self.min_off_lgt.get())
        lgt_max = int(self.max_off_lgt.get())
        baseline_camera = int(self.baseline_value.get())
        emgain_cam = int(self.emgain_value.get())
        qe_cam = int(self.qe_value.get())
        epadu_cam = int(self.epadu_value.get())
        
        generate_stack(frames, molecules, filename+'.tif', 
                       randomize=True, 
                       intensity=self.intensity, 
                       x_image=2500, 
                       y_image=2500,
                       length_min=lgt_min, 
                       length_max=lgt_max, 
                       blink_min=blk_min, 
                       blink_max=blk_max, 
                       baseline=baseline_camera,
                       e_per_adu=epadu_cam, 
                       max_value=65535, 
                       em_gain=emgain_cam, 
                       qe=qe_cam)
        
        self.state_simulation.config(text='Done!')


window = Tk()
mywin = MyWindow(window)
window.mainloop()