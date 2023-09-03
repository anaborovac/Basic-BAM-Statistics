
import argparse
import numpy as np
import os

from basic_info import extract_basic_info
from report import write_to_pdf
from coverage import plot_coverage


parser = argparse.ArgumentParser(description = 'Basic statistics of a BAM file.')
parser.add_argument('bam', default = None, type = str, help = 'BAM file to be analysed')
parser.add_argument('-chromosomes', default = [str(i) for i in range(1, 23)] + ['X'] + ['Y'], type = list, help = 'list of chromosome names included in the analysis')
args = parser.parse_args()

bam_file_name = args.bam 
chromosomes = args.chromosomes

bfn = os.path.basename(bam_file_name)
bfn = bfn.replace('.bam', '')

report_file_name = f'files/report_{bfn}.pdf'
coverage_plot_file_name = f'files/coverage_plot_{bfn}.png'

# EXTRACT BASIC INFO
n_reads, len_chromosomes, info_reads, coverage = extract_basic_info(bam_file_name, chromosomes)

# ANALYSIS
print('\nCalculating metrics...')

total_reads = sum(n_reads.values()) 
len_genome = sum(len_chromosomes.values())

n_atgc = np.sum(info_reads[:, 1]) 
n_gc = np.sum(info_reads[:, 2]) 
mean_len_read = np.mean(info_reads[:, 1])

estimated_coverage = total_reads * mean_len_read / len_genome
gc_percentage = n_gc / n_atgc * 100

calculated_coverage = np.sum([np.sum(v) for v in coverage.values()]) / len_genome

n_covered_bases = np.sum([np.nonzero(v)[0].shape[0] for v in coverage.values()])
breadth_coverage = n_covered_bases / len_genome * 100

print(f'Total number of reads: {total_reads}')
print(f'Total length of the genome: {len_genome}')

print(f'Estimated average coverage across genome: {estimated_coverage:.2f} ({round(estimated_coverage)}x)')
print(f'Calculated average coverage across genome: {calculated_coverage:.2f} ({round(calculated_coverage)}x)')
print(f'Breadth of coverage: {breadth_coverage:.2f} %')

print(f'GC percentage: {gc_percentage:.2f} %')

# PLOT COVERAGE 
plot_coverage(coverage_plot_file_name, chromosomes, coverage)

# MAKE REPORT
write_to_pdf(bam_file_name, report_file_name, n_reads, breadth_coverage, estimated_coverage, calculated_coverage, gc_percentage, coverage_plot_file_name)


