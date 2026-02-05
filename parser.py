import json


def main():
    with open("FolketsHus.json") as f:
        data = json.load(f)

    print(data)


if __name__ == "__main__":
    main()
