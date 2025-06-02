import openai

def identify_pii_agent_llm(column_name, data_type, dama_categories, model="gpt-4o"):
    categories_str = ', '.join(dama_categories)
    example_prompt = f"""
Classify database columns into one of these DAMA data classification categories: {categories_str}.
Respond with only one word from the provided list.
If the category is not obvious, use "unknown".

Examples:
Q: Column name: "email_address", Data type: "VARCHAR"
A: pii

Q: Column name: "order_id", Data type: "INTEGER"
A: general

Q: Column name: "salary", Data type: "NUMERIC"
A: confidential

Q: Column name: "medical_history", Data type: "TEXT"
A: sensitive

Q: Column name: "department", Data type: "VARCHAR"
A: general

Q: Column name: "foo", Data type: "TEXT"
A: general

Now, classify this column:
Q: Column name: "{column_name}", Data type: "{data_type}"
A:
""".strip()

    try:
        openai_client = openai.Client()  # Uses OPENAI_API_KEY from env, loaded at program entry
        response = openai_client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a data privacy and governance expert."},
                {"role": "user", "content": example_prompt}
            ],
            temperature=0
        )
        label = response.choices[0].message.content.strip().lower()
        return label
    except Exception as e:
        print(f"LLM error for column {column_name}: {e}")
        return "general"
