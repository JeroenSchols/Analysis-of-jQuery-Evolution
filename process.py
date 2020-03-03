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

    matches = dict()
    for i1, release1 in enumerate(releases):
        release1 = release1['tag']
        matches[i1] = dict()
        for i2, release2 in enumerate(releases):
            release2 = release2['tag']
            if i1 < i2:
                with open(f"./out/return/{release1}-{release2}.txt", encoding='cp850') as handle:
                    jsInspectResults = json.loads(handle.read())
                    intervals = {}

                    # Go over all duplication matches
                    for match in jsInspectResults:
                        # Check to make sure they are not just matches only within the same version
                        includesR1 = False
                        includesR2 = False
                        for instance in match['instances']:
                            version = instance['path'].split('/')[2]
                            if version == release1:
                                includesR1 = True
                            if version == release2:
                                includesR2 = True

                        # Only consider matches between different versions
                        if (not includesR1) or (not includesR2):
                            break

                        # Add the new intervals of these matches
                        for instance in match['instances']:
                            file = instance['path']
                            version = instance['path'].split('/')[2]
                            start = int(instance['lines'][0])
                            end = int(instance['lines'][1])
                            if file not in intervals.keys():
                                intervals[file] = []

                            # TODO Handle intervals gracefully instead of blatantly adding
                            intervals[file].append({'start': start, 'end': end})

                    overlapSize = 0
                    for fileIntervals in intervals.values():
                        for interval in fileIntervals:
                            overlapSize += interval['end'] - interval['start']

                    matches[i1][i2] = overlapSize
    print(matches)


if __name__ == "__main__":
    main()
