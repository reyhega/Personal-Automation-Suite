import os
import argparse
import logging
from datetime import datetime

logging.basicConfig(
    filename="file_renamer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def rename_files(path, prefix="", suffix=""):

## Check if path exists if not, exit ##

    if not os.path.exists(path):
        logging.error(f"Path not found: {path}")
        print(f"❌ ERROR! Path not found: {path}")
        return
    
## Check if there are files in the specified path ##

    files = os.listdir(path)
    if not files:
        logging.warning(f"No files found in {path}")
        print(f"⚠️ No files found in {path}")
        return

    for file in files:
        old_path = os.path.join(path, file)
        if os.path.isdir(old_path):
            continue # skips directories

        root, ext = os.path.splitext(file)
        timestamp = datetime.now().strftime("%H:%M:%S|%m%d%Y")
        new_name = f"{prefix}{root}{suffix}{ext}"
        
        new_path = os.path.join(path, new_name)

        if os.path.exists(new_path):
            new_name = f"{prefix}{root}{timestamp}{suffix}{ext}"
            new_path = os.path.join(path, new_name)

        try:
            os.rename(old_path, new_path)
            logging.info(f"Renamed: {file} → {new_name}")
            print(f"✅ Renamed {file} → {new_name}")
        except Exception as e:
            logging.error(f"Failed to rename {file}: {e}")
            print(f"❌ Failed to rename {file}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Batch file renamer')
    parser.add_argument('--path', required=True, help='Folder with files to be renamed')
    parser.add_argument('--prefix', '-pf', default="", help='Prefix to be added')
    parser.add_argument('--suffix', '-sf', default="", help='Suffix to be added')
    args = parser.parse_args()
    rename_files(args.path, args.prefix, args.suffix)
