"""
./path/to/a/file --> ./path/to/a/main_file : rename a file
./path/to/a/file --> ./path/to/file : move file to par directory
./one/two/three/four/file --> ./one/three/four/file : create subdirs
three/four under /one and move file to it

"""
from pathlib import Path
import shutil

TEST_FILE_NAME_1 = 'file_1'
TEST_FILE_NAME_2 = 'file_2'

TEST_FOLDER = Path('./path/to/a/')
TEST_FILE_PATH_1 = TEST_FOLDER / TEST_FILE_NAME_1
TEST_FILE_PATH_2 = TEST_FOLDER / TEST_FILE_NAME_2


def make_test_struct():
    """Make test directory with test files."""
    if TEST_FOLDER.exists():
        shutil.rmtree(TEST_FOLDER)
    Path.mkdir(TEST_FOLDER, parents=True)
    Path.touch(TEST_FILE_PATH_1)


def make_file(name):
    """Create file under ./"""
    path = Path(name)
    Path.mkdir(path.parent, parents=True, exist_ok=True)
    Path.touch(path)


def vidir(p1, p2):
    """Test file raname."""
    if p1.parts[:-1] == p2.parts[:-1]:
        p1.rename(p2)


path1 = Path(TEST_FILE_PATH_1)

make_file(path1)

path2 = Path(TEST_FILE_PATH_2)

vidir(path1, path2)
