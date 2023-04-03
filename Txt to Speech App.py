import PySimpleGUI as sg
import pyttsx3 as ptt

layout = [
    [sg.Input(key='TEXT'),sg.Button('Speak',key='Speak Button')],
    [sg.Text('Select Voice Type'),sg.Radio('Male','group 1' ,key= 'Male Voice'),sg.Radio('Female','group 1',key='Female Voice')]
    ]

window = sg.Window('Text To Speech App', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Speak Button' and values['Male Voice'] == True :
       engine = ptt.init()
       text= values['TEXT']
       voices = engine.getProperty('voices')       
       engine.setProperty('voice', voices[0].id)
       engine.say(text)
       engine.runAndWait()
    if event == 'Speak Button' and values['Female Voice'] == True :
       engine = ptt.init()
       text= values['TEXT']
       voices = engine.getProperty('voices')       
       engine.setProperty('voice', voices[1].id)
       engine.say(text)
       engine.runAndWait()
        
   
window.close()
