class Tools:
    def __init__ (self, matrix = None, iter = 1000):
        self.matrix = matrix if matrix is not None else []
        self.iter = iter

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
    
    def norm(self, l):
        sumL = 0
        for i in l:
            sumL += abs(i) ** 2
        return sumL ** (1/2)
    
    def qr_decomposition(self):
        n, _ = self.shape
        V = [row[:] for row in self.T]
        R = [[1.0 if i == j else 0.0 for j in range(n)] for i in range (n)] # identify matrix
        Q = [[0.0] * n for _ in range(n)] # zeros matrix
        for i in range(n):
            V_norm = self.norm(V[i])
            Q[i] = [V[i][k] / V_norm for k in range (n)]
            R[i][i] *= self.norm(V[i])
            for j in range (i+1, n):
                R[i][j] += sum(Q[i][k] * V[j][k] for k in range(n))
                V[j] = [V[j][k] - R[i][j] * Q[i][k] for k in range(n)]
        return Tools(Q).T, R

    def qr_algorithm(self):
        n, _ = self.shape
        X = [row[:] for row in self.matrix]
        eigvecs = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

        for _ in range(self.iter):
            Q, R = Tools(X).qr_decomposition()
            X_new = self.dot(R, Q)
            eigvecs = self.dot(eigvecs, Q)

            # check if off-diagonal is close enough to zero
            diff = sum(X_new[i][j]**2 for i in range(n) for j in range(n) if i != j)
            if diff < 1e-10:
                break

            X = X_new

        return [X[i][i] for i in range(n)], eigvecs
    
    def eig(self):
        """Returns eigenvalues and eigenvectors."""
        n, _ = self.shape
        X = [row[:] for row in self.matrix]
        # start eigenvectors as identity
        eigvecs = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

        for _ in range(self.iter):
            Q, R = Tools(X).qr_decomposition()
            X = self.dot(R, Q)
            eigvecs = self.dot(eigvecs, Q)  # accumulate Q

        eigenvalues = [X[i][i] for i in range(n)]
        return eigenvalues, eigvecs
    
    def svd(self):
        n, _ = self.shape
        # A^T * A and A * A^T
        ATA = self.dot(self.T, self.matrix)
        AAT = self.dot(self.matrix, self.T)

        # eigenvalues/vectors
        eigenvalues, V = Tools(ATA).eig()
        _, U = Tools(AAT).eig()

        # singular values = sqrt of eigenvalues
        S = [e ** 0.5 for e in eigenvalues]

        return U, S, V

# if __name__ == "__main__":  
#     t = Tools([[4, 1], [2, 3]])
#     print(t.qr_algorithm())  # [5.0, 2.0]