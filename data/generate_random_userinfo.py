import random
import string

domains = ["@helloatg.com"]
ascii_lowercase_letters = string.ascii_lowercase[:12]
ascii_uppercase_letters = string.ascii_uppercase[:12]
digits = string.digits


class GenearteRandomUserInfo:

    def random_user_data(self, email_id_type='get_random_string'):
        user_info = {}
        method_to_call = getattr(self, email_id_type)

        firstname = method_to_call()
        user_info['firstname'] = firstname

        lastname = self.get_random_string()
        user_info['lastname'] = lastname

        email = self.get_random_email_id()
        user_info['email'] = email

        password = self.get_random_string_start_with_uppercase()
        user_info['password'] = password

        confirm_password = password
        user_info['confirmpassword'] = confirm_password

        return user_info

    @staticmethod
    def get_random_string():
        random_string = ''.join(random.choice(ascii_lowercase_letters) for _ in range(7))
        return random_string

    @staticmethod
    def get_random_email_id():
        random_string = ''.join(random.choice(ascii_lowercase_letters) for _ in range(7))
        return 'auto_user' + random_string + random.choice(domains)

    @staticmethod
    def get_random_string_in_uppercase():
        random_string = ''.join(random.choice(ascii_uppercase_letters) for _ in range(7))
        return 'AUTO_' + random_string

    @staticmethod
    def get_random_string_start_with_uppercase():
        random_string = ''.join(random.choice(ascii_lowercase_letters) for _ in range(7))
        return 'Auto_' + random_string

    @staticmethod
    def get_random_alpha_numeric_value():
        random_string = ''.join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        return random_string

    @staticmethod
    def get_random_join_numeric_value():
        random_string = ''.join(random.choice(ascii_lowercase_letters) for _ in range(7))
        random_string = random_string + '_'
        random_string = random_string + ''.join(random.choice(digits) for _ in range(10))
        return random_string

    @staticmethod
    def random_number(length=10):
        random_no = ''.join(random.choice(digits) for _ in range(length))
        return random_no

    @staticmethod
    def random_email(username):
        return username + "@" + random.choice(domains)


t1 = GenearteRandomUserInfo()
user_info = t1.random_user_data()
print(user_info)
