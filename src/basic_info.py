
import pysam
import numpy as np


def extract_basic_info(bam_file_name, chromosomes):

	# read the bam file
	bam_file = pysam.AlignmentFile(bam_file_name, 'rb')

	# name of chromosomes
	ref_names = bam_file.header.references

	# verify if all the desired chromosomes to be analysed are in the file
	for c in chromosomes:
		if c not in ref_names: 
			raise Exception(f'Chromosome {c} not in the bam file. Available chromosomes are: {ref_names}.')

	# get number of (mapped) reads from the index (.bai) file
	index_stats = bam_file.get_index_statistics()
	n_reads = dict()
	for x in index_stats:
		if x.contig not in chromosomes: continue 
		n_reads[x.contig] = x.mapped
	total_reads = sum(n_reads.values()) 

	# dictionary with lengths of reference chromosomes
	len_chromosomes = {rn: l for rn, l in zip(ref_names, bam_file.header.lengths) if rn in chromosomes}

	# analysis
	print('\nLooping through reads...')
	info_reads = np.zeros((total_reads, 3), dtype = object)
	coverage = {c: np.zeros(len_chromosomes[c]) for c in chromosomes}
	i = 0
	for read in bam_file:

		rn = read.reference_name
		if rn not in chromosomes: continue # ignore reads that do not belong to any chromosome
		if not read.is_mapped: continue # ignore unmapped reads

		seq = read.query_sequence
		info_reads[i] = [rn, read.query_length, seq.count('C') + seq.count('G')]

		ref_pos = read.get_reference_positions()
		coverage[rn][ref_pos] = coverage[rn][ref_pos] + 1
		
		i += 1
		if i % 1e6 == 0:
			print(f'Completed {i/total_reads*100:.2f} %')
	print(f'Completed 100 %')

	bam_file.close()

	return n_reads, len_chromosomes, info_reads, coverage
