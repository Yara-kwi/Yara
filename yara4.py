numbers=[1,2,3,4,5,6]
def sum_even_odd(numbers):
    result={
        "even_sum":0,
        "odd_sum":0
    }
    for number in numbers:
        if number % 2==0:
            result["even_sum"] += number
        else:
            result["odd_sum"] += number
    return result
result= sum_even_odd(numbers)
print(result)