  <script>
    import axios from 'axios';
    let userMessage = '';
    let messages = [];
  
    const sendMessage = async () => {
      if (userMessage.trim() === '') return;
      
      messages = [...messages, { text: userMessage, type: 'user' }];
      const messageToSend = userMessage;
      console.log('Sending message:', messageToSend);
      userMessage = '';
      
      try {
        const response = await axios.post('http://127.0.0.1:5000/chat', {
          question: messageToSend
        });
        messages = [...messages, { text: response.data.response, type: 'bot' }];
      } catch (error) {
        messages = [...messages, { text: 'Sorry, something went wrong.', type: 'bot' }];
      }
    };
  </script>
  
  <style>
    :global(body) {
      font-family: 'Arial', sans-serif;
      background-color: #1e1e2f;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
  
    .chat-container {
      background-color: #2b2b3d;
      border-radius: 20px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
      width: 100%; /* Full width */
      height: 100%; /* Full height */
      margin: 0;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      color: white;
    }
  
    .header {
      display: flex;
      align-items: center;
      padding: 20px;
      border-bottom: 1px solid #444;
    }
  
    .header img {
      border-radius: 50%;
      width: 50px;
      height: 50px;
      margin-right: 15px;
    }
  
    .header h1 {
      font-size: 20px;
      margin: 0;
    }
  
    .header p {
      font-size: 14px;
      margin: 0;
      color: #aaa;
    }
  
    .messages {
      padding: 20px;
      overflow-y: auto;
      flex-grow: 1;
      display: flex;
      flex-direction: column;
    }
  
    .message {
      padding: 10px 15px;
      margin-bottom: 10px;
      border-radius: 20px;
      max-width: 80%;
      word-wrap: break-word;
      background-color: #444;
    }
  
    .user {
      align-self: flex-end;
      background-color: #007bff;
      color: white;
    }
  
    .bot {
      align-self: flex-start;
      background-color: #555;
      color: #eee;
    }
  
    .input-container {
      display: flex;
      padding: 15px;
      background-color: #1e1e2f;
      border-top: 1px solid #444;
    }
  
    input {
      flex-grow: 1;
      border: none;
      padding: 15px;
      font-size: 18px;
      border-radius: 20px;
      outline: none;
      background-color: #2b2b3d;
      color: white;
    }
  
    button {
      background-color: #007bff;
      border: none;
      color: white;
      padding: 15px;
      font-size: 18px;
      border-radius: 50%;
      cursor: pointer;
      margin-left: 10px;
    }
  
    button:hover {
      background-color: #0056b3;
    }
  
    button:focus {
      outline: none;
    }
  
    .input-container button::before {
      content: "➤";
      display: block;
    }
  </style>
  
  
  
  
  <div class="chat-container">
    <div class="header">
      <img src="https://www.creativefabrica.com/wp-content/uploads/2021/07/05/Chatbot-Logo-Modern-bot-logo-Graphics-14298242-1.jpg" alt="Chatbot Logo" />
      <div>
        <h1>ChatBot</h1>
        <p>Ask me anything!</p>
      </div>
    </div>
  
    <div class="messages">
      {#each messages as message}
        <div class="message {message.type}">
          {message.text}
        </div>
      {/each}
    </div>
  
    <div class="input-container">
      <input bind:value={userMessage} on:keydown={(e) => e.key === 'Enter' && sendMessage()} placeholder="Type a message..." />
      <button on:click={sendMessage}></button>
    </div>
  </div>
  
  
  

