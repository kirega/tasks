def mergesort(a):
    if len(a) > 1:
        midpoint = len(a)//2
        la = a[:midpoint] #left array
        ra = a[midpoint:] #right array
        
        mergesort(la)
        mergesort(ra)

        i,j,k = 0,0,0
        while i < len(la) and j< len (ra):
            if la[i] < ra[j]:
                a[k] = la[i]
                i+=1
            else:
                a[k] = ra[j]
                j+=1
            k+= 1
        #this section checks to see if any iutem in either the left 
        # or the right side has any item left. this covers the cases where 
        # the array has an odd no.of items such that the split arrays arent 
        #going to be of the same length.
        while i < len(la):
            a[k] = la[i]
            i+=1
            k+=1
        while j < len(ra):
            a[k] = ra[j]
            j+=1
            k+=1
    return a
if __name__ == '__main__':
    array =  [4,5,6,12,3,1,10]
    mergesort(array)
    print(array)