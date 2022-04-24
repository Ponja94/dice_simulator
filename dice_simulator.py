import random
import PySimpleGUI as sg


class DiceSimulator:
    def __init__(self):
        self.random_value = 0
        self.min_value = 1
        self.max_value = 6
        self.name_image = 'img/dice_pattern.png'

    def start(self):
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Image(filename=self.name_image, key='-IMAGE-')],
            [
                [sg.Text('Play the Dice?')],
                [sg.Button('Yes'), sg.Button('No')]
            ]
        ]

        self.window = sg.Window('Game', layout=layout)

        try:
            while True:
                self.event, self.value = self.window.Read()
                if self.event == sg.WIN_CLOSED:
                    print('The game will end')
                    break
                else:
                    if self.event == 'Yes':
                        self.generateDiceValue()
                        self.window['-IMAGE-'].update(filename=self.name_image)
                    elif self.event == 'No':
                        print('Ok, thanks.')
                    else:
                        print('Please enter yes or no')


            print('the window is closing')
            self.window.Close()

        except:
            print('Please enter only numbers')
            self.start()

    def generateDiceValue(self):
        random_value = random.randint(self.min_value, self.max_value)
        if random_value == 1:
            self.name_image = 'img/dice1.png'
        elif random_value == 2:
            self.name_image = 'img/dice2.png'
        elif random_value == 3:
            self.name_image = 'img/dice3.png'
        elif random_value == 4:
            self.name_image = 'img/dice4.png'
        elif random_value == 5:
            self.name_image = 'img/dice5.png'
        elif random_value == 6:
            self.name_image = 'img/dice6.png'
        else:
            print('We have a problem in randomNumberGenerator function')


start_game = DiceSimulator()
start_game.start()
