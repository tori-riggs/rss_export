import requests
import json
import os
import time
from feedbin_config import username, password, path


session = requests.Session()
session.auth = (f"{username}", f"{password}")
path = (f"{path}")
date = "2024-09-25"


def write( feed_id, title, start, end ):
    end = end + 1
    print(f"\nExporting: '{title}' (pages {start} - {end})")
    file_name = (os.path.join(path, f"{date} Feedbin {title}.txt"))

    with open(file_name, "w") as f:
        for page_number in range(start, end):
            url = f"https://api.feedbin.com/v2/feeds/{feed_id}/entries.json?page={page_number}"
            print("\t" + url)
            response = session.get(url)
            
            if (response.status_code != 200):
                print(f"Unexpected response {response.status_code}: {response.text}")
                exit(1)
                
            data = response.json()
            
            f.write(json.dumps(data, indent=2, ensure_ascii=False))
            f.write("\n")
            if (page_number % 5 == 0):
                time.sleep(5)


def main():
    """
    Maybe put this stuff in config?
    :return:
    """
    write( 849084, "The Verge", 1, 5 )
    write( 2036837, "The Gamer", 1, 11 )
    write( 1422183, "PCGamesN", 1, 10 )
    write( 1408992, "gameindustry biz", 1, 5 )
    write( 2191136, "GameDeveloper", 1, 5 )
    write( 2247279, "Gaming Alexandria", 1, 4 )
    write( 2247274, "Video Game History Foundation", 1, 2 )


main()