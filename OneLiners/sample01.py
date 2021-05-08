# 1) Swapping Two Variables
a = "Value of A"
b = "Value of B"
a, b = b, a


# 2) multiple Variable Assignments
num, String, List = 100, "Hello", [1, 2]

# assigning multiple values
# And use '_'
a1, *a2, a3 = [1, 2, 3, 4, 5]


# 3) Sum of Even Numbers In a List
sum([num for num in range(10)])


# 4) Deleting Multiple Elements from a List
a = [1, 2, 3, 4, 5]
del a[1::2]


# 5) Reading Files

# way 1
file = [line.strip() for line in open('data.txt')]
# way 2
file = list(open('data.txt'))
# way 3
with open("data.txt") as f:file=[line.strip() for line in f]


# 6) Writing data to file
with open("data.txt",'a',newline='\n') as f:f.write(''.join(file))


# 7) Creating List 
[val for val in range(0,10)]
[val for val in range(0,10, 2)]
[val for val in range(0,10,2) if val%3==0]


# 8) mapping 
"""  [ (a_0),  (a_1),  (a_2),  (a_3),  (a_4)]
                   
                map(f, a)
                   
     [f(a_0), f(a_1), f(a_2), f(a_3), f(a_4)]
"""
add_5 = lambda x : x + 5;

m = map(add_5, [1, 2, 3, 4, 5])

for item in m:
    print(item , end = ' ')

# 9) Set Creation

{x**2 for x in range(10) if x%2==0}


# 10) FizzBuzz 
"""if number is 
    1) div by 3 it is Fizz, 
    2) div by 5 it is Buzz,
    3) both then  FizzBuzz
    4) else number itself
    """

['FizzBuzz' if i%3==0 and i%5==0 
 else 'Fizz' if i%3==0 
 else 'Buzz' if i%5==0 
 else i  for i in range(1,20)]

# 11) Palindrome

"""
def checkPalindrome(x: str) -> bool:
    return x == x[::-1]
"""
checkPalindrome = lambda x : x == x[::-1]


# 12) Space Separated integers to a List

List = list(map(int, input().split()))


# 13) To Check The Existence of a number in a list


if 3 in List: print("number exist")

# 14) Printing Patterns
print('\n'.join('😀' * i for i in range(1, 5 + 1)))


# 15) Fibonacci Series
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(3)]

# 16) prime numbers 
isPrime = lambda x : all(x%y!=0 for y in range(2, int(x**0.5)+1))
list(filter(isPrime , range(1, 15)))

# 17) Finding Max Number

"""
def findmax(*y):
    if len(y) == 1: return y[0]
    else :
        if y[0] > findmax(*y[1:]): return y[0]
        else: return findmax(*y[1:])"""

findmax = lambda *x : x[0] if len(x)==1 else x[0] if x[0] > findmax(*x[1:]) else findmax(*x[1:])

findmax(1, 2, 3, 4)



# 18) Transpose of a matrix

a = [[1,2,3],
     [4,5,6],
     [7,8,9]] 

transpose = [list(i) for i in zip(*a)] 


