stud = [['Krishna', 67, 68, 69], ['Arjun', 70, 98, 63], ['Malika', 52, 56, 60]]

stud_dic = {}

for student in stud:
    # add new key-value to dict
    stud_dic[student[0]] = student[1:4]

print("Enter a student name: ")
name = input()

if name in stud_dic.keys():
    # get values by key and dividing by length of the list
    notes = sum(stud_dic.get(name))/len(stud_dic.get(name))
    print("{} average note is {}".format(name, notes))
else:
    print("Name not in dict")
