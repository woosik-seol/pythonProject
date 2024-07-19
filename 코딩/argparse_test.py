# python script.py John -a 30
import argparse

def main():
    parser = argparse.ArgumentParser(description="This is a sample program.")
    parser.add_argument("name", help="Your name")
    parser.add_argument("-a", "--age", type=int, help="Your age", required=False)

    args = parser.parse_args()

    print(f"Hello, {args.name}!")
    if args.age:
        print(f"You are {args.age} years old.")

if __name__ == "__main__":
    main()