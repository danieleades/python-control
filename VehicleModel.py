from PhysicsModel import PhysicsModel_1D

class VehicleModel:
    def __init__(self):
        self.model = PhysicsModel_1D()
        self.maxForce = 1
    
    def _limit_force(self,force):
        return min(force,self.maxForce)
    
    def 
        
    def apply_force_request(self,force, timestep):
        force = self._limit_force(force)
        self.model.push(force, timestep)
        