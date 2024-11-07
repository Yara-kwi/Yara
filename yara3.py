def strings_to_lengths(strings):
    lengths_dict={}
    for s in strings:
        lengths_dict[s]= len(s)
    return lengths_dict
strings_list= ["yara","bish","moon"]
result=" "
print(strings_to_lengths(strings_list))

    