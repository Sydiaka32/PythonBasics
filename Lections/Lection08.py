
def log(add):
    def wrapped(a: int, b:int):
        result = add(a, b)
        with open("file.txt", "w") as f:
            f.write(str(result))
        return result
    return wrapped


def add(a: int, b:int) -> int:
    res = a + b
    return res


add = log(add)