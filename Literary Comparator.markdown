## The reason we choose Julia:
	Julia is generally fast than most of other languages due to its JIT compilation since it includes a compiler as part of its runtime environment.

## Similarity Score is evaluated by two standards, each has 0.5 point counting towards the total score.
The first one is to compare the average sentence lengths of the two texts, since books in different genre usually have very different sentence lengths. E.g. a philosophy book tends to have much longer sentences than a math textbook.
The score is calculated by (Average sentence length of the longer-average-sentence-length text)/(Average sentence length of the shorter-average-sentence-length text).

	The second one is to compare the total number of sentences in the two different books. The score is calculated by (the number of sentences of the fewer-sentence book)/(the number of sentences of the more-sentences book).

	Add the two scores we get the final score.

## Complexity of each step: 
	1. Clean text for text1: O(n)
	2. Count words for text1: O(n)
	3. Clean text for text2: O(n)
	4. Count words for text2: O(n)
	5. Sort!(  ) for compare the sentence lengths and the total number of sentences of the two  books: O(nlog(n)). However since we only sort two things here, the complecity can be ignored.
	6. Compute similarity score: O(1)
	Therefore the time complexity for this algorithm is O(n).
