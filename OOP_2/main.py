#  Читаем файл и распечатываем словарь
import os

path = os.path.join(os.getcwd(), 'recipe.txt')
with open(path, encoding='utf-8') as recipes:
    cooker = {}
    for string in recipes:
        dish = string.strip()
        ingredients_count = int(recipes.readline().strip())
        dish_dict = []
        for item in range(ingredients_count):
            ingredients_name, quantity, measure = recipes.readline().strip().split('|')
            dish_dict.append({'ingredient_name': ingredients_name,
                              'quantity': quantity,
                              'measure': measure})
        cooker[dish] = dish_dict
        recipes.readline()
print(cooker)


#  Рассчитываем количество продуктов
person_count = int(input("Укажите количество человек: "))
def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    for dish in dishes:
        for ingredient in cooker[dish]:
            ingredients_list = dict([(ingredient['ingredient_name'],
                                     {'quantity': int(ingredient['quantity']) * person_count,
                                      'measure': ingredient['measure']})])
            if shop_dict.get(ingredient['ingredient_name']) == 'None':
                union = (int(shop_dict[ingredient['ingredient_name']]['quantity']) +
                         int(ingredients_list[ingredient['ingredient_name']]['quantity']))
                shop_dict[ingredient['ingredient_name']]['quantity'] = union
            else:
                shop_dict.update(ingredients_list)
    return shop_dict
print(f'Количество продуктов на {person_count} человек составляет ', get_shop_list_by_dishes(['Омлет', 'Утка по-пекински', 'Запеченный картофель', 'Фахитос'], person_count))
