# Creating and defining a Class to define a TypedDict Dictionary.

from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'Anshu', 'age':27}

print(new_person)