tt = input('Enter Hours: ')
rt = input('Enter Rates: ')

rt = float(rt)
tt = float(tt)

if tt > 40:
    apay = tt * rt
    cpay =(tt - 40.0) * (0.5 *rt )
    pay = cpay + apay
    print('Pay:',pay)
else:
    apay = tt * rt
    print('Pay:',apay)


