import csv
from itertools import count
from time import process_time

f = open("22 (1) (4).csv")
csv_reader = csv.reader(f, delimiter = ",")
processes = {}
k = 0
for row in csv_reader:
    process_id = row[0]
    time = int(row[1])
    dependencies = row[2]

    if dependencies == "0":
        processes[process_id] = time
        continue

    process_dependencies = dependencies.split(";")
    dependencies_times = []

    for dep in process_dependencies:
        dependency_time = processes[dep]
        dependencies_times.append(dependency_time)
    end_time = max(dependencies_times)
    processes[process_id] = time + end_time
k = 0
for process, end_time in sorted(processes.items(), key = lambda kv: kv[1]):
    k += 1
    print(k, process, end_time)