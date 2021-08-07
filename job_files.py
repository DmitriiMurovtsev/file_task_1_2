from pprint import pprint


def create_dict_from_file(file_name):
    cook_dict = {}
    with open(file_name, 'r', encoding='utf-8') as recipes:
        for line in recipes:
            dish_name = line.strip()
            list_of_ingridient = []
            for i in range(int(recipes.readline())):
                temp_dict = {}
                my_list = recipes.readline().strip().split(' | ')
                temp_dict['ingredient_name'] = my_list[0]
                temp_dict['quantity'] = int(my_list[1])
                temp_dict['measure'] = my_list[2]
                list_of_ingridient.append(temp_dict)
            cook_dict[dish_name] = list_of_ingridient
            recipes.readline()
    return cook_dict


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

cook_book = create_dict_from_file('recipes.txt')
pprint(food_preparation(['Запеченный картофель', 'Омлет'], 2))

