import os
import json

def parseAlbumFolder(path):
    if not os.path.isfile(path + "/album.json"):
        print path + "/album.json file not found"
        return None

    with open(path + "/album.json") as albumJsonFile:
        albumJsonData = json.load(albumJsonFile)

    return albumJsonData
