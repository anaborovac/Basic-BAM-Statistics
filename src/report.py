
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import numpy as np


def write_to_pdf(
    bam_file_name: str,
    report_file_name: str,
    n_reads: dict[str, int],
    mean_len_read: float, 
    std_len_read: float,
    breadth_coverage: float,
    estimated_coverage: float,
    calculated_coverage: float,
    gc_percentage: float,
    plot_file_name: str,
    lengths_plot_file_name: str
) -> None:
	"""
	Input:
		bam_file_name: file location of a .bam file to be analysed
		report_file_name: where report is about to be saved
		n_reads: dictionary with numbers of reads per chromosome
		mean_len_read: average read length
		std_len_read: standard deviation of read length
		breadth_coverage: breath of the coverage (percent of covered reference bases)
		estimated_coverage: estimated average coverage calculated as total_reads * mean_len_read / len_genome
		calculated_coverage: average coverage across genome
		gc_percentage: ratio of G's and C's in reads
		plot_file_name: location of the plot visualizing average coverage across genome 
		lengths_plot_file_name: location of the plot visualizing lengths of reads
	"""

	pdf_canvas = canvas.Canvas(report_file_name, pagesize = A4)

	h = 100
	v = 750
	par_space = 30
	line_space = 15
	tab_space = 80

	pdf_canvas.setFontSize(20)
	pdf_canvas.drawString(h, v, 'BASIC STATISTICS OF A BAM FILE')

	pdf_canvas.setFontSize(12)

	v -= par_space
	pdf_canvas.drawString(h, v, f'BAM file: {bam_file_name}')

	v -= par_space
	total_reads = sum(n_reads.values())
	pdf_canvas.drawString(h, v, f'Total number of reads: {total_reads}')

	v -= line_space
	n_one_column = np.ceil(len(n_reads.keys()) / 3)
	pdf_canvas.drawString(h, v, f'Number of reads per chromosome:')
	column = 0
	row = 0
	for i, (c, l) in enumerate(n_reads.items()):
		if i % n_one_column == 0:
			column += 1
			row = 1
		row += 1
		pdf_canvas.drawString(h + column * tab_space, v - row * line_space, f'{c}: {l}')
	v -= (row + 1) * line_space

	v -= par_space
	pdf_canvas.drawString(h, v, f'Average read length (standard deviation): {mean_len_read:.2f} ({std_len_read:.2f})')

	v -= par_space
	pdf_canvas.drawString(h, v, f'Breadth of coverage: {breadth_coverage:.2f} %')
	v -= line_space
	pdf_canvas.drawString(h, v, f'Estimated coverage across genome: {estimated_coverage:.2f} ({round(estimated_coverage)}x)')
	v -= line_space
	pdf_canvas.drawString(h, v, f'Calculated coverage across genome: {calculated_coverage:.2f} ({round(calculated_coverage)}x)')

	v -= par_space + 300
	pdf_canvas.drawImage(plot_file_name, 0, v)

	v -= par_space
	pdf_canvas.drawString(h, v, f'Average GC percentage: {gc_percentage:.2f} %')

	pdf_canvas.showPage()

	h = 100
	v = 750

	pdf_canvas.setFontSize(20)
	pdf_canvas.drawString(h, v, 'Additional statistics')

	pdf_canvas.setFontSize(12)

	v -= par_space + 300
	pdf_canvas.drawImage(lengths_plot_file_name, 0, v)

	pdf_canvas.save()