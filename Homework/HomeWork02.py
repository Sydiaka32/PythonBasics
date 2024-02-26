
def get_user_input():
    """
    Ask user to enter words separated be spaces
    :return: list with entered words
    """


    user_input = input("Enter words, separated by spaces: ")
    user_list = user_input.split()
    return user_list





def main():
    user_list = get_user_input()
    print(f"Ви ввели: {user_list}")


if __name__ == '__main__':
    main()