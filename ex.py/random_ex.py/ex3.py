#ex3 List Overlap Comprehensions
import random

a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)

#1
result_overlap = [i for i in set(a) if i in b]
result = []
for element in result_overlap:
  if element not in result:
    result.append(element)
#2
result_overlaps = [i for i in set(a) if i in b]
result = [i for i in result_overlaps if result_overlaps.count(i) == 1]

print result

# A set object is an unordered collection of distinct hashable objects. 
# Common uses include membership testing, removing duplicates from a sequence, 
# and computing mathematical operations such as intersection, union, difference, and symmetric difference. 
# (For other containers see the built-in dict, list, and tuple classes, and the collections module.)
# see python docs 4.9. Set Types