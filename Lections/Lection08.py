from typing import List


def logger(filename):
    def decorator(func):
        def wrapped(num_list: List):
            result = func(num_list)
            with open(filename, "w") as f:
                f.write(str(result))
            return result
        return wrapped
    return decorator


@logger("file_decorator.txt")
def summator(num_list: List) -> int:
    return sum(num_list)




def main():
    my_list = [1, 2, 3, 4, 5]
    print(summator.__name__)
    result = summator(my_list)
    print(result)


if __name__ == '__main__':
    main()