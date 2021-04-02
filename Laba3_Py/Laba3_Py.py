import numpy as np

def SortAndCountInv(A): #модифікація процедури CountInv яка використовує сортування злиттям всередині себе
   n = len(A)
   if n == 1:
       return A, 0;
   else:
       L = A[:int(len(A)/2)] #лівий підмасив
       R = A[int(len(A)/2):] #правий підмасив
       L, x = SortAndCountInv(L) #відсортований лівий підмасив і кількість знайдених інверсій в ньому
       R, y = SortAndCountInv(R) #відсортований правий підмасив і кількість знайдених інверсій в ньому
       A, z = MergeAndCountSplitInv(A, L, R) #обєднаний масив А і кількість розділених інверсій
       return A, x + y + z #відсортований масив і знайдена кількість інверсій в масиві

def MergeAndCountSplitInv(A, L, R): # L i R відсортовані
   a = []
   i = 0
   j = 0
   c = 0    # c - кількість розділених інверсій
   while i < len(L) and j < len(R):
       if L[i] <= R[j]:
           a.append(L[i])
           i += 1
       else:
           a.append(R[j])
           j += 1
           c += (len(L) - i)
   a = a + L[i:]
   a = a + R[j:]
   return a, c;  


def Input():
   f = open("input_22_7.txt")
   lst = []
   for line in f:
       strs = line.split(' ')
       for s in strs:
           if s != ' ':
               lst = lst + [int(s)]
   n = int(lst[0]) #кількість глядачів
   k = int(lst[1]) #кількість фільмів
   arr = np.zeros((n, k), dtype=int) #масив для підрахунку інверсій
   t = 2
   for i in range(n):
       num = int(lst[t])
       t += 1
       for j in range(k):
           arr[i][j] = lst[t]
           t += 1
   f.close()
   return n, k, arr


def InBubbleSort(arr, x, n, k): #сортування бульбашкою елементів для порівняння; x - кого порівнюємо, n - всі користувачі, k - всі фільми
   for i in range(k):
       for j in range(k-i-1):
           if arr[x][j] > arr[x][j+1]:
               for t in range(n):
                   arr[t][j], arr[t][j+1] = arr[t][j+1], arr[t][j]
   return arr


def OutBubbleSorter(result, n):
   for i in range(n):
       for j in range(n - i - 1):
           if result[j][1] > result[j + 1][1]:
               result[j][1], result[j + 1][1] = result[j + 1][1], result[j][1]
               result[j][0], result[j + 1][0] = result[j + 1][0], result[j][0]
   return result

def Output(result, x, n):
   f = open("is01_vozniak_01_output.txt", 'wt')
   x += 1
   s = str(x) + '\n'
   f.write(s)
   for i in range(1, n):
       s1 = str(result[i][0])
       s2 = str(result[i][1])
       f.write(s1 + ' ' + s2 + '\n')

def MainFunc(arr, x, n, k):
   arr = InBubbleSort(arr, x, n, k)
   result = np.zeros((n, 2), dtype=int)
   t = 0
   for i in range(n):
       if i != x:
           t += 1
           result[t][0] = i+1
           mas = arr[i]
           A, result[t][1] = SortAndCountInv(list(mas))
   result = OutBubbleSorter(result, n)
   Output(result, x, n)


n, k, arr = Input() # arr - масив для підрахунку інверсій, n - всі користувачі, k - всі фільми

x = int(input("З ким порiвнюємо: ")) - 1

MainFunc(arr, x, n, k)