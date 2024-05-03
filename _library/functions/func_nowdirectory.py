import sys
from pathlib import Path

def get_now_dir():
    this_file_path = Path(sys.argv[0])
    #print(this_file_path.parent)
    return this_file_path.parent