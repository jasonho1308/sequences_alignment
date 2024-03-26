import csv
import os
from collections import Counter
import ast
import json


def mutation_count():
    file_dir = os.listdir("output/csv/AA")
    count_summary = {}
    for file in file_dir:
        if file.endswith(".csv"):
            with open(f"output/csv/AA/{file}", "r") as f:
                count_summary[file] = {}
                data = csv.DictReader(f)
                for row in data:
                    list_i = ast.literal_eval(row["Amino Acids variations"])
                    counts = Counter(list_i)
                    count_summary[file][row["Position"]] = dict(counts)
    with open("output/mutation_count.json", "w") as f:
        json.dump(count_summary, f, indent=4)


if __name__ == "__main__":
    mutation_count()
