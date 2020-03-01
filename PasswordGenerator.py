import random


class PassGen(object):
    """Password Generator

    Class to generate a random password with default length 8.
    Author marcopaulomartins@hotmail.com
    Fev 2020.
    """

    #  Settings
    __password_size = 8

    __min_symbols = 1
    __min_numbers = 2
    __min_l_letters = 0
    __min_u_letters = 0

    __symbols = ['!', '#', '$', '%', '&', '=', '+', '-', '?']
    __numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    __l_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    __u_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def __init__(self, pass_len=3):
        if pass_len > 3:
            self.__password_size = pass_len

    def new(self):
        tokens = [self.__symbols, self.__numbers, self.__l_letters, self.__u_letters]
        minims = [self.__min_symbols, self.__min_numbers, self.__min_l_letters, self.__min_u_letters]
        password = []
        totals = [0, 0, 0, 0]
        for x in range(self.__password_size):
            idx = None
            if self.__password_size - len(password) <= sum(minims):
                for i in range(len(tokens)):
                    if minims[i] > totals[i]:
                        idx = i
                        break
            if idx is None:
                idx = random.randrange(len(tokens))
            token_type = tokens[idx]
            totals[idx] += 1

            password.append(str(token_type[random.randrange(len(token_type))]))

        return ''.join(password)


if __name__ == "__main__":
    generator = PassGen()
    print(generator.new())
