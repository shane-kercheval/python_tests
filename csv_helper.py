def open_with_csv(filename, delimiter='\t'):
    data = []
    with open(filename, encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=delimiter)
        for line in reader:
            data.append(line)

    return data

def occurances_in_nested_list(nested_list, search_term):
    count = 0

    for row in nested_list:
        count += row.count(search_term)

    return count
