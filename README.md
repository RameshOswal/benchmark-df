# Project Name

## Prerequisites

### Install Bazel
1. **Linux/macOS**:
   ```bash
   # Using Bazelisk (recommended)
   npm install -g @bazel/bazelisk

   # Or using Homebrew (macOS)
   brew install bazelisk
   ```

2. **Windows**:
   ```bash
   # Using Chocolatey
   choco install bazelisk
   ```

### Python Setup
1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   
   # On Windows
   .\venv\Scripts\activate
   
   # On Linux/macOS
   source venv/bin/activate
   ```

2. Generate requirements.txt:
   ```bash
   pip freeze > requirements.txt
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Bazel Commands

### Build
```bash
bazel build //src:benchmark
```

### Run
bazel run //src:benchmark -- polars
```Running benchmarks for polars_ops
create_dataframe took 15.2651 seconds to run
Dataframe creation time: 15.265246s
process_dataframe took 0.3914 seconds to run
Dataframe processing time: 0.391443s
```


bazel run //src:benchmark -- pandas
```Running benchmarks for pandas_ops
Dataframe creation time: 2.393626s
process_dataframe took 0.1723 seconds to run
Dataframe processing time: 0.172354s
```



