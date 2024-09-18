#Phoenix Valent
  #U1L1
    #Disregard ethics in favor of big rat

import time
import random
from os import system as screen
from rat_eugenics import Rat

GOAL = 50000
NUM_RATS = 20
INITIAL_MIN_WT = 200
INITIAL_MAX_WT = 600
INITIAL_MODE_WT = 300
MUTATE_ODDS = .01
MUTATE_MIN = .5
MUTATE_MAX = 1.2
LITTER_SIZE = 8
GENERATIONS_PER_YEAR = 10
GENERATION_LIMIT = 500

def print_results(mean, generations, years, seconds, meanList, chonkList):
  print(("<>"*10+"RESULTS"+"<>"*10).center(40))
  print(f"Final Population Mean: {mean}g\n\nGenerations: {generations} generations\nExperiment Duration: {years} years\nSimulation Duration: {seconds} seconds\n")
  print(f"🐀 Fattest rat🐀\n🤨 Sex: {chonkList[-1].sex}🤨\n🏛 Weight: {chonkList[-1].getWeight()}g🏛\n")
  print(("<>"*5+"Weight Averages (in grams)"+"<>"*5).center(40))
  for i in range(len(meanList)):
    print(f"{meanList[i]}".ljust(6), end=" ")
    if (i+1) % 15 == 0:
      print()
  print()

def calculate_mean(rats, meanList):
  mean = 0
  for i in rats:
    for j in i:
      mean+=j.getWeight()
  meanList.append(mean//NUM_RATS)
  return mean // NUM_RATS

def fitness(rats, list):
  mean = calculate_mean(rats, list)
  list.append(mean)
  return mean

def select(rats, chonkHallOfFame):
  rats2 = [[], []]
  for i in rats:
    for j in i:
      if j.canBreed:
        if j.sex == "M":
          rats2[0].append(j)
        else:
          rats2[1].append(j)
  masterRace = []
  mList = rats2[0]
  fList = rats2[1]
  mList.sort(reverse=True)
  fList.sort(reverse=True)
  masterRace.append(mList[:10])
  masterRace.append(fList[:10])
  if mList[0] > fList[0]:
    chonk = masterRace[0][0]
  else:
    chonk = masterRace[1][0]
  chonkHallOfFame.append(chonk)
  return masterRace, chonkHallOfFame

def breed(rats):
  random.shuffle(rats[0])
  random.shuffle(rats[1])
  for x in range(len(rats[0])):
    male = rats[0][x]
    female = rats[1][x]
    for i in range(LITTER_SIZE):
      sex = random.choice(["M", "F"]) #ayo???
      child = (Rat(sex, calculate_weight(sex, male, female)))
      mutate(child)
      if child.sex == "M":
        rats[0].append(child)
      else:
        rats[1].append(child)
  return [rats[0], rats[1]]

def mutate(pup):
  scale = random.uniform(MUTATE_MIN, MUTATE_MAX)
  pup.mutate(scale, MUTATE_ODDS)
  return pup

def calculate_weight(sex, mother, father):
  #generate the weight of a single rat
  minWt = mother.getWeight()
  maxWt = father.getWeight()
  #use the triangular function from the random library to skew the baby's weight based on its sex
  if sex == "M":
    wt = int(random.triangular(minWt, maxWt, maxWt))
  else:
    wt = int(random.triangular(minWt, maxWt, minWt))

  return wt

def initial_population():
  #Create the initial set of rats based on constants
  rats = [[], []]
  mother = Rat("F", INITIAL_MIN_WT)
  father = Rat("M", INITIAL_MAX_WT)

  for r in range(NUM_RATS):
    if r < 10:
      sex = "M"
      ind = 0
    else:
      sex = "F"
      ind = 1

    wt = calculate_weight(sex, mother, father)
    R = Rat(sex, wt)
    rats[ind].append(R)

  return rats

def main():
  meanList = []
  chonkHallOfFame = []
  startTime = time.time()
  print("Hey this seems a little unethical") #absolutely essential, the code will literally explode if this print statement isn't here
  screen("clear")
  potentialMean = 0
  generations = 0
  rats = initial_population()
  while potentialMean < GOAL and generations < GENERATION_LIMIT:
    children = breed(rats)
    rats, chonkHallOfFame = select(children, chonkHallOfFame)
    potentialMean = fitness(rats, meanList)
    generations+=1
  endTime = time.time()
  finishTime = round(endTime-startTime, 5)
  print_results(potentialMean, generations, generations/10, finishTime, meanList, chonkHallOfFame)

if __name__ == "__main__":
  main()