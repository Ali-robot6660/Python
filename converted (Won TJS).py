money = input("Won to TJS write 'won' or TJS to Won write 'tjs': " ) #просто переменный отвечает за тип валюты

if money == 'won'or money == 'Won' or money == 'WON': #условие для перевода из вон в сомони
    Won = float(input("Enter Won amount: "))
    TJS = 0.0068
    convert = Won * TJS
    print(Won, "won is to tajik somoni", convert)
elif money == 'tjs' or money == 'TJS' or money == 'Tjs': #условие для перевода из сомони в вон
    TJS = float(input("Enter TJS somoni: "))
    Won = 145
    convert = TJS * Won
    print(TJS, "tajik somoni is to won", convert)
else:
    print("please write 'won' or 'tjs'")