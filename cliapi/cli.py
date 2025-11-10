import argparse
from core import greet, farewell

def parse_args():
    parser = argparse.ArgumentParser(description="Multi-Command Python Console App")
    subparsers = parser.add_subparsers(dest="command", required=True)

    greet_parser = subparsers.add_parser("greet", help="say hello")
    greet_parser.add_argument("name", help="your name")

    farewell_parser = subparsers.add_parser("farewell", help="say goodbye")
    farewell_parser.add_argument("name", help="your name")

    return parser.parse_args()

def run():
    args = parse_args()
    if args.command == "greet":
        print(greet(args.name))
    elif args.command == "farewell":
        print(farewell(args.name))

