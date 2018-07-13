import json
from TestRunner import TestRunner

class HighScores:
    def __init__(self):
        self.filepath = "highscores.json"
        self.high_scores = {}

    def load(self,filepath = "highscores.json"):
        self.filepath = filepath

        try:
            with open(self.filepath) as file:
                self.high_scores = json.load(file)
        except:
            print("no high score file")
            return
        
        print("high scores loaded")

    def insert(self,test_runner,result,score):
        obstacle_course = test_runner.pilot.name
        duration = test_runner.max_time
        timestep = test_runner.timestep
        controller = test_runner.get_control_type()

        new_score = score
        parameters = result.x
        print("new score: {}".format(new_score))

        try:
            old_score = self.high_scores[obstacle_course][duration][timestep][controller]['score']
            print("old score: {}".format(old_score))
        except: # old score doesn't exist
            self.high_scores[obstacle_course][duration][timestep][controller]['score']=new_score
            self.high_scores[obstacle_course][duration][timestep][controller]['parameters']=parameters
        else:            
            if new_score < old_score:
                print("new score is better than the old score")
                self.high_scores[obstacle_course][duration][timestep][controller]['score']=new_score
                self.high_scores[obstacle_course][duration][timestep][controller]['parameters']=parameters
            else:
                print("old score is better than the new score")
            
    def save(self):
        with open(self.filepath,'w') as file:
            json.dump(self.high_scores, file)

