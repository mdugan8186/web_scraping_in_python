# ==== Xpath syntax, functions and operations ====

# Xpath stands for XML path language

# == xpath syntax ==
# we can select an element by using the double slash and then we write the element name. this is the most basic way to locate an element or node
# //tag_name

# = // =
# Specifies that the matching node set should be located at any level within the document


# = selecting all the h1 elements =
# //h1

# = selecting an element based on its position =
# //tag_name[1]
# for getting the first h1 element
# //h1[1]

# = selecting based on attribute name =
# this is the standard version of an xpath
# //tag_name[@attribute_name='value']


# = xpath functions to find specific values =
# contains() - search for text included inside an element
# starts-with() - searches for text at the beginning

# //tagName[contains(@attribute_name,'value')]

# == and or logical expressions ==
# //tag_name[(expression 1) and (expression 2)]
