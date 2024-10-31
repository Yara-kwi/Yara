tuples_list= [("Alice",25),("Bob",30),("Charlie",25),("David",30),("Eve",35)]
result=" "

def group_names_by_age(tuples_list):
    age_dict={}
    for name, age in tuples_list:
        if age in age_dict:
            age_dict[age].append(name)
        else:
            age_dict[age]=[name]
    return age_dict
group_names_by_age(tuples_list)
print(result)