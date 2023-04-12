import random
import string

password_length = 12

password_characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(password_characters) for i in range(password_length))

print(f"Your random password is: {password}")
