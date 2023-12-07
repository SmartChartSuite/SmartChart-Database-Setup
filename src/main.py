import argparse
from src.dbmodels.omop54 import Base as omop54
from src.dbmodels.claritynlp import Base as claritynlp
from src.dbmodels.viewer import Base as viewer
from utils.builder import buildTablesInSchema

parser = argparse.ArgumentParser(
                    prog='SmartChart Suite Database Builder',
                    description='This application helps create the various schemas for SmartChart Suite.')

parser.add_argument('build', choices=['vocab', 'claritynlp', 'viewer'])
parser.add_argument('conn_string')

def build_vocab_schema(conn_string: str):
    print("Building Registry Vocab Schema")
    buildTablesInSchema(conn_string, omop54.metadata, "vocab")

def build_claritynlp_schema(conn_string: str):
    print("Building ClarityNLP Schema")
    buildTablesInSchema(conn_string, claritynlp.metadata, "nlp")

def build_viewer_schema(conn_string: str):
    print("Building Registry Viewer/Viewer API Schema ")
    buildTablesInSchema(conn_string, viewer.metadata, "viewer")

if __name__ == '__main__':
    args = parser.parse_args()
    if args.build == 'vocab':
        build_vocab_schema(args.conn_string)
    elif args.build == 'claritynlp':
        build_claritynlp_schema(args.conn_string)
    elif args.build == 'viewer':
        build_viewer_schema(args.conn_string)
    else:
        parser.print_help()