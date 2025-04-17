import os
import argparse
import subprocess
from datetime import datetime

# Define log path inside the engine folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "conversion_log.txt")

def log(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    entry = f"{timestamp} {message}"
    print(entry)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")

def decompress_nsz_file(nsz_file):
    log(f"Decompressing: {nsz_file}")
    try:
        subprocess.run(["nsz", "-D", nsz_file], check=True)
        os.remove(nsz_file)
        log(f"Successfully converted and deleted: {nsz_file}")
    except subprocess.CalledProcessError as e:
        log(f"Error processing {nsz_file}: {e}")

def decompress_nsz(folder_or_file):
    if not os.path.exists(folder_or_file):
        log(f"Error: Path '{folder_or_file}' does not exist.")
        return

    nsz_files = []

    if os.path.isfile(folder_or_file):
        if folder_or_file.lower().endswith(".nsz"):
            nsz_files.append(folder_or_file)
        else:
            log("Provided file is not an NSZ file.")
            return
    else:
        for root, _, files in os.walk(folder_or_file):
            for file in files:
                if file.lower().endswith(".nsz"):
                    nsz_files.append(os.path.join(root, file))

    if not nsz_files:
        log("No NSZ files found.")
        return

    for nsz_file in nsz_files:
        decompress_nsz_file(nsz_file)

    log("All NSZ files processed.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decompress NSZ files from a folder or single file.")
    parser.add_argument("folder_or_file", nargs="?", help="Path to a folder or single NSZ file.")
    args = parser.parse_args()

    if not args.folder_or_file:
        args.folder_or_file = input("Enter a folder or file path: ").strip()

    decompress_nsz(args.folder_or_file)
