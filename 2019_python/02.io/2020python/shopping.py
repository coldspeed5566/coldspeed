class Notebook:
  _sku = 'uknown'
  _price = 0
  _size = 'uknown'
  def __init__(self, sku, price, size):
      self._sku = sku
      self._price = price
      self._size = size
  def getSku(self):
      return self._sku
  def getPrice(self):
      return self._price
  def getSize(self):
      return self._size
  def info(self):
      return 'Notebook: {}{}{}' .format(self._sku, self._price, self._size)
  def prDetails(self):
      print(self.info)

class Pen:
  _sku = 'uknown'
  _price = 0
  _color = 'uknown'
  def __init__(self, sku, price, color):
      self._sku = sku
      self._price = price
      self._color = color
  def getSku(self):
      return self._sku
  def getPrice(self):
      return self._price
  def getColor(self):
      return self._color
  def info(self):
      return 'Pen: {}{}{}' .format(self._sku, self._price, self._color)
  def prDetails(self):
      print(self.info)

def test():
    SmallNotebook = Notebook('11', 20, 'Small')
    NormalNotebook = Notebook('12', 30, 'Normal')
    BigNotebook = Notebook('13', 40, 'Big')

    BluePen = Pen('21', 10, 'Blue')
    RedPen = Pen('22', 12, 'Red')
    BlackPen = Pen('23', 8, 'Black')

    Notebook.getSku(SmallNotebook)
    Notebook.getSku(NormalNotebook)
    Notebook.getSku(BigNotebook)
    Pen.getSku(BluePen)
    Pen.getSku(RedPen)
    Pen.getSku(BlackPen)

    Notebook.getPrice(SmallNotebook)
    Notebook.getPrice(NormalNotebook)
    Notebook.getPrice(BigNotebook)
    Pen.getPrice(BluePen)
    Pen.getPrice(RedPen)
    Pen.getPrice(BlackPen)

    Notebook.info(SmallNotebook)
    Notebook.info(NormalNotebook)
    Notebook.info(BigNotebook)
    Pen.info(BluePen)
    Pen.info(RedPen)
    Pen.info(BlackPen)

    Notebook.getSize(SmallNotebook)
    Notebook.getSize(NormalNotebook)
    Notebook.getSize(BigNotebook)
    Pen.getColor(BluePen)
    Pen.getColor(RedPen)
    Pen.getColor(BlackPen)

    Notebook.prDetails(SmallNotebook)
    Notebook.prDetails(NormalNotebook)
    Notebook.prDetails(BigNotebook)
    Pen.prDetails(BluePen)
    Pen.prDetails(RedPen)
    Pen.prDetails(BlackPen)

    





    

    
