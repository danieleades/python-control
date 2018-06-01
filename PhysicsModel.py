
from scipy.integrate import solve_ivp

class PhysicsModel_1D:

    def __init__(self):
        self.mass = 1
        self.pos = 0
        self.vel = 0   

    def _dx_dt(self,t,X,force):
        # this is simply the jacobian of "F=ma"
        x1, x2 = X
        x1dot = x2
        x2dot = force/self.mass
        return [x1dot, x2dot]

    def push(self,force,timestep):
        X0 = [self.pos,self.vel]
        args=[]
        args.append(force)
        fun=lambda t, y: self._dx_dt(t,y, *args)

        #this uses an adaptive timestep to return an accurate numerical solution
        solution = solve_ivp(fun, (0,timestep), X0, method='RK45')
        self.pos = solution.y[0][-1]
        self.vel = solution.y[1][-1]