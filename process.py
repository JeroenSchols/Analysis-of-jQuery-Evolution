import csv
import json


def collectReleases():
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

    for release in releases:
        with open(f"jQuery-linecounts/{release['tag']}.json", mode='r') as json_file:
            data = json.loads(json_file.read())
            release['cloc'] = data

    return releases


def calcOverlaps(releases):
    overlaps = dict()
    for i1, release1 in enumerate(releases):
        release1 = release1['tag']
        overlaps[i1] = dict()
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

                            # Shrink the interval to not overlap any already existing intervals of this file
                            for interval in intervals[file]:
                                if interval['start'] <= start <= interval['end']:
                                    start = interval['end']
                                if interval['start'] <= end <= interval['end']:
                                    end = interval['start']
                            # If the interval is still nonempty, add it
                            if start <= end:
                                intervals[file].append({'start': start, 'end': end})

                    overlapSize = 0
                    for fileIntervals in intervals.values():
                        for interval in fileIntervals:
                            overlapSize += interval['end'] - interval['start']

                    overlaps[i1][i2] = overlapSize
    return overlaps


def calcSymMatrix(releases, overlaps):
    matrix = dict()
    for i1, release1 in enumerate(releases):
        matrix[i1] = dict()
        for i2, release2 in enumerate(releases):
            if i1 < i2:
                similarity = overlaps[i1][i2] / (getNLOC(release1) + getNLOC(release2))
                matrix[i1][i2] = similarity
    return matrix


def normalizeMatrix(matrix):
    # An arbitrary element of the matrix to start with
    maxval = next(iter(next(iter(matrix.values())).values()))

    # Find the biggest value
    for row in matrix.values():
        for value in row.values():
            maxval = max(maxval, value)

    # Divide all values by the maximal value
    for row in matrix.values():
        for i in row.keys():
            row[i] /= maxval


def getNLOC(release):
    return release['cloc']['header']['n_lines']


def main():
    releases = collectReleases()
    overlaps = calcOverlaps(releases)
    similarity_matrix = calcSymMatrix(releases, overlaps)

    normalizeMatrix(similarity_matrix)

    # print(releases)
    # print(overlaps)
    print(similarity_matrix)


if __name__ == "__main__":
    main()
