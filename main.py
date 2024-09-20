#Phoenix Valent
  #U1L2
    #Graph the progress of the world domination rats

import matplotlib.pyplot as plt #super clever and original ik
import oldMain as o

def getThatData():
  mean = []
  big = []
  small = []

  mf = open("meanFile.txt", "r")
  m = (mf.read()).split('\n')
  mf.close()
  for i in m:
    mean.append(int(i))

  bf = open("bigFile.txt", "r")
  b = (bf.read()).split('\n')
  bf.close()
  for i in b:
    big.append(int(i))

  sf = open("smallFile.txt", "r")
  s = (sf.read()).split('\n')
  sf.close()
  for i in s:
    small.append(int(i))

  return [mean, big, small]

def straightGraphinIt():
  statz = getThatData()
  for i in statz:
    plt.plot(i)
    plt.title("Number Changes")
    plt.xlabel("Index")
    plt.ylabel("Integer Value")
    plt.legend(["mean", "big", "small"])
    plt.show()
    plt.savefig("ratMasterRaceProject.png")

def main():
  o.ldMain() #see it spells old main bc of the o
  straightGraphinIt()

if __name__ == "__main__":
  main()