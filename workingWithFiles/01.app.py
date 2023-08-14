### CHAPTER 06 - Files in Python
########################################################
#
########################################################
### Files in Python
#
my_file = open('data.txt', 'r')
file_content = my_file.read()
#always close the file after reading it
my_file.close()

print(file_content)
#PS: open and close the file as fast as you can

#####

user_name = input( 'Enter your name: ')

#when we open a file with the 'w', 
#it will erase the content of the file and OVERWRITE with the new content
my_file_writing = open('data.txt', 'w')
my_file_writing.write(user_name)
my_file_writing.close()


