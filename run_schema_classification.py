import os
import yaml
import pandas as pd
from dotenv import load_dotenv

from pii_meta.metadata import fetch_all_tables, fetch_table_metadata
from pii_meta.classify import classify_table_columns

def main():
    # --- Load config from YAML ---
    with open("config/user_config.yaml") as f:
        config = yaml.safe_load(f)

    db_uri = config["db_uri"]
    schema = config["schema"]
    dama_categories = config["dama_categories"]
    output_filename = config.get("output_filename", "output/full_schema_classification.csv")
    dotenv_path = config.get("dotenv_path", ".env")
    openai_model = config.get("openai_model", "gpt-3.5-turbo")

    # --- Load .env (API key etc.) at main entry ---
    load_dotenv(dotenv_path=dotenv_path)

    table_names = fetch_all_tables(db_uri, schema)
    all_results = []

    for table in table_names:
        meta_df = fetch_table_metadata(db_uri, schema, table)
        # Pass all config needed for LLM classification
        classified_df = classify_table_columns(meta_df, dama_categories, openai_model)
        classified_df['table_name'] = table
        all_results.append(classified_df)

    final_df = pd.concat(all_results, ignore_index=True)
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    final_df.to_csv(output_filename, index=False)
    print(f"Classification report for schema '{schema}' written to {output_filename}")

if __name__ == "__main__":
    main()
