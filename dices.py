from random import randint
import pandas as pd
dice1 = []
dice2 = []
nr_dices = 100000
for i in range(nr_dices):
  throw1 = randint(1,6)
  throw2 = randint(1,6)
  dice1.append(throw1)
  dice2.append(throw2)

summed = []
for i in range(len(dice1)):
  s = dice1[i] + dice2[i]
  summed.append(s)

counts = {}
for c in range(2, 13):
  counts[c] = 0

for s in summed:
  counts[s] = counts[s] + 1


data = []
for c in counts:
  data.append({
      'value': c,
      'counts' : int(counts[c]),
      'percentage': round(
          counts[c] / nr_dices * 100,
          2
      )
  })

df = pd.DataFrame(data).set_index('value').astype(int)
df.transpose().to_csv('assets/dices.csv')
