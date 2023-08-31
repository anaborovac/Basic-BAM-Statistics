# Basic statistics of a BAM file

The aim of the project is to extract some information from a BAM file:
- Number of (mapped) reads per chromosome and in total.
- Average coverage across the genome.
- GC percentage across the genome.

The final output is a report in a pdf document.

## Setting up the virtual environment

Create a Python virtual environment using `venv`.
- MacOS: ```python -m venv /path/to/new/virtual/environment```
- Windows: ```c:\>python -m venv c:\path\to\myenv```

Activate the virtual environment.
- MacOS (bash): ```source /path/to/new/virtual/environment/bin/activate```
- Windows (cmd): ```C:\> c:\path\to\myenv\Scripts\activate.bat```

Install required libraries (requirements.txt) using `pip`.
```pip install requirements.txt```

For other operating systems and shell options see [documentation](https://docs.python.org/3/library/venv.html).

## Running the scripts

## Deactivating the virtual environment

Type `deactivate` in your shell.

