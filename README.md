# Chatbot Application
This project is a Chatbot application built using Svelte for the frontend and Flask for the backend. The chatbot uses a Retrieval-Augmented Generation (RAG) approach with Langchain, Groq, and SerpAPI for generating responses.
  
<br>

## Project Structure
**Frontend:** Built with Svelte, the frontend provides a user interface for interacting with the chatbot.  
**Backend:** Built with Flask, the backend handles requests from the frontend, processes them using Langchain, Groq, and SerpAPI, and returns responses.  

<br>

![ArchitectureDiagram](https://github.com/user-attachments/assets/b83c1a07-9dcf-41b6-ad0a-60476dd6c655)

<br>


## Technologies Used
**Frontend:** *Svelte, HTML, CSS, JavaScript (Axios for HTTP requests)*  
**Backend:** *Python, Flask, Langchain, Groq, SerpAPI*  
**Containerization:** *Docker*

<br>

## How It Works  

**User Interaction:**  The user types a message in the Chat UI within the Frontend (Svelte).  

**Frontend (Svelte):** The user’s input is captured and sent to the Backend (Flask) via an HTTP Request using Axios.  

**Backend (Flask):** 
- Flask Server:
  - *Acts as the entry point for all incoming HTTP requests.*
  - *Passes the user’s query to the RAG Process for processing.*

- RAG Process (Retrieval-Augmented Generation):
  - *Manages the retrieval of relevant information and the generation of a coherent response.*
  - *Sends the user’s query to Langchain for orchestration.*
  
- Langchain Orchestrator:
    - *Controls how different components like Groq and SerpAPI interact.*  
    - *May decide whether additional information is needed via SerpAPI or if the Groq LLM can handle the query directly.*

- Groq (LLM):
    - *Uses a large language model to generate a human-like response based on the user’s query.*
    - *May need additional information to provide a complete answer, triggering the use of SerpAPI.*
    
- SerpAPI Wrapper:
    - *Handles the integration with SerpAPI for external data retrieval.*
    - *Sends a search query to SerpAPI based on the user’s query or the generated response’s needs.*

- SerpAPI:
    - *Performs a web search to find relevant information.*
    - *Returns search results, which are processed and integrated back into the response by Groq.*

- Flask Server:
    - *Once the response is fully generated (with or without external data), it sends it back to the Frontend via an HTTP Response.*
    
**Frontend (Svelte):**
The response is received and displayed in the Chat UI for the user to read.

**User:**
The user views the chatbot’s response and may continue the conversation, repeating the flow.

<br>

## Setup and Installation

*Prerequisites*  
1. Docker Desktop installed on your machine  
2. Node.js installed on your machine (for building the frontend)  

<br>

**Backend Setup**  

*Build the Backend Docker Image: (make sure you are in the same directory as your backend code)*  
`docker build -t chatbot-app .`  


*Run the Backend Docker Container: (make sure you are in the directory of your backend code)*  
`docker run -d -p 5000:5000 --name chatbot-container chatbot-app`  
This command will run the backend on http://127.0.0.1:5000.


<br>

**Frontend Setup**  

*Build the Frontend Docker Image: (make sure you are in the directory of your frontend code)*  
`docker build . -t sveltekit:node`  

<br>

*Run the Frontend Docker Container: (make sure you are in the directory of your frontend code)*  
`docker run -d -p 5173:5173 --name svelte-container sveltekit:node`  
This command will run the frontend on http://127.0.0.1:5173.



