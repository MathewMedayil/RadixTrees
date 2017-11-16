import time
from Radix import *

def main():
	word_lists = ['words_44k.txt', 'words_109k.txt', 'words_178k.txt', 'words_263k.list', 'words_370k.txt']

	# insert
	print("Insertion:\n")
	insert_times = []
	counter = 1
	for file in word_lists:
		print("Processing file " + str(counter))
		f_read = open('word_list/' + file)
		R = RadixTree()
		start = time.time()
		for word in f_read.readlines():
			R.insert(R.root, word.rstrip())
		endtime = time.time() - start
		print(endtime)
		insert_times.append(endtime)
		f_read.close()
		counter += 1
	f_write_insertradix = open('data/radix_insert.txt', 'w')
	for timetaken in insert_times:
		f_write_insertradix.write(str(timetaken) + '\n')
	f_write_insertradix.close()

	# search
	print("\nSearch:\n")
	word_searches = ['to', 'unappeasableness', 'pseudopseudohypoparathyroidism', 'hippopotomonstrosesquippedaliophobia', 'pneumonoultramicroscopicsilicovolcanoconiosis']
	counter = 1
	search_times = []
	for word in word_searches:
		print("Processing word " + str(counter))
		start = time.time()
		R.search(R.root, word)
		endtime = time.time() - start
		print(endtime)
		search_times.append(endtime)
		counter += 1
	f_write_searchradix = open('data/radix_search.txt', 'w')
	for timetaken in search_times:
		f_write_searchradix.write(str(timetaken) + '\n')
	f_write_searchradix.close()

if __name__ == '__main__':
	main()