import os

def list_aiff_files(directory: str) -> list[str]:
    files = []
    for filename in os.listdir(directory):
        if filename.lower().endswith('.aiff'):
            full_path = os.path.join(directory, filename)
            files.append(full_path)
    return files