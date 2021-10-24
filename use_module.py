import my_module

my_module.greet("Albert Einstein")
print("My favorite ice cream flavor is", my_module.flavor)


##alternatively, this can save us memory by importing only the module we need to use.
from my_module import greet, flavor

greet("Albert Einstein")
print("My favorite ice cream flavor is", flavor)

from my_module import greet

greet("Albert Einstein")