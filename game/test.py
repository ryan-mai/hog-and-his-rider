import os, zipfile
src = r"C:\Users\mayma\Downloads\TheRiderandHisHog-dists\TheRiderandHisHog-web"
dst = r"C:\Users\mayma\Downloads\TheRiderandHisHog-dists\TheRiderandHisHog-web-upload.zip"
if os.path.exists(dst):
    os.remove(dst)
with zipfile.ZipFile(dst, "w", compression=zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(src):
        for f in files:
            full = os.path.join(root, f)
            arc = os.path.relpath(full, src).replace(os.sep, "/")
            z.write(full, arc)
print("created:", dst)