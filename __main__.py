from VehicleController import VehicleController
from matplotlib import pyplot as plt

vehicle_controller = VehicleController()
vehicle_controller.set_setpoint(100)
vehicle_controller.set_timestep(0.2)

i = 0
class Results:
    def __init__(self):
        self.positions = []
        self.setpoint = []
        self.error = []
    
results = Results()
results.positions.append(vehicle_controller.get_position())
results.setpoint.append(vehicle_controller.setpoint)
results.error.append(vehicle_controller.error)

while i<1000:
    vehicle_controller.run_step()
    results.positions.append(vehicle_controller.get_position())
    results.setpoint.append(vehicle_controller.setpoint)
    results.error.append(vehicle_controller.error)
    i+=1

plot = plt.plot(results.positions)
plot = plt.plot(results.setpoint)
plot = plt.plot(results.error)
plt.legend()
plt.show()