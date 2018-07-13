# this class describes the setpoint as a function of time for evaluating the controller performance

class ObstacleCourse:
    name = "basic obstacle course"
    def get_setpoint(self,time):
        if time < 5:
            return 0
        elif time < 25:
            return 1
        elif time < 50:
            return -10
        else:
            return 0