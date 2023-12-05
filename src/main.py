from src.utils.database import create_connection
import argparse

parser = argparse.ArgumentParser(
                    prog='SmartChart Suite Database Builder',
                    description='This application helps create the various schemas for SmartChart Suite.')

parser.add_argument('build', choices=['vocab'])
parser.add_argument('conn_string')

def build_vocab_schema(conn_string: str):
    print("Building Vocab Schema")
    print(conn_string)
    create_connection(conn_string)


if __name__ == '__main__':
    args = parser.parse_args()
    if args.build == 'vocab':
        build_vocab_schema(args.conn_string)
    else:
        parser.print_help()