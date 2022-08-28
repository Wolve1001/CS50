i=input('File name:').strip().lower()
if 'gif' in i:
    print("image/gif")
elif 'png' in i:
    print("image/png")
elif 'jpg' in i:
    print("image/jpeg")
elif 'jpeg' in i:
    print("image/jpeg")
elif 'pdf' in i:
    print("application/pdf")
elif 'zip' in i:
    print("application/zip")
elif 'txt' in i:
    print("text/plain")
else:
    print("application/octet-stream")
