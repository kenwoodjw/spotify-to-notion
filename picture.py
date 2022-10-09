# save picture to github
import urllib.request, os
from github import Github

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
def save_image_to_github(image_path: str):
    new_image_name = image_path.split('/')[-1]+ ".jpeg"
    urllib.request.urlretrieve(image_path, "/Users/kenwoodchan/Documents/图片/spotify/{}".format(new_image_name))
    #commit to github
    g = Github(GITHUB_TOKEN)
    # Get repository
    repo = g.get_repo("kenwoodjw/spotify_albums_cover")
    print(repo)
    img = open("/Users/kenwoodchan/Documents/图片/spotify/{}".format(new_image_name), 'rb').read()
    repo.create_file(new_image_name, "update", img)
    link = "https://github.com/kenwoodjw/spotify_albums_cover/blob/main/{}".format(new_image_name)
    new_link = link.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    return new_link

