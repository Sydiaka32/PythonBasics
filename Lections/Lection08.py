from typing import List


def logger(func):
    def wrapped(num_list: List):
        result = func(num_list)
        with open("decorator.txt", "w") as f:
            f.write(str(result))
        return result
    return wrapped


def summator(num_list: List) -> int:
    return sum(num_list)


summator = logger(summator)


def main():
    my_list = [1, 2, 3, 4, 5]
    print(summator.__name__)
    result = summator(my_list)
    print(result)


if __name__ == '__main__':
    main()