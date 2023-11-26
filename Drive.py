import requests
import os
from setup import *


parser = argparse.ArgumentParser(
    description="download from google drive by id tag (id file which you want to downloaded)"
)
parser.add_argument(
    "-id",
    "--id",
    type=str,
    help="To get id from element : ctrl + shift + i , then click to body & ctrl + f (data-id) and get this value you find it in div tag and you can sure from file type in same div (data-target='{file type}')",
)
parser.add_argument("-dir", "--directorty", type=str, help="your directory")
parser.add_argument("-n", "-name", "--name", type=str, help="file name")

args = parser.parse_args()


if __name__ == "__main__":
    print(args)
    file_id = f"{args.id}"
    destination = f"{args.directorty}/{args.name}"
    download_file_from_google_drive(file_id, destination)
