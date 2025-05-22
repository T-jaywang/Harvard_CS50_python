import sys
import os
from PIL import Image, ImageOps




def main():
    input_file, output_file = evaluate_args()
    overlay_shirt(input_file, output_file)


def evaluate_args():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments.")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments.")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    ext = (".jpg",".jpeg",".png")

    input_file_ext = os.path.splitext(input_file)[1].lower()
    output_file_ext = os.path.splitext(output_file)[1].lower()

    if input_file_ext not in ext:
        sys.exit("Invalid input.")
    if output_file_ext not in ext:
        sys.exit("Invalid output.")
    if input_file_ext != output_file_ext:
        sys.exit("Input and output have different extensions.")
    
    if not os.path.exists(input_file):
        sys.exit("First file not found.")

    return (input_file, output_file)


def overlay_shirt(input_file, output_file):
    shirt = Image.open(os.path.join(os.path.dirname(__file__), "shirt.png"))
    photo = Image.open(input_file)
    
    photo = ImageOps.fit(photo, shirt.size)

    photo.paste(shirt,(0, 0),shirt)
    photo.save(output_file)



if __name__ == "__main__":
    main()