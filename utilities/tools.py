def get_root_path(url):
    path = ""
    chunks = url.split("/")
    for i in range(0,len(chunks)-1):
        path = path+chunks[i]+"/"
    return path
