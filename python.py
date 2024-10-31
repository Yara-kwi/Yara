total=0
change=0
coin=" "
while total<50:
    coin= int(input('amount of coin: '))
    if coin in[25,10,5]:
        total += coin
        print(f'amount:{50-total} cent')
    else:
        print('the currency is invalid please enter only 25,10,5.')
change=total-50
print(f'the remaining amount is{change}cent: ')