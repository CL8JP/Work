def BinarySearch(List, Value):
    ListSize = len(List) - 1

    Index0 = 0

    IndexN = ListSize

    # Finding the middle most value

    while Index0 <= IndexN:
        MidValue = (Index0 + IndexN) // 2

        Index0 += 1

        if List[MidValue] == Value:
            return MidValue
        
    # Compare value with middle most value

    if Value > List[MidValue]:
        Index0 = MidValue + 1

    else:
        IndexN = MidValue - 1

    if Index0 > IndexN:
        return None
    
List = [1, 20, 51, 63, 123, 357]

#print(BinarySearch(List, 123))

def RecursiveBinarySearch(List, Value, Index0, IndexN):
    if IndexN < Index0:
        return None
    else:
        MidValue = Index0 + ((IndexN - Index0) // 2)

    if List[MidValue] > Value:
        return RecursiveBinarySearch(List, Value, Index0, MidValue - 1)
    elif List[MidValue] < Value:
        return RecursiveBinarySearch(List, Value, MidValue + 1, IndexN)
    else:
        return MidValue
    
print(RecursiveBinarySearch(List, 64, 0, 6))