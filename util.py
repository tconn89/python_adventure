import datetime as Date
import webbrowser

months = ['', 'January', 'Febuary', 'March', 'April',
          'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']
greeting = {}

time = Date.datetime.today().strftime('%Y-%m-%d')
print(months[Date.datetime.today().month])
greeting['month'] = months[Date.datetime.today().month]
greeting['day'] = Date.datetime.today().day
if(greeting['day'] % 10 == 1):
  greeting['suffix'] = 'st'
elif(greeting['day'] % 10 == 2):
  greeting['suffix'] = 'nd'
elif(greeting['day'] % 10 == 3):
  greeting['suffix'] = 'rd'
else:
  greeting['suffix'] = 'th'
  
print(f"The day is {greeting['month']} {greeting['day']}{greeting['suffix']}")

class Adventurer:
  def setName(self, name):  
    self.name = name

  def setBelief(self, belief):
    if(belief == 'democrap'):
      self.isDemo = true
      self.isRepub = false
    else:
      self.isDemo = false
      self.isRepub = true
  
  def setKnowledge(self, knowedge):
    self.knowledge = knowledge

  def setIniative(self, iniatiative):
    self.iniative = iniatiative
  def setAthleticism(self, athlete):
    self.athlete = athlete

class Questions:
  def askName():
    return input('What is the name of your player?\n$ ')
  def askRide():
    return input('How will you get to the voting booth?\n$ ')

# url = 'http://tyconnors.com'
# webbrowser.open(url, 0)
# url = input('What website do you like?\n$ ')
# webbrowser.open(url, 0)
