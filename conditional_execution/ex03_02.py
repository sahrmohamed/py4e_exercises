try:
    tt = float(input('Enter Hours: '))
    rt = float(input('Enter rate: '))
except:
    print('Error, Please enter a numeric value')
    quit()
if tt > 40:
    apay = tt * rt
    cpay =(tt - 40.0) * (0.5 *rt )
    pay = cpay + apay
    print('Pay:',pay)
else:
    apay = tt * rt
    print('Pay:',apay)
