from execution_logger import ExecutionLogger
from dataset_reader import DatasetReader

class KnapsackGreedy:
  def __init__(self, n, weight, profit, max_weight):
    self.n = n
    self.weight = weight
    self.profit = profit
    self.max_weight = max_weight

  def run(self):
    self.build_ratio_list()
    self.best_value = 0
    self.total_weight = 0
    self.s = []

    for index in range(0, self.n - 1):
      self.s.append(0)

    for item in self.ratio:
      if self.total_weight + self.weight[item['index']] <= self.max_weight:
        self.best_value += self.profit[item['index']]
        self.total_weight += self.weight[item['index']]
        self.s[item['index']] = 1

  def build_ratio_list(self):
    self.ratio = []

    for index in range(0, self.n - 1):
      self.ratio.append({
        "index": index,
        "ratio": self.profit[index] / self.weight[index]
      })

    def ratio_value(elem):
      return elem["ratio"] * -1

    self.ratio = sorted(self.ratio, key=ratio_value)

dataset = DatasetReader().read('p08')
kg = KnapsackGreedy(len(dataset[0]), dataset[0], dataset[1], dataset[2])
ExecutionLogger().run(kg)
