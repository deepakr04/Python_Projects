class Add:

    def __init__(self, a, b):
        self.n1 = a
        self.n2 = b

    def add_two_number(self):
        return self.n1 + self.n2


def main():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))

    add_num = Add(n1, n2)
    res = add_num.add_two_number()
    print("Addition of two numbers:", res)


if __name__ == '__main__':
    main()
