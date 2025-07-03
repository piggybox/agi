def mapper(document_id, text):
    """
    Map function that processes a single document.
    
    Args:
        document_id (str): Unique identifier for the document
        text (str): Content of the document
    
    Returns:
        List[Tuple[str, int]]: List of (word, count) pairs
    """
    return [(word, 1) for word in text.split()]

def reducer(word, counts):
    """
    Reduce function that aggregates counts for a single word.
    
    Args:
        word (str): The word to aggregate
        counts (List[int]): List of counts for this word from different mappers
    
    Returns:
        Tuple[str, int]: (word, total_count) pair
    """
    return (word, sum(counts))

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
    # Step 1: Map phase
    mapped = []
    for doc_id, text in documents.items():
        mapped.extend(mapper_func(doc_id, text))

    # Step 2: Shuffle phase
    shuffled = {}
    for word, count in mapped:
        if word not in shuffled:
            shuffled[word] = []
        shuffled[word].append(count)

    # Step 3: Reduce phase
    reduced = {}
    for word, counts in shuffled.items():
        reduced[word] = reducer_func(word, counts)

    return reduced.values()


if __name__ == "__main__":
    # Example usage
    documents = {
        "doc1": "hello world",
        "doc2": "hello from the other side",
        "doc3": "world of map reduce",
        "doc4": "map reduce is fun"
    }
    
    # Assuming mapper and reducer functions are implemented
    result = map_reduce(documents, mapper, reducer)
    print(result)