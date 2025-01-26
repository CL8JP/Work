# Intro

# Bubble sort
# Merge sort
# Insertion sort
# Shell sort
# Selection sort

InitData = [14, 125, 61, 357, 42]

# Bubble Sort:

"""
def BubbleSort(Data):
    for i in range(len(Data) - 1, 0, -1):
        for index in range(i):
            if Data[index] > Data[index + 1]:
                Temp = Data[index]

                Data[index] = Data[index + 1]

                Data[index + 1] = Temp

BubbleSort(InitData)

print(InitData)
"""
# Shell sort

"""
def ShellShort(Data):
    Gap = int(len(Data) / 2)

    while Gap > 0:
        for i in range(Gap, len(Data)):
            Temp = Data[i]

            J = i

    while J >= Gap and Data[J - Gap] > Temp:
        Data[J] = Data[J - Gap]

        J = J - Gap

        Data[J] = Temp

    Gap = int(Gap / 2)
"""
"""
def ShellSort(input_list):

   gap = len(input_list) // 2

   while gap > 0:

      for i in range(gap, len(input_list)):

         temp = input_list[i]

         j = i

   while j >= gap and input_list[j - gap] > temp:

      input_list[j] = input_list[j - gap]

      j = j-gap

      input_list[j] = temp

ShellSort(InitData)

print(InitData)
"""

def ShellSort(Array):
    Gap = len(Array) // 2

    while Gap > 0:
        i = 0

        j = Gap 

        # Check the array from left to right until the last possible index of j

        while j < len(Array):
            print(j < len(Array))
            if Array[i] > Array[j]:
                Array[i], Array[j] = Array[j], Array[i]

            i += 1
            j += 1

            # Now we look back from index to the left and we swap the values that are not in the right order

            k = i 

            while (k - Gap) > -1:
                print((k - Gap))
                if Array[k - Gap] > Array[k]:
                    Array[k - Gap], Array[k] = Array[k], Array[k - Gap]

        Gap //= 2

arr2 = [12, 34, 54, 2, 3]

print("input array:",arr2)

 

ShellSort(arr2)

print("sorted array", arr2)

"""
Time complexity is categorized in 3 types:

Best-Case Time Complexity: The minimum amount of time required by an algorithm to run, based on the given most suitable input is known as best-case complexity. It is denoted by the sign Big Omega (Ω).
Average Case Complexity: The average amount of time required by an algorithm to run, taking into consideration all the possible inputs is known as average-case complexity. It is denoted by the sign Big Theta (Θ).
Worst Case Complexity: The maximum amount of time required by an algorithm to run, taking into consideration possible worst case is known as worst-case complexity. It is denoted by the sign Big O(O).
"""

"""
What Does Big O(N2) Complexity Mean?

It is also known as Quadratic Time complexity. In this type the running time of algorithm grows as square function of input size. This can cause very large time for large inputs. Here, the notation ‘O’ in O(N2) represents its worst cases complexity.

What is O(N2) Time Complexity?

The O(N^2) time complexity means that the running time of an algorithm grows quadratically with the size of the input. It often involves nested loops, where each element in the input is compared with every other element.
"""