from google.cloud import bigquery
client = bigquery.Client()


dataset_ref = client.dataset("hacker_news", project="bigquery-public-data")
dataset = client.get_dataset(dataset_ref)