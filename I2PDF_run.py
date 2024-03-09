import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image

def list_and_merge_images_to_pdf(folder_path):
    try:
        # Get the list of files in the folder
        files = os.listdir(folder_path)

        # Filter out only files (excluding directories)
        files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

        # Print the number of files
        #print(f"Number of files in '{folder_path}': {len(files)}\n")

        # Print the name of each file along with its extension
        #for file in files:
            #print(f"File: {file}")

        # Filter for image files
        image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp"}
        image_files = [f for f in files if os.path.splitext(f.lower())[1] in image_extensions]

        if not image_files:
            print("No image files found in the specified folder.")
            return

        # Create 'output_folder' if it doesn't exist
        script_directory = os.getcwd()
        output_folder = os.path.join(script_directory, "output_folder")
        os.makedirs(output_folder, exist_ok=True)

        pdf_output_path = os.path.join(script_directory, "output_folder", f"{os.path.basename(folder_path)}.pdf")

        

        pdf_writer = canvas.Canvas(pdf_output_path, pagesize=letter)

        for image_file in image_files:
            image_path = os.path.join(folder_path, image_file)
            img = Image.open(image_path)
            img_width, img_height = img.size
            pdf_writer.setPageSize((img_width, img_height))
            pdf_writer.drawInlineImage(image_path, 0, 0, width=img_width, height=img_height)
            pdf_writer.showPage()

        pdf_writer.save()

        #print(f"PDF created: {pdf_output_path}")

    except FileNotFoundError:
        print(f"Folder '{folder_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_folder = "input_folder"
    print("Initiating process...")

    if os.path.exists(target_folder) and os.path.isdir(target_folder):
        list_and_merge_images_to_pdf(target_folder)
        print("Process finished, check output folder")
    else:
        print("Invalid folder path. Please provide a valid folder path.")

def process_folder(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        list_and_merge_images_to_pdf(folder_path)
    else:
        print(f"Invalid folder path: {folder_path}")