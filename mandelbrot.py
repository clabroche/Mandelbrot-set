
"""
Suite de MandelBrot: 
Z0 = U
Zn+1 = (Zn)² + c
"""
import matplotlib.pyplot as plt
import random
import matplotlib.colors as colors


"""
test if complex number c is in the range from mandelbrot
"""
def suiteM(c):
    max_iterations = 200 # define how many test for c
    i = 0 # variable to increment in while loop
    zn = i # init equation to zero
    while i<max_iterations: # while we cannot reach the max iteration
        i+=1 # increment indice of the loop
        zn = (zn * zn) + c # save the result of the equation
        if abs(zn)>2: # if the result is not under 2, complex number is not in the mandelbrot range and return false to break the function
            return False
    return True # if the function is not breaking, complex number is in the range 


"""
Return an array containing n coordinate from xmin to xmax and ymin to ymax
"""
def rectangle(xmin, xmax,  ymin, ymax, n):
    # Init variable to their min value
    x = xmin
    y = ymin
    # Calculate interval we must iterate to have correct number of points
    xInterval = (xmax - xmin) / (n -1)
    yInterval = (ymax - ymin) / (n -1)
    # prepare array in the right scope
    listOfPoints = []
    while x <= xmax: # iterate over x
        while y<=ymax: # iterate over y
            listOfPoints.append((x,y)) # save coordinate in a tuple that we append to the list
            y+=yInterval # increment y axis to get the next coordinate 
        y = ymin  # reinit y axis to loop on the next x axis
        x += xInterval  # increment x axis to get the next coordinate
    return listOfPoints # return the list
    

"""
coords is a list of coords (from rectangle function for instance) 
and return only matching points with the suiteM function (Mandelbrot test) 
"""
def creerListMandelbrot(coords):
    xMandelBrot = [] # array representing x axis of all points in the mandelbrot range
    yMandelBrot = [] # array representing y axis of all points in the mandelbrot range
    for coord in coords: # iterate over each points
        x = coord[0] # get x value from point
        y = coord[1] # get y value from point
        if suiteM(complex(x, y)) == True: # test if complex number (x+yj) is in mandelbrot range
            # save all matching point
            xMandelBrot.append(x) 
            yMandelBrot.append(y)
    return (xMandelBrot,yMandelBrot) # return x axis and y axis on a tuple

"""
Same function that suiteM but return how many iteration we make
"""
def suiteFract1(c, nmax):
    i = 0
    zn = i
    while i < nmax: # iterate since nmax is reach
        zn = (zn * zn) + c
        if abs(zn) > 2: 
            return i  # return number of iteration and break the function
        i += 1
        # return False
    return i # return number of iteration if function is not previously breaking

"""
Return a list of n list containing points that unmatch in nbIteration
"""
def creerListMandelbrotCoul(coords, n):
    list = [] # instance of a list
    i=0
    while i<n: # add empties list to prepare all possibility of iterations
        list.append([])
        i+=1
    for coord in coords: # iterate over coordinate to dispatch them in their list
        x = coord[0]
        y = coord[1]
        nbIteration = suiteFract1(complex(x, y), n) # get the number of iterations to unmatch with mandelbrot
        list[nbIteration - 1].append(coord) # save in nbIteration list 
    return list


def Q4():
    print('Question 4:')
    # prepare the user interface
    plt.figure(figsize=(10, 10), dpi=96)
    plt.axis("equal")

    # Get all corrdinate to represent in the UI
    print("     get all points...")
    allPoints = rectangle(-1.5, 0.5, -1, 1, 700)
    # Get all corrdinate that match with mandelbrot
    print("     create mandelbrot list... (can take a while)")
    listMandelbrot = creerListMandelbrot(allPoints)
    x = listMandelbrot[0] # get x axis from points 
    y = listMandelbrot[1] # get y axis from points
    plt.plot(x, y, ',') # send x axis and y axis to UI and say it to use one pixel per points
    plt.show() # show UI


def Q5():
    print('Question 5:')
    # prepare the user interface
    plt.figure(figsize=(10, 10), dpi=96)
    plt.axis("equal")

    # number of points in each axis
    n = 400

    # get all points between [-1.4, -0.6] x [-0.4,0.4]
    print("     get all points for graph1...")
    allPoints1 = rectangle(-1.4, -0.6, -0.4, 0.4, n)
    print("     get all points for graph2...")    
    allPoints2 = rectangle(-1.4, -1.2, -0.1, 0.1, n)
    print("     get all points for graph3...")    
    allPoints3 = rectangle(-1.4, -1.35, -0.025, 0.025, n)
    # get all points that match in mandelbrot
    print("     create mandelbrot list for graph1... (can take a while)")
    listMandelbrot1 = creerListMandelbrot(allPoints1)
    print("     create mandelbrot list for graph2... (can take a while)")
    listMandelbrot2 = creerListMandelbrot(allPoints2)
    print("     create mandelbrot list for graph3... (can take a while)")
    listMandelbrot3 = creerListMandelbrot(allPoints3)

    # get all axis
    x1 = listMandelbrot1[0]
    y1 = listMandelbrot1[1]
    x2 = listMandelbrot2[0]
    y2 = listMandelbrot2[1]
    x3 = listMandelbrot3[0]
    y3 = listMandelbrot3[1]

    # split view 
    plt.subplot(221)
    # send graph1
    plt.plot(x1, y1, ',')
    # split view     
    plt.subplot(222)
    # send graph2    
    plt.plot(x2, y2, ',')
    # split view     
    plt.subplot(224)
    # send graph3  
    plt.plot(x3, y3, ',')
    # show UI
    plt.show()


"""
default number of points to put in graph on each axis: 1000
default number of list to dispatch points: 80
"""
def Q6(n=1000, lengthOfList=80):
    print('Question 6:')
    # prepare the user interface
    plt.figure(figsize=(10, 10), dpi=96)
    plt.axis("equal")

    print("     get all points...")
    allPoints = rectangle(-1.5, 0.5, -1, 1, 1000) # ...
    print("     create mandelbrot lists... (can take a while)")
    listMandelbrot = creerListMandelbrotCoul(allPoints, lengthOfList)  # get all points of mandelbrot dispatched by iteration
    listPure = listMandelbrot.pop() # get all matching points with mandelbrot and remove them to the listMandelbrot

    for list1 in listMandelbrot: # iterate over the unmatching mandelbrot list
        x = []
        y = []
        for point in list1: # dispatch all points by x axis and y axis
            x.append(point[0])
            y.append(point[1])
        plt.plot(x, y, ',',color=(0, random.uniform(0, 1), random.uniform(0, 1))) # send each list with random color between blue and green
    
    pureX = []
    pureY = []
    for x, y in listPure:  # dispatch all points by x axis and y axis
        pureX.append(x)
        pureY.append(y)
    plt.plot(pureX, pureY, ',', color=(0,0,1)) # send points to UI with pure blue color
    plt.show() # show UI
        

# call all exercise result one by one
Q4()
Q5()
Q6()
