import argparse
import sys
from typing import Optional, Sequence

def main(argv : Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("person")
    args = parser.parse_args(argv)
    if(args.person == ''):
        print("Enter a non-empty name",file = sys.stderr)
        return 1
    print(f"Hello {args.person}!")
    return 0

if __name__ == '__main__':
    exit(main())