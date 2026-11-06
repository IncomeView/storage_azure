from storage_azure.datasets.catalog import (list_datasets, list_projects, list_domains)

print(list_datasets().head())
print(list_projects().head())
print(list_domains().head())

