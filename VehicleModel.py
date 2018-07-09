from PhysicsModel import PhysicsModel_1D
import numpy as np

class VehicleModel:
    def __init__(self):
        self.model = PhysicsModel_1D()
        self.max_force = 10
        self.force_request = 0

    def set_force_request(self,force):
        if abs(force)>self.max_force:
            force = np.sign(force)*self.max_force
        self.force_request = force

    def set_time_interval(self,time_interval):
        self.time_interval = time_interval

    def add_noise(self):
        ##self.force_request += np.random.normal(scale = 1)
        pass

    def add_current(self):
        self.force_request += 1
    
    def run_step(self):
        self.add_noise()
        self.add_current()
        self.model.push(self.force_request,self.time_interval)

    def get_position(self):
        return self.model.position

    def get_velocity(self):
        return self.model.velocity