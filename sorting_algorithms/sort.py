# Implement bubble sort
def bubble_sort(arr):
    n = len(arr) # length of the array
    for i in range(n-1): # iterate through the array
        for j in range(n-i-1): # iterate through the array starting from the first element
            if arr[j] > arr[j+1]: # if the current element is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j] # swap the current element with the next element
    return arr # bubble sort has a time complexity of O(n^2)


# Implement selection sort
def selection_sort(arr):
    n = len(arr) # length of the array
    for i in range(n-1): # iterate through the array
        min_index = i # set the minimum index to the current index
        for j in range(i+1, n): # iterate through the array starting from the next index
            if arr[j] < arr[min_index]: # if the current element is less than the minimum element
                min_index = j   # set the minimum index to the current index
        arr[i], arr[min_index] = arr[min_index], arr[i] # swap the minimum element with the current element
    return arr # selection sort has a time complexity of O(n^2)


# Implement insertion sort
def insertion_sort(arr):
    n = len(arr) # length of the array
    for i in range(1, n): # iterate through the array starting from the second element
        key = arr[i] # set the key to the current element
        j = i-1 # set j to the previous index
        while j >= 0 and key < arr[j]: # while j is greater than or equal to 0 and the key is less than the current element
            arr[j+1] = arr[j] # set the next element to the current element
            j -= 1 # decrement j
        arr[j+1] = key # set the next element to the key
    return arr # insertion sort has a time complexity of O(n^2)


# Implement merge sort
def merge_sort(arr):
    if len(arr) > 1: # if the length of the array is greater than 1
        mid = len(arr)//2 # set the mid index to the length of the array divided by 2
        L = arr[:mid] # set L to the first half of the array
        R = arr[mid:] # set R to the second half of the array

        merge_sort(L) # recursively call merge_sort on L
        merge_sort(R) # recursively call merge_sort on R

        i = j = k = 0 # set i, j, and k to 0

        while i < len(L) and j < len(R): # while i is less than the length of L and j is less than the length of R
            if L[i] < R[j]: # if the current element in L is less than the current element in R
                arr[k] = L[i] # set the current element in arr to the current element in L
                i += 1 # increment i
            else: # if the current element in L is greater than the current element in R
                arr[k] = R[j] # set the current element in arr to the current element in R  
                j += 1 # increment j
            k += 1 # increment k

        while i < len(L): # while i is less than the length of L
            arr[k] = L[i] # set the current element in arr to the current element in L
            i += 1 # increment i
            k += 1 # increment k

        while j < len(R): # while j is less than the length of R
            arr[k] = R[j] # set the current element in arr to the current element in R
            j += 1 # increment j
            k += 1 # increment k
    return arr # merge sort has a time complexity of O(nlogn)


# Implement quick sort
def quick_sort(arr):
    if len(arr) <= 1: # if the length of the array is less than or equal to 1
        return arr # return the array
    else: # if the length of the array is greater than 1
        pivot = arr[0] # set the pivot to the first element
        less = [x for x in arr[1:] if x <= pivot] # set less to the elements less than or equal to the pivot
        greater = [x for x in arr[1:] if x > pivot] # set greater to the elements greater than the pivot
        return quick_sort(less) + [pivot] + quick_sort(greater) # return the sorted less, the pivot, and the sorted greater
    

# Implement heap sort
def heapify(arr, n, i):
    largest = i # set the largest index to i
    l = 2*i + 1 # set l to the left child of i
    r = 2*i + 2 # set r to the right child of i

    if l < n and arr[l] > arr[largest]: # if l is less than n and the left child is greater than the largest element
        largest = l # set the largest index to l

    if r < n and arr[r] > arr[largest]: # if r is less than n and the right child is greater than the largest element
        largest = r # set the largest index to r

    if largest != i: # if the largest index is not i
        arr[i], arr[largest] = arr[largest], arr[i] # swap the current element with the largest element
        heapify(arr, n, largest) # recursively call heapify on the largest index


def heap_sort(arr):
    n = len(arr) # length of the array

    for i in range(n//2-1, -1, -1): # iterate through the array starting from the middle
        heapify(arr, n, i) # call heapify on the current element

    for i in range(n-1, 0, -1): # iterate through the array starting from the end
        arr[i], arr[0] = arr[0], arr[i] # swap the current element with the first element
        heapify(arr, i, 0) # call heapify on the current element
    return arr # heap sort has a time complexity of O(nlogn)


# Implement counting sort
def counting_sort(arr):
    n = len(arr)
    output = [0]*n
    count = [0]*(max(arr)+1)
    for i in range(n):
        count[arr[i]] += 1
    for i in range(1, len(count)):
        count[i] += count[i-1]
    i = n-1
    while i >= 0:
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]
    return arr # counting sort has a time complexity of O(n+k) where k is the range of the non-negative key values


# Implement radix sort
def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0]*n
    count = [0]*10
    for i in range(n):
        index = arr[i]//exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    i = n-1
    while i >= 0:
        index = arr[i]//exp
        output[count[index % 10]-1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]
    return arr # radix sort has a time complexity of O(nk) where k is the number of digits in the largest number


def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    while max1//exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10
    return arr # radix sort has a time complexity of O(nk) where k is the number of digits in the largest number


# Implement bucket sort
def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for i in range(n):
        index = int(n*arr[i])
        buckets[index].append(arr[i])
    for i in range(n):
        buckets[i].sort()
    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1
    return arr  # bucket sort has a time complexity of O(n^2) in the worst case


# Implement shell sort
def shell_sort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr # shell sort has a time complexity of O(n^2)


# Implement cocktail sort
def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end-1, start-1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        start += 1
    return arr # cocktail sort has a time complexity of O(n^2)


# Implement gnome sort
def gnome_sort(arr):
    n = len(arr)
    index = 0
    while index < n:
        if index == 0:
            index += 1
        if arr[index] >= arr[index-1]:
            index += 1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index -= 1
    return arr # gnome sort has a time complexity of O(n^2)


# Implement comb sort
def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    swapped = True
    while gap > 1 or swapped:
        gap = int(gap/shrink)
        if gap < 1:
            gap = 1
        i = 0
        swapped = False
        while i+gap < n:
            if arr[i] > arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                swapped = True
            i += 1
    return arr # comb sort has a time complexity of O(n^2)


# Implement pancake sort
def flip(arr, i):
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1


def find_max(arr, n):
    mi = 0
    for i in range(0, n):
        if arr[i] > arr[mi]:
            mi = i
    return mi


def pancake_sort(arr):
    n = len(arr)
    curr_size = n
    while curr_size > 1:
        mi = find_max(arr, curr_size)
        if mi != curr_size-1:
            flip(arr, mi)
            flip(arr, curr_size-1)
        curr_size -= 1
    return arr # pancake sort has a time complexity of O(n^2)


# Implement stooge sort
def stooge_sort(arr, l, h):
    if l >= h:
        return
    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]
    if h-l+1 > 2:
        t = (h-l+1)//3
        stooge_sort(arr, l, h-t)
        stooge_sort(arr, l+t, h)
        stooge_sort(arr, l, h-t)
    return arr # stooge sort has a time complexity of O(n^(log3/log1.5))


