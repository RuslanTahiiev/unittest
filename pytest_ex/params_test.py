
FILENAME = 'myfile.txt'

money_list = [
    (10, 10, 'USD', 0),
    (123, 23, 'USD', 100)
]


def file_list_generator(size):
    file_list = []
    for i in range(1, size+1):
        title = f'Test lines #{i}:'
        text = f'Some text... and new text'
        args = [title] + [text] * i
        file_list.append(args)
    return file_list
