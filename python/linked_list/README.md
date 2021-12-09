# Challenge Summary 05
TBD

## Specifications
- TBD

## Whiteboard Process
<!-- Embedded whiteboard image -->
![TBD](../wireframes/code-ch-05.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The approach I took was to write the code first with an idea of getting to the end point.


## Solution
<!-- Show how to run your code, and examples of it in action -->
```
TBD
```

# Challenge Summary 06
TBD

## Specifications
- TBD

## Whiteboard Process
<!-- Embedded whiteboard image -->
![TBD](../wireframes/code-ch-06.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The approach I took was to write the code first with an idea of getting to the end point.


## Solution
<!-- Show how to run your code, and examples of it in action -->
```
TBD
```

# Challenge Summary 07
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
![Linked List - KTH - Whiteboard](../wireframes/code-ch-07.png)

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

# Challenge Summary 08
Zip two linked lists.

## Specifications
- Write a function called zip lists
- Arguments: 2 linked lists
- Return: Linked List, zipped as noted below
- Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.
- Try and keep additional space down to O(1)
- You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![Linked List - KTH - Whiteboard](../wireframes/code-ch-08.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The approach I took was to write the code first with an idea of getting to the end point.

The O space i believe is O(n) with the length of the linked list in question determines the run time.

## Solution
<!-- Show how to run your code, and examples of it in action -->
```
TBD
```
