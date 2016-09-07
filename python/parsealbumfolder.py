import os
import json

def parseAlbumFolder(path):
    if not os.path.isfile(path + "/album.json"):
        print path + "/album.json file not found"
        return None

    with open(path + "/album.json") as albumJsonFile:
        albumJsonData = json.load(albumJsonFile)

    # Read all image%d%d%d.json files into images array
    images = []
    index = 1
    imageJsonPath = "%s/image%03d.json" % (path, index)
    while os.path.isfile(imageJsonPath):
        with open(imageJsonPath) as imageJsonFile:
            imageJsonData = json.load(imageJsonFile)
            imageJsonData["path"] = path + "/" + imageJsonData["path"]
            images.append(imageJsonData)

        index += 1
        imageJsonPath = "%s/image%03d.json" % (path, index)

    albumJsonData["images"] = images

    return albumJsonData
