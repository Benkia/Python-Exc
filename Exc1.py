import logging


class Calc:
    @staticmethod
    def class_logger(a, b):
        logging.warning("The Input Values Of A and B Are {0} and {1}".format(a, b))  # if a =123 and b=234

    @staticmethod
    def sum(a, b):
        Calc.class_logger(a, b)
        return a + b

    @staticmethod
    def multiply(a, b):
        Calc.class_logger(a, b)
        return a * b

    @staticmethod
    def divide(a, b):
        Calc.class_logger(a, b)
        return a / b

    @staticmethod
    def subtract(a, b):
        Calc.class_logger(a, b)
        return a - b


def main():
    print("{}".format(Calc.sum(100, 100)))


if __name__ == "__main__": main()
