occ = [4,1,3,4]
def frequency(list, value, start, end):
    if(start == end):
        if(list[start] == value):
            return 1
        else:
            return 0
    else:
        mid = int((start + end) / 2)
        left = frequency(list, value, start, mid)
        right = frequency(list, value, mid+1, end)
        return right + left
print(frequency(occ,4,0,len(occ)-1))