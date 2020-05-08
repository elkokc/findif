# findif
Tool for extracting some info from you project's source code by regex pattern

# Installation & Usage
```
git clone https://github.com/elkokc/findif.git
cd findif
pip install requests
python3 findif.py --path /home/admin/project_directory --pattern "doCall\(\s*'(.*?)'," --extension .js
```

Options
-------
```
It is preferable work in editor mode in order to manage code for a particular task, but it can be easily launched in console.

usage: findif.py [-h] [--path PATH] [--extension EXTENSION]
                 [--pattern PATTERN] [--mode MODE]

optional arguments:
  -h, --help            show this help message and exit
  --path PATH           root directory ( it goes recursive)
  --extension EXTENSION, -e EXTENSION
                        File extension ex ".php".
  --pattern PATTERN     regex pattern, ex: `doCall\(\s*'(.*?)',`
  --mode MODE, -m MODE  "findif" - aimed to find a pattern or "walker" - just
                        return list of files with required extension
  ```
