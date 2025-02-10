
courses = ['History','Math','Physics','CompSci']
print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses[2:])

courses.append('Art')
print(courses)

courses.insert(0,'Chemistry')
print(courses)

couses_2 = ['Art','Education']
courses.insert(0,couses_2)
print(courses)
print(courses[0])
print(courses[1:])

courses = ['History','Math','Physics','CompSci']
courses.extend(couses_2)
print(courses)

courses.remove('Math')
print(courses)
popped = courses.pop()
print(courses)
print(popped)

courses.reverse()
print(courses)

nums = [1,5,2,4,3]

courses.sort()
nums.sort()

print(courses)
print(nums)

courses.sort(reverse=True)
nums.sort(reverse=True)

print(courses)
print(nums)

courses = sorted(courses)
print(courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('Physics'))
# print(courses.index('Artt'))

# print('Math' in courses)
# print('Art' in courses)
#
for item in courses:
    print(item)

for index,course in enumerate(courses):
    print(index,course)

for i,x in enumerate(courses):
    print(i,x)

print()
for index, course in enumerate(courses,start=1):
    print(index, course)

course_str = ', '.join(courses)
print(course_str)

course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)


# -------------------------------------------------

tuple_1 = ('Art', 'CompSci', 'History', 'Physics')
tuple_2 = tuple_1

# tuple_1[0] = 'Artt'

print(tuple_1)
print(tuple_1)

cs_course = {'History', 'Physics','DLD','TOC','Physics','Math'}
art_course = {'History','Design','Math'}

print(cs_course)
print('Physics' in cs_course)

print(cs_course.intersection(art_course))
print(cs_course.difference(art_course))
print(cs_course.union(art_course))

#list---------
empty_list = []
empty_list = list()

#tuple -----------
# empty_tuple = ()
# empty_tuple = tuple()


#set------------
# # this is invalid(this is dictionary) :: empty-set = {}
# empty_set = set()
#
#
#
#

# Appending to list +=
a_list = []

for number in range(1,6):
    a_list += [number]

print(a_list)

#
letter = []
letter += 'Python'
print(letter)

# concat list
list1 = [10,20,30]
list2 = [40,50]
concatList = list1 + list2
print(concatList)

# one element Tuple

a_singleton_tuple = ('red',)
print(a_singleton_tuple)

# Appending tuple to list -> list
numbers = [1,2,3,4,5]
numbers += (6,7)
print(numbers)

# tuple may contain mutable object

student_tuple = ('Amanda','Blue',[98,75,87] )
student_tuple[2][1] = 85
print(student_tuple)

# Unpacking Sequence
student_tuple2 = ('Amanda',[98,75,87])
first_name,grades  = student_tuple2
print(f'{first_name}->{grades}')

#
first_name, grades, another = 'hei'
print(f'{first_name}->{grades}->{another}')

#
num1 , num2 ,num3 = [2,3,5]
print(f'{num1}->{num2}->{num3}')

#
num1 , num2 ,num3 = range(10,40,10)
print(f'{num1}->{num2}->{num3}')

# swap using unpacking

num1 = 99
num2 = 22
num2 , num1 = (num1,num2)
print(f'{num1} and {num2}')

# Enumerate
colors = ['red','orange','yellow']

print(list(enumerate(colors)))
print(tuple(enumerate(colors)))

for index,value in enumerate(colors):
    print(f'{index}: {value}')

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# EMPTY
numbers[5:10] = []
print(numbers)

# del Statement
del numbers[-1]
print(numbers)

# SORT

numbers = [10,3,7,1,9,4,2,8,5,6]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)