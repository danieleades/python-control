
from scipy.integrate import solve_ivp

class PhysicsModel_1D:

    def __init__(self):
        self.mass = 1
        self.position = 0
        self.velocity = 0   

    def _dx_dt(self,X,force):
        #jacobian
        x1, x2 = X
        x1dot = x2
        x2dot = force/self.mass
        return [x1dot, x2dot]

    def push(self,force,timestep):
        X0 = [self.position,self.velocity]
        args=[]
        args.append(force)
        fun=lambda t, y: self._dx_dt(y,force)

        #this uses an adaptive timestep to return an accurate numerical solution
        solution = solve_ivp(fun, (0,timestep), X0, method='RK45')
        self.position = solution.y[0][-1]
        self.velocity = solution.y[1][-1]