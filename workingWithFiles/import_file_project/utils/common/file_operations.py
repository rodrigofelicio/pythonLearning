def read_file(file_name):
    with open(file_name, 'rt') as a_file:
        file_read = [line.strip() for line in a_file.readlines()]
    return file_read


def save_to_file(file_name, file_content):
    with open(file_name, 'w') as a_file:    
        a_file.writelines(file_content)

print(__name__)