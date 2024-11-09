# # !pip install PyPDF2 openai pinecone-client
# # !pip install sentence-transformers

# import pickle
# from pinecone import Pinecone
# from sentence_transformers import SentenceTransformer
# from genResponse import generate_response
# import asyncio
# # Initialize Pinecone
# pc = Pinecone(api_key="57be1c1e-799c-4c1a-ae23-a46ad7f03326")
# index_name = 'iiitdindex2'
# index = pc.Index(index_name)

# # User Query
# query = "Tell me more about the information required to fill the honour code form of IIITD?"

# # Initialize the Sentence Transformer model
# model_name = 'all-MiniLM-L6-v2'  # A lightweight and efficient model
# model = SentenceTransformer(model_name)

# # Step 1: Generate an embedding for the query
# query_embedding = model.encode(query, convert_to_tensor=False).tolist()  # Ensure the embedding is a list of floats

# # Step 2: Query Pinecone to get the top 3 most similar vectors with metadata
# result = index.query(
#     vector=query_embedding,  # The embedding vector for the query
#     top_k=5,  # Number of top results to return
#     include_values=True,  # Include the vector values in the response
#     include_metadata=True  # Include metadata associated with each result
# )

# # Step 3: Combine the query with the top 3 results
# combined_text =  "\n"
# if not result['matches']:
#     combined_text += "No relevant information found in the database.\n"
# else:
#     for match in result['matches']:
#         metadata = match['metadata']
#         combined_text += metadata['text'] + "\n"

# # Attach the question at the end
# combined_text += "\n" + "Question: " + query

# # combined_text now contains the concatenated user input and top 3 results
# print("Combined Text:")
# print(combined_text)
# async def callthis():
#     text=await generate_response(combined_text)
#     print(text)



# asyncio.run(callthis())



import pickle
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
import asyncio
import google.generativeai as genai

# Initialize Pinecone
pc = Pinecone(api_key="57be1c1e-799c-4c1a-ae23-a46ad7f03326")
index_name = 'iiitdindex2'
index = pc.Index(index_name)

# Initialize the Sentence Transformer model
model_name = 'all-MiniLM-L6-v2'  # A lightweight and efficient model
model = SentenceTransformer(model_name)

# Configure Generative AI
genai.configure(api_key="AIzaSyDJ28JgBvJys-phUHPFQu-HgfRTDCh4S3k")
gen_model = genai.GenerativeModel('gemini-1.5-flash')

async def generate_response_async(text):
    response = gen_model.generate_content(text)  # Generate content
    # Print safety ratings and return the response text
    for candidate in response.candidates:
        print(f"Safety ratings: {candidate.safety_ratings}")
    return response.text if hasattr(response, 'text') and response.text else "No text content returned."

async def process_query(query):
    # Step 1: Generate an embedding for the query
    query_embedding = model.encode(query, convert_to_tensor=False).tolist()

    # Step 2: Query Pinecone to get the top 3 most similar vectors with metadata
    result = index.query(
        vector=query_embedding,  # The embedding vector for the query
        top_k=10,  # Number of top results to return
        include_values=True,  # Include the vector values in the response
        include_metadata=True  # Include metadata associated with each result
    )

    # Step 3: Combine the query with the top 3 results
    combined_text = "\n"
    if not result['matches']:
        combined_text += "No relevant information found in the database.\n"
    else:
        for match in result['matches']:
            metadata = match['metadata']
            combined_text += metadata['text'] + "\n"
    
    combined_text += "\n" + "Question: " + query+ "Give answer to the question as if you are a chatbot"

    # Generate response asynchronously
    return await generate_response_async(combined_text)

# async def main():
#     # query = "Tell me more about the information required to fill the honour code form of IIITD?"
#     response_text = await process_query(query)
#     # print("Generated Response:")
#     # print(response_text)

# # Run the main function
# asyncio.run(main())
