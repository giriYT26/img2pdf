from PIL import Image
from pathlib import Path
import argparse
from colorama import init, Fore, Style
from tqdm import tqdm

init(autoreset=True)

def CLI():
    parser = argparse.ArgumentParser(prog="Image_to_PDF")
    parser.add_argument(
        "--images","--image","-i",
        nargs= "+",
        required= True,
        help = "Image name or path with[.jpg, .jpeg, .png, .bmp, .tiff, .webp] extension"
        )
    parser.add_argument(
        "-o","--output",
        default="output.pdf",
        help = "pdf name by defalut it's called default"
        )

    return parser.parse_args()

def verify_file(image_path : list[Path]):
    for path in image_path:
        if not path.exists():
            print(Fore.RED+f"+ Error: The File {str(path)} not found")
            exit(1)

        if path.suffix.lower() not in [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp"]: 
            print(Fore.RED+f"+ Error: Unsupported file format {path.name}")
            exit(1)
    
def image_to_pdf():
    args = CLI()           
    image_path = [Path(p).resolve() for p in args.images]
    verify_file(image_path)

    images = []
    for p in tqdm(image_path,desc ="Processing",unit="img"):
        images.append(Image.open(p).convert("RGB"))

    images[0].save(args.output,save_all = True,append_images = images[1:])
    print(Fore.GREEN + Style.BRIGHT + f"\u2714 Successfully converted {len(images)} Images to {args.output}" ) #To print the tick mark either this \u2713 or ✓ ,\u2714 or ✔ 

if __name__ == "__main__":
    image_to_pdf()

