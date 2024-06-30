import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from jumps.jump import Jump

class Lateral_Jump(Jump):
     
    def __init__(self,voluntary,jump_type,attempt,weight,hurdle_height, filepath):
     
            super().__init__(voluntary,jump_type,attempt,weight,filepath)
            self.hurdle_height = float(hurdle_height)/100
            self.force = self.apply_lowpass_filter(self.force,10,1000,4)
            self.norm_force = self.normalize_data(self.force,self.weight)
            self.peak_force_index = self.get_peak_force(self.norm_force,self.weight)
            self.peak_force = self.norm_force[self.peak_force_index]

    def get_peak_force(self,force,weight):
        
        peak_force,_ = signal.find_peaks(force, height=weight)

        return peak_force
    
    def plot_curve_ft(self):
    

        fig, ax = plt.subplots()
        ax.plot(self.time,self.norm_force,"k", linewidth=1)
        ax.grid(True)
        ax.scatter(self.time[self.peak_force_index],self.peak_force,color="0",marker="o",label="Peak Force")    
        ax.set_title("Curve Force x Time")
        ax.set_xlabel("Time(s)")
        ax.set_ylabel("Force(N)")
        ax.legend()