new_dozen = lambda n: n + 12

def myfunc(x):
    return lambda n : n + x

new_century = myfunc(100)

print(new_century(2000))

#This sorts our list of lists by the values at index 1 (the type of vehicle)
#,with the added option to sort in ascending or descending (reverse=True) order.
l = [['red', 'truck'],['blue', 'truck'],['red', 'sedan']]
sorted(l, key=lambda v: v[1])
sorted(l, key=lambda v: v[1], reverse=True)

#We can also return lambdas as new, unique functions, as seen in the previous section
def myfunc(x):
    return lambda a, b : (a + b) * x

sum_times_2 = myfunc(2)
print(sum_times_2(10, 20))

