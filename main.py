import os
from time import sleep

progress = 0
while progress != 100:
  progress += 10
  for x in range(int(progress/10)):
    print("█", end="")
  print(progress, "%")
  sleep(0.5)
  os.system("clear")
else:
  print("Ielāde pabeigta!")