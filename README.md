
# pii-schema-classifier

A robust Python package for **automated data classification of database columns** according to DAMA International data classification standards (e.g., `pii`, `confidential`, `general`, etc.) using a large language model (LLM, e.g., GPT-4).
This tool supports **schema-wide analysis** for any SQLAlchemy-compatible database, with flexible configuration and YAML-driven workflows.

---

## Features

- **Automated Data Classification:**  
  Classifies columns in all tables of a database schema using DAMA categories, leveraging an LLM (e.g., OpenAI GPT-4) for context-aware classification.
- **Database-Agnostic:**  
  Works with PostgreSQL, MySQL, SQLite, SQL Server, Oracle, and more (any DB supported by SQLAlchemy).
- **Configurable Categories:**  
  Categories and workflow parameters are user-configurable via a YAML file.
- **Few-Shot Prompting:**  
  Uses in-context Q&A examples to improve LLM accuracy.
- **Parallel LLM Calls:**  
  Supports concurrent requests for rapid analysis of large schemas.
- **Easy to Install:**  
  Distributed as a Poetry-built package and pip-installable.
- **Clean Outputs:**  
  Writes results as CSV with table, column, data type, and assigned category.
- **Modular Codebase:**  
  Well-organized, with extensible submodules for future features.


## Usage

### 0. Requires Python >=3.10,<3.12. Also, install requirements.txt

### 1. **Prepare your configuration**

Edit `config/user_config.yaml`:

```yaml
db_uri: "postgresql://username:password@localhost:5432/yourdb"
schema: "public"
output_filename': 'output/full_schema_classification.csv',
dotenv_path: '.env',
openai_model: 'gpt-3.5-turbo',
output_filename: "output/classification_report.csv"
dama_categories:
  - pii
  - confidential
  - sensitive
  - internal
  - public
  - general
# Add or adjust categories as needed
```

### 2. **Set up your OpenAI API key**

You can either:
- Set `OPENAI_API_KEY` in your environment (`export OPENAI_API_KEY=sk-xxxx...`)
- Or put it in a `.env` file in the project root:
  ```
  OPENAI_API_KEY=sk-xxxx...
  ```

### 3. **Run the Classifier**

From the project root:
```bash
poetry run python bin/run_schema_classification.py
```
or, after install with pip:
```bash
python -m pii-schema-classifier.bin.run_schema_classification
```

### 4. **Check Output**

Find the resulting CSV at the location you specified in `output_filename` (e.g., `output/classification_report.csv`).

---

## Example Output

| table_name | column_name   | data_type | dama_category |
|------------|--------------|-----------|--------------|
| customers  | email        | VARCHAR   | pii          |
| orders     | order_id     | INTEGER   | general      |
| employees  | salary       | NUMERIC   | confidential |
| ...        | ...          | ...       | ...          |

---

## Configuration Details

- **db_uri:**  
  The full SQLAlchemy-style database URI.
- **schema:**  
  The schema name to scan (e.g., `public` for Postgres).
- **output_filename:**  
  Where the classification report CSV should be written.
- **dama_categories:**  
  List of DAMA or organizational data categories for LLM classification (include `'unknown'` or `'other'` for uncategorized columns).

---

## LLM Setup

- By default, uses [OpenAI’s API](https://platform.openai.com/) (set your `OPENAI_API_KEY` in environment or `.env` file).
- You may adapt the LLM code to use other providers or open models.

---

## Advanced

- **Parallelism:**  
  Can be configured to process multiple LLM calls at once for faster runs.
- **Few-Shot Prompting:**  
  Adjust `llm_agent.py` to supply more or different classification examples for your domain.
- **Extendable:**  
  Add your own rules or preprocessing for hybrid (rule+LLM) classification.

---

## Contributing

- Fork this repo and submit pull requests for improvements.
- Please add tests for any new features.

---

## License

MIT License.  
See `LICENSE` file for details.

---

## Authors

- Param Iyer  
  <paramiyer@gmail.com>

---

## Disclaimer

This package uses an external LLM API and sends **only schema metadata** (not actual data values).
Review your organizational privacy policies before use.

---

## Acknowledgements

- [DAMA International](https://www.dama.org/) for their data management framework.
- [OpenAI](https://openai.com/) for language model APIs.
- [SQLAlchemy](https://www.sqlalchemy.org/), [pandas](https://pandas.pydata.org/), and [PyYAML](https://pyyaml.org/).

---
