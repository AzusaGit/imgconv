import util
import os
from pathlib import Path
import pytest
from pyfakefs.fake_filesystem_unittest import Patcher


class TestPathExist:
    def setup_method(self):
        self.patcher = Patcher()
        self.patcher.setUp()

        self.HOME_DIR = str(Path.home())

        self.patcher.fs.create_dir(self.HOME_DIR)
        self.patcher.fs.create_dir(os.path.join(self.HOME_DIR, "Pictures"))
        self.patcher.fs.create_dir(os.path.join(self.HOME_DIR, "Projects"))
        self.patcher.fs.create_file(os.path.join(
            self.HOME_DIR, "Pictures", "test.txt"))

    def teardown_method(self):
        """Clean up the fake filesystem after each test"""
        self.patcher.tearDown()

    @pytest.mark.parametrize("input, expected", [
        (".", True),
        (str(Path.home()), True),
        (os.path.join(str(Path.home()), "Pictures"), True),
        (os.path.join(str(Path.home()), "Pictures", "x"), False),
        (os.path.join(str(Path.home()), "Projects"), True),
        (os.path.join(str(Path.home()), "Pictures", "test.txt"), True),
        (os.path.join(str(Path.home()), "Pictures", "non-existent.txt"), False)
    ])
    def test_check_pathname(self, input, expected):
        assert util.check_pathname(input) == expected


class TestGetFileExt():
    @pytest.mark.parametrize("input, expected", [
        ("input.jpg", "jpg"),
        ("image.png.png", "png"),
        ("error!txt", "Invalid filename"),
        ("valid!jpg.cs", "cs"),
        ("bin", "Invalid filename"),
        ("many.many.many.jpeg", "jpeg"),
        ("x.z.y", "y"),
        ("dot..webp", "webp"),
        ("double_dot..", "Invalid filename")
    ])
    def test_get_file_ext(self, input, expected):
        assert util.get_file_ext(input) == expected
