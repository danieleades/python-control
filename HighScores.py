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

    def insert(self,hash,parameters_in,score):

        hash_string = hash.hexdigest()
        parameters = parameters_in.tolist()

        print("new score: {}".format(score))

        try:
            old_score = self.high_scores[hash_string]['score']
        except:
            old_score=None

        if old_score:
            print("old score: {}".format(old_score))
        else:
            new_data = {}
            new_data['score'] = score
            new_data['parameters'] = parameters
            self.high_scores[hash_string] = new_data
            return
        
        if score < old_score:
            print("new score is better than the old score")
            new_data = {}
            new_data['score'] = score
            new_data['parameters'] = parameters
            self.high_scores[hash_string] = new_data
        else:
            print("old score is better than the new score")
            
    def save(self):
        with open(self.filepath,'w') as file:
            json.dump(self.high_scores, file)

