import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="arxiv")

collection.add(
    documents=["To golf, one typically holds the club (in their hands).  The golfer will then swing at the ball.  It's easy.",
               "To swim, one typically gets in the water.  He or she will then move their arms and legs in swim-like motions.  It's easy.",
               "To code, one typically types on the keyboard.  He or she will then run the code.  It's easy.",
               "To cook, one typically gets some food.  The cooking person will then put it in the oven.  Easy."],
    # metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2", "id3", "id4"]
)

results = collection.query(
    query_texts=["How do you program?"],
    n_results=2
)

print(results)
