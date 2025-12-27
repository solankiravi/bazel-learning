py_binary(
    name = "app",
    srcs = ["main.py"],
    main = "main.py",
    deps = [
        "//lib:math_lib",        
    ],
)

py_binary(
    name = "read_file",
    srcs = ["read_file.py"],
    
    data = [
        "//config:app_config",
    ],
    deps = [
        "//lib:file_lib",
        "@rules_python//python/runfiles",
    ],
)