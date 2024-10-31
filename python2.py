divisors_sum=0
def is_perfect_number(num):
    divisors_sum=0
    for i in range(1,num):
        if num % i ==0:
            divisors_sum += i
    return divisors_sum == num
perfect_number=[]
for number in range(1,100000):
    if is_perfect_number(number):
        perfect_number.append(number)
        print('the perfect number less then 1000000 is: ',perfect_number)