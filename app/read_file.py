from python.runfiles import runfiles
from lib.file_utils import get_content

def file_utils():
    r = runfiles.Create()
    config_path = r.Rlocation("bazel_demo/config/config.json")
    if not config_path:
        raise FileNotFoundError("Config file not found in runfiles.")
    print(f"Config Path: {config_path}")
    print(f"File Content: {get_content(config_path)}")

if __name__ == "__main__":
    file_utils()