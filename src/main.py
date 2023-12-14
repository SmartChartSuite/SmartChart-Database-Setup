import argparse
from src.dbmodels.omop54 import Base as omop54
from src.dbmodels.claritynlp import Base as claritynlp
from src.dbmodels.viewer import Base as viewer
from src.dbmodels.registry import Base as registry
from utils.builder import buildTablesInSchema

parser = argparse.ArgumentParser(
                    prog='SmartChart Suite Database Builder',
                    description='This application helps create the various schemas for SmartChart Suite.')

parser.add_argument('build', choices=['vocab', 'claritynlp', 'viewer', 'registry'])
parser.add_argument('-conn')
parser.add_argument('-schema')

def build_vocab_schema(conn_string: str):
    print("Building Registry Vocab Schema")
    buildTablesInSchema(conn_string, omop54.metadata, "vocab")

def build_claritynlp_schema(conn_string: str):
    print("Building ClarityNLP Schema")
    buildTablesInSchema(conn_string, claritynlp.metadata, "nlp")

def build_viewer_schema(conn_string: str):
    print("Building Registry Viewer/Viewer API Schema")
    buildTablesInSchema(conn_string, viewer.metadata, "viewer")

def build_registry_schema(conn_string: str, schema_name: str):
    print(f"Building Registry Schema in {schema_name}")
    buildTablesInSchema(conn_string, registry.metadata, schema_name)

if __name__ == '__main__':
    args = parser.parse_args()
    print(args)
    if args.build == 'vocab':
        build_vocab_schema(args.conn)
    elif args.build == 'claritynlp':
        build_claritynlp_schema(args.conn)
    elif args.build == 'viewer':
        build_viewer_schema(args.conn)
    elif args.build == 'registry':
        build_registry_schema(args.conn, args.schema)
    else:
        parser.print_help()