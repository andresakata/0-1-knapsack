import time

class ExecutionLogger:
  def __init__(self):
    self

  def run(self, solver):
    start_time = time.time()
    solver.run()
    print("Time: %s seconds" % (time.time() - start_time))
    print("Solution: %s" % solver.s)
    print("Total weight: %s" % solver.total_weight)
    print("Best value: %s" % solver.best_value)
