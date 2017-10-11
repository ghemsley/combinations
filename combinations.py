#!/usr/bin/python3
from argparse   import ArgumentParser
from itertools  import chain
from itertools  import combinations


def createArgumentParser():

    parser = ArgumentParser()
    parser.add_argument("list",
                        type=list,
                        help="List from which to find possisble combinations of its elements")
    return parser.parse_args()


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def main():

    args = createArgumentParser()
    for element in powerset(args.list):
        print(element)


main()
