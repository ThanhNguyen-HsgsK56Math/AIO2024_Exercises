def count_words(file_path):
    file = open(file_path, 'r')
    result = {}
    for line in file:
        words = line.split()
        for word in words:
            if word not in result:
                result[word] = 1
            else:
                result[word] = result[word] + 1
    print(result)