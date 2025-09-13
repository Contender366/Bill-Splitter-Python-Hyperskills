import random

def get_friends():
    dic = {}
    friends_num = 0
    while True:
        user_input = input('Enter the number of friends joining (including you): ')
        if user_input.isdigit():
            friends_num = int(user_input)
        if friends_num <= 0:
            print('No one is joining for the party')
            exit()
        break
    for i in range(friends_num):
        name = input('Enter the name of every friend (including you), each on a new line: ')
        dic[name] = 0
    get_bill(dic)

def get_bill(dic):
    lucky_name = ''
    denominator= len(dic)
    user_input = input('Enter the total bill value: ')
    answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
    if answer == 'Yes':
        lucky_name = random.choice(list(dic.keys()))
        print(lucky_name, 'is the lucky one!')
        dic[lucky_name] = 0
        denominator -= 1
    else:
        print('No one is going to be lucky')
    if user_input.isdigit():
        total_amount = float(user_input)
        amount = round(total_amount / denominator, 2)
        for k, v in dic.items():
            if k == lucky_name:
                dic[k] = 0
            else:
                dic[k] = amount
    print(dic)

get_friends()
