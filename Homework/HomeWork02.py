
def get_user_input():
    """
    Ask user to enter words separated be spaces
    :return: list with entered words
    """


    user_input = input("Enter words, separated by spaces: ")
    user_list = user_input.split()
    return user_list


def find_shortest_word(user_list):
    """
    Find the shortest word
    :param user_list:
    :return: the shortest word from list
    """
    short_word = min(user_list, key=len)
    return short_word


def find_longest_word(user_list):
    """
    Find the longest word
    :param user_list:
    :return: the longest word from list
    """
    long_word = max(user_list, key=len)
    return long_word


def matching_edge(user_list):
    """
    Find words that start and end with the same letter
    :param user_list:
    :return: words from list that start and end with the same letter
    """
    matching_words = []

    for word in user_list:
        if word[0] == word[-1]:
            matching_words.append(word)
    return matching_words


def main():
    user_list = get_user_input()
    print(f"Ви ввели: {user_list}")
    short_word = find_shortest_word(user_list)
    print(f"Shortest word: {short_word}")
    long_word = find_longest_word(user_list)
    print(f"Longest word: {long_word}")
    matching_words = matching_edge(user_list)
    print(f"Matching words: {matching_words}")


if __name__ == '__main__':
    main()