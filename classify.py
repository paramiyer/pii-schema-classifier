from .llm_agent import identify_pii_agent_llm

def classify_table_columns(meta_df, dama_categories, openai_model="gpt-4o"):
    categories = []
    for _, row in meta_df.iterrows():
        label = identify_pii_agent_llm(
            row['column_name'],
            row['data_type'],
            dama_categories,
            model=openai_model
        )
        categories.append(label)
    meta_df['dama_category'] = categories
    return meta_df
