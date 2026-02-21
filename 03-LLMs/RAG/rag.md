# RAG (Retrieval-Augmented Generation)

Retrieval-Augmented Generation (RAG) is a technique for enhancing the accuracy and reliability of Large Language Models (LLMs) by grounding them with information from an external knowledge base. Instead of relying solely on its internal, pre-trained knowledge, the LLM is provided with relevant, up-to-date data at query time.

The external data can be from various sources, such as documents, databases, Confluence pages, or APIs.

## How RAG Works

The RAG process typically involves two main phases:

### 1. Indexing (Data Ingestion)
This is an offline process where the external knowledge base is prepared for efficient retrieval.
- **Load:** Documents are loaded from the data source.
- **Chunk:** The documents are split into smaller, manageable chunks of text.
- **Embed:** Each chunk is converted into a numerical representation (a vector embedding) using an embedding model.
- **Store:** The chunks and their corresponding embeddings are stored in a specialized database, typically a vector database, which allows for fast similarity searches.

### 2. Retrieval and Generation (Query Time)
This happens in real-time when a user submits a query.
- **Retrieve:** The user's query is also converted into a vector embedding. The vector database is then searched to find the chunks of text with embeddings most similar to the query's embedding. These are the most relevant pieces of information from the knowledge base.
- **Augment:** The original user query is combined with the retrieved text chunks into a new, more detailed prompt.
- **Generate:** This augmented prompt is then fed to the LLM, which uses the provided context to generate a comprehensive and factually grounded answer.

## Benefits of RAG

- **Reduces Hallucinations:** By providing factual context, RAG helps prevent the LLM from making up incorrect information.
- **Uses Up-to-Date Information:** RAG allows LLMs to access information that was not part of their original training data, keeping responses current.
- **Provides Source Attribution:** Since the model uses specific retrieved documents, it's possible to cite the sources used for the answer, increasing transparency and trust.