# scripts/upload_dataset.py

import argparse
from storage_azure.azure.upload_dataset import (upload_dataset)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dataset",
        required=True,
    )

    args = parser.parse_args()
    result = upload_dataset(args.dataset)

    print(result)


if __name__ == "__main__":
    main()