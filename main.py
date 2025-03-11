import argparse
import os
import sys
import util
from pathlib import Path
from PIL import Image


def main():
    parser = argparse.ArgumentParser(description="check if file exists.")
    parser.add_argument("filename", type=str, help="filename input")
    parser.add_argument("output", type=str,
                        help="output filename")
    parser.add_argument("-p", type=str, default=".",
                        help="output pathname (default: current directory)")
    args = parser.parse_args()

    success = convert_img(args.filename, args.output, args.p)
    if not success:
        sys.exit(1)

    print("Success")


def convert_img(filename: str, output: str, output_path=".") -> bool:
    """Convert image to desired output"""
    if not util.check_pathname(filename):
        print("File doesn't exist")
        return False

    if not util.check_pathname(output_path):
        print("Output path doesn't exist")
        return False

    file_ext = util.get_file_ext(filename)
    if file_ext == "Invalid filename":
        print("Invalid input filename")
        return False

    output_name, output_ext = os.path.splitext(output)
    if not output_ext:
        temp = output_name
        output_ext = "." + temp
        output_name = util.get_file_name(filename)

    valid_ext = Image.registered_extensions().keys()
    if "." + file_ext not in valid_ext or output_ext not in valid_ext:
        print("Invalid file convertion")

        return False
    with Image.open(filename) as img:
        try:
            output_path = Path(output_path).expanduser().resolve()
            img.save(output_path / f"{output_name}{output_ext}")
        except ValueError:
            print("Invalid output format")
            return False
        except OSError as err:
            print(f"Unexpected error occured: {err}")
            return False

    return True


if __name__ == "__main__":
    main()
