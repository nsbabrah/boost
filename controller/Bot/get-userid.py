from six.moves.urllib.request import urlopen

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
id_loop = True
while id_loop == True:
    username = input('Please enter the Instagram username that you would like to find the User ID for: ')

    link = 'http://www.instagram.com/' + username
    response = urlopen(link)
    content = str(response.read());

    start_index = (content.index('"owner": {"id": "')) + len('"owner": {"id": "')

    test_string = ''

    for collect in range(14):
        test_string = test_string + content[start_index]
        start_index = start_index + 1

    edit_string = ''

    for char in test_string:
        if is_number(char) == True:
            edit_string = edit_string + char
        else:
            edit_string = edit_string + ''

    print(username + "'s Instagram ID = " + edit_string)
