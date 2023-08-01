// JavaScript code to handle user input submission
document.addEventListener('DOMContentLoaded', function() {
    const inputField = document.querySelector('.chat-footer input[type="text"]');
    const chatMessages = document.querySelector('.chat-messages');
    const select = document.getElementById("selectOption");
    const messageForm = document.getElementById("messageForm");

    messageForm.addEventListener('keydown', function(event) {

        if (event.key === 'Enter') {
            event.preventDefault();
            const message = inputField.value.trim();

            if (isValidMessage(message)) {
                appendUserMessage(message);

                if(select.value == 'bard') {
                  bardResponse(message);
                } else {
                  chatgptResponse(message);
                }

                inputField.value = '';
                clearError()
            } else {
                displayError('Invalid message. Please enter a valid message.');
            }
        }
    });
      // Handle form submission
    messageForm.addEventListener("submit", function (event) {
      // Prevent the default form submission behavior
      event.preventDefault();
      const message = inputField.value.trim();
      if (isValidMessage(message)) {
        appendUserMessage(message);

        if(select.value == 'bard') {
          bardResponse(message);
        } else {
          chatgptResponse(message);
        }

        inputField.value = '';
        clearError()
      } else {
          displayError('Invalid message. Please enter a valid message.');
      }
      // Your form processing logic here, if needed
      // For example, you can access the selected value from the select element:
      const selectedValue = select.value;
      console.log("Selected value:", selectedValue);
    });

  // Handle select option change
    select.addEventListener("change", function (event) {
      // Your select option change logic here, if needed
      const selectedValue = event.target.value;
      console.log("Selected value:", selectedValue);
    }); 

    function isValidMessage(message) {
        return message.length <= 100 && message !== '';
    }
    
    function displayError(errorMessage) {
        inputField.classList.add('error');
        inputField.setAttribute('title', errorMessage);
    }
    
    function clearError() {
        inputField.removeAttribute('title');
    }


    function appendUserMessage(message) {
        const userMessage = document.createElement('div');
        userMessage.className = 'message user-message';
        userMessage.innerHTML = `
        <div class="avatar user-avatar"></div>
        <div>${message}</div>
        `;
        chatMessages.appendChild(userMessage);
    }

    function appendBotMessage(message) {
        const userMessage = document.createElement('div');
        userMessage.className = 'message bot-message';
        userMessage.innerHTML = `
            <div class="avatar bot-avatar"></div>
            <div>${message}</div>
        `;
        chatMessages.appendChild(userMessage);
    }

    document.addEventListener('DOMContentLoaded', function() {
        const dropdownButton = document.querySelector('.dropdown-button');
        const dropdownContent = document.querySelector('.dropdown-content');
      
        dropdownButton.addEventListener('click', function() {
          dropdownContent.classList.toggle('show');
        });
      
        window.addEventListener('click', function(event) {
          if (!event.target.matches('.dropdown-button')) {
            dropdownContent.classList.remove('show');
          }
        });
      });
    
      function bardResponse(prompt) {
        fetch('http://127.0.0.1:5000/api/bard', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ prompt: prompt }),
        })
          .then(response => response.json())
          .then(data => {
            appendBotMessage(data)
          })
          .catch(error => {
            console.error(error);
          });
      }

      function chatgptResponse(prompt) {
        fetch('http://127.0.0.1:5000/api/chatgptbyindex', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ prompt: prompt }),
        })
          .then(response => response.json())
          .then(data => {
            appendBotMessage(data.data)
          })
          .catch(error => {
            console.error(error);
          });
      }
});