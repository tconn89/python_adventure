import datetime as Date
import webbrowser

time = Date.datetime.today().strftime('%Y-%m-%d')
print(time)

class MultipleChoice:
  def listChoices(self):
    print('a, b, c, d')
  def listAs():
    print('Class a, b, c, d')

choice = MultipleChoice()
choice.listChoices()
MultipleChoice.listAs()


#name = input('What is your name?\n$ ')
#print(name)
url = 'http://tyconnors.com'
webbrowser.open(url, 0)
url = input('What website do you like?\n$ ')
webbrowser.open(url, 0)

