from scipy.integrate import solve_ivp
import numpy as np

## The underlying physics model for the vehicle's movements

class PhysicsModel_1D:

    def __init__(self):
        self.mass = 1
        self.position = 0
        self.velocity = 0   
        self.drag_coefficient = 0.1

    # jacobian
    def _dx_dt(self,X,force):
        
        x1, x2 = X
        drag =  - self.drag_coefficient * x2**2 * np.sign(x2)
        x1dot = x2
        x2dot = (force+drag)/self.mass
        return [x1dot, x2dot]

    def push(self,force,timestep):
        X0 = [self.position,self.velocity]
        fun=lambda t, y: self._dx_dt(y,force)

        #this uses an adaptive timestep to return an accurate numerical solution
        solution = solve_ivp(fun, (0,timestep), X0, method='RK45')
        self.position = solution.y[0][-1]
        self.velocity = solution.y[1][-1]


## The model for the vehicle itself. adds force limits, currents, and noise to the physics model

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