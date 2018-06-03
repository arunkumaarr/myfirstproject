def validate(pin):
    if len(pin) == (4,6):
        return True
    else:
        return False

    if pin.isdigit() == True:
        return True
    else:
        return False

x=input('enter pin:')
print(len(x))

print(validate(x))