# Exercise extending list

class SuperList(list):
  def __len__(self):
    return 1000

superlist1 = SuperList()

superlist1.append(6)
superlist1.append(5)
superlist1.append(4)
superlist1.append(9)
superlist1.append(1235)

print(len(superlist1))