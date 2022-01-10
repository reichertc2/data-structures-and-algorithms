# Challenge Summary 28
Quick Sort

## Specifications
- Read all of these instructions carefully.
- Name things exactly as described.
- Do all your work in a your data-structures-and-algorithms public repository.
- Create a new branch in your repo named as noted below.
- Follow the language-specific instructions for the challenge type listed below.
- Update the “Table of Contents” - in the README at the root of the repository - with a link to this challenge’s README file.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![Quick Sort](../code_challenges/wireframes/code-ch-28.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The approach I took was to write the code first with an idea of getting to the end point.


## Solution
<!-- Show how to run your code, and examples of it in action -->
```
def quick_sort(arr, left, right):
    if left < right:
        position = partition(arr, left, right)
        quick_sort(arr, left, position - 1)
        quick_sort(arr, position + 1, right)


def partition(arr, left, right):
    pivot = arr[right]
    low = left - 1
    for i in range(left,right):
        if arr[i]<pivot:
            low += 1
            arr[low],arr[i] = arr[i],arr[i]
    arr[low + 1],arr[right] = arr[right], arr[low + 1]
```
<!-- good yutube overview --= https://www.youtube.com/watch?v=0SkOjNaO1XY -->
