import os
import csv


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

    command = "mkdir ../out/return"
    os.system(command)

    i = 0
    l = len(releases) * len(releases) / 2
    for i1, release1 in enumerate(releases):
        for i2, release2 in enumerate(releases):
            if i1 < i2:
                i += 1
                ## @TODO ignore /src/intro.js and /src/outro.js as these are not properly formatted javascript files on which jsinspect crashes.
                command = f"jsinspect -r json ./jquery-data/{release1['tag']}/src ./jquery-data/{release2['tag']}/src > ../out/return/{release1['tag']}-{release2['tag']}.txt"
                print(f"Executing {i} out of {l}")
                os.system(command)


if __name__ == "__main__":
    main()
