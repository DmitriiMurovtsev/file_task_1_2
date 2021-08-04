with open('recipes.txt', 'r', encoding='utf-8') as recipes:
    cook_book = {}
    while True:
        b = recipes.readline().strip()
        my_list_1 = []
        for i in range(0, int(recipes.readline())):
            my_dict = {}
            my_list = recipes.readline().strip().split(' | ')
            my_dict['ingredient_name'] = my_list[0]
            my_dict['quantity'] = int(my_list[1])
            my_dict['measure'] = my_list[2]
            my_list_1.append(my_dict)
        cook_book[b] = my_list_1
        if not recipes.readline():
            break

def food_preparation(list_food, person_count):
    my_dict = {}
    for i in list_food:
        for j in cook_book[i]:
            my_dict_1 = {}
            if j['ingredient_name'] in my_dict:
                my_dict_1['quantity'] += j['quantity'] * person_count
            else:
                my_dict_1['quantity'] = j['quantity'] * person_count
                my_dict_1['measure'] = j['measure']
                my_dict[j['ingredient_name']] = my_dict_1
    return my_dict
