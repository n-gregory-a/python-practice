import numpy as np

# a8 = np.int8(26)
# a16 = np.int16(26)
# a32 = np.int32(26)
# a64 = np.int64(26)

# print(np.iinfo(a8))
# print(np.iinfo(a16))
# print(np.iinfo(a32))
# print(np.iinfo(a64))
#
# print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')

# x = -456
# y = np.uint8(x)
# print(y)

# arr = np.array([1,5,2,9,10], dtype=np.int8)
# nd_arr = np.array([
#                [12, 45, 78],
#                [34, 56, 13],
#                [12, 98, 76]
#                ], dtype=np.int16)
#
# print(arr.ndim)
# print(nd_arr.ndim)
# print(arr.size)
# print(nd_arr.size)
# print(arr.shape)
# print(nd_arr.shape)
# print(arr.itemsize)
# print(nd_arr.itemsize)
#
# zeros_1d = np.zeros((5,4,3), dtype=np.int16)
# print(zeros_1d)

# lin_arr, step = np.linspace(-6, 21, 60, endpoint=False, retstep=True)
# print(lin_arr, step)

# mystery = np.array([
#        [-13586,  15203,  28445, -27117,  -1781, -17182, -18049],
#        [ 25936, -30968,  -1297,  -4593,   6451,  15790,   7181],
#        [ 13348,  28049,  28655,  -6012,  21762,  25397,   8225],
#        [ 13240,   7994,  32592,  20149,  13754,  11795,   -564],
#        [-21725,  -8681,  30305,  22260, -17918,  12578,  29943],
#        [-16841, -25392, -17278,  11740,   5916,    -47, -32037]],
#       dtype=np.int16)
#
# elem_5_3 = mystery[4,2]
# # print(elem_5_3)
#
# last = mystery[-1,-1]
# # print(last)
#
# line_4 = mystery[3]
# # print(line_4)
#
# col_2 = mystery[:,5]
# # print(col_2)
#
# part = mystery[1:4, 2:5]
# # print(part)
#
# rev = mystery[::-1,-1]
# # print(rev)
#
# trans = np.transpose(mystery)
# # print(trans)

# mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
#         -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
#         29810.], dtype=np.float32)
#
# nans_index = np.isnan(mystery)
# print(nans_index)
# print(mystery)
#
# n_nan = np.isnan(mystery).sum()
# print(n_nan)
#
# mystery_new = np.copy(mystery)
# mystery_new[np.isnan(mystery_new)] = 0
# print(f'mystery_new: {mystery_new}')
#
# mystery_int = mystery.astype(np.int32)
# print(f'mystery_int: {mystery_int}')
#
# array = np.sort(mystery)
# print(f'array: {array}')
#
# table = array.reshape(5, 3, order='F')
# print(f'table: {table}')
#
# col = table[:, 1]
# print(col)
#
# print(np.median(mystery))

# seed = 2021
# np.random.seed(2021)
#
# simple = np.random.rand()
# randoms = np.random.uniform(-150, 2021, 120)
# table = np.random.randint(1, 101, (3,2))
# even = np.arange(2, 17, 2)
# mix = even.copy()
# np.random.shuffle(mix)
# select = np.random.choice(even, 3, False)
# triplet = np.random.permutation(select)
#
# print(simple)
# print(randoms)
# print(table)
# print(even)
# print(mix)
# print(select)
# print(triplet)

# def get_chess(a):
#         array = np.zeros((a,a))
#         array[1::2, ::2] = 1  # Нечетные строки, четные столбцы
#         array[::2, 1::2] = 1  # Четные строки, нечетные столбцы
#         print(array)
#
#         return array
#
#
# get_chess(1)
# # array([[0.]])
#
# get_chess(4)
# # array([[0., 1., 0., 1.],
# #        [1., 0., 1., 0.],
# #        [0., 1., 0., 1.],
# #        [1., 0., 1., 0.]])

# def shuffle_seed(array_to_shuffle):
#         seed = np.random.randint(0, 2**32)
#         np.random.seed(seed)
#         shuffled_array = np.random.permutation(array_to_shuffle)
#         return shuffled_array, seed
#
# array = [1, 2, 3, 4, 5]
# print(shuffle_seed(array), array)
# # (array([1, 3, 2, 4, 5]), 2332342819)
# print(shuffle_seed(array))
# # (array([4, 5, 2, 3, 1]), 4155165971)

def min_max_dist(*vectors):
        vectors = np.array(vectors)

        distances = []
        for i in range(len(vectors)):
                for j in range(i+1, len(vectors)):
                        distance = np.linalg.norm(vectors[i] - vectors[j])
                        distances.append(distance)

        return min(distances), max(distances)


vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])

# print(min_max_dist(vec1, vec2, vec3))
# (5.196152422706632, 10.392304845413264)

def any_normal(*vectors):
        vectors = np.array(vectors)

        for i in range(len(vectors)):
                for j in range(i+1, len(vectors)):
                        dot_result = np.dot(vectors[i], vectors[j])
                        if dot_result == 0:
                                return True

        return False


vec1 = np.array([2, 1])
vec2 = np.array([-1, 2])
vec3 = np.array([3,4])
print(any_normal(vec1, vec2, vec3))
# True

def get_loto(num):
        return np.random.randint(1, 101, (num, 5, 5))

# print(get_loto(3))

def get_unique_loto(num):
        return np.array([np.random.choice(range(1, 101), size=(5, 5), replace=False) for _ in range(num)])

# print(get_unique_loto(3))

simplelist = [19, 242, 14, 152, 142, 1000]

av = np.average(simplelist)
print(av)




