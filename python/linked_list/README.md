# Challenge Summary
k-th value from the end of a linked list.

## Specifications
- Read all of these instructions carefully.
- Name things exactly as described.
- Do all your work in a your data-structures-and-algorithms public repository.
- Create a new branch in your repo named as noted below.
- Follow the language-specific instructions for the challenge type listed below.
- Update the “Table of Contents” - in the README at the root of the repository - with a link to this challenge’s README file.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![Linked List - KTH - Whiteboard](/assets/code-ch-7.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The approach I took was to write the code first with an idea of getting to the end point.

The O space i believe is O(n) with the length of the linked list in question determines the run time.

## Solution
<!-- Show how to run your code, and examples of it in action -->
```
    def kth_from_end(self, k_element):
        length_count = 0
        temp = self.head
        while (temp):
            temp = temp.next
            length_count += 1
        if length_count < k_element:
            return IndexError
        elif k_element < 0:
            return None
        else:
            index_from_end = k_element
            index = length_count - index_from_end
            item = self.head
            for x in range(index-1):
                # item += '.next'
                if item.next:
                    item = item.next

            return item.value
```
