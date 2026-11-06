# scripts/discover_adls.py

from storage_azure.azure.containers import (list_containers, list_paths)


def main():
    print("\nContainers:\n")

    for container in list_containers():
        print(f"- {container}")
        paths = list_paths(container)

        for path in paths:
            print(f"  {path}")


if __name__ == "__main__":
    main()