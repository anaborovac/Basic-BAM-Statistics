
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def plot_coverage(plot_file_name, chromosomes, coverage):
	
	fig = plt.figure(figsize = (6, 3))
	ax = fig.add_subplot(111)

	i = 0
	chromosomes_end_points = []
	for c in chromosomes:

		v = coverage[c]

		# to reduce the number or points in the plot and make it more readable
		n = v.shape[0] / 100000 
		n = np.round(n, 0)

		v = np.array_split(v, n)

		vmean = list(map(np.mean, v))
		vmax = list(map(np.max, v))
		vmin = list(map(np.min, v))
		x = np.arange(len(v)) + i

		ax.plot(x, vmean, color = 'k', linewidth = 0.5)

		i += x.shape[0]
		chromosomes_end_points.append(i)

	ax.set_yscale('log')
	ax.yaxis.set_major_formatter(lambda x, _: f'{x:g}')

	(ymin, ymax) = ax.get_ylim()

	for c, x in zip(chromosomes, chromosomes_end_points):
		ax.plot([x, x], [ymin, ymax], color = 'k', linestyle = '--', linewidth = 0.5)
	
	ax.set_xlabel('Chromosome', fontsize = 8)
	ax.set_ylabel('Coverage', fontsize = 8)

	ax.set_xticks(chromosomes_end_points)
	ax.set_xticklabels([f'\n{c}' if j % 2 == 1 and chromosomes_end_points[j] - chromosomes_end_points[j-1] < 0.03*i else c for j, c in enumerate(chromosomes)], fontsize = 8, ha = 'right')

	ax.set_yticks(ax.get_yticks())
	ax.set_yticklabels(ax.get_yticklabels(), fontsize = 8)

	ax.set_ylim(bottom = ymin, top = ymax)
	ax.set_xlim(left = 0, right = i)

	fig.tight_layout()

	plt.savefig(plot_file_name)
