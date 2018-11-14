class DatasetReader:
  def __init__(self):
    self

  def read(self, dataset):
    return [
      self.list_reader("datasets/%s_w.txt" % dataset),
      self.list_reader("datasets/%s_p.txt" % dataset),
      int(open('datasets/%s_c.txt' % dataset).read())
    ]

  def list_reader(self, file_name):
    file = open(file_name).read().split('\n')
    file.remove('')
    return list(map(int, file))
