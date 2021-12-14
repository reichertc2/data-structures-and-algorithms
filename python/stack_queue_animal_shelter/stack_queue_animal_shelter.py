# from stack_and_queue.stack_and_queue import Node,Stack

# Create a class called AnimalShelter which holds only dogs and cats.
# The shelter operates using a first-in, first-out approach.

# isinstance() <----------

class AnimalShelter:
    def __init__(self):
        self.front_cat = None
        self.front_dog = None


    def enqueue(self,value):
        print('enqueue initial value: ',value.value)
        if isinstance(value,Dogs):
            self.front_dog = value
            print('enqueue after queue assignment value: ',value.value)
            return True
        elif isinstance(value,Cats):
            self.front_cat = value
            print('enqueue after queue assignment value: ',value.value)
            return True
        print('if statement does not work')
        return Exception('please add Dog or Cat')


    def dequeue(self):
        pass

class Cats(AnimalShelter):
    def __init__(self,value):
        self.value = value

class Dogs(AnimalShelter):
    def __init__(self,value):
        self.value = value




shelter = AnimalShelter()
dog_a = Dogs('spike')
cat_a = Cats('fluffy')
false_cat = 'false'

shelter.enqueue(dog_a)
shelter.enqueue(cat_a)

print('dog value: ',shelter.front_dog.value)
print('cat value: ',shelter.front_cat.value)

