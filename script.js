const sendMessage = async () => {
    const userInput = document.getElementById('user-input').value;  

    if (!userInput) return; 
    const chatBox = document.getElementById('chat-box');
    const userMessageDiv = document.createElement('div');
    userMessageDiv.className = 'user-message';
    userMessageDiv.innerHTML = `<p>${userInput}</p>`;
    chatBox.appendChild(userMessageDiv);

    
    const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput }),
    });

    if (!response.ok) {
       
        console.error('Error communicating with backend:', response.statusText);
        alert('Failed to communicate with backend.');
        return;
    }

    const data = await response.json(); 
    const botReply = data.response;  

   
    const botMessageDiv = document.createElement('div');
    botMessageDiv.className = 'bot-message';
    botMessageDiv.innerHTML = `<p>${botReply}</p>`;
    chatBox.appendChild(botMessageDiv);

    
    document.getElementById('user-input').value = '';
};
