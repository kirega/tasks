def bubblesort(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if(a[j] > a[j + 1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return a


if __name__ == '__main__':
    array = [4, 5, 6, 12, 3, 1]  # sorted array  is [1,3,4,5,6,12]
    print(bubblesort(array))
