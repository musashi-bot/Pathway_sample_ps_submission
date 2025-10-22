import pathway as pw

# Define schema for the input CSV
class InputSchema(pw.Schema):
    value: int

# Read the CSV from the 'input' folder
input_table = pw.io.csv.read(
    "./input/",
    schema=InputSchema
)

# Filter rows where value >= 0
filtered_table = input_table.filter(input_table.value >= 0)

# Compute the sum of the remaining values
result_table = filtered_table.reduce(
    sum_value=pw.reducers.sum(filtered_table.value)
)

pw.io.jsonlines.write(result_table, "output.jsonl")

pw.run()

