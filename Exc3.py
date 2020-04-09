def Exc3(dict):
    dictionary_1 = []
    dictionary_2 = []
    for node in dict:
        if type(node) == type({}):
            flat1 = {}
            flat2 = {}
            for child in node:
                if type(node[child]) == type(""):
                    flat1[child] = node[child]
                else:
                    child_dict = node[child]
                    flat2["ParentID"] = child
                    for iChild in child_dict:
                        flat2[iChild] = child_dict[iChild]
            dictionary_1.append(flat1)
            dictionary_2.append(flat2)
    return dictionary_1, dictionary_2


sample_object = [
                {'Name': 'Farhad',
                 'Surname': 'Malik',
                 'Blogs': {'BlogName': 'Python1',
                           'Date1': '20180901'}},
                {'Name': 'Farhad2',
                 'Surname': 'Malik2',
                 'Blogs': {'BlogName': 'Python3',
                           'Date1': '20180101'}}]

print(Exc3(sample_object))
