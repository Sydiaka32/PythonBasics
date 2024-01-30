
dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_two = {'a': 6, 'b': 7, 'z': 20, 'x': 40}

common_keys = []

for key_dict_one in dict_one.keys():
    if key_dict_one in dict_two:
        common_keys.append(key_dict_one)

print("Спільні ключі у двох словниках: ", common_keys)