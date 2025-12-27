from lib.math_utils import add, substract, multiply, divide
from lib.http_utils import get_response_code
from lib.file_utils import get_content



def math_utils():
    print(f"Add: {(add(3,5))}")
    print(f"substract: {(substract(3,5))}")
    print(f"multiply: {(multiply(3,5))}")
    print(f"divide: {(divide(3,5))}")

def http_utils():
    print(f"HTTP Status: {get_response_code('https://httpbin.org/get')}")


def main():
    math_utils()
    http_utils()

if __name__ == "__main__":
    main()
