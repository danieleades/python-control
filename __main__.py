from TestRunner import TestRunner

test_runner = TestRunner()

test_runner.run()
test_runner.draw_plot()
print("score: {}".format(test_runner.get_score()))