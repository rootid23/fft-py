
#Add y , x times
def fun1(x, y, tab='') :
  print("%s %s, %s"%(tab ,x, x))
  if(x == 0) :
    return y
  else :
    return fun1(x - 1,  x + y, tab+' ')


print fun1(4, 2)

#Print the stars n times
def print_stars(n) :

  if(n <= 0) :
    print "\n"
  else :
    print "*",
    return print_stars(n-1)

print_stars(4)


#Evaluate power function
def power(base, exp, tab=' ') :
  print("%s %s, %s"%(tab ,base, exp))
  if(exp == 0) :
    return 1
  else :
    return base * power(base, exp-1, tab+' ')

print(power(4,2))


#Perform palindrome check by spliting the string
def is_pal(st) :
  m = len(st)
  if(m == 0 or m == 1) : return True
  else :
    return st[0] == st[-1] and is_pal(st[1:m-1])
  return False

assert(is_pal('aba') == True)
assert(is_pal('abbbbbba') == True)
assert(is_pal('abcd') == False)


def print_bin(x) :
  if(x < 0) :
    return "-" + print_bin(-x)
  if(x < 2) :
    return str(x)
  else :
    last = x % 2
    rest = x // 2
    return print_bin(rest) + str(last)

# print( print_bin(42) )
assert(print_bin(2) == '10')
assert(print_bin(12) == '1100')
assert(print_bin(42) == '101010')
assert(print_bin(-42) == '-101010')

#How to debug?
#1. put print at the start
#How to evaluate?
#2. Recusive condition replace with base and evaluate (False start from the DP)
#Buzz words -
#1. BAse, recursive case, call stack
#Thinking with the saptial brain



