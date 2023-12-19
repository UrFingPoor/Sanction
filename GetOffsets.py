import requests, os
from tqdm import *

def get_download(url, filename):
    with requests.get(url, stream=True) as r:
        with open(filename, 'wb') as f:           
            bar = tqdm(total=int(r.headers['Content-Length']), colour='green', desc=print('Downloading Update, Please Wait'))
            for data in r.iter_content(chunk_size=8192):
                if data:  
                    f.write(data)
                    bar.update(len(data))
def main():
    cleanup = input("Would You Like To Remove The Old Config?(Y/N): ")
    if os.path.isfile("sanction.json"):
        if cleanup == "y" or cleanup == "Y":
            os.remove("sanction.json")
            print("Removed Old Config!")
    download = input("Would You Like To Download The Sanction.json?(Y/N): ")
    if download == "y" or download == "Y":
      get_download("https://raw.githubusercontent.com/UrFingPoor/Sanction/main/sanction.json", "sanction.json")

if __name__ == '__main__':
    main()