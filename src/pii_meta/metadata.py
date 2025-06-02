import pandas as pd
from sqlalchemy import create_engine, inspect

def fetch_all_tables(db_uri, schema):
    engine = create_engine(db_uri)
    inspector = inspect(engine)
    # For most DBs: 'schema' argument is optional but recommended for non-default schemas
    tables = inspector.get_table_names(schema=schema)
    return tables

def fetch_table_metadata(db_uri, schema, table):
    engine = create_engine(db_uri)
    inspector = inspect(engine)
    columns = inspector.get_columns(table, schema=schema)
    # Convert to DataFrame for consistency
    df = pd.DataFrame([{'column_name': col['name'], 'data_type': col['type']} for col in columns])
    return df
