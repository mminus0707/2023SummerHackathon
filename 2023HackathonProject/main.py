from periodic_Array import *

global periodic_Table
global generated

periodic_Table = []
generated = []


class Element:

  #Constructor
  def __init__(self, name, atomic_Number, group, period, fullName, neutron,
               electronegativity):
    self.myName = name
    self.myAtomicNumber = atomic_Number
    self.myGroup = group
    self.myPeriod = period
    self.myFull = fullName
    self.myNeutron = neutron
    self.myEN = electronegativity

    #Generates an array that has the electronic configuration
    config = []
    orbitals = [2, 2, 6, 2, 6, 10]
    for x in orbitals:
      if (atomic_Number - x) >= 0:
        config.append(x)
      elif ((atomic_Number - x) < 0) and (atomic_Number > 0):
        config.append(atomic_Number)
      else:
        config.append(0)
      atomic_Number -= x

    self.myConfig = config

    #Calculates the oxidation number based on the group
    if self.myGroup < 5:
      self.myOxidation = self.myGroup
    else:
      self.myOxidation = self.myGroup - 8

  #Getters
  def getName(self):
    return self.myName

  def getAtomicNuber(self):
    return self.myAtomicNumber

  def getGroup(self):
    return self.myGroup

  def getPeriod(self):
    return self.myPeriod

  def getConfig(self):
    return self.myConfig

  def getOxidationNumber(self):
    return self.myOxidation

  def getFullName(self):
    return self.myFull

  def getNeutron(self):
    return self.myNeutron

  def getEN(self):
    return self.myEN

  #Gives information about the element
  def returnInfo(self):
    return ("INFORMATION \n" +
            "--------------------------------------------- \n" + "Element: " +
            self.myName + "\n" + "Atomic Number: " + str(self.myAtomicNumber) +
            "\n" + "Group: " + str(self.myGroup) + "\n" + "Period: " +
            str(self.myPeriod) + "\n" + "Electron Configuration: " +
            str(self.myConfig) + "\n" + "Oxidation Number: " +
            str(self.myOxidation) + "\n" + "Full Name: " + str(self.myFull) +
            "\n" + "Neutron Number: " + str(self.myNeutron) + "\n" +
            "Electronegativity: " + str(self.myEN) + "\n"
            "---------------------------------------------")


class Compound:

  def __init__(self, elements):
    self.myElements = elements

    tot = 0
    for i in self.myElements:
      tot += i.getOxidationNumber()

    if tot != 0:
      newMol = Molecule(self.myElements, tot)
      generated.append(newMol)
    else:
      generated.append(self)

  def getElements(self):
    return self.myElements

  def getOxidationNumber(self):
    return 0


  def getName(self):

    string = ""
    elems = []
    test = self.myElements
    smallest = self.myElements[0]
    #Sort the elements by their elctronegativities for the correct naming
    while len(test) > 1:
      for i in range(1,len(test)):
        if test[i].getEN() < smallest.getEN():
          smallest = test[i]
      elems.append(smallest)
      test.remove(smallest)
      
    elems.append(test[0])
    test.pop(0)  
    

    for j in elems:
      string += j.getName()
      
    return string

   


class Molecule(Compound):

  def __init__(self, elements, charge):
    self.myElements = elements
    self.myCharge = charge

  def getElements(self):
    return self.myElements

  def getOxidationNumber(self):
    return self.myCharge

  def check(elements):
    tot = 0
    for i in elements:
      tot += i.getOxidationNumber()

    return tot

  def getEN(self):
    test = self.myElements
    tot = 0
    largest = self.myElements[0]

    for i in test:
      if i.getEN() > largest.getEN():
        largest = i

    test.remove(largest)
    tot += largest.getEN()
    
    for i in test:
      if i.getEN() == largest.getEN():
        tot += i.getEN()
        test.remove(i)

    for i in test:
      tot -= i.getEN()

    return tot


  def getName(self):
    string = ""
    elems = []
    test = self.myElements

    smallest = self.myElements[0]
    #Sort the elements by their elctronegativities for the correct naming
    while len(test) != 1:
      for i in range(1,len(test)):
        if test[i].getEN() < smallest.getEN():
          smallest = test[i]
      elems.append(smallest)
      test.remove(smallest)
      
    elems.append(test[0])
    test.pop(0)
    
    for i in elems:
      if i.getName() not in test:
        test.append(i.getName())
        test.append(1)
      else:
        for k in range(0,len(test)):
          if test[k] == i.getName():
            test[k+1] += 1

    for j in test:
      if j != 1:
        string += str(j)

    string = string[::-1]
    
    return string

def reaction(reactants):
  return Null

#Generate the table
for x in periodic_Array:
  periodic_Table.append(Element(x[0], x[1], x[2], x[3], x[4], x[5], x[6]))

#Testing


newc = Compound([periodic_Table[7], periodic_Table[0]])

for i in generated[0].getElements():
  print(i.returnInfo())
comp = Compound([generated[0],periodic_Table[10]])

print(generated[0].getName())

test = Compound([periodic_Table[16], periodic_Table[0]])
print("#############################################")
for i in generated[2].getElements():
  print(i.returnInfo())
print(generated[2].getName())