#!/usr/bin/env python3
import sys

def main():
    try:
        name = sys.argv[1] if len(sys.argv) > 1 else "GitHub User"
        greeting = f"Hello, {name}!"
        print(greeting)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
