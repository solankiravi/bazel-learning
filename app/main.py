import requests
from lib.math_utils import add, substract, multiply, divide

def getResponseCode():
    response = requests.get("https://httpbin.org/get")
    print("HTTP Status:", response.status_code)

def main():
    print(f"Add: {(add(3,5))}")
    print(f"substract: {(substract(3,5))}")
    print(f"multiply: {(multiply(3,5))}")
    print(f"divide: {(divide(3,5))}")
    getResponseCode()


if __name__ == "__main__":
    main()
