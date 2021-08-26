class Person():
  def __init__(self, attribute, attribute2):
    super().__init__()

class Enemy(Person):
  def __init__(self, attribute, attribute2):
    super().__init__(attribute, attribute2)    