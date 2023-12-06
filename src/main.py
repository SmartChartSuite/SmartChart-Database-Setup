import argparse
from src.dbmodels.omop54 import Base as omop54
from src.dbmodels.claritynlp import Base as claritynlp
from utils.builder import buildTablesInSchema

parser = argparse.ArgumentParser(
                    prog='SmartChart Suite Database Builder',
                    description='This application helps create the various schemas for SmartChart Suite.')

parser.add_argument('build', choices=['vocab'])
parser.add_argument('conn_string')

def build_vocab_schema(conn_string: str):
    print("Building Vocab Schema")
    buildTablesInSchema(conn_string, omop54.metadata, "vocab")

def build_claritynlp_schema(conn_string: str):
    print("Building ClarityNLP")
    buildTablesInSchema(conn_string, claritynlp.metadata, "nlp")

if __name__ == '__main__':
    args = parser.parse_args()
    if args.build == 'vocab':
        build_vocab_schema(args.conn_string)
    else:
        parser.print_help()