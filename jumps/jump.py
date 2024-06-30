import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

class Jump:
    
    def __init__(self, voluntary,jump_type,attempt,weight, filepath):
        self.voluntary =voluntary
        self.jump_type = jump_type
        self.attempt= attempt
        self.mass = (float(weight))/10
        self.weight = self.mass*9.81
        self.time = None
        self.force = None
        self.norm_force = None
        self.jump_height = None
        self.acceleration = None
        self.velocity = None
        self.power = None
    
        self.read_data(filepath)
        self.force=self.apply_lowpass_filter(self.force)
        

    def read_data(self,file_path):
        _x = []
        _y = []

        with open(file_path, 'r') as file:
            for linha in file:
                linha = linha.strip()
                if linha:
                    x, _, _, y, _, _, _ = linha.split('\t')
                    _x.append(float(x))
                    _y.append(float(y))

        self.time = np.array(_x)
        self.force = np.array(_y)
    
    def butter_lowpass(self,fc, fs, order):
        normal_cutoff = fc / (0.5 * fs)
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        return b, a

    def apply_lowpass_filter(self, data,fc=100, fs=1000, order=2):
        b, a = self.butter_lowpass(fc, fs, order)
        force= filtfilt(b, a, data)
        
        return force
        
    def normalize_data(self,force,weight):
        
        norm_force = force - weight
        return norm_force
    
    def get_acceleration(self, norm_force,mass):
        
        acceleration = norm_force / mass
        return acceleration
    
    def get_velocity(self,acceleration):
        
        velocity = integrate.cumulative_trapezoid(acceleration,dx=0.001)
        return velocity
    
    def get_power(self,force,velocity):
        
        return force[:-1]*velocity