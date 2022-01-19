# ------------------------------------------------ #
'''largest_num'''

# Write a function called largest_num which will take in a list of numbers and return the largest number from that list. Do not use any built-in methods to solve this problem.


### YOUR CODE STARTS HERE ###

def largest_num(my_list):
  biggest=my_list[0]

  for element in my_list[1:]:
    if element > biggest:
      biggest = element
  return biggest


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''includes'''

# Write a function called includes that takes a list of numbers and a number as input. This function returns a boolean indicating whether or not the list contains the number. Do not use the list.index() method.


### YOUR CODE STARTS HERE ###

def includes(my_list, my_num):
  if my_num in my_list:
    return True
  else:
    return False


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''average'''

# Write a function called average that takes in a list of numbers and returns a float representing the average value of the those numbers.


### YOUR CODE STARTS HERE ###

def average(my_list):

  sum = 0
  for element in my_list:
    sum += element
  return sum / len(my_list)


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''median'''

# Write another function called median that takes in a list of numbers and returns a float representing the median from that list.


### YOUR CODE STARTS HERE ###

def median(my_list):
  
  length=len(my_list)

  my_list.sort()
  
  if length % 2 ==0:
    med_right=my_list[length//2]
    #the fifth position is the number 6 because the list beings at zero.
    med_left=my_list[(length//2)-1]
    med=(med_left+med_right)/2
    return med
  
  else:
    med = my_list[length//2]
    return med


#METHOD 2
  # length=len(my_list)

  # #assemble the relevant index position numbers
  # for i in range(len(my_list)):
  #   #assemble the index position 'to the right' of 'i'
  #   for j in range(i + 1, len(my_list)):
  #     #compare the two numbers at index_position and index_position+1
  #     if my_list[i] > my_list[j]:
  #       # if the order is not increasing, swap those elements
  #       # then the 'rightside' element will be the next 'i'
  #       my_list[i], my_list[j] = my_list[j], my_list[i]
  #     # otherwise maintain the order by doing nothing

  # if length % 2 ==0:
  #   med_right=my_list[length//2]
  #   #the fifth position is the number 6 because the list beings at zero.
  #   med_left=my_list[(length//2)-1]
  #   med=(med_left+med_right)/2
  #   return med
  
  # else:
  #   med = my_list[length//2]
  #   return med

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''only_a'''

# Write a function called only_a that takes in a list of strings and returns a list of strings that contain the letter 'a'.


### YOUR CODE STARTS HERE ###

def only_a(list_of_strings:list):
  a_only = []
  count = 0
  for element in list_of_strings:
    if 'a' in element:
      a_only.append(element)
      count += 1

  return a_only

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''odd_couple'''

# Write a function called odd_couple that takes a list and returns a list.

# odd_couple should:

  # return a list with the first two odd numbers of the input.
  
  # return a list with only one odd number if the input is only one odd number.
  
  # returns an empty list if the input has no odd numbers


### YOUR CODE STARTS HERE ###

def odd_couple(num_list:list):
  oc = []
  count = 0
  for item in num_list:
    if item % 2 != 0 and count <= 2:
      oc.append(item)
    count += 1  


  return oc





### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''overachiever'''

# Write a function called overachiever which takes in a list of lists. The sublists contain both a name (string) of a student followed by a float representing his/her/their average for the class. Return the name of the student with the highest exam score.


### YOUR CODE STARTS HERE ###

def overachiever(group:list):
 group.sort()
 top = group[0]
 return top[0]

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''absolute_total'''

# Write a function called absolute_total which takes in a list of integers. return the sum of the absolute value of each element.


### YOUR CODE STARTS HERE ###

def absolute_total(nums:list):
  absolute = [abs(number) for number in nums] 
  return sum(absolute)



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''sum_of_cubes'''

# Write a function called sum_of_cubes which takes in a list of integers. return the sum of the cubes of each element.


### YOUR CODE STARTS HERE ###

def sum_of_cubes(nums:list):
  cube = [(number **3) for number in nums]
  return sum(cube)


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''multiply_by_index'''

# Write a function called multiply_by_index which takes in a list of integers. return the sum of the elements multiplied with their list indices.


### YOUR CODE STARTS HERE ###

def multiply_by_index(nums:list):
  mult = []
  index = 0
  for number in nums:
    mult.append(number * index)
    index += 1
  return sum(mult)


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''move_knight'''

'''Write a function move_knight which takes in a list coords_and_dirs, whose first element is a list, indicating the coordinates of the Knight's starting position, and whose second element is a four-character string, indicating where the Knight should move in one turn.

A Knight must move exactly three spaces, either two spaces in a vertical direction and one in a horizontal direction, or one space in a vertical direction and two spaces in a horizontal direction.

Assume the string at the first index of coords_and_dirs will always be formatted such that:

  The first character is either 'U' or 'D' (where 'U' is up and 'D' is down) and represents the file (vertical direction)

  The second character is either '1' or '2' and represents how many spaces in the vertical direction the Knight will travel
  
  The third character is either 'L' or 'R' (where 'L' is left and 'R' is right) and represents the rank (horizontal direction)
  
  The fourth character is either '1' or '2' and represents how many spaces in the horizontal direction the Knight will travel

For example: "U1L2" would read as "up one space, left two spaces".



The chess board is a grid, with each space identified as [file, rank]:

  [0, 7] --> .    .    .    .    .    .    .    . <-- [7, 7]

             .    .    .    .    .    .    .    .

             .    .    .    .    .    .    .    .

             .    .    .    .    .    .    .    .

             .    .    .    .    .    .    .    .

             .    .    .    .    .    .    .    .

             .    .    .    .    .    .    .    . 

  [0, 0] --> .    .    .    .    .    .    .    . <-- [7, 0]

For example: The starting coordinates [7, 7] would represent the knight starting in the upper right corner of the chess board.



If the given directions would be an illegal move, or if the move would cause the Knight to fall off the board, return the string "Illegal Move - Horsey Down!"

Else, the function should return a string with updated file and rank, formatted as such: "The knight has moved to [file, rank]."
'''

### YOUR CODE STARTS HERE ###

def move_knight(moves:list):
  start = []
  start.append(moves[0])
  position = moves[0]
  movement = []
  direction = ['default' , 'default']

  for character in moves[1]:
    if character == '1' or character == '2':
      movement.append(int(character))
    elif character == 'U' or character == 'D':
      direction[0] = character
    elif character == 'R' or character == 'L':
      direction[1] = character
    else:
      return "Illegal Move - Horsey Down!"
  
  if (movement[0]) + (movement[1]) != 3:
    return "Illegal Move - Horsey Down!"
  
  if direction[0] == 'U':
    position[1] += movement[0]
  elif direction[0] == 'D':
    position[1] -= (movement[0])
  else:
    return "Illegal Move - Horsey Down!"
  
  if direction[1] == 'R':
    position[0] += (movement[1])
  elif direction[1] == 'L':
    position[0] -= (movement[1])
  else:
    return "Illegal Move - Horsey Down!"
  
  if int(position[0]) < 0 or int(position[0]) > 7:
    return "Illegal Move - Horsey Down!"
  elif int(position[1]) < 0 or int(position[1]) > 7:
    return "Illegal Move - Horsey Down!"
  else:
    return "The knight has moved to " + str(position) + "."




### YOUR CODE ENDS HERE ###
