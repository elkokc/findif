import os

def walker(root_directory, file_extension):
  res = []
  for dirpath, dirs, files in os.walk(root_directory):
    for filename in files:
      fname = os.path.join(dirpath, filename)
      if fname.endswith(file_extension):
        res.append(fname)
  return res







