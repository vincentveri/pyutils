from random import choice, randint, sample
import string


def add_to_password(num_to_include, choices):
    temp = ""
    for i in range(num_to_include):
        temp = temp + str(choice(choices))
    return temp


if __name__ == "__main__":
    num_upper = randint(3, 5)
    # print(f"Adding {num_upper} uppercase letters to the password")
    num_lower = randint(3, 5)
    # print(f"Adding {num_lower} lowercase letters to the password")
    num_digits = randint(3, 5)
    # print(f"Adding {num_digits} digits to the password")
    num_specials = randint(1, 2)
    # print(f"Adding {num_specials} special characters to the password")

    uppers = add_to_password(num_upper, string.ascii_uppercase)
    lowers = add_to_password(num_lower, string.ascii_lowercase)
    numbers = add_to_password(num_digits, string.digits)
    specials = add_to_password(num_specials, '!$#(*')

    pwd = uppers + lowers + numbers + specials

    # Suffle the password
    pwd = "".join(set(sample(pwd, len(pwd))))
    print(f"> Password: {pwd}")

