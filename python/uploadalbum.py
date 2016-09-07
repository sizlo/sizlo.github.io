from imgurpython import ImgurClient
import parsealbumfolder
import sys
import os

# Adapted from github examples
def authenticate():
    # Get client ID and secret from auth.ini
    client_id = open("clientid.secret").read()
    client_secret = open("clientsecret.secret").read()

    client = ImgurClient(client_id, client_secret)

    # Authorization flow, pin example (see docs for other auth types)
    authorization_url = client.get_auth_url('pin')

    print("Go to the following URL: {0}".format(authorization_url))

    # Read in the pin, handle Python 2 or 3 here.
    pin = raw_input("Enter pin code: ")

    # ... redirect user to `authorization_url`, obtain pin (or code or token) ...
    credentials = client.authorize(pin, 'pin')
    client.set_user_auth(credentials['access_token'], credentials['refresh_token'])

    print("Authentication successful! Here are the details:")
    print("   Access token:  {0}".format(credentials['access_token']))
    print("   Refresh token: {0}".format(credentials['refresh_token']))

    return client

def parseAlbumData(path):
    albumData = parsealbumfolder.parseAlbumFolder(path)
    if albumData == None:
        print "Problem parsing folder " + path
        print "Exitting"
        sys.exit(0)
    return albumData
    

def uploadImage(client, imageData):
    if not os.path.isfile(imageData["path"]):
        print "Cannot find file " + path
        print "Skipping upload"
        return None
    image = client.upload_from_path(imageData["path"], config=imageData, anon=False)
    print "Uploaded " + image["link"]
    return image

def uploadAlbum(client, albumData):
    album = client.create_album(albumData)
    albumID = album["id"]
    print "Created http://imgur.com/a/" + albumID

    for imageData in albumData["images"]:
        imageData["album"] = albumID
        image = uploadImage(client, imageData)

def main():
    if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
        print "Please supply a valid folder to parse the album from"
        sys.exit(0)

    albumData = parseAlbumData(sys.argv[1])
    client = authenticate()
    uploadAlbum(client, albumData)


main()
