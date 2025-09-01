"""Remove rows with a missing region from a raw sales CSV."""

import csv
import sys


def main(src, dst):
    with open(src, newline="") as f_in, open(dst, "w", newline="") as f_out:
        reader = csv.DictReader(f_in)
        writer = csv.DictWriter(f_out, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            if row["region"]:
                writer.writerow(row)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
