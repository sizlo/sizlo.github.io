import os
import json

def parseAlbumFolder(path):
    if not os.path.isfile(path + "/album.json"):
        print path + "/album.json file not found"
        return None

    with open(path + "/album.json") as albumJsonFile:
        albumJsonData = json.load(albumJsonFile)

    # Path stored for images in json is relative to the folder
    # containing album.json, prepend this to each image path
    index = 0
    for imageJsonData in albumJsonData["images"]:
        fullImagePath = path + "/" + imageJsonData["path"]
        albumJsonData["images"][index]["path"] = fullImagePath
        index += 1

    return albumJsonData
