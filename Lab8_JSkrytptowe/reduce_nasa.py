input_path = 'NASA'
output_path = 'NASA_reduced'
spliter = 100

with open(input_path, 'r', encoding='utf-8') as file, open(output_path, 'w', encoding='utf-8') as outfile:
    i = 0
    for index, line in enumerate(file):
        if index % 100 == 0:
            outfile.write(line)
            print(i)
            i += 1
