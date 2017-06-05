import parsealbumfolder
import os
import sys
import subprocess

def resizeImage(path):
    if not os.path.isfile(path):
        print "Could not find " + path
        print "Skipping"
        return

    pathWithoutExtension = os.path.splitext(path)[0]
    extension = os.path.splitext(path)[1]
    
    fullSizePath = pathWithoutExtension + "_full" + extension
    if not os.path.isfile(fullSizePath):
        print fullSizePath + " not found, assuming " + path + " is full size image"
        print "Renaming " + path
        os.rename(path, fullSizePath)

    if not os.path.isfile(path):
        resizeFactor = "33%"
        print "Resizing " + fullSizePath + " by " + resizeFactor + " to " + path
        subprocess.call(["convert", fullSizePath, "-resize", resizeFactor, path])

    smallpath = pathWithoutExtension + "_small" + extension
    if not os.path.isfile(smallpath):
        resizeFactor = "400x"
        print "Resizing " + fullSizePath + " to " + resizeFactor + " to " + smallpath
        subprocess.call(["convert", fullSizePath, "-resize", resizeFactor, smallpath])


def main():
    if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
        print "Please provide a valid album folder"
        sys.exit(0)

    path = sys.argv[1]
    albumData = parsealbumfolder.parseAlbumFolder(path)
    resizeImage(path + "/" + albumData["coverimagepath"])
    for imageData in albumData["images"]:
        resizeImage(path + "/" + imageData["path"])


main()