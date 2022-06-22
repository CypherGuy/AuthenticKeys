import random
import sys
import PySimpleGUI as sg  #Library used to load the GUI  

sg.theme('DarkTeal10')

layout = [[sg.Text('Authenticator key generator', size=(30, 2), font=("Helvetica", 25))],
                 [sg.Text('How many keys would you like?')],      
                 [sg.InputText()],      
                 [sg.Text("How many keys should each section have?")],
                 [sg.InputText()],   
                 [sg.Text('Enter a seperator:')],
                 [sg.InputText()],
                 [sg.Radio('Uppercase letters', 'Radio1')],
                 [sg.Radio('Lowercase Leters', 'Radio2')],
                 [sg.Radio('Numbers', 'Radio3')],
                 [sg.Radio('Symbols', 'Radio4')],
                 [sg.Submit(), sg.Cancel()]]    

window = sg.Window('Code Generator', layout, resizable=True)    

event, values = window.read()    
window.close()

times = values[0]    #How many keys they want
parts = values[1]    #Parts to each key. For example, 4356-2046 has 2 parts of 4 numbers.
seperator = values[2]  #A seperator to seperate each set of parts
Upper = values[3] 
Lower = values[4] 
Numbers = values[5]
Symbols = values[6]

def get5(values): #Gets 5 values without a seperator
  keylist = []
  keySep = []
  for _ in range(parts): #Do each part n times
    randomkey(values, keylist)
  for line in keylist:
    keySep.append(line)
  keySep = ''.join(keySep)
  keylist = list([])#Make it empty again so we can repick
  return keySep

def randomkey(values, keylist):#returns a random key
  if values[3] == values[4] == values[5] == values[6] == False:
    print('Error: you must choose at least one of Upper/lowercase or numbers.'),
    sys.exit()
  if values[3] is True:
    upper_letter = chr(random.randint(65,90)) #Pick a random number between 65 and 90
    keylist.append(upper_letter)
  if values[4] is True:
    lower_letter = chr(random.randint(97,122))
    keylist.append(lower_letter)
  if values[5] is True:
    number = str(random.randint(1, 9))
    keylist.append(number)
  if values[6] is True:
    chrSelSym = random.randint(33,64)
    if 48 <= int(chrSelSym) <= 57:
      symbol = chr(chrSelSym)
    else:
      symbol = chr(random.randint(58,64))
    keylist.append(symbol)
  return keylist 

def get5sep(seperator): #Generates a 5-section part with a seperator
  key = get5(values)
  return f'{key}{seperator}'

def makeKey(times, seperator):#Joins all the parts together to make a key
  wholekeys = []
  for _ in range(times):
    key1 = get5sep(seperator)
    key2 = get5sep(seperator)
    key3 = get5(values)
    answerkey = f'{key1}{key2}{key3}'
    wholekeys.append(answerkey)
  return wholekeys

times = int(times)
parts = int(parts)

timecheck = isinstance(times, int)#Is 'times' an integer?
partcheck = isinstance(parts, int)

if partcheck:
  if timecheck:
    sampleAnswer = makeKey(times, seperator)
    finalKeylist = [] #I will put all the keys in here, then split it later on
    for i in range(times):
      i += 1
      firstkey = f'{sampleAnswer[i-1]}\n\n'
      finalKeylist.append(firstkey)
      print(finalKeylist)

    finalKeys = ' '.join([str(v) for v in finalKeylist])
    layout = [[sg.Text('Here are your keys!', size=(30, 2),
     font=("Helvetica", 25))],
                [sg.Text(finalKeys,
                 size=(20, len(finalKeylist)+ 2),
                 justification='left',
                 auto_size_text = True)],
                [sg.Button('Exit')]]
    window = sg.Window('Code Generator', layout, resizable=True)
    event, values = window.read()
    if event in [sg.WIN_CLOSED, 'Quit']:
      window.close()

    window.close()
  else:
    print("The following is wrong: The amount of times is not an integer.")
else:
  print("The following is wrong: The amount of parts you want is not an integer.")

