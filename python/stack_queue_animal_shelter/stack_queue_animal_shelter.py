# from stack_and_queue.stack_and_queue import Node
# Create a class called AnimalShelter which holds only dogs and cats.
# The shelter operates using a first-in, first-out approach.

# isinstance() <----------

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class AnimalShelter:
    def __init__(self):
        self.front_cat = None
        self.front_dog = None


    def enqueue(self,animal):

        print('enqueue initial value: ',animal.value)
        if isinstance(animal,Dogs):
            if self.front_dog == None:
                self.front_dog = animal

                print('enqueue after queue assignment dog_value: ',animal.value)
                print('enqueue after queue assignment dog_value: ',animal.next)
                return
            if self.front_dog.next == None:

                temp = self.front_dog
                print('inside second if',temp.value)

                while temp == None:
                    print('inside while',temp.value)
                    self.front_dog.next = animal
                    print('queue front next', temp.value)
                    print('queue front next-next', temp.next)
                    temp = temp.next
                    return True
            return True
        elif isinstance(animal,Cats):
            self.front_cat = animal
            print('enqueue after queue assignment cat_value: ',animal.value)
            return True
        else:
            print('if statement does not work')
            return Exception('please add Dog or Cat')


    def dequeue(self,pref):
        pass
        # animal_pref = str(pref).lower()
        # if animal_pref == 'dog':
        #     temp = self.front_dog
        #     print('animal pref dog: ',self.front_dog.value)
        #     self.front_dog = temp.next
        #     print('animal pref dog: ',self.front_dog.next)
        #     return 'Dog'
        # elif animal_pref == 'cat':
        #     return 'Cat'
        # else:
        #     return None





class Cats(AnimalShelter):
    def __init__(self,value):
        self.value = value
        self.next = None

class Dogs(AnimalShelter):
    def __init__(self,value):
        self.value = value
        self.next = None




shelter = AnimalShelter()
dog_a = Dogs('spike')
cat_a = Cats('fluffy')
dog_b = Dogs('bruno')
dog_c = Dogs('hunter')
dog_d = Dogs('cujo')

false_cat = Node('false')

shelter.enqueue(dog_a)
# shelter.enqueue(cat_a)
shelter.enqueue(dog_b)
shelter.enqueue(dog_c)
shelter.enqueue(dog_d)
# shelter.enqueue(false_cat)
shelter.dequeue('dog')

print('dog value: ',shelter.front_dog.value)
# print('cat value: ',shelter.front_cat.value)

