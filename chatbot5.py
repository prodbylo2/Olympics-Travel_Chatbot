import os
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain_community.utilities import SerpAPIWrapper

# Set up environment variables if needed
os.environ['SERPAPI_API_KEY'] = '29c117f1b96c7eaf6619cee675d57cec6d11dc0fda202de1481e709cd6f543fb'
os.environ['GROQ_API_KEY'] = "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"


# Initialize SerpAPIWrapper for the retrieval component
api_wrapper = SerpAPIWrapper(serpapi_api_key=os.environ['SERPAPI_API_KEY'])

# Initialize Groq for the generation component
groq_chat = ChatGroq(
    groq_api_key=os.environ['GROQ_API_KEY'], 
    model_name='llama3-8b-8192'
)

# Initialize conversation memory
memory = ConversationBufferWindowMemory(k=10, memory_key="chat_history", return_messages=True)

def retrieve_information(query):
    # """
    # Retrieves relevant information using SerpAPI.
    # """
    # return api_wrapper.run(query)
    print(f"Received query: {query}") 
    if not query:
        raise ValueError("Query parameter is missing.")
    
    try:
        results = api_wrapper.run(query)
        return results
    except Exception as e:
        print(f"Error retrieving information: {e}")
        raise

def generate_response(retrieved_info, query):
    """
    Generates a response using Groq with the retrieved information.
    """
    # Construct the input for the LLM with retrieved information
    prompt_text = f"Based on the following information, answer the question: {retrieved_info}\n\nQuestion: {query}"

    # Define the prompt
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content="You are an assistant thet specializes in Travel and Tourism and the Olympics. You have to valuable information regarding tourism spots, tourism costs and prices, and the Olympics. You have to use the retrieved information to answer questions."),  # System context
            MessagesPlaceholder(variable_name="chat_history"),  # Chat history
            HumanMessagePromptTemplate.from_template(prompt_text)  # User input with retrieved info
        ]
    )
    
    # Generate the response directly
    response = groq_chat.invoke(prompt_text)
    return response

def rag_response(query):
    try:
        """
        Handles RAG process: retrieves relevant information and generates a response.
        """
        # Retrieve relevant information
        search_results = retrieve_information(query)
        
        # Generate a response using Groq
        response = generate_response(search_results, query)
        
        return response
    except Exception as e:
        print(f"Error in rag_response: {e}")
        raise

def main():
    while True:
        user_question = input("Ask a question (or type 'exit' to quit): ")
        if user_question.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Get RAG response
        response = rag_response(user_question)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
