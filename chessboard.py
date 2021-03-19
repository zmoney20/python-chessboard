class Chessboard:
    def __init__(self, tr, startX, startY, width=250, height=250):
        self.__tr = tr
        self.__startX = startX
        self.__startY = startY
        self.__width = width
        self.__height = height

    def __getTurtle(self):
        return self.__tr

    def __getStartX(self):
        return self.__startX

    def __getStartY(self):
        return self.__startY

    def __getWidth(self):
        return self.__width

    def __getHeight(self):
        return self.__height

    def draw(self):
        self.__getTurtle()
        self.__getStartX()
        self.__getStartY()
        self.__getWidth()
        self.__getHeight()
        self.__tr.up()
        self.__tr.speed(15)
        self.__tr.showturtle()
        self.__tr.goto(self.__startX, self.__startY)
        # outside box is red
        self.__tr.color("red")
        self.__tr.down()
        self.__tr.seth(0)
        self.__tr.forward(self.__width)
        self.__tr.left(90)
        self.__tr.forward(self.__height)
        self.__tr.left(90)
        self.__tr.forward(self.__width)
        self.__tr.left(90)
        self.__tr.forward(self.__height)
        self.__tr.color("black")
        self.__tr.seth(0)
        # call upon another method to draw every single rectangle
        self.__drawAllRectangles()
        self.__tr.hideturtle()

    # this method will draw every square/rectangle
    # uses another method which draws the square and moves it to the next position and loops it

    def __drawAllRectangles(self):
        self.__getTurtle()
        self.__getStartX()
        self.__getStartY()
        self.__getWidth()
        self.__getHeight()
        row1 = 0
        row2 = 0
        while row1 < 3:
            loop1 = 0
            while loop1 < 4:
                # this method is in charge of drawing the little square
                self.__drawRectangle()
                loop1 += 1
            row1 += 1
            self.__tr.up()
            self.__tr.seth(0)
            self.__tr.goto(self.__startX, self.__startY + ((self.__height / 4) * row1))
        while row2 < 5:
            loop2 = 0
            while loop2 < 4:
                self.__drawRectangle()
                loop2 += 1
            row2 += 1
            self.__tr.goto(self.__startX + (self.__width / 8), (self.__startY + ((self.__height / 8) * row2) * 2) -
                           (self.__height / 8))

    # this method draws and fills the rectangle

    def __drawRectangle(self):
        self.__getTurtle()
        self.__getWidth()
        self.__getHeight()
        self.__tr.seth(0)
        self.__width1 = self.__width / 8
        self.__height1 = self.__height / 8
        self.__tr.fillcolor("black")
        self.__tr.begin_fill()
        self.__tr.forward(self.__width1)
        self.__tr.left(90)
        self.__tr.forward(self.__height1)
        self.__tr.left(90)
        self.__tr.forward(self.__width1)
        self.__tr.left(90)
        self.__tr.forward(self.__height1)
        self.__tr.end_fill()
        self.__tr.seth(0)
        self.__tr.up()
        self.__tr.forward(self.__width1 * 2)
