
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import numpy as np


def write_to_pdf(bam_file_name, report_file_name, n_reads, breadth_coverage, estimated_coverage, calculated_coverage, gc_percentage, plot_file_name):

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
	pdf_canvas.save()