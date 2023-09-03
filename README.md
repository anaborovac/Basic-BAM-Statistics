# Basic statistics of a BAM file

The aim of the project is to extract some information from a BAM file:
- Number of (mapped) reads per chromosome and in total.
- Average estimated and calculated coverage across the genome.
- GC percentage across the genome.

The final output is a report in a pdf document.

## 1) Setting up the virtual environment

Create a Python virtual environment using `venv`.
- MacOS: ```python -m venv <path_to_myenv>```
- Windows: ```c:\>python -m venv <path_to_myenv>```

Activate the virtual environment.
- MacOS (bash): ```source <path_to_myenv>/bin/activate```
- Windows (cmd): ```C:\> <path_to_myenv>\Scripts\activate.bat```

Install required libraries ([requirements.txt](https://github.com/anaborovac/Basic-BAM-Statistics/blob/main/requirements.txt)) using `pip`:
```pip install requirements.txt```

For other operating systems and shell options see [documentation](https://docs.python.org/3/library/venv.html).

## 2) Running the script

Run the [`analysis.py`](https://github.com/anaborovac/Basic-BAM-Statistics/blob/main/src/analysis.py) script by typing the following in the shell: ```python src/analysis.py <bam_file_name>.bam```

By default chromosomes [1, 2, ..., 22, X, Y] are analysed. If you would like to analyse different ones use the flag `-chromosomes`, e.g. ```python analysis.py <bam_file_name>.bam -chromosomes [1, 2, X]```

*Note*: For running the script a corresponding `.bai` file needs to exist. In case it does not exist, it can be created with `samtools` and the [`index`](http://www.htslib.org/doc/samtools-index.html) function.

The final report is saved in `files/report_<bam_file_name>.pdf`. (Plot visualising average coverage across the genome is saved in `files/coverage_plot_<bam_file_name>.png`)

## 3) Deactivating the virtual environment

Type `deactivate` in your shell.

