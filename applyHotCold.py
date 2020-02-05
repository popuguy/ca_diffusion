import numpy as N

def applyHotCold(bar, hotSites, coldSites):
    newBar = bar
    for i in len(range(hotSites)):
        newBar[hotSites[i][0], hotSites[i][1]] = HOT;
    for i in len(range(coldSites)):
        newBar[coldSites[i][0], coldSites[i][1]] = COLD;
        
    return newBar

