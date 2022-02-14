
def bumpVersion(file_loc, which="patch", dry_run = False, all_matching_lines = False):
  if which not in ["major", "minor", "patch"]:
    print(f"Argument must be one of major, minor, or patch, instead was {which}")
    raise ValueError(which)

  with open(file_loc, "r") as f:
    lines = []
    linesAltered = 0
    while s:= f.readline():
      if s.startswith("version"):
        linesAltered += 1
        if "'" in s: quote = "'"
        if '"' in s: quote = '"'
        vers = s.split("=")[1].replace(quote, "").replace(' ', '').replace('\n', '').split('.')
        vers = [int(x) for x in vers]
        while len(vers) < 3: vers.append(0)
        major, minor, patch = vers
        if which == "major":
          major += 1
          minor, patch = 0, 0
        elif which == "minor":
          minor +=1
          patch = 0
        elif which == "patch":
          patch +=1

        lines.append(f'version={quote}{major}.{minor}.{patch}{quote}\n')
      else:
        lines.append(s)

  


  if dry_run:
    [print(line) for line in lines]
  elif linesAltered == 0:
    print("No changes were made. Do you have a line that starts with 'version' ?")
  elif linesAltered > 1:
    print("More than one line has been altered, this is unexpected. Set 'all_matching_lines' to True if this is intended.")
  else:
    with open(file_loc, 'w') as f:
      f.writelines(lines)
        