import random
class Rat:
  def __init__(self, sex, weight):
    self.sex = sex
    self.weight = round(weight)
    self.litters = 0  

  def __str__(self):
    return f"{self.weight}"

  def __repr__(self):
    return f"{self.weight}"

  def __lt__(self, other):
    return self.weight < other.weight

  def __gt__(self, other):
    return self.weight > other.weight

  def __le__(self, other):
    return self.weight <= other.weight

  def __ge__(self, other):
    return self.weight >= other.weight

  def __eq__(self, other):
    return self.weight == other.weight

  def getWeight(self):
    return self.weight
  
  def getSex(self):
    return self.sex

  def canBreed(self):
    if self.litters <= 5:
      canIt = True
    else:
      canIt = False
    return canIt

  def mutate(self, scale, chance):
    mutateChance = random.random()
    if mutateChance <= chance:
      self.weight*=scale
      self.weight = round(self.weight)