import os
import csv


def main():
    releases = []

    with open('jquery_releases.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            releases.append(row)

    command = "mkdir ../out/return"
    os.system(command)

    for i, release in enumerate(releases):
        release = release['tag']
        # cloc jquery-data/3.4.0/src --skip-uniqueness --json --report-file=../out/cloc/3.4.0.json
        ignoreCommand = f"echo \"jquery-data/{release}/src/intro.js \njquery-data/{release}/src/outro.js\" > clocIgnore.txt"
        countCommand = f"cloc jquery-data/{release}/src --skip-uniqueness --json --exclude-list-file=clocIgnore.txt --report-file=../out/cloc/{release}.json"
        print(f"Executing {i} out of {len(releases)}")
        os.system(ignoreCommand)
        os.system(countCommand)


if __name__ == "__main__":
    main()
