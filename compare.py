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

    i = 0
    l = len(releases) * len(releases) / 2
    for i1, release1 in enumerate(releases):
        for i2, release2 in enumerate(releases):
            if i1 < i2:
                i += 1
                command = f"jsinspect -r json --ignore \".*/outro\.js|.*/intro\.js\" ./jquery-data/{release1['tag']}/src ./jquery-data/{release2['tag']}/src > ../out/return/{release1['tag']}-{release2['tag']}.json"
                print(f"Executing {i} out of {l}")
                os.system(command)


if __name__ == "__main__":
    main()
