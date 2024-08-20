  <script>
    import axios from 'axios';
    let userMessage = '';
    let messages = [];
    let isDarkMode = true;

    // Toggle dark/light mode
    const toggleMode = () => {
        isDarkMode = !isDarkMode;
        document.body.className = isDarkMode ? 'dark-mode' : 'light-mode';
        console.log('Mode toggled to:', isDarkMode ? 'Dark' : 'Light'); // Debug log
    };

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
            console.log('Response:', response.data); // Debug log
            messages = [...messages, { text: response.data.response, type: 'bot' }];
        } catch (error) {
            console.error('Error sending message:', error); // Debug log
            messages = [...messages, { text: 'Sorry, something went wrong.', type: 'bot' }];
        }
    };
</script>

<style>
    :global(body) {
        font-family: 'Arial', sans-serif;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        width: 100vw;
        background-color: var(--bg-color);
        transition: background-color 0.3s ease;
    }

    :global(.dark-mode) {
        --bg-color: #1e1e2f;
        --chat-bg-color: #2b2b3d;
        --input-bg-color: #2b2b3d;
        --user-msg-bg-color: #007bff;
        --bot-msg-bg-color: #555;
        --text-color: white;
        --input-text-color: white;
        --header-border-color: #444;
        --button-bg-color: #007bff;
        --button-hover-color: #0056b3;
    }

    :global(.light-mode) {
        --bg-color: #f5f5f5;
        --chat-bg-color: white;
        --input-bg-color: #e0e0e0;
        --user-msg-bg-color: #007bff;
        --bot-msg-bg-color: #dcdcdc;
        --text-color: black;
        --input-text-color: black;
        --header-border-color: #ccc;
        --button-bg-color: #007bff;
        --button-hover-color: #0056b3;
    }

    .chat-container {
        background-color: var(--chat-bg-color);
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        width: 100%;
        height: 100%;
        margin: 0;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        color: var(--text-color);
    }

    .header {
        display: flex;
        align-items: center;
        padding: 20px;
        border-bottom: 1px solid var(--header-border-color);
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

    .toggle-button {
    margin-left: auto;
    cursor: pointer;
    background: none;
    border: none;
    font-size: 14px;
    color: var(--text-color);
    width: 50px; /* Ensure a consistent width */
    height: 50px; /* Ensure a consistent height */
    border-radius: 50%; /* Keep it circular, reduce or remove if needed */
    display: flex;
    justify-content: center;
    align-items: center;
    }

      .toggle-button:hover {
      background-color: rgba(255, 255, 255, 0.1); /* Example hover effect */
  }

  .toggle-button:focus {
      outline: none;
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
        background-color: var(--bot-msg-bg-color);
    }

    .user {
        align-self: flex-end;
        background-color: var(--user-msg-bg-color);
        color: white;
    }

    .bot {
        align-self: flex-start;
        background-color: var(--bot-msg-bg-color);
        color: #eee;
    }

    .input-container {
        display: flex;
        padding: 15px;
        background-color: var(--input-bg-color);
        border-top: 1px solid var(--header-border-color);
    }

    input {
        flex-grow: 1;
        border: none;
        padding: 15px;
        font-size: 18px;
        border-radius: 20px;
        outline: none;
        background-color: var(--input-bg-color);
        color: var(--input-text-color);
    }

    button {
        background-color: var(--button-bg-color);
        border: none;
        color: white;
        padding: 15px;
        font-size: 18px;
        border-radius: 50%;
        cursor: pointer;
        margin-left: 10px;
    }

    button:hover {
        background-color: var(--button-hover-color);
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
        <button class="toggle-button" on:click={toggleMode}>
            {isDarkMode ? '🌞 Light Mode' : '🌜 Dark Mode'}
        </button>
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

  


  
  
  

