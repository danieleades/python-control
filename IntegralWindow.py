from collections import deque
import numpy as np

class Datapoint:
    def __init__(self,value,timestep):
        self.value = value
        self.timestep = timestep
        self.integral = value*timestep

class IntegralWindow:
    def __init__(self):
        self.datapoints = deque()

        self.max_time_interval = 1
        self.max_accumulated_integral = None
        self.max_datapoints = None

        self.time_interval = 0
        self.accumulated_total = 0
        self.number_of_datapoints = 0

    def _window_overfilled(self):
        if self.max_time_interval is not None and self.time_interval > self.max_time_interval:
            return True
        if self.max_accumulated_integral is not None and abs(self.accumulated_total) >self.max_accumulated_integral:
            return True
        if self.max_datapoints is not None and self.number_of_datapoints > self.max_datapoints:
            return True
        else:
            return False

    def _pop_datapoint(self):
        datapoint = self.datapoints.popleft()
        self.time_interval -= datapoint.timestep
        self.accumulated_total -= datapoint.integral
        self.number_of_datapoints -= 1

    def _resize_to_constraints(self):
        while self._window_overfilled():
            self._pop_datapoint()

    def push_data(self,value,timestep):
        self.time_interval += timestep
        self.accumulated_total += value*timestep
        self.number_of_datapoints += 1
        datapoint = Datapoint(value,timestep)
        self.datapoints.append(datapoint)
        self._resize_to_constraints()