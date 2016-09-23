# Created by: Matthew Lourenco
# Created on: 23 Sept 2016
# This program is a program that calculates the price of a pizza

import ui

HST = 1.13
LABOUR = 0.75
RENT = 1.00

def calculate_touch_up_inside(sender):
    #calculate price baised on diameter
    
    #input
    diameter = float(view['diameter_textfield'].text)
    
    #process
    pizza_price = (LABOUR + RENT + 0.50 * float(diameter)) * HST
    
    #output
    view['pizza_price_label'].text = 'the price is: $' + str(round(pizza_price, 2))

view = ui.load_view()
view.present('full_screen')
