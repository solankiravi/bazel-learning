import pytest
from python.runfiles import runfiles
from lib.file_utils import get_content

class TestFileUtils:
    def test_file_read(self):
        r = runfiles.Create()
        config_path = r.Rlocation("bazel_demo/config/config.json")
        content = get_content(config_path)
        assert content["name"] == "bazel-demo"
        assert content["version"] == "1.0.0"