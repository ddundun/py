import numpy as np

# array = np.arange(0,10)
# np.save('saved.npy',array)
#
# print('saved')
# # 간단하게 배열 저장
# result = np.load('saved.npy')
# print(result)
#
# array1 = np.arange(10,20)
# # 복수로 저장하는 것이기때문에 savez
# np.savez('saved.npz',array = array, array1 = array1)
#
# print(np.load('saved.npz')['array'])
# print(np.load('saved.npz')['array1'])
array = np.linspace(0, 10, 5)
print(array)

array1 = np.random.randint(0, 10, (2, 3))
print(array1)

arr1 = np.arange(0, 10)
arr2 = arr1.copy() #깊은복사 copy
arr2[3] = 55
print(arr1)
print(arr2)

arr3 = np.array([1, 3, 1, 2, 1, 3, 1])
print(np.unique(arr3))
