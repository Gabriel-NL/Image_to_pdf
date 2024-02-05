import os
import time
import progressbar
from I2PDF_run import process_folder

def process_folders_with_progress(subfolders):
    total_folders = len(subfolders)
    
    # You can customize the progress bar appearance and behavior as needed
    bar = progressbar.ProgressBar(maxval=total_folders, \
        widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()

    for i, subfolder in enumerate(subfolders):
        process_folder(subfolder)
        time.sleep(0.1)  # Simulating some work being done

        # Update the progress bar
        bar.update(i + 1)

    bar.finish()

if __name__ == "__main__":
    main_folder = input(r"Enter the main folder path: ")
    print("If any of the subfolders has too many images, this could take a while.")
    print("Please, wait until the process is finished")
    print("Converting all subfolders into pdf...")
    if os.path.exists(main_folder) and os.path.isdir(main_folder):
        os.system('cls')
        subfolders = [f.path for f in os.scandir(main_folder) if f.is_dir()]
        
        process_folders_with_progress(subfolders)
    else:
        print("Invalid main folder path. Please provide a valid folder path.")
