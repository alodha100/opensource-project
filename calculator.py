import argparse


def calculate(operation: str, a: float, b: float) -> float:
    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b
    if operation == "multiply":
        return a * b
    if operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    raise ValueError(f"Unsupported operation: {operation}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Basic math calculator")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"])
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)

    args = parser.parse_args()
    result = calculate(args.operation, args.a, args.b)
    print(result)


if __name__ == "__main__":
    main()
