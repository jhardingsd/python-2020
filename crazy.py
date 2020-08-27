def crazy(callback):
    callback('my mind!!!!')


def saySomething(thingToSay):
    print(thingToSay)

crazy(saySomething)
crazy(print)