class Tools:
    def __init__ (self, matrix = None):
        self.matrix = matrix if matrix is not None else []

    @property
    def shape(self):
        """Return the shape of a list (row and column)"""
        return len(self.matrix), len(self.matrix[0])

    @property
    def T(self):
        """Return the transpose of the data."""
        r, c = self.shape
        transpose = [[0.0] * r for _ in range (c)]
        for i in range (c):
            for j in range(r):
                transpose[i][j] = self.matrix[j][i]
        return transpose
    
    def dot(self, matrix1, matrix2):
        """Column of matrix 1 should be match Row of matListArrayFunctionrix 2"""
        r1, c1 = len(matrix1), len(matrix1[0])
        r2, c2 = len(matrix2), len(matrix2[0])
        if c1 != r2:
            raise ValueError("Column of matrix 1 should be match Row of matrix 2")
        
        new_matrix = [[0.0] * c2 for _ in range(r1)]
        for i in range(r1):
            for j in range(c2):
                cell_sum = 0
                for k in range(c1):
                    cell_sum += matrix1[i][k] * matrix2[k][j]
                new_matrix[i][j] = cell_sum
        return new_matrix
    
    def det(self):
        """Returns determinant."""
        n, _ = self.shape
        if n == 1:
            return self.matrix[0][0]
        if n == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]

        result = 0
        for col in range(n):
            minor = [
                [self.matrix[row][c] for c in range(n) if c != col]
                for row in range(1, n)
            ]
            sign = (-1) ** col
            result += sign * self.matrix[0][col] * Tools(minor).det() # recursive

        return result
    
    def qr_decomposition(self):
        n, _ = self.shape
        V = self.matrix
        R = [[1 if i == j else 0 for j in range(n)] for i in range (n)] # identify matrix
        Q = [[0] * n for _ in range(n)] # zeros matrix
        for i in range(n):
            

            
    def svd(self):
        U = self.dot(matrix1=self.matrix, matrix2=self.T)
        Vt = self.dot(matrix1=self.T, matrix2=self.matrix)
        S = 
        return U, S, Vt