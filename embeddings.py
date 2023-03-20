# import config
# import openai
# from typing import List, Tuple, Dict
# import numpy as np
# import pandas as pd
# EMBEDDINGS_MODEL_NEW = config.DevelopmentConfig.EMBEDDINGS_MODEL_NEW


# def get_embedding(text: str, model: str) -> List[float]:
#     result = openai.Embedding.create(
#         model=model,
#         input=text)
#     return result["data"][0]["embedding"]


# def get_doc_embedding(text: str) -> List[float]:
#     return get_embedding(text, EMBEDDINGS_MODEL_NEW)


# def get_query_embedding(text: str) -> List[float]:
#     return get_embedding(text, EMBEDDINGS_MODEL_NEW)


# def compute_doc_embeddings(df: pd.DataFrame) -> Dict[Tuple[str, str], List[float]]:
#     """
#     Create an embedding for each row in the dataframe using the OpenAI Embeddings API.

#     Return a dictionary that maps between each embedding vector and the index of the row that it corresponds to.
#     """
#     return {
#         idx: get_doc_embedding(r.content.replace("\n", " ")) for idx, r in df.iterrows()
#     }


# def load_embeddings(fname: str) -> Dict[Tuple[str, str], List[float]]:
#     """
#     Read the document embeddings and their keys from a CSV.

#     fname is the path to a CSV with exactly these named columns:
#         "title", "heading", "0", "1", ... up to the length of the embedding vectors.
#     """

#     df = pd.read_csv(fname, header=0)
#     max_dim = max([int(c) for c in df.columns if c != "title" and c != "heading"])
#     return {
#         (r.title, r.heading): [r[str(i)] for i in range(max_dim + 1)] for _, r in df.iterrows()
#     }


# def vector_similarity(x: List[float], y: List[float]) -> float:
#     """
#     We could use cosine similarity or dot product to calculate the similarity between vectors.
#     In practice, we have found it makes little difference.
#     """
#     return np.dot(np.array(x), np.array(y))


# def order_document_sections_by_query_similarity(query: str, contexts: Dict[Tuple[str, str], np.array]) -> List[
#     Tuple[float, Tuple[str, str]]]:
#     """
#     Find the query embedding for the supplied query, and compare it against all of the pre-calculated document embeddings
#     to find the most relevant sections.

#     Return the list of document sections, sorted by relevance in descending order.
#     """
#     query_embedding = get_query_embedding(query)

#     document_similarities = sorted([
#         (vector_similarity(query_embedding, doc_embedding), doc_index) for doc_index, doc_embedding in contexts.items()
#     ], reverse=True)

#     return document_similarities