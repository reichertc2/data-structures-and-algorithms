# Quick Sort

Quick sort is a sorting function with three arguments of: a list, left most index, and right most index. At the most high level, quick sort identifies the left and right most limits inside of a list. Sets a low and high point and identifies a pivot point in the range. Compares each index the pivot point and reassigns indexes based on a conditional of higher or lower than the pivot.

The following will be demonstrated and explained in a combination of a recursive and iterative functions.

## Psuedocode

```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```
## Trace



### Pass #1





## Efficiency

- Time:
    - O(n log(n))
- Space:
    - O(n)
