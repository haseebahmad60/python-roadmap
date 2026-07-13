from pathlib import Path
from config import categories
import shutil
base_dir=Path(__file__).parent
file_path =base_dir/ "test_files"

def print_everything():
    """Print all filenames in the test_files folder."""
    for path in file_path.iterdir():
        print(path.name)


def find_extension():
    """Print the extension of every file."""
    for path in file_path.iterdir():
        print(path.suffix)


def get_category(file_extension):
    """Return the category of a file based on its extension."""
    for category,extensions in categories.items():
        if file_extension in extensions:
            return category
    return "Unknown"

    """"
    if extension in images:
        return "Images"
    elif extension in media:
        return "Media"
    elif extension in documents:
        return "Documents"
    elif extension in archives:
        return "Archives"
    elif extension in programs:
        return "Programs"
    return "Unknown"
    """

def categorize_files():
    """Print each filename along with its category."""
    for path in file_path.iterdir():
        extension = path.suffix
        category = get_category(extension)
        print(f"{path.name} -> {category}")

def create_category_folder(category):
    folder_path=file_path/category
    folder_path.mkdir(exist_ok=True)
    return folder_path

def move_to_folder(source_file,category,dry_run=True):
   
    if dry_run==True:
        print(f"will move {source_file.name} to {category}")
    else:
        category_folder=create_category_folder(category)
        destination_path=category_folder/source_file.name
        shutil.move(str(source_file),str(destination_path))


def organize_files(dry_run=True):
    for item in file_path.iterdir():
        if not item.is_file():
            continue
        extension = item.suffix
        category = get_category(extension)
        move_to_folder(item, category, dry_run=dry_run)
    print("all the damn files organized successfully")

    """
    
    if dry_run==False:
        for item in file_path.iterdir():
            if not item.is_file():
                        continue
        extension=item.suffix
        category=get_category(extension)
        destination=create_category_folder(category)
        move_to_folder(item,category,dry_run=False)
    else:   
        for item in file_path.iterdir():
            if not item.is_file():
                continue
            extension=item.suffix
            category=get_category(extension)
            move_to_folder(item,category,dry_run=True)
    print("all tfhe damn files organized successfully")
    """


organize_files(dry_run=True)


""""
print("Files:")
print_everything()


print("\nExtensions:")
find_extension()

print("\nCategories:")
categorize_files()
         """