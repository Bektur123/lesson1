revenue = int(input('Enter sum!:'))
costs = int(input('Enter costs!:'))
financialresualt = (revenue - costs)
employees = int(input('Enter number of employees!:'))
if financialresualt >= 0:
    print('indicator employess', financialresualt / employees)
else:
    print('This is your Financial resualt:', financialresualt)