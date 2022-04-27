
def scoregrade(p):

    if p < 60 and p >= 0:
        return("D ")
    elif p >= 60 and p < 70:
        return("C ")
    elif p >= 70 and p < 80:
        return("B ")
    elif p >= 80 and p < 90:
        return("A ")
    else:
        return("S ")
