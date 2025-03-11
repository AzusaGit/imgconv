# Image Converter
Convert image extension to other format.

### Examples
Convert image and create new filename:

`imgconv img.png new.jpg`

Convert image but don't rename:

`imgconv img.png jpg`

You can also use `-p` flag to specify where to put the output file:

`imgconv img.png jpg -p ~/Pictures/`
`imgconv img.png jpg -p D://my_folder/`

By default, output will always be in the current directory.

### Supported Formats
Here are the list of supported formats:
*https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html*

### Used libraries
- argparse
- pillow
- pytest
