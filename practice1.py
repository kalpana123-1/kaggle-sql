from google.cloud import bigquery

# Create a "Client" object
client = bigquery.Client()


# Construct a reference to the "hacker_news" dataset
dataset_ref = client.dataset("hacker_news", project="bigquery-public-data")
dataset = client.get_dataset(dataset_ref)

# List of all the tables
tables = list(client.list_tables(dataset))
for table in tables:  
    print(table.table_id)


# Fecth full table
table_ref = dataset_ref.table("full")
table = client.get_table(table_ref)


# Print information on all the columns in the full table
table.schema


# First five lines of the full table
client.list_rows(table, max_results=5).to_dataframe()


# First five entries in the by column of the full table
client.list_rows(table, selected_fields=table.schema[:1], max_results=5).to_dataframe()