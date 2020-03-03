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

    # @TODO im not sure whether this function made sense.
    # Side-note, I was not 100% sober when writing this. Have fun future me Look at all that indentation booiii
    matchedValues = []
    for i1, release1 in enumerate(releases):
        matchedValues.append([])
        for i2, release2 in enumerate(releases):
            if i1 < i2:
                with open(f"./out/return/{release1['tag']}-{release2['tag']}.txt", encoding='cp850') as handle:
                    dict = json.loads(handle.read())

                    overlap = 0
                    for match in dict:
                        version = match['instances'][0]['path'].split('/')[2]
                        for instance in match['instances']:
                            if instance['path'].split('/')[2] != version:
                                overlap += (instance['lines'][1] - instance['lines'][0]) * len(match['instances'])
                                break
                    matchedValues[i1].append(overlap)
    print(matchedValues)


if __name__ == "__main__":
    main()
