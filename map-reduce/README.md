# Map-Reduce Interview Question: Word Frequency Analysis

## Problem Statement

You are given a large collection of text documents and need to find the frequency of each word across all documents. Implement a simplified map-reduce framework in Python to solve this problem.

**Your task is to implement three functions:**

1. `mapper(document_id, text)` - Takes a document ID and its text content, returns key-value pairs
2. `reducer(word, counts)` - Takes a word and list of its counts, returns the final count
3. `map_reduce(documents, mapper_func, reducer_func)` - Orchestrates the map-reduce process

## Function Signatures

```python
def mapper(document_id, text):
    """
    Map function that processes a single document.
    
    Args:
        document_id (str): Unique identifier for the document
        text (str): Content of the document
    
    Returns:
        List[Tuple[str, int]]: List of (word, count) pairs
    """
    pass

def reducer(word, counts):
    """
    Reduce function that aggregates counts for a single word.
    
    Args:
        word (str): The word to aggregate
        counts (List[int]): List of counts for this word from different mappers
    
    Returns:
        Tuple[str, int]: (word, total_count) pair
    """
    pass

def map_reduce(documents, mapper_func, reducer_func):
    """
    Main map-reduce orchestrator.
    
    Args:
        documents (Dict[str, str]): Dictionary of {document_id: text_content}
        mapper_func: The mapper function to use
        reducer_func: The reducer function to use
    
    Returns:
        Dict[str, int]: Dictionary of {word: total_count}
    """
    pass
```

## Requirements

- Words should be case-insensitive and stripped of punctuation
- Ignore empty strings and whitespace-only strings
- The map-reduce function should properly group intermediate results by key before reducing

## Example

```python
# Test data
documents = {
    "doc1": "Hello world! This is a test.",
    "doc2": "Hello Python. Python is great!",
    "doc3": "World of programming is wonderful."
}

# Expected output
result = map_reduce(documents, mapper, reducer)
print(result)
# Should output something like:
# {'hello': 2, 'world': 2, 'this': 1, 'is': 3, 'a': 1, 'test': 1, 
#  'python': 2, 'great': 1, 'of': 1, 'programming': 1, 'wonderful': 1}
```

## Follow-up Questions

After implementing the solution, be prepared to discuss:

1. **Scalability**: How would you modify this to handle billions of documents?
2. **Memory optimization**: What if individual documents are too large to fit in memory?
3. **Fault tolerance**: How would you handle mapper or reducer failures?
4. **Performance**: What are the bottlenecks in your implementation?
5. **Alternative problems**: How would you adapt this framework for finding the most common bigrams (two-word phrases)?

## Hints

- Consider using Python's `collections.defaultdict` for grouping
- Use `string.punctuation` and `str.translate()` for cleaning text
- Think about the shuffle/sort phase between map and reduce
- Remember that map-reduce is about parallelization - your intermediate data structure should support this conceptually

## Time Complexity Analysis

Be ready to analyze:
- Time complexity of your mapper
- Time complexity of your reducer  
- Overall time complexity of the map-reduce process
- Space complexity considerations