from VehicleModel import VehicleModel
from PidLoop import PidLoop

class VehicleController:
    def __init__(self):
        self.vehicle_model = VehicleModel()
        self.controller = PidLoop()
        self.error = 0

    def set_setpoint(self,setpoint):
        self.setpoint = setpoint

    def set_timestep(self,timestep):
        self.controller.set_timestep(timestep)
        self.vehicle_model.set_time_interval(timestep)

    def run_step(self):
        self.error = self.setpoint - self.vehicle_model.get_position()
        self.controller.set_error(self.error)
        force_request = self.controller.run_loop()
        self.vehicle_model.set_force_request(force_request)
        self.vehicle_model.run_step()

    def get_position(self):
        return self.vehicle_model.get_position()

    def get_velocity(self):
        return self.vehicle_model.get_velocity()

    def get_control_parameters(self):
        return self.controller.get_control_parameters()

    def set_control_parameters(self,parameters):
        self.controller.set_control_parameters(parameters)

    def get_control_parameter_bounds(self):
        return self.controller.get_control_parameter_bounds()