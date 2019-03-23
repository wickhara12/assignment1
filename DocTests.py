# docTests for class maker
"""
>>> new_class_name = 'Toy'
>>> print(new_class_name)
Toy

>>> data = 'name'
>>> print(data)
name

>>> data = 'color'
>>> print(data)
color

>>> attributes = 'createAttributes()'
>>> print(attributes)
createAttributes()

>>> methods = 'createMethods()'
>>> print(methods)
createMethods()

>>> new_class_name = 'ToyBox'
>>> print(new_class_name)
ToyBox

>>> ToyBoxData = 'name'
>>> print(ToyBoxData)
name

>>> ToyBoxAttributes = 'createAttributes()'
>>> print(ToyBoxAttributes)
createAttributes()

>>> ToyBoxMethods = 'createMethods()'
>>> print(ToyBoxMethods)
createMethods()

>>> classDiagram = "'ToyBox', 'name', 'createAttributes()', 'createMethods()'"
>>> print(classDiagram)
'ToyBox', 'name', 'createAttributes()', 'createMethods()'

>>> classDiagram = "toy, name, color, createAttributes(), createMethods()"
>>> print(classDiagram)
toy, name, color, createAttributes(), createMethods()

"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # doctest.testmod(verbose=True)
