import argparse
import re
import sys

from walker import walker


settings = {
    "path" : "/tmp/project/",
    "extension" : ".js",
    "pattern" : "doCall\(\s*'(.*?)',",
    "mode" : "findif"
}

if (len(sys.argv) > 1):
    console_mode = True
    parser = argparse.ArgumentParser(description='Command line mode')
    parser.add_argument('--path', type=str,
                        help='root directory ( it goes recursive)')
    parser.add_argument('--extension', '-e', type=str,
                        help='File extension ex ".php". ', default=".php")
    parser.add_argument('--pattern', type=str,
                        help="regex pattern, ex: `doCall\(\s*'(.*?)',`")
    parser.add_argument('--mode', '-m', type=str,
                        help='"findif" - aimed to find a pattern or "walker" - just return list of files with required extension', default="findif")

    args = parser.parse_args()
    if(not args.path):
        print("'--scope' was omited")
        exit(-1)
    if (not args.pattern):
        print("'--scope' was omited")
        exit(-1)
    settings["path"] = args.path
    settings["extension"] = args.extension
    settings["pattern"] = args.pattern
    settings["mode"] = args.mode




def extract_pattern_in_file(text, pttern):
    res = re.findall(pattern, text)
    return res


def grep_pattern():
    global pattern, final_res
    print("Search in {} files".format(len(files)))
    for file in files:
        text = open(file, encoding="utf8", errors="ignore").read()
        pattern = settings["pattern"]
        res = extract_pattern_in_file(text, pattern)
        final_res = final_res + res
    print("\n".join(final_res))
    print("{} hits was found".format(len(final_res)))


if __name__== "__main__":
    final_res = []
    files = walker(settings["path"], settings["extension"])
    if(settings["mode"] == "findif"):
        grep_pattern()
    else:
        print("\n".join(files))
