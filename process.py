import csv
import json


def main():
    releases = []

    with open('jquery_releases.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                releases.append(row)
            line_count += 1

        print(f'Processed {line_count} lines.')

    i = 1
    l = len(releases) * (len(releases) - 1) / 2
    for i1, release1 in enumerate(releases[:4]):
        for i2, release2 in enumerate(releases[:4]):
            if i1 < i2:
                i += 1
                print(f"Processing {i} out of {l}")
                with open(f"./out/return/{release1['tag']}-{release2['tag']}.txt") as handle:
                    dict = json.loads(handle.read())
                    print(dict)
                    ## @TODO currently doesn't do anything compare the files


if __name__ == "__main__":
    main()
