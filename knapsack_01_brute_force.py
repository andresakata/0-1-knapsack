from execution_logger import ExecutionLogger
from dataset_reader import DatasetReader

# O(2^n)

class KnapsackBruteForce:
  def __init__(self, n, weight, profit, max_weight):
    self.n = n
    self.weight = weight
    self.profit = profit
    self.max_weight = max_weight

  def run(self):
    self.best_value = 0
    self.total_weight = 0
    self.s = []
    self.solve(self.n - 1, self.s, 0, 0)

  def solve(self, n, s, current_weight, current_value):
    if n == -1 and current_weight <= self.max_weight and current_value > self.best_value:
      self.best_value = current_value
      self.total_weight = current_weight
      self.s = s.copy()

    if n == -1:
      return

    self.solve(n - 1, [0] + s, current_weight, current_value)
    self.solve(n - 1, [1] + s, current_weight + self.weight[n], current_value + self.profit[n])

dataset = DatasetReader().read('p08')
kbf = KnapsackBruteForce(len(dataset[0]), dataset[0], dataset[1], dataset[2])
ExecutionLogger().run(kbf)
