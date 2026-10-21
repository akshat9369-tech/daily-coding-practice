#include <iostream>
#include <vector>

typedef std::vector<std::vector<int>> Matrix;

Matrix multiply_2x2(const Matrix& A, const Matrix& B) {
    Matrix C(2, std::vector<int>(2, 0));
    int m1 = (A[0][0] + A[1][1]) * (B[0][0] + B[1][1]);
    int m2 = (A[1][0] + A[1][1]) * B[0][0];
    int m3 = A[0][0] * (B[0][1] - B[1][1]);
    int m4 = A[1][1] * (B[1][0] - B[0][0]);
    int m5 = (A[0][0] + A[0][1]) * B[1][1];
    int m6 = (A[1][0] - A[0][0]) * (B[0][0] + B[0][1]);
    int m7 = (A[0][1] - A[1][1]) * (B[1][0] + B[1][1]);

    C[0][0] = m1 + m4 - m5 + m7;
    C[0][1] = m3 + m5;
    C[1][0] = m2 + m4;
    C[1][1] = m1 - m2 + m3 + m6;
    return C;
}

int main() {
    Matrix A = {{1, 3}, {7, 5}};
    Matrix B = {{6, 8}, {4, 2}};
    Matrix C = multiply_2x2(A, B);

    std::cout << "Strassen 2x2 Product:" << std::endl;
    for (const auto& row : C) {
        for (int v : row) std::cout << v << " ";
        std::cout << std::endl;
    }
    return 0;
}
