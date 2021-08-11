def convert_sentence(phase):
    derev = ("How","Why","What")
    cPhase = phase.capitalize()
    if (cPhase.startswith(derev)):
        return ("{} ? ".format(cPhase))
    else:
        return ("{} .".format(cPhase))

results = []

while True:
    uInput = input("Enter something ")
    if (uInput == '/End'):
        break
    else:
        results.append(convert_sentence(uInput))

print(" ".join(results))