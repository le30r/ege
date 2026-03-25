lines = open("22 (2).txt").read().splitlines()

completion_time = {}

for line in lines:
    process_id, duration, dependencies = line.split(maxsplit=2)
    duration = int(duration)

    dependency_ids = []
    for dep_id in dependencies.replace("\"", "").replace(" ", "").split(";"):
        if dep_id != "0":
            dependency_ids.append(dep_id)

    # Если зависимостей нет — процесс независимый
    if not dependency_ids:
        completion_time[process_id] = duration
        continue

    max_dependency_time = max(
        completion_time[dep_id] for dep_id in dependency_ids
    )

    completion_time[process_id] = duration + max_dependency_time

print(max(completion_time.values()))