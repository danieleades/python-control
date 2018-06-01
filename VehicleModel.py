from PhysicsModel import PhysicsModel_1D

class VehicleModel:
    def __init__(self):
        self.model = PhysicsModel_1D()
        self.max_force = 1
        self.force_request = 0

    def set_force_request(self,force):
        if force<0:
            force = max(force,-self.max_force)
        else:
            force = min(force,self.max_force)
        self.force_request = force

    def set_time_interval(self,time_interval):
        self.time_interval = time_interval
    
    def run_step(self):
        self.model.push(self.force_request,self.time_interval)

    def get_position(self):
        return self.model.position

    def get_velocity(self):
        return self.model.velocity