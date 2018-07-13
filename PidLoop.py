from IntegralWindow import IntegralWindow
import numpy as np

class PidLoop:
    control_type = "simple PID loop"
    def __init__(self):
        self.pos_Kp = 1
        self.pos_Ki = 1
        self.pos_Kd = 1
        self.timestep = 0
        self.position_error = 0
        self.last_position_error = 0
        self.current_velocity=0
        self.velocity_request = 0
        self.force_request = 0
        self.position_integral_window = IntegralWindow()

    def set_position_error(self,position_error):
        self.last_position_error = self.position_error
        self.position_error = position_error
    
    def set_velocity(self,velocity):
        self.current_velocity = velocity
        
    def set_timestep(self,timestep):
        self.timestep = timestep

    def run_position_loop(self):
        self.position_integral_window.push_data(self.position_error,self.timestep)
        proportional = self.pos_Kp*self.position_error
        integral = self.pos_Ki*self.position_integral_window.accumulated_total
        derivative = self.pos_Kd*(self.position_error - self.last_position_error)/self.timestep
        self.velocity_request = proportional + integral + derivative

    def run_velocity_loop(self):
        # bypass this (velocity loop doesn't exist)
        self.force_request = self.velocity_request

    def run_step(self):
        self.run_position_loop()
        self.run_velocity_loop()
        return self.force_request

    def get_control_parameters(self):
        parameters=np.array([self.pos_Kp, self.pos_Ki, self.pos_Kd])
        return parameters
    
    def set_control_parameters(self,parameters):
        self.pos_Kp,self.pos_Ki,self.pos_Kd = parameters

    def get_control_parameter_bounds(self):
        return [(0.0,100.0),(0.0,100.0),(0.0,100.0)]

class CascadePidLoop(PidLoop):
    control_type = "cascade PID loop"
    
    def __init__(self):
        PidLoop.__init__(self)
        self.vel_Kp = 1
        self.vel_Ki = 1
        self.vel_Kd = 1
        self.velocity_request=0
        self.velocity_integral_window = IntegralWindow()
        self.velocity_error=0
        self.last_velocity_error=0

    def run_velocity_loop(self):
        self.last_velocity_error = self.velocity_error
        self.velocity_error = self.velocity_request - self.current_velocity

        self.velocity_integral_window.push_data(self.velocity_error,self.timestep)

        proportional = self.vel_Kp*self.velocity_error
        integral = self.vel_Ki*self.velocity_integral_window.accumulated_total
        derivative = self.vel_Kd*(self.velocity_error - self.last_velocity_error)/self.timestep
        self.force_request = proportional + integral + derivative

    def get_control_parameters(self):
        parameters=np.array([self.pos_Kp, self.pos_Ki, self.pos_Kd,self.vel_Kp, self.vel_Ki, self.vel_Kd])
        return parameters

    def set_control_parameters(self,parameters):
        self.pos_Kp,self.pos_Ki,self.pos_Kd, self.vel_Kp, self.vel_Ki, self.vel_Kd = parameters

    def get_control_parameter_bounds(self):
        return [(0.0,100.0),(0.0,100.0),(0.0,100.0),(0.0,100.0),(0.0,100.0),(0.0,100.0)]