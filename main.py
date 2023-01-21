import random


def ran():
  randomN = random.randint(0,90)
  return randomN

numbers = []

for i in range(8):
  numbers.append(ran())

numbers.sort()

my2DList = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]

print("Bingo Card Generator")
print()
print(my2DList[0][0], "|", my2DList[0][1], "|", my2DList[0][2])
print("---------------")
print(my2DList[1][0], "|", my2DList[1][1], "|", my2DList[1][2])
print("---------------")
print(my2DList[2][0], "|", my2DList[2][1], "|", my2DList[2][2])
