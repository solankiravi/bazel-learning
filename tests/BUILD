py_test(
    name = "test_math_unit",
    srcs = ["test_math_unit.py"],
    size = "small",
    timeout = "short",
    tags = ["unit"],
    deps = [
        "//lib:math_lib",
        "@my_python_deps//pytest"
    ]
)

py_test(
    name = "test_math_integration",
    srcs = ["test_math_integration.py"],
    size = "small",
    timeout = "short",
    tags = ["integration"],
    deps = [
        "//lib:math_lib",
        "@my_python_deps//pytest"
    ]
)

py_test(
    name = "test_http",
    srcs = ["test_http.py"],
    size = "small",
    timeout = "short",
    tags = ["unit"],
    deps = [
        "//lib:http_lib",
        "@my_python_deps//pytest"
    ]
)

py_test(
    name = "test_files",
    srcs = ["test_files.py"],
    size = "small",
    timeout = "short",
    tags = ["unit"],
    deps = [
        "//lib:file_lib",
        "@my_python_deps//pytest",
        "@rules_python//python/runfiles",
    ]
)
