hrs = float(input('Enter Hours: '))
rate = float(input('Enter rate: '))

def computepay(hours, rate):
    if hours > 40:
        apay = hours * rate
        cpay =(hours - 40.0) * (0.5 *rate )
        pay = cpay + apay
        print('Pay:',pay)

    else:
        apay = hours * rate
        print('Pay:',apay)

computepay(hrs, rate)
