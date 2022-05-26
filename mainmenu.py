from PySimpleGUI import *
import PySimpleGUI as sg
from main import *
from remainder import *
from squareroot import *

sg.theme('Reddit')

layout = [[Txt('' * 10)],
		[Text('', size = (15, 1), font = ('Arial', 18),
				text_color = 'black', key = 'input')],
		[Txt("Simple Calculator" * 1)],
		[ReadFormButton('Basic Calculator')],
		[ReadFormButton('Square Root')],
		[ReadFormButton('Remainder')],
		[ReadFormButton('Quit')],
		]
form = FlexForm("Simple Calculator", default_button_element_size = (20, 2),
				auto_size_buttons = False, grab_anywhere = False)
form.Layout(layout)
Result = ''






while True:
        button, value = form.Read()
        
        if button == 'Basic Calculator':
            calculate()
        elif button == 'Square Root':
            sqroot()
        elif button == 'Remainder':
            remainder()
        elif button == 'Quit' or button == None:
            break