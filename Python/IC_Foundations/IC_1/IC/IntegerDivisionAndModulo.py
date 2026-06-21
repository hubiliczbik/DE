def fullBoxes(totalItems, boxCapacity):
    return totalItems // boxCapacity

def leftoverCupcakes(totalItems, boxCapacity):
    return totalItems % boxCapacity

def totalBoxesNeeded(totalItems, boxCapacity):
    if leftoverCupcakes(totalItems, boxCapacity) == 0:
        return fullBoxes(totalItems, boxCapacity)
    else:
        return fullBoxes(totalItems, boxCapacity) + 1


tests = [0,11,12,13,25,100]
for n in tests:
    print(f"{n} items: {fullBoxes(n, 12)} full boxes, {leftoverCupcakes(n, 12)} leftover cupcakes, {totalBoxesNeeded(n, 12)} total boxes needed")