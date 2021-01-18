#!/usr/bin/python3
"""
Matrix Multiplication Module
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices."""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for value in m_a:
        if type(value) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(value) == 0:
            raise ValueError("m_a can't be empty")
        for x in value:
            if type(x) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
        if len(value) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        ma_cols = len(value)
    ma_rows = len(m_a)
    for value in m_b:
        if type(value) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(value) == 0:
            raise ValueError("m_b can't be empty")
        for x in value:
            if type(x) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
        if len(value) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        mb_cols = len(value)
    mb_rows = len(m_b)
    if ma_cols != mb_rows:
        raise ValueError("m_a and m_b can't be multiplied")
    m_c = [[0 for i in range(mb_cols)] for j in range(ma_rows)]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                m_c[i][j] += m_a[i][k] * m_b[k][j]
    return m_c
