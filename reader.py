import sys
import csv

arg = sys.argv[1:]

input_file = arg[0]
output_file = arg[1]
instructions = arg[2:]


def read_file(input_file, output_file):
    file_content = []
    with open(input_file, mode="r") as file:
        for row in file.readlines()[1:7]:
            row = row.replace("\n", "")
            row = row.split(",")
            file_content.append(row)

    actions = []  # INSTRUCTIONS
    for p in instructions:
        pp = p.split(',')
        nowe_polecenie = [int(pp[0]), int(pp[1]), pp[2]]
        actions.append(nowe_polecenie)

    for a in actions:
        numer_wiersza = a[0]
        numer_kolumny = a[1]
        wartosc_do_zmiany = a[2]

        file_content[numer_wiersza][numer_kolumny] = wartosc_do_zmiany


    with open(output_file, mode="w", newline="") as f:
        writer = csv.writer(f)
        for line in file_content:
            writer.writerow(line)
            print(file_content)

read_file(input_file, output_file)

