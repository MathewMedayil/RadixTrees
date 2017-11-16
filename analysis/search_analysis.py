import matplotlib.pyplot as plt
import numpy as np

def main():
	f1 = open("../data/radix_search.txt")
	radix_list = f1.readlines()
	radix_list = [float(i.rstrip()) for i in radix_list]
	f1.close()

	f1 = open("../data/ternarysearchtree_search.txt")
	tst_list = f1.readlines()
	tst_list = [float(i.rstrip()) for i in tst_list]
	f1.close()

	f1 = open("../data/trie_search.txt")
	trie_list = f1.readlines()
	trie_list = [float(i.rstrip()) for i in trie_list]
	f1.close()

	builds = np.array([2, 16, 30, 36, 45])
	y_stack = np.row_stack((radix_list, tst_list, trie_list)) 

	fig = plt.figure(figsize=(11,8))
	fig.canvas.set_window_title('Analysis of Search')
	ax1 = fig.add_subplot(111)

	ax1.plot(builds, y_stack[0,:], label='Radix Tree', color='c', marker='o')
	ax1.plot(builds, y_stack[1,:], label='Ternary Search Tree', color='g', marker='o')
	ax1.plot(builds, y_stack[2,:], label='Trie', color='r', marker='o')

	plt.xticks(builds)
	plt.xlabel('Length of words')
	plt.ylabel('Time taken (seconds)')
	plt.title('Length of words Vs. Time Taken')

	handles, labels = ax1.get_legend_handles_labels()
	lgd = ax1.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.2,0.98))
	ax1.grid('on')

	plt.savefig('search.png')
	plt.show()

if __name__ == '__main__':
	main()