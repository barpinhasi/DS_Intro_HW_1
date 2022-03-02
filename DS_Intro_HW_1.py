###~~~~~~~~~~~ A ~~~~~~~~~~~###
def  my_func(x1, x2, x3):
    pass
    try:
        if type(x1) != float or type(x2) != float or type(x3) != float:
             return ValueError("Error: parameters should be float")
        value = ((x1 + x2 + x3) * (x2 + x3) * x3) / (x1 + x2 + x3)
        return value
    except ZeroDivisionError:
        return "Not a number – denominator equals zero"  

###~~~~~~~~~~~ B ~~~~~~~~~~~###
def convert(hours, minutes = 0):
    try:
        if hours < 0 or minutes < 0:
            return  "Input error!"
        value = hours * 3600 + minutes * 60
        return value
    except:
        return "Input error!"
