import numpy as np
import scipy
import matplotlib.pyplot as plt
from jumps.jump import Jump

class Scm(Jump):
    def __init__(self,voluntary,jump_type,attempt,weight, filepath):
        
        super().__init__(voluntary,jump_type,attempt,weight,filepath)
        self.onset = None
        self.takeoff = None
        self.impulse = None
        self.takeoff_velocity = None  
        self.peak_power = None
        self.contact_time =None
        self.reactive_strength_index = None

        
        
        self.calculate_attributes()

    
        
    def calculate_attributes(self):
        
        self.onset = self.get_onset(self.force)
        self.takeoff = self.get_takeoff(self.force,self.onset)
        self.contact_time = self.get_contact_time(self.onset,self.takeoff)
        self.norm_force = self.normalize_data(self.force,self.weight)
        self.impulse = self.get_impulse(self.norm_force)
        self.takeoff_velocity = self.get_takeoff_velocity(self.impulse,self.weight)
        self.jump_height = self.calculate_jump_height(self.takeoff_velocity)
        self.reactive_strength_index = self.get_reactive_stength_index(self.jump_height,self.contact_time)
        self.time,self.force,self.norm_force = self.clean_data(self.time,self.force,self.norm_force,self.onset,self.takeoff)
        self.acceleration = self.get_acceleration(self.norm_force,self.mass)
        self.velocity = self.get_velocity(self.acceleration)
        self.power = self.get_power(self.norm_force,self.velocity)
        self.peak_power = self.get_peak_power(self.power)

    def print_jump_data(self):
        txt = "SCM {} {}:\nImpulse(N): {:.2f}\nTakeoff Velocity(m/s): {:.2f}\nJump Height(m): {:.2f} \nRSI: {}\nPeak Power(W): {}\n"
        print(txt.format(self.voluntary,self.attempt, self.impulse, self.takeoff_velocity, self.jump_height,self.reactive_strength_index,self.peak_power))    
        
    def get_onset(self,force):
        threshold = 0.95 * np.mean(force[:1000])
        for index, value in np.ndenumerate(force):
            if value < threshold:
                return index[0]

    
    def get_takeoff(self,force,onset):
    
        left_flight =0
        right_flight = 0
        value =18
        takeoff=0

        for i in range(onset,len(force)):
            if force[i]<value:
                left_flight = i
                value = int(force[i])+1
                break
        
        for i in range(left_flight+1,len(force)):
            if force[i]>value:
                right_flight = i
                break
        
        diff=right_flight -left_flight           
        left_flight = left_flight+(int(0.10*diff))
        right_flight = right_flight -(int(0.10*diff))

        mean = np.mean(force[left_flight:right_flight])
        std= np.std(force[left_flight:right_flight])        

        threshold = mean + 5*std
        for i in range(onset,len(force)):
            if force[i]<threshold:
                takeoff = i
                break
        return takeoff
    
    def clean_data(self,time,force,norm_force,onset,takeoff):
        
        force = force[onset:takeoff+1]
        time = time[onset:takeoff+1]
        norm_force = norm_force[onset:takeoff+1]
        
        return time,force,norm_force
        
    def get_weight(self,force):
        
        return np.mean(force[:1000])


    def get_impulse(self, norm_force):
        
        impulse = np.trapz(norm_force[self.onset:self.takeoff], dx=0.001)
        return impulse

    def get_takeoff_velocity(self, impulse,weight):
        mass = weight / 9.81
        takeoff_velocity = impulse / mass
        return takeoff_velocity

    def calculate_jump_height(self, takeoff_velocity):
        jump_height = (takeoff_velocity ** 2) / (2 * 9.81)
        return jump_height   # Convert to cm
    
    def get_contact_time(self,onset,takeoff):
        
        return (takeoff -onset)/1000
    
    def get_reactive_stength_index(self,jump_height,contact_time):
        
        return jump_height/contact_time

    def get_peak_power(self,power):
        
        return np.max(power)
    
    def plot_curve_ft(self):
    

        fig, ax = plt.subplots()
        ax.plot(self.time,self.norm_force,"k", linewidth=1)
        ax.grid(True)
        ax.plot([self.time[self.onset]],[self.norm_force[self.onset]],color="0",marker="o",label="Onset")    
        ax.plot([self.time[self.takeoff]],[self.norm_force[self.takeoff]],color="0.5",marker="o", label='Takeoff')
        ax.set_title("Curve Force x Time")
        ax.set_xlabel("Time(s)")
        ax.set_ylabel("Force(N)")
        ax.legend()
        
    def plot_curves(self):
        fig, ax = plt.subplots(2,2,figsize=(15,12))
        
        ax[0,0].plot(self.time,self.norm_force,"k", linewidth=1,label="norm force") 
        ax[0,0].grid(True)
        ax[0,0].set_title("Norm Force x Time")
        ax[0,0].set_xlabel("Time")
        ax[0,0].set_ylabel("Norm Force")
        ax[0,0].legend()
        
        ax[0,1].plot(self.time,self.acceleration,"k", linewidth=1,label="acceleration") 
        ax[0,1].grid(True)
        ax[0,1].set_title("Acceleration x Time")
        ax[0,1].set_xlabel("Time")
        ax[0,1].set_ylabel("Acceleration")
        ax[0,1].legend()
        ''
        ax[1,0].plot(self.time[:-1],self.velocity,"k", linewidth=1,label="velocity") 
        ax[1,0].grid(True)
        ax[1,0].set_title("Velocity x Time")
        ax[1,0].set_xlabel("Time")
        ax[1,0].set_ylabel("Velocity")
        ax[1,0].legend()
         
        ax[1,1].plot(self.time[:-1],self.power,"k", linewidth=1,label="power") 
        ax[1,1].grid(True)
        ax[1,1].set_title("Power x Time")
        ax[1,1].set_xlabel("Time")
        ax[1,1].set_ylabel("Power")
        ax[1,1].legend()