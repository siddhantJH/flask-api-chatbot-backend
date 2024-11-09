# Embedding generator functions
# Initialize Pinecone with your API key and environment
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
import pickle

# Path to your input .pkl file
pkl_file_path = '/content/drive/MyDrive/ContentFolder/ChunkedContent/VisaAdmissionAnnexIIIchunk.pkl'

# Initialize the Sentence Transformer model
pc = Pinecone(api_key="57be1c1e-799c-4c1a-ae23-a46ad7f03326")
index = pc.Index("iiitdindex2")

#this could be incorporated in javascript as well
model_name = 'all-MiniLM-L6-v2'  # A lightweight and efficient model
model = SentenceTransformer(model_name)

# Function to generate embeddings
def generate_embeddings(text_chunks):
    embeddings = []
    for chunk in text_chunks:
        embedding = model.encode(chunk, convert_to_tensor=False)
        embeddings.append(embedding)
    return embeddings


# this part stored the embedding in the defined path 
import pickle
# Path to your .pkl file
pkl_file_path = '/content/drive/MyDrive/ContentFolder/ChunkedContent/VisaAdmissionAnnexIIIchunk.pkl'
output_file_path= '/content/drive/MyDrive/ContentFolder/ChunkedContent/Embeddings/VisaAdmissionAnnexIIIembedding.pkl';
# Load the chunks from the .pkl file
with open(pkl_file_path, 'rb') as file:
    chunks = pickle.load(file)

# Now `chunks` contains the data that was saved in the .pkl file
print(chunks)



# Load the chunks from the .pkl file
with open(pkl_file_path, 'rb') as file:
    chunks = pickle.load(file)
    
# Initialize the Sentence Transformer model
model_name = 'all-MiniLM-L6-v2'  # A lightweight and efficient model
model = SentenceTransformer(model_name)

# Function to generate embeddings
def generate_embeddings(text_chunks):
    embeddings = []
    for chunk in text_chunks:
        embedding = model.encode(chunk, convert_to_tensor=False)
        embeddings.append(embedding)
    return embeddings

# Generate embeddings for the text chunks
embeddings = generate_embeddings(chunks)

# Path to your output .pkl file to save embeddings
output_pkl_file_path = '/content/drive/MyDrive/ContentFolder/ChunkedContent/Embeddings/VisaAdmissionAnnexIIIembedding.pkl'

# Save the embeddings to a .pkl file
with open(output_pkl_file_path, 'wb') as file:
    pickle.dump(embeddings, file)

print("Embeddings have been generated and stored successfully.")

