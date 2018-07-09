from IntegralWindow import IntegralWindow

class PidLoop:
    def __init__(self):
        self.Kp = 7.18921353
        self.Ki = 9.83735663
        self.Kd = 0.67080847
        self.timestep = 0
        self.error = 0
        self.last_error = 0
        self.output = 0
        self.integral_window = IntegralWindow()

    def set_error(self,error):
        self.last_error = self.error
        self.error = error
        
    def set_timestep(self,timestep):
        self.timestep = timestep

    def run_loop(self):
        self.integral_window.push_data(self.error,self.timestep)
        proportional = self.Kp*self.error
        integral = self.Ki*self.integral_window.accumulated_total
        derivative = self.Kd*(self.error - self.last_error)/self.timestep
        self.output = proportional + integral + derivative
        return self.output
