def bubbleSort(lst):
    """
    bubbleSort is one the slowest algorithms with O(n^2) time coplexity
    
    Returns a sorted list
    
    Input: unsorted list of numbers
    
    Output: sorted list of numbers
    
    >>>bubbleSort([8,4,5,1,0,3,2,6])
    [0, 1, 2, 3, 4, 5, 6, 8]
    """
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j]>lst[j+1]:
                lst[j], lst[j+1], = lst[j+1], lst[j]
    print(lst)

test = bubbleSort([8,4,5,1,0,3,2,6])
