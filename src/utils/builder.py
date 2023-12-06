from sqlalchemy.schema import CreateSchema

from utils.database import create_connection

def buildTablesInSchema(conn_string: str, metadata, schema_name: str):
    engine = create_connection(conn_string, True)
    with engine.connect() as conn:
        conn.execute(CreateSchema(schema_name, if_not_exists=True))
        conn.commit()
        engine.update_execution_options(schema_translate_map={None: schema_name})
        metadata.create_all(bind=engine)