from execution_logger import ExecutionLogger
from dataset_reader import DatasetReader

# O(2^n)

class KnapsackBruteForceOpt:
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

  def solve(self, n, s, current_w, current_v):
    if current_w > self.max_weight:
      return

    if n == -1:
      if current_w <= self.max_weight and current_v > self.best_value:
        self.best_value = current_v
        self.total_weight = current_w
        self.s = s.copy()
      return

    self.solve(n - 1, [0] + s, current_w, current_v)
    self.solve(n - 1, [1] + s, current_w + self.weight[n], current_v + self.profit[n])

dataset = DatasetReader().read('c09')
kbfo = KnapsackBruteForceOpt(len(dataset[0]), dataset[0], dataset[1], dataset[2])
ExecutionLogger().run(kbfo)