# Implement bogo sort
import random
def is_sorted(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True


def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr # bogo sort has a time complexity of O((n+1)!) on average


# Implement slow sort
def slow_sort(arr, l, h):
    if l >= h:
        return
    m = (l+h)//2
    slow_sort(arr, l, m)
    slow_sort(arr, m+1, h)
    if arr[m] > arr[h]:
        arr[m], arr[h] = arr[h], arr[m]
    slow_sort(arr, l, h-1)
    return arr # slow sort has a time complexity of O(n^logn)


# Implement cocktail shaker sort
def cocktail_shaker_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end-1, start-1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        start += 1
    return arr # cocktail shaker sort has a time complexity of O(n^2)


# Implement odd-even sort
def odd_even_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return arr # odd-even sort has a time complexity of O(n^2)


# Implement bitonic sort
def compAndSwap(arr, i, j, dire):
    if (arr[i] > arr[j] and dire == 1) or (arr[i] < arr[j] and dire == 0):
        arr[i], arr[j] = arr[j], arr[i]


def bitonic_merge(arr, low, cnt, dire):
    if cnt > 1:
        k = cnt//2
        for i in range(low, low+k):
            compAndSwap(arr, i, i+k, dire)
        bitonic_merge(arr, low, k, dire)
        bitonic_merge(arr, low+k, k, dire)


def bitonic_sort(arr, low, cnt, dire):
    if cnt > 1:
        k = cnt//2
        bitonic_sort(arr, low, k, 1)
        bitonic_sort(arr, low+k, k, 0)
        bitonic_merge(arr, low, cnt, dire)
    return arr # bitonic sort has a time complexity of O(nlog^2n)


# Implement quantum bogosort
def quantum_bogosort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr # quantum bogosort has a time complexity of O((n+1)!) on average


# Implement permutation sort
def permutation_sort(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] != i+1:
            arr[i], arr[arr[i]-1] = arr[arr[i]-1], arr[i]
    return arr # permutation sort has a time complexity of O(n^2)


# Implement tournament sort
def tournament_sort(arr):
    n = len(arr)
    tree = [0]*(2*n)
    for i in range(n):
        tree[n+i] = i
    for i in range(n-1, 0, -1):
        tree[i] = arr[tree[2*i]] < arr[tree[2*i+1]] and tree[2*i] or tree[2*i+1]
    for i in range(n):
        j = 1
        while j < n:
            j = 2*j
            if j < n-1 and arr[tree[j]] < arr[tree[j+1]]:
                j += 1
            if arr[i] < arr[tree[j]]:
                arr[i], arr[tree[j]] = arr[tree[j]], arr[i]
            j = j
    return arr # tournament sort has a time complexity of O(nlogn)


# Implement spread sort
def spread_sort(arr):
    n = len(arr)
    max_val = max(arr)
    min_val = min(arr)
    spread = max_val - min_val
    buckets = [[] for _ in range(n)]
    for i in range(n):
        index = int((arr[i]-min_val)/spread*(n-1))
        buckets[index].append(arr[i])
    for i in range(n):
        buckets[i].sort()
    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1
    return arr # spread sort has a time complexity of O(n^2) in the worst case


# Implement patience sort
class Pile:
    def __init__(self, card):
        self.cards = [card]
        self.top_card = card
        
    def add_card(self, card):
        self.cards.append(card)
        self.top_card = card
        
    def __repr__(self):
        return str(self.cards)
    

def patience_sort(arr):
    piles = []
    for card in arr:
        new_pile = Pile(card)
        for pile in piles:
            if card < pile.top_card:
                pile.add_card(card)
                break
        else:
            piles.append(new_pile)
    while len(piles) > 1:
        new_piles = []
        for i in range(0, len(piles), 2):
            if i+1 < len(piles):
                new_pile = Pile(piles[i].top_card)
                for card in piles[i+1].cards:
                    new_pile.add_card(card)
                new_piles.append(new_pile)
            else:
                new_piles.append(piles[i])
        piles = new_piles
    return [pile.cards.pop() for pile in piles] # patience sort has a time complexity of O(nlogn)


# Implement library sort
def library_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr # library sort has a time complexity of O(n^2)


# Implement stooge sort
def stooge_sort(arr, l, h):
    if l >= h:
        return
    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]
    if h-l+1 > 2:
        t = (h-l+1)//3
        stooge_sort(arr, l, h-t)
        stooge_sort(arr, l+t, h)
        stooge_sort(arr, l, h-t)
    return arr # stooge sort has a time complexity of O(n^(log3/log1.5))
