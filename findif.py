import re
from walker import walker

# dproject directory
PATH = "D:\\test_project\\"

# extension  js, html, jsp ...
FILE_EXTENSION = ".js"

# searching pattern
PATTERN = "doCall\(\s*'(.*?)',"


def extract_pattern_in_file(text, pttern):
    res = re.findall(pattern, text)
    return res


if __name__== "__main__":
    final_res = []
    files = walker(PATH, FILE_EXTENSION)
    print("Search in {} files".format(len(files)))
    for file in files:
        text = open(file, encoding="utf8").read()
        pattern = PATTERN
        res = extract_pattern_in_file(text, pattern)
        final_res = final_res + res

    print("\n".join(final_res))
    print("{} hits was found".format(len(final_res)))