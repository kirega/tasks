def check_type(a):
    if all(isinstance(x, int) for x in a) or all(isinstance(x, str) for x in a):
        return True
    else:
        return False


def bubblesort(a):
    if len(a) > 1:
        if check_type(a):
            for i in range(len(a)):
                for j in range(len(a)-1):
                    if(a[j] > a[j + 1]):
                        temp = a[j]
                        a[j] = a[j+1]
                        a[j+1] = temp

            return a
        else:
            return 'Can not sort items of different types'
    else:
        return 'Empty list'

if __name__ == '__main__':
    array = [4, 5, 6, 12, 3, 1]  # sorted array  is [1,3,4,5,6,12]

    print(bubblesort(array))
