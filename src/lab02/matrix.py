# def transpose(mat: list[list[float | int]]) -> list[list]:
#     if not mat:
#         return []
#     row_len = len(mat[0])
#     for row in mat:
#         if len(row) != row_len:
#             raise ValueError
#     return [[mat[r][c] for r in range(len(mat))] for c in range(row_len)]
# print(transpose([[1, 2, 3]]))
# print(transpose([[1], [2], [3]]))
# print(transpose([[1, 2], [3, 4]]))
# print(transpose([]))
# print(transpose([[1, 2], [3]]))


# def row_sums(mat: list[list[float | int]]) -> list[float]:
#     if not mat:
#         return []
#     row_len = len(mat[0])
#     for row in mat:
#         if len(row) != row_len:
#             raise ValueError
#     return [sum(row) for row in mat]
# print(row_sums([[1, 2, 3], [4, 5, 6]]))
# print(row_sums([[-1, 1], [10, -10]]))
# print(row_sums([[0, 0], [0, 0]]))
# print(row_sums([[1, 2], [3]]))


# def col_sums(mat: list[list[float | int]]) -> list[float]:
#     if not mat:
#         return []
#     row_len = len(mat[0])
#     for row in mat:
#         if len(row) != row_len:
#             raise ValueError
#     return [sum(row[c] for row in mat) for c in range(row_len)]
# print(col_sums([[1, 2, 3], [4, 5, 6]]))
# print(col_sums([[-1, 1], [10, -10]]))
# print(col_sums([[0, 0], [0, 0]]))
# print(col_sums([[1, 2], [3]]))








# def transpose(mat: list[list[float | int]]) -> list[list]:
#     if not mat:
#         raise ValueError
#     return (transpose(mat))

# def row_sums(mat: list[list[float | int]]) -> list[float]:
#     return(row_sums)

# def col_sums(mat: list[list[float | int]]) -> list[float]:
    