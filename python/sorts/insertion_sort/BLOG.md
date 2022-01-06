# Insertion Sort

Insertion sort is a type of sort that compares two items together, in numerical sense. For example 1 < 3. In the example below, I will walk you through an example run-through of a version of insertion sorting.

Here is an example of a insertion sort in psuedocode without language specificity, but for this example I will reference code in python.

## Psuedocode

```
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```
## Trace

The sort function takes in a list as an argument. For this example we will use the list ```ls = [3,2,5,22]```.

### Pass #1

In the first pass as the new ``ls`` is passed into the function a few things happen initially. First a for loop is initiated. During this initialization the value of ```i``` is assigned to the first index to the list, in this case ```0```. Simultaneously the length of ```ls``` is determined. With the example list above it is ```4```.

Now the for loop is set up, some more values are assigned. ```j``` is assigned to the value of ```i - 1```. For the first pass it is ```-1```. The next value assigned is ```temp```. for this case it is assigned to the value of ```ls``` at index ```i```, which in the example list above is ```3```.

Next is the initialization of a while loop. The conditions for the first pass of the while loop are the value of ```j```, ```-1```, is compared as greater than or equal to ```0```. The second condition required to enter into the value of ```temp``` is greater than ```ls[j]```, in this case the index value does not exist. So in this first pass the while loop is bypassed.

The last step is to reassign the value of ```temp```. It is assigned to ```ls[j + 1]```, or ```0```.

With the for loop pass one complete we return to the begining of the for loop assuming ```i``` is less than the length of ```ls```, in this case it is. So off to Pass #2.

### Pass #2
<!-- Need to finish rewrite -->
Pass #2 loop set up, some values are reassigned. ```j``` is assigned to the value of ```i - 1```. For the second pass it is now ```0```. The next value assigned is ```temp```. for this case it is assigned to the value of ```ls``` at index ```i```, which in the example list above is ```2```.

Next is the initialization of a while loop. The conditions for the second pass of the while loop are the value of ```j```, ```0```, is compared as greater than or equal to ```0```. The second condition required to enter into the value of ```temp``` is greater than ```ls[j]```, ```3```. SO i this first pass the while loop is bypassed.

The last step is to reassign the value of ```temp```. It is assigned to ```ls[j + 1]```, or ```0```.

With the for loop pass one complete we return to the begining of the for loop assuming ```i``` is less than the length of ```ls```, in this case it is. So off to Pass #2.

## Efficiency

- Time:
    - TBD
- Space:
    - TBD
