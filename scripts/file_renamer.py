import os
import argparse

def rename_files(path, prefix="", sufix=""):
    for file in os.listdir(path):
        root, ext = os.path.splitext(file)
        new_name = f"{prefix}{root}{sufix}{ext}"
        old_path = os.path.join(path, file)
        new_path = os.path.join(path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed {file} → {new_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Batch file renamer')
    parser.add_argument('--path', required=True, help='Folder with files to be renamed')
    parser.add_argument('--prefix', '-pf', default="", help='Prefix to be added')
    parser.add_argument('--sufix', '-sf', default="", help='Suffix to be added')
    args = parser.parse_args()
    rename_files(args.path, args.prefix, args.sufix)
