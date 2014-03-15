import copy

class Matrix2D(object):
    """
    This works with 2 dimensional matrixes. It takes a string representation to build it.
    """
    def __init__(self, values):
        """
        Constructor. Import values from a list of lists of integers
        example: [[1,2,3],[4,5,6],[7,8,9]] is a valid matrix
        """
        self.matrix = values
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])

    @classmethod
    def fromstring(cls, valueString):
        """
        Constructor. Import values from string formatted with column
        values separated by spaces and rows deliminated by a ';'.
        example: 1 2 3;4 5 6;7 8 9 or 1 2 3; 4 5 6; 7 8 9 will be
                 evaluated to the following Matrix
                    [[1,2,3]
                     [4,5,6]
                     [7,8,9]]
        """
        strings = valueString.split(';')  # Get matrix rows
        for str in strings:
            str.strip()  # Remove whitespace in each string
        intlist = []
        for str in strings:
            intlist.append([int(i) for i in str.split()])   #   Ensure they're integers
        return cls(intlist)

    def add(self, Matrix):
        """
        Returns a new matrix with the added value of self and Matrix
        """
        if not isinstance(Matrix, Matrix2D):
            raise TypeError("Not a valid type to use with matrix")
        if self.rows != Matrix.rows or self.columns != Matrix.columns:
            raise ValueError("Matrixes are not the same size")
        result = copy.deepcopy(self.matrix)
        for row in range(0, self.rows):
            for column in range(0, self.columns):
                result[row][column] += Matrix.matrix[row][column]

        return Matrix2D(result)

    def subtract(self, Matrix):
        if not isinstance(Matrix, Matrix2D):
            raise TypeError("Not a valid type to use with matrix")
        if self.rows != Matrix.rows or self.columns != Matrix.columns:
            raise ValueError("Matrixes are not the same size")
        result = self.matrix[:]
        for row in range(0, self.rows):
            for column in range(0, self.columns):
                result[row][column] -= Matrix.matrix[row][column]

        return Matrix2D(result)

    def __scalar(self, multiplier):
        new = copy.deepcopy(self.matrix)
        for row in new:
            for entry in row:
                entry *= multiplier
        return Matrix2D(new)

    def multiply(self, Matrix):
        if isinstance(Matrix, int):
            return self.__scalar(Matrix)
        if not isinstance(Matrix, Matrix2D):
            raise TypeError("Not a valid type to use with matrix")
        # Do matrix math stuff
        return None

    def transpose(self):
        """
        Returns a matrix that has been transposed according to matrix math.
        """
        #   Transposition is a reflection upon the main diagonal (0,0 to n,n)
        #   This will work for any NxM matrix
        old = self.matrix[:]
        new = []
        # print(old)
        # print(self.matrix)
        for y in range(0, self.columns):
            new.append([])
            for x in range(0, self.rows):
                new[y].append(old[x][y])
        old = None
        return Matrix2D(new)

    def toString(self):
        string = ""
        for row in self.matrix:
            string = string + "\n" + str(row)
        return string


def main():
    print("Start!")
    matrixs = [Matrix2D.fromstring("1 2"),
               Matrix2D([[1, 2, 3], [4, 5, 6]]),
               Matrix2D.fromstring("1 1 1; 1 1 1"),
               Matrix2D.fromstring("1 2 3;4 5 6;7 8 9"),
               Matrix2D.fromstring("1 2 3; 4 5 6; 7 8 9"),
               Matrix2D.fromstring("1 1 1; 1 1 1; 1 1 1")]
    print(matrixs[0].transpose().toString())
    print(matrixs[1].transpose().toString())
    print(matrixs[3].transpose().toString())
    print(matrixs[1].add(matrixs[2]).toString())
    print(matrixs[4].add(matrixs[5]).toString())
    print(matrixs[1].toString())
    print(matrixs[4].toString())
    print(matrixs[1].subtract(matrixs[2]).toString())
    print(matrixs[4].subtract(matrixs[5]).toString())

    # for matrix in matrixs:
    #     print(matrix.toString())

if __name__ == '__main__':
    main()
