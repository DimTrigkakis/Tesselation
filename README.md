# Tesselation

An animated visualization of a 2d matrix transformation.

Example usage: "python tesselation.py 0.01,-5,-2,4" with no spaces between the arguments.

![alt text](https://github.com/DimTrigkakis/Tesselation/blob/master/Before.png)

Every point on the plane has two coordinates. The result, y = Ax, is a vector which is the linear combination

of the columns of A (the amount depends on the components of x).

![alt text](https://github.com/DimTrigkakis/Tesselation/blob/master/middle.png)

During the animation, we can already see the matrix is not invertible, since points in a diagonal all get "squashed" into a line. Thus, it is impossible to recover the original x from a point on this line (there are infinite solutions to Ax = b). For all b not on the final line, there are no x vectors where Ax = b so there are no solutions (b is not in the span of the columns of A).

Finally, we have the clash of all x after the transformation to a line:

![alt text](https://github.com/DimTrigkakis/Tesselation/blob/master/end.png)

