import csv #  добавляем библиотеку для работы с csv

f = open("22 (1) (3).csv") # читаем файл с данными
csv_reader = csv.reader(f, delimiter = ";") # создаём читатель csv-формата из файла с разделителем ;
processes = {} # создаём словарь с процессами вида "id процесса: (время начала, время завершения)"
for row in csv_reader: # по каждой строке из файла
    process_id = row[0] # id процесса
    time = int(row[1]) # время выполнения (преобразовываем в число)
    dependencies = row[2]  # зависимости процесса

    # если независимый процесс
    if dependencies == "0":
        processes[process_id] = (0, time) # просто записываем его время выполнения (время выполнения = время работы процесса), время начала = 0
        continue # пропускаем всё что ниже, переходим к следующей строке

    # номера зависимостей
    process_dependencies = dependencies.split(";") # разделяем строку зависимостей на список 1;2 -> [1, 2]

    dependencies_times = [] # пустой список со временем окончания работы родительских процессов

    for dep in process_dependencies: # для каждого родительского процесса
        _, dependency_time = processes[dep] # находим время окончания работы
        dependencies_times.append(dependency_time) # сохраняем в список окончания работы родительских процессов

    end_time = max(dependencies_times) # находим максимальное время окончания

    processes[process_id] = (end_time, time + end_time) # прибавляем время работы ко времени окончания родительского процесса и сохранияем, время начала = время окончания родительского процесса


sorted_processes = sorted(processes.items(), key = lambda item: item[1][1])

count = 0
for k, v in sorted_processes:
    count += 1
    print(count, k, v)
#лямбда
# count = 0
# for v in sorted(processes.values(), key = lambda  x: x[1]):
#     begin_time, end_time = v
#     if count == 69:
#         print(begin_time, end_time)
#         break
#     count += 1

#Определите, через какое время после запуска первых процессов будет завершено 70 процессов. В ответе укажите целое число  — время в мс.






