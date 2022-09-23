cook_books = {}
with open('cooking.txt', 'r', encoding='utf-8') as file:
	for line in file:
		name_dish = line.strip()
		cook_books[name_dish] = []
		ingr_count = file.readline()
		for i in range(int(ingr_count)):
			emp = file.readline()
			ingredient_name, quantity, measure = emp.split(' | ')
			ingredient = {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.rstrip()}
			cook_books[name_dish].append(ingredient)
		file.readline()	
			
# print(cook_books)		


def get_shop_list_by_dishes(dishes, person_count):
    new_cook_books = {}
    for h in dishes:
        for i in cook_books[h]:
            ingr = {'measure': i['measure'], 'quantity': i['quantity'] * person_count}
            if i['ingredient_name'] not in new_cook_books:    
                new_cook_books[i['ingredient_name']] = ingr        
            else:
                new_cook_books[i['ingredient_name']]['quantity'] += ingr['quantity']             
                   
    return new_cook_books	



print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))

file_list_finel = []
with open('3 задача/1.txt', 'r', encoding='utf-8') as f:
    f_list = {}
    f_list['name'] = '1.txt'
    f_list['len'] = str(len(f.readlines()))
    f.seek(0)
    f_list['text'] = f.read()
    file_list_finel.append(f_list)

with open('3 задача/2.txt', 'r', encoding='utf-8') as f_2:
    f_list_2 = {}
    f_list_2['name'] = '2.txt'
    f_list_2['len'] = str(len(f_2.readlines()))
    f_2.seek(0)
    f_list_2['text'] = f_2.read()
    file_list_finel.append(f_list_2)

    
with open('3 задача/3.txt', 'r', encoding='utf-8') as f_3:
    f_list_3 = {}
    f_list_3['name'] = '3.txt'
    f_list_3['len'] = str(len(f_3.readlines()))
    f_3.seek(0)
    f_list_3['text'] = f_3.read()
    file_list_finel.append(f_list_3)

sort_list = sorted(file_list_finel, key=lambda row: row['len'])
with open('finel_file.txt', 'w', encoding='utf-8') as finel_file:
   for i in sort_list:
    finel_file.write(i['name'] + '\n')
    finel_file.write(i['len'] + '\n')
    for k in i['text']:
        finel_file.write(k)
    finel_file.write('\n')




