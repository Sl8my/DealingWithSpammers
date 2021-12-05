import re
pattern = re.compile("[\w.+-]+@in.[\w-]+\.eu")

for i, line in enumerate(open('output.txt')):
    for match in re.finditer(pattern, line):
        print(match.group(), file=open("output_clean.txt", "a"))