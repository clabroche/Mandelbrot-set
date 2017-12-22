
import matplotlib.pyplot as plt
import random
import matplotlib.colors as colors


"""
test if complex number c is in the range from Julia
"""

def suiteJ(c, z):
    max_iterations = 200  # define how many test for c
    i = 0  # variable to increment in while loop
    zn = z  # init equation to a complex number in argument
    while i < max_iterations:  # while we cannot reach the max iteration
        i += 1  # increment indice of the loop
        zn = (zn * zn) + c  # save the result of the equation
        if abs(zn) > 2:  # if the result is not under 2, complex number is not in the julia range and return false to break the function
            return False
    return True  # if the function is not breaking, complex number is in the range


"""
Return an array containing n coordinate from xmin to xmax and ymin to ymax
"""

def rectangle(xmin, xmax,  ymin, ymax, n):
    # Init variable to their min value
    x = xmin
    y = ymin
    # Calculate interval we must iterate to have correct number of points
    xInterval = (xmax - xmin) / (n - 1)
    yInterval = (ymax - ymin) / (n - 1)
    # prepare array in the right scope
    listOfPoints = []
    while x <= xmax:  # iterate over x
        while y <= ymax:  # iterate over y
            # save coordinate in a tuple that we append to the list
            listOfPoints.append((x, y))
            y += yInterval  # increment y axis to get the next coordinate
        y = ymin  # reinit y axis to loop on the next x axis
        x += xInterval  # increment x axis to get the next coordinate
    return listOfPoints  # return the list


def creerListJulia(coords, c):
    xJulia = []  # array representing x axis of all points in the julia range
    yJulia = []  # array representing y axis of all points in the julia range
    for coord in coords:  # iterate over each points
        x = coord[0]  # get x value from point
        y = coord[1]  # get y value from point
        if suiteJ(c, complex(x, y)) == True:  # test if complex number (x+yj) is in julia range
            # save all matching point
            xJulia.append(x)
            yJulia.append(y)
    return (xJulia, yJulia)  # return x axis and y axis on a tuple


def Q3():
    print('Question 3:')
    # prepare the user interface
    plt.figure(figsize=(10, 10), dpi=96)
    plt.axis("equal")

    # Get all corrdinate to represent in the UI
    print("     get all points...")
    allPoints = rectangle(-1.5, 0.5, -1, 1, 800)
    # Get all corrdinate that match with julia
    complexToDraw = [0.3 + 0.5j, 0.285 + 0.013j]
    for c in complexToDraw:
        print("     create Julia list for",c,"... (can take a while)")
        listJulia = creerListJulia(allPoints, c)
        x = listJulia[0]  # get x axis from points
        y = listJulia[1]  # get y axis from points
        # send x axis and y axis to UI and say it to use one pixel per points
        plt.plot(x, y, ',')
        plt.show()  # show UI


Q3()
