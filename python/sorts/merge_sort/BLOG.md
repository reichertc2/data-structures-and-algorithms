# Merge Sort

Merge sort is a sorting function with one argument of a list and returns a sorted list. The execution at a basic level is it splits the list in half and compares values and swaps them if out of order.

The following will be demonstrated and explained in a combination of a recursive and iterative functions.

## Psuedocode

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

```
## Trace

The sort function takes in a list as an argument. For this example we will use the list ```ls = [8,4,23,42,16,15]```.

### Pass #1

The first pass declare a ```n``` as the length of the list. Then enter into a conditional stating if ```n > 1```, if it is true then execute the following sequence. declare ```mid``` is equal to ```n/2```, declare ```left``` is equal to ```arr[0:mid]```, and declare ```right``` is equal to ```arr[mid:n]```.

Then the next part gets fun. recursively enter into the ```merge_sort``` function for ```left``` and ```right```. Lastly enter into a helper function ```merge``` with ```left```, ```right```, and ```arr``` as arguments.



## Efficiency

- Time:
    - O(N*log(n))
- Space:
    - O(N)
