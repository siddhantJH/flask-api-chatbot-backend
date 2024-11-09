#generating the chunk using the file and then store it back into the pkl file
import pickle

def chunk_text(text, max_length=200):
    sentences = text.split('. ')
    chunks = []
    current_chunk = []
    current_length = 0

    for sentence in sentences:
        if current_length + len(sentence.split()) > max_length:
            chunks.append('. '.join(current_chunk))
            current_chunk = []
            current_length = 0
        current_chunk.append(sentence)
        current_length += len(sentence.split())

    if current_chunk:
        chunks.append('. '.join(current_chunk))

    return chunks

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def save_chunks_to_pkl(chunks, pkl_file_path):
    with open(pkl_file_path, 'wb') as file:
        pickle.dump(chunks, file)

# Example usage
text_file_path = '/content/drive/MyDrive/ContentFolder/VisaAdmissionAnnexIII_01022018.txt'  # Replace with your text file path
pkl_file_path = '/content/drive/MyDrive/ContentFolder/VisaAdmissionAnnexIIIchunk.pkl'  # Replace with the desired output pkl file path

# Read text from the file
text = read_text_from_file(text_file_path)

# Chunk the text
chunks = chunk_text(text)

# Save the chunks to a pkl file
save_chunks_to_pkl(chunks, pkl_file_path)

print(f"Text chunks have been saved to {pkl_file_path}.")




# reading the chunks and then storing it in the chunks variable 

import pickle
# Path to your .pkl file
pkl_file_path = '/content/drive/MyDrive/ContentFolder/ChunkedContent/VisaAdmissionAnnexIIIchunk.pkl'

# Load the chunks from the .pkl file
with open(pkl_file_path, 'rb') as file:
    chunks = pickle.load(file)

# Now `chunks` contains the data that was saved in the .pkl file
print(chunks)
