load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("@my_deps//:requirements.bzl", "requirement")


py_binary(
    name = "pandas_ops",
    srcs = ["pandas_ops.py"],
    main = "pandas_ops.py",
    deps = [
        # "@pip_deps//pandas",
        # "@pip_deps//numpy",
        requirement("pandas"),
        requirement("numpy"),
    ],
)


py_binary(
    name = "polars_ops",
    srcs = ["polars_ops.py"],
    main = "polars_ops.py",
    deps = [
        requirement("polars"),
        requirement("numpy"),
    ],
)

py_binary(
    name = "benchmark",
    srcs = ["benchmark.py"],
    main = "benchmark.py",
    deps = [
        ":pandas_ops",
        ":polars_ops",
        "//helpers:helpers",
    ],
)

