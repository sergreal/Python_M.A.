
# ******************** 1 ********************

class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0, 0],
                [0, 0, 0, 0]]

        for i in range(len(self.list_1)):
            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

my_matrix = Matrix([[7, 77, 37, 11],
                    [4, 15, 12, 3]],
                   [[23, 8, 30, 4],
                    [91, 45, 9, 94]])

print(my_matrix.__add__())

# ******************** 2 ********************

class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def get_square_c(self):
        return self.v / 6.5 + 0.5

    def get_square_j(self):
        return self.h * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Суммарный расход ткани: {round((self.v / 6.5 + 0.5) + (self.h * 2 + 0.3))}')

class Coat(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_c = round((self.v / 6.5 + 0.5), 2)

    def __str__(self):
        return f'Расход ткани на пальто: {self.square_c}'

class Jacket(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_j = round((self.h * 2 + 0.3), 2)

    def __str__(self):
        return f'Расход ткани на костюм: {self.square_j}'

coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
