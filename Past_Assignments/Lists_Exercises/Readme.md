# Lists


&nbsp;
## A Series of Elements:

 - Each character of a list is assigned an **index** 

 - The indexes of lists always start at `0` and increase by `1`, in order, until the end of the list

 - Bracket notation `[]` is used to access a particular index of a list
    - ex: `print(list[3])` prints the 4th element in `list`

&nbsp;

 - You can get a sublist of a list using `slicing` 
    - Syntax: `[`start_index(inclusive)`:`end_index(exclusive)`]`
    
    - Slice to the end of a list like this: `[`start_index`:]`

    - Slice from the beginning of a list to a specific element like this: `[:`end_index`]`
    
    - Slice from the end of a list with negative numbers `[`-index_from_the_end`:]`


&nbsp;

### Examples:

```python

# INDEXES

beatles = ['George', 'Paul', 'John', 'Ringo']
# index:       0        1       2       3



# BRACKET NOTATION

print(beatles[1])     # prints 'Paul'



# SLICING


# EX 1 - slice from a start_index to an end_index

print(beatles[2:4])   # prints ['John', 'Ringo']




# EX 2 - slice from an elem to the end of a list

print(beatles[1:])    # prints [Paul', 'John', 'Ringo']




# EX 3 - slice from the end of a string using negative numbers

print(beatles[-4:])   # prints ['Paul', 'John', 'Ringo']

```




&nbsp;

## Lists Are Mutable:

 - Lists can be changed (*mutated*)

 - Be careful with this!


&nbsp;

### Examples:

```python

# LET'S CHANGE THE NAMES OF THE BEATLES TO THEIR LAST NAMES

beatles = ['George', 'Paul', 'John', 'Ringo']



# EX 1 - direct reassignment:

beatles[1] = 'McCartney'

print(beatles)      # prints ['George', 'McCartney', 'John', 'Ringo']



# EX 2 - reassignment by slicing:

beatles[2:4] = ['Lennon', 'Starr']

print(beatles)      # prints ['George', 'McCartney', 'Lennon', 'Starr']



# EX 3 - negative indexing works too:

beatles[-4] = 'Harrison'

print(beatles)      # prints ['Harrison', 'McCartney', 'Lennon', 'Starr']

```



&nbsp;

## Lists Can Contain Mixed Elements:

 - Ints
 - Strings
 - Other Lists
 - Other Data Types (*we will get there soon*)


&nbsp;

### Examples:

```python

# LIST WITH INTS

int_list = [1, 2, 3, 4]



# LIST WITH STRS

str_list = ['one', 'two', 'three', 'four']



# LIST WITH BOTH INTS AND STRS

ints_and_strs = [1, 'one', 2, 'two', 3, 'three', 4, 'four']



# LIST OF LISTS OF INTS AND STRS

list_of_lists = [[1, 2, 3, 4], ['one', 'two', 'three', 'four']]

```





&nbsp;

## Lists Have Methods:

 - List Methods mostly start with a `.`

 - Built-in Methods are lowercase 

 - Just like functions, Methods must be invoked with parens `()`

 - List Methods are mostly called at the end of a string ex: `list.sort()`

 - List Methods sometimes return something, sometimes not

 - Some List Methods change (*mutate*) the list, do not 


&nbsp;

### Examples:

```python

# LIST METHODS WITH DESTINYS CHILD

destinys_child = ['Beyonce', 'Kelly', 'LeToya', 'LaTavia']



# .remove() - mutative, removes the specified elem, returns None

destinys_child.remove('LeToya')     # returns None

print(destinys_child)   # prints ['Beyonce', 'Kelly', 'LaTavia']



# .append() - mutative, adds an elem to the end of a list, returns None

destinys_child.append('Farrah')   # returns None

print(destinys_child)       # prints ['Beyonce', 'Kelly', 'LaTavia', 'Farrah']



# .pop() - mutative, removes the elem at the specified index and returns it.
# if no index is given, .pop() removes the last elem in the list

destinys_child.pop(2)       # returns 'LaTavia'

print(destinys_child)       # prints ['Beyonce', 'Kelly', 'Farrah']

destinys_child.pop()        # returns 'Farrah'

print(destinys_child)       # prints ['Beyonce', 'Kelly']



# .insert() - mutative, takes 2 args, an index, and an elem to insert. 
# Inserts given elem at given index, returns None

destinys_child.insert(1, 'Michelle')        # returns None

print(destinys_child)       # prints ['Beyonce', 'Michelle', 'Kelly']



# .sort() - mutative, sorts elements alphabetically, returns None

destinys_child.sort()       # returns None

print(destinys_child)       # prints ['Beyonce', 'Kelly', 'Michelle']



# sorted() METHOD - non-mutative, sorts by whatever key (a function) is given to it. Returns a new list.
# one required arg, two optional args: 
# 1. arg_1 is required (the list to sort)
# 2. optional key (a function to sort by) defaults to alphabetical
# 3. optional reverse (Boolean) to sort in reverse, default is False

sorted(destinys_child, reverse=True)      # returns ['Michelle', 'Kelly', 'Beyonce']

print(destinys_child)       # prints ['Beyonce', 'Kelly', 'Michelle']



# .index() - non-mutative, returns the index first occurance of the elem given:

destinys_child.index('Kelly')       # returns 1

print(destinys_child)       # prints ['Beyonce', 'Kelly', 'Michelle']



# .extend() - mutative, concatenates the given list to the end of the original list. Returns None.

old_members = ['LeToya', 'LaTavia', 'Farrah']

destinys_child.extend(old_members)          # returns None

print(destinys_child)   # prints ['Beyonce', 'Kelly', 'Michelle', 'LeToya', 'LaTavia', 'Farrah']

```
