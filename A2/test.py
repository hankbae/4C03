import os

def get_file_info():
    """ Get file info in the local directory (subdirectories are ignored) 
    Return: a JSON array of {'name':file,'mtime':mtime}
    i.e, [{'name':file,'mtime':mtime},{'name':file,'mtime':mtime},...]
    Hint: a. you can ignore subfolders, *.so, *.py, *.dll
          b. use os.path.getmtime to get mtime, and round down to integer
    """
    file_arr = []
    # not sure if it works
    # print(os.listdir("."))
    for f in os.listdir("."):
        if os.path.isfile(f) and not f.endswith(".so") and not f.endswith(".py") and not f.endswith(".dll"):
                file_arr.append({'name': f, 'mtime': os.path.getmtime(f)})
    return file_arr
print(get_file_info())
