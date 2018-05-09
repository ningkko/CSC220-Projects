## Objective
Given the full text of two books as book1.txt and book2.txt, generate a summary comparison between the two which includes: 

total number of words in each book
total number of sentences in each book
the top 10 words in each book
average sentence length in each book
a "similarity score" indicating how similar the two books are (how you define this is up to you)

## Examples
--------------------------------------------------------------
            FILENAME: book1.txt
         TOTAL WORDS: < words in book1.txt>
     TOTAL SENTENCES: < sentences in book1.txt>
AVG. SENTENCE LENGTH: <avg.  words per sentence in book1.txt>
        TOP 10 WORDS: word1: <count>
                      ... 
                      word10: <count>
--------------------------------------------------------------
            FILENAME: book2.txt
         TOTAL WORDS: < words in book2.txt>
     TOTAL SENTENCES: < sentences in book2.txt>
AVG. SENTENCE LENGTH: <avg.  words per sentence in book2.txt>
        TOP 10 WORDS: word1: <count>
                      ...
                      word10: <count>
--------------------------------------------------------------
          SIMILARITY: <similarity score>
	

## The reason we choose Julia:
	Julia is generally fast than most of other languages due to its JIT compilation since it includes a compiler as part of its runtime environment.

## The Similarity Score
	The similarity score is evaluated by two standards, each has 0.5 point counting towards the total score.
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
