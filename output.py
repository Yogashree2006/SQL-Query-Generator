def chat(user_input):
    sql = generate_sql(user_input)
    return sql

demo = gr.Interface(
    fn=chat,
    inputs="text",
    outputs="text",
    title="SQL Query Generator",
    description="Convert natural language to SQL query"
)