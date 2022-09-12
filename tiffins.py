items = ['dosa','vada','idly','bonda','tea','coffe']
cost = [40,30,20,25,15,10]
d = {}
for i,j in zip(items,cost):
    d[i] = j

order = input()
order = order + " "

ite = []
asked = ''
quantity = []
for i in order:
    if i.isnumeric()==True:
        quantity.append(int(i))
        order = order.replace(i,'')


order = order.lstrip()
for i in order:
    if i.isalpha()==True:
        asked += i

    elif i == ' ' and asked not in ite:
        ite.append(asked)
        asked = ''

for i in ite:
    if i.isalpha()==True:
        pass
    else:
        ite.remove(i)


total = 0
for  i,j in zip(ite,quantity):
    if i not in items:
        print('sorry only items on the list')
        break
    else:
        total+=(d[i]*j)

if total!=0:
    total = total  + (total*(5/100))
    print('Total price(GST Inclusive):  {}'.format(total))