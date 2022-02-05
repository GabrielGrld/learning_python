def get_credentials(text_file):
    """Method to get credentials from text file.
        the text file must have the  data in this order:
        'NAME', 'USER', 'PASSWORD', 'HOST','PORT'
        each one must be in a line
        Args:
        text file: Name of the text File

        Returns:
        list: a list with the data
    """
    with open(text_file) as f:
        credentials_list = f.read().split('\n')
    return credentials_list


"""
for value in get_credentials('credentials.txt'):
    print(f"{value} \n")
credentials_list = get_credentials('credentials.txt')
print(credentials_list)
print(f" 1  is {credentials_list[1]}")
print(f" 2  is {credentials_list[2]}")
print(f" 3  is {credentials_list[3]}")
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_credentials('credentials.txt')[0],
        'USER': get_credentials('credentials.txt')[1],
        'PASSWORD': get_credentials('credentials.txt')[2],
        'HOST': get_credentials('credentials.txt')[3],
        'PORT': get_credentials('credentials.txt')[4],
    }
}
print(DATABASES)
