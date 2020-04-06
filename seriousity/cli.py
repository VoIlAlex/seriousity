import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'command',
        help='there is only one serious command - start.'
    )
    parser.add_argument(
        'way',
        help='the command can be executed ony one way - seriously.'
    )
    args = parser.parse_args()
    return args


def cli():
    args = parse_args()
    if args.command == 'start' and args.way == 'seriously':
        print('💩')
    else:
        print('You was not serious enough.')


if __name__ == "__main__":
    cli()
