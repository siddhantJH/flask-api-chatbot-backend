


# finally storing everything including embedding along with the meta data in the poinecone DB 

import pickle
from pinecone import Pinecone
pc = Pinecone(api_key="57be1c1e-799c-4c1a-ae23-a46ad7f03326")
index_name = 'iiitdindex2'
index = pc.Index(index_name)

# Paths to your .pkl files
embeddings_pkl_path1 = '/content/drive/MyDrive/ContentFolder/ChunkedContent/Embeddings/IIITDDelhiEmbeddings.pkl'
metadata_pkl_path1 = '/content/drive/MyDrive/ContentFolder/ChunkedContent/IIITDDelhichunk.pkl'
embeddings_pkl_path2 = '/content/drive/MyDrive/ContentFolder/ChunkedContent/Embeddings/InternationalBrochureEmbeddings.pkl'
metadata_pkl_path2 = '/content/drive/MyDrive/ContentFolder/ChunkedContent/InternationalBrochurechunk.pkl'
embeddings_pkl_path3 = '/content/drive/MyDrive/ContentFolder/ChunkedContent/Embeddings/StudentHandbook15Embeddings.pkl'
metadata_pkl_path3 = '/content/drive/MyDrive/ContentFolder/ChunkedContent/StudentHandbook15chunk.pkl'
embeddings_pkl_path4 = '/content/drive/MyDrive/ContentFolder/ChunkedContent/Embeddings/ChunkedContentFacultyEmbedding.pkl'
metadata_pkl_path4 = '/content/drive/MyDrive/ContentFolder/ChunkedContentFacultyInfochunk.pkl'
embeddingas_pkl_path5 = '/content/drive/MyDrive/ContentFolder/ChunkedContent/Embeddings/VisaAdmissionAnnexIIIembedding.pkl'
metadata_pkl_path5 = '/content/drive/MyDrive/ContentFolder/ChunkedContent/VisaAdmissionAnnexIIIchunk.pkl'

# Load all embeddings and metadata into a single list
all_embeddings = []
all_metadata = []

for embeddings_pkl_path, metadata_pkl_path in [
    (embeddings_pkl_path1, metadata_pkl_path1),
    (embeddings_pkl_path2, metadata_pkl_path2),
    (embeddings_pkl_path3, metadata_pkl_path3),
    (embeddings_pkl_path4, metadata_pkl_path4),
    (embeddingas_pkl_path5, metadata_pkl_path5)
]:
    with open(embeddings_pkl_path, 'rb') as file:
        embeddings = pickle.load(file)
        all_embeddings.extend(embeddings)

    with open(metadata_pkl_path, 'rb') as file:
        metadata = pickle.load(file)
        all_metadata.extend(metadata)

# Function to store embeddings along with metadata in Pinecone
def store_embeddings_with_metadata(embeddings, metadata, batch_size=100):
    vectors = []
    for i, (embedding, meta) in enumerate(zip(embeddings, metadata)):
        vector_id = f'embedding_{i}'
        vectors.append((vector_id, embedding, {"text": meta}))

        # Batch upsert
        if len(vectors) >= batch_size:
            response = index.upsert(vectors)
            print(f"Batch upserted with response: {response}")
            vectors = []

    # Upsert remaining vectors if any
    if vectors:
        response = index.upsert(vectors)
        print(f"Final batch upserted with response: {response}")

# Store the embeddings and their corresponding metadata in Pinecone
store_embeddings_with_metadata(all_embeddings, all_metadata)

print("All embeddings and metadata have been stored successfully in Pinecone.")