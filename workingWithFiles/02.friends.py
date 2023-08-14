### CHAPTER 06 - Files in Python
########################################################
#
########################################################
### Python Exercise: Copying Files
#
# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to 'nearby_friends.txt'

# hint: readlines()

def read_a_file(file_name):
    a_file = open(file_name, 'rt')    
    file_read = [line.strip() for line in a_file.readlines()]
    a_file.close()
    return file_read


def write_in_file(file_name, file_content):
    a_file = open(file_name, 'w')    
    a_file.writelines(file_content)
    a_file.close()
    print('File opened, written and closed successfully')

user_input = input('Please, provide 03 names of close friends: ')
name_list = user_input.split(', ')
print(name_list)

people_file = read_a_file('people.txt')
print(people_file)

nearby_friends = []
away_friends = []
for name in name_list:
    if name in people_file:
        nearby_friends.append(name + '\n')
    else:
        away_friends.append(name)

write_in_file("nearby_friends.txt", nearby_friends)
print(f' These are your nearby friends: {nearby_friends}')
print(f' These are your away friends: {away_friends}')