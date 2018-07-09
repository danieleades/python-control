from TestRunner import TestRunner

test_runner = TestRunner()

test_runner.run()
test_runner.draw_plot()
score = test_runner.get_score()

print("score: {}".format(score))