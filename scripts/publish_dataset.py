# scripts/publish_dataset.py

import argparse
from storage_azure.pipelines.publish_dataset import (publish_dataset)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dataset",
        required=True,
    )

    args = parser.parse_args()
    result = publish_dataset(args.dataset)

    print(result)


if __name__ == "__main__":
    main()