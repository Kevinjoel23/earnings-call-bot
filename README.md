# LangChain Streamlit Chatbot App

## Overview

This Streamlit app leverages LangChain, an open-source library, to create a custom memory-based chatbot for analyzing earnings call transcripts. The chatbot uses LangChain's ConversationalRetrievalChain, powered by the OpenAI API, to understand and respond to user queries. The app is designed to work with earnings call transcripts in PDF format.

## Key Features

1. **Welcome Page:**
   - Upload an earnings call transcript in PDF format.
   - Click "Process" to summarize the transcript.
   - The app uses LangChain's Chroma vector store for similarity search to retrieve relevant context chunks.

2. **Opening Remarks Summary:**
   - This section summarizes the opening remarks before the Q&A session in the transcript.

3. **Question Answer Summary:**
   - Summarizes the Q&A part of the earnings call transcript.

4. **Chatbot:**
   - Engage in a conversational chat with the LangChain-powered chatbot.
   - The chatbot remembers previous chat history within the current session.
   - User can ask questions related to the transcript content, and the chatbot responds based on the context.

## Implementation Details

- **Libraries Used:**
  - Streamlit: Frontend framework for creating web applications.
  - LangChain: Customizable conversational AI library.
  - OpenAI API: Utilized for embeddings and language models.

- **Authentication:**
  - OpenAI API key is required for embeddings.
  - OpenAI API key is utilized for language models.

- **LangChain Components:**
  - `OpenAI`: Connects to the OpenAI API for language models.
  - `Chroma`: Vector store for similarity search.
  - `ConversationalRetrievalChain`: Memory-based chatbot using LangChain.

- **Pages:**
  - **Welcome Page:** Upload and process the transcript, summarize it, and display the results.
  - **Opening Remarks Summary:** Placeholder for future functionality.
  - **Question Answer Summary:** Placeholder for future functionality.
  - **Chatbot Page:** Engage in a conversation with the custom chatbot.

## How to Use

1. Upload your earnings call transcript on the "Welcome" page.
2. Click "Process" to summarize the transcript and view the results.
3. Explore the different sections for opening remarks summary, Q&A summary, and interact with the chatbot on the respective pages.

## Note

Ensure that you have the necessary API keys for OpenAI to run this application successfully.

Feel free to customize the app further based on your project requirements.
