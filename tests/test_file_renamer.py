import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import shutil
import pytest
from scripts.file_renamer import rename_files

TEST_DIR = "tests/tmp_files"

## Decorator that marks the function as a fixture, this will run for all functions since 'autouse=True' ##

@pytest.fixture(scope="function", autouse=True)

def setup_and_cleanup():
    ## Create temporary folder with test files before each test ##
    os.makedirs(TEST_DIR, exist_ok=True)
    # Create test files
    open(os.path.join(TEST_DIR, "file1.txt"), "w").close()
    open(os.path.join(TEST_DIR, "file2.txt"), "w").close()
    yield
    # Remove files
    shutil.rmtree(TEST_DIR)

def test_prefix():
    rename_files(TEST_DIR, prefix="IMG_")
    files = os.listdir(TEST_DIR)
    assert all(f.startswith("IMG_") for f in files), "Not all files have prefix applied"

def test_suffix():
    rename_files(TEST_DIR, suffix="_final")
    files = os.listdir(TEST_DIR)
    assert all(f.endswith("_final.txt") for f in files), "Not all files have suffix applied"

def test_no_files_found(tmp_path):
    rename_files(tmp_path)
    assert os.listdir(tmp_path) == [], "Folder should remain empty"

def test_invalid_path():
    fake_path = "invalid_folder"
    rename_files(fake_path)
    assert not os.path.exists(fake_path), "Invalid path should not be created"