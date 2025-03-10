# Object Introspection
"""
Object introspection refers to the ability of a program to examine an object at runtime
to determine its attributes, methods, type, and more.
Python provides several built-in functions for introspection.

Function                            |             Purpose
---------------------------------------------------------------
type(obj)                           | 	Gets the type/class of an object.
dir(obj)                            |   Lists all attributes and methods.
hasattr(obj, "attr")                |   Checks if an object has a certain attribute.
getattr(obj, "attr", default)       |   Retrieves an attribute safely.
callable(obj.attr)                  |   Checks if an attribute is a method.
obj.__dict__                        |   Gets an object's instance variables.
inspect	                            |   Advanced introspection for classes and methods.

"""