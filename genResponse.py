#AIzaSyDJ28JgBvJys-phUHPFQu-HgfRTDCh4S3k google api key keep it

# we will use gemini3 free access to generate the resposne
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyDJ28JgBvJys-phUHPFQu-HgfRTDCh4S3k")

model = genai.GenerativeModel('gemini-1.5-flash')


def generate_response(combined_text):
    # Generate content using the model based on the combined text
    response = model.generate_content(combined_text)  # Modified prompt
    
    # Check and print safety ratings for each candidate in the response
    for candidate in response.candidates:
        print(f"Safety ratings: {candidate.safety_ratings}")
    
    # Try printing the generated text if available
    if hasattr(response, 'text') and response.text:
        return response
    else:
        print("No text content returned.")
