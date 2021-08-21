l = [1,2,3,4,5,6,7,8]
f = 3

def find(val, subarr):
    if subarr[len(subarr) // 2] == val:
        return len(subarr) // 2
    elif subarr[len(subarr) // 2] > val:
        return find(val, subarr[:len(subarr) // 2])# removes right half
    elif subarr[len(subarr) // 2] < val:
        return find(val, subarr[len(subarr) // 2:])# removes left half

print(find(f, l))
