import os


def check_pathname(pathname: str) -> bool:
    """Check if pathname exist"""
    pathname = os.path.expanduser(pathname)

    if os.path.exists(pathname):
        return True

    return False


def get_file_ext(filename: str) -> str:
    """Get the file extension"""
    ext = os.path.splitext(filename)
    return ext[len(ext) - 1].lstrip(".") or "Invalid filename"


def get_file_name(filename: str) -> str:
    """Get the file name"""
    return os.path.splitext(filename)[0]
