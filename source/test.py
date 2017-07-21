dict_first = {}
dict_second = {}
dict_test = {}
dict_target = {'1':1, '10':10, '100' : 100}

if int(dict_target['1']) == 1 :
    dict_test[dict_target['1']] = 2
else :
    dict_test[dict_target['1']] = 20

print(dict_test)
print(dict_target)

'''
{'0600': 30, '0000': 20, '0300': 30, '0900': 30}
{1200: 60, 1800: 70, 1500: 70, 2100: 60}
'''