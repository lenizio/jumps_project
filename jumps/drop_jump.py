import numpy as np
import scipy
import matplotlib.pyplot as plt
from jumps.jump import Jump

class Drop_Jump(Jump):
    def __init__(self,voluntary,jump_type,attempt,weight,drop_platform_height, filepath):
        
        super().__init__(voluntary,jump_type,attempt,weight,filepath)
        self.drop_platform_height = float(drop_platform_height)/100
        self.landing = None
        self.takeoff = None
        self.contact_time = None
        self.takeoff_velocity = None
        self.landing_velocity = None 
        self.second_landing = None
        self.flight_time = None 
        self.reactive_strength_index = None
        self.peak_power = None
        
        
        self.calculate_attributes()
    
    def calculate_attributes(self):
        self.landing = self.get_landing(self.force)
        self.takeoff =self.get_takeoff(self.force,self.landing)
        self.second_landing = self.get_second_landing(self.force,self.takeoff)
        self.time,self.force = self.clean_data(self.time,self.force,self.landing,self.takeoff)
        self.norm_force = self.normalize_data(self.force,self.weight)
        self.acceleration = self.get_acceleration(self.norm_force,self.mass)
        self.velocity = self.get_velocity(self.acceleration)
        self.power = self.get_power(self.norm_force,self.velocity)
        self.flight_time = self.get_flight_time(self.takeoff,self.second_landing)
        self.contact_time = self.get_contact_time(self.landing,self.takeoff)
        self.takeoff_velocity = self.get_takeoff_velocity(self.flight_time)
        self.jump_height = self.calculate_jump_height(self.takeoff_velocity)
        self.reactive_strength_index = self.get_reactive_stength_index(self.jump_height,self.contact_time)
        self.peak_power = self.get_peak_power(self.power)
        
    def get_landing(self,force):
        threshold= np.mean(force[:1000]) + 5 * np.std(force[:1000])
        
        for i in range(len(force)):
            if force[i]>=threshold:
                return i
    
    def get_takeoff(self,force,landing):
        
        threshold= np.mean(force[:1000]) + 5 * np.std(force[:1000])
        onset = landing+100
        for i in range(onset,len(force)):
            if force[i]<=threshold:
                return i
    def get_second_landing(self,force,takeoff):
        
        threshold= np.mean(force[:1000]) + 5 * np.std(force[:1000])
        
        for i in range(takeoff,len(force)):
            if force[i]>=threshold:
                return i
    
    def clean_data(self,time,force,landing,takeoff):
    
        force = force[landing-200:takeoff+200]
        time = time[landing-200:takeoff+200]

        return time,force
    
    def get_flight_time(self,takeoff,second_landing):
        
        return (second_landing - takeoff)/1000
    
    def get_contact_time(self,landing,takeoff):
        
        return (takeoff -landing)/1000
            
    # def get_landing_velocity(self,height_drop_platform):
        
    #     landing_velocity = np.sqrt(2*9.81*height_drop_platform)
        
    #     return landing_velocity

    def get_takeoff_velocity(self,flight_time):
        
         
        takeoff_velocity = flight_time *(9.81/2)
        
        return takeoff_velocity
    
    def calculate_jump_height(self, takeoff_velocity):
        jump_height = (takeoff_velocity ** 2) / (2 * 9.81)
        return jump_height   
    
    def get_reactive_stength_index(self,jump_height,contact_time):
        
        return jump_height/contact_time
    
    def print_jump_data(self):
        txt = "Drop Jump {}cm {} {}:\nTakeoff Velocity(m/s): {:.2f}\nJump Height(m): {:.2f}\nContact Time(s): {}\nFlight Time(s): {}\nRSI: {}\nPeak Power(W): {}\n"
        print(txt.format(int(self.drop_platform_height*100),self.voluntary,self.attempt, self.takeoff_velocity, self.jump_height,self.contact_time,self.flight_time,self.reactive_strength_index,self.peak_power))
    
    
    def get_peak_power(self,power):
        
        return np.max(power)
        
    
    def plot_curve_ft(self):
    
        fig, ax = plt.subplots()
        ax.plot(self.time,self.norm_force,"k", linewidth=1)
        ax.grid(True)
        ax.plot([self.time[self.landing]],[self.norm_force[self.landing]],color="0",marker="o",label="Landing")    
        ax.plot([self.time[self.takeoff]],[self.norm_force[self.takeoff]],color="0.5",marker="o", label='Takeoff')
        ax.plot([self.time[self.second_landing]],[self.norm_force[self.second_landing]],color="0.3",marker="o", label='Second Landing')
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
        
       