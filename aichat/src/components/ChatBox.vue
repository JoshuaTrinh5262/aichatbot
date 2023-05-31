
<template>
  <div class="chatbox-container" :style="{width: fullWidth ? '100%' : '30%'}">
    <div class="container">
      <div class="header">
        <span class="icon-zoom">
          <span
            @click="zoom('zoomin')"
            :style="{display: !fullWidth ? 'block' : 'none'}"
          >
            +
          </span>
          <span
            :style="{display: fullWidth ? 'block' : 'none'}"
            @click="zoom('zoomout')"
          >
            -
          </span>
        </span>
        <div style="flex-grow: 1;">
          <h1>Help Center</h1>
        </div>
      </div>
      
      <div class="messageBox mt-8">
        <template v-for="(message, index) in messages" :key="index">
          <div :class="message.from == 'user' ? 'messageFromUser' : 'messageFromChatGpt'">
            <img class="icon-user" :src="message.from == 'user' ? user : bot">
            <div :class="message.from == 'user' ? 'userMessageWrapper' : 'chatGptMessageWrapper'">
              <div :class="message.from == 'user' ? 'userMessageContent' : 'chatGptMessageContent'">{{ message.data }}</div>
            </div>
          </div>
        </template>
      </div>
      <div class="inputContainer">
        <input
          v-model="currentMessage"
          type="text"
          class="messageInput"
          placeholder="Ask me anything..."
          @keyup.enter="sendMessage(currentMessage)"
        />
        <button
          @click="sendMessage(currentMessage)"
          class="askButton"
        >
          Ask
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import bot from './../images/bot.svg'
import user from './../images/user.svg'

export default {
  name: 'ChatBox',
  data() {
    return {
      currentMessage: '',
      messages: [],
      bot,
      user,
      fullWidth: false,
    };
  },
  methods: {
    zoom(val) {
      if (val === 'zoomin') {
        this.fullWidth = true
      } else {
        this.fullWidth = false
      }
    },
    async sendMessage(message) {
      this.currentMessage = '';
      this.messages.push({
        from: 'user',
        data: message,
      });
      await axios
        .post('http://127.0.0.1:5000/api/chatgpt', {
          prompt: message,
        })
       .then((response) => {
        this.messages.push({
          from: 'chatGpt',
          data: response.data, // Access the 'data' property of the response object
        });
      });
    },
  },
};
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap');

  .icon-user {
    background: #6c6c60;
    padding: 8px;
    border-radius: 18px;
    height: 18px;
  }

  .header {
    display: flex;
    background-color: #f7f7f7;
    border-bottom: 1px solid #e7e7e7;
  }

  .icon-zoom {
    display: block;
    text-align: left;
    cursor: pointer;
    align-self: center;
    margin-left: 10px
  }

  .chatbox-container {
    position: fixed;
    top: 0;
    right: 2px;
    z-index: 1000;
  }

  .container {
    height: auto;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    font-family: 'Roboto', sans-serif;
  }

  h1 {
    font-size: 24px;
    font-weight: 500;
    text-align: center;
    color: #222;
    padding: 16px;
    margin: 0;
    
  }

  .messageBox {
    padding: 16px;
    flex-grow: 1;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .messageFromUser,
  .messageFromChatGpt {
    display: flex; }



  .messageBox {
    max-height: 700px;
    overflow-y: auto;
    padding: 0 16px;
    border-top: 1px solid #f0f0f0;
    border-bottom: 1px solid #f0f0f0;
    flex-grow: 1;
  }

  .messageFromUser,
  .messageFromChatGpt {
    display: flex;
    margin-bottom: 8px;
  }

  .userMessageWrapper,
  .chatGptMessageWrapper {
    display: flex;
    flex-direction: column;
    margin-left: 5px;
  }

  .userMessageWrapper {
    align-self: flex-end;
  }

  .chatGptMessageWrapper {
    align-self: flex-start;
  }

  .userMessageContent,
  .chatGptMessageContent {
    padding: 8px 12px;
    border-radius: 18px;
    margin-bottom: 2px;
    font-size: 14px;
    line-height: 1.4;
  }

  .userMessageContent {
    background-color: #1877F2;
    color: white;
    border-top-left-radius: 0;
  }

  .chatGptMessageContent {
    background-color: #EDEDED;
    color: #222;
    border-top-right-radius: 0;
  }

  .userMessageTimestamp,
  .chatGptMessageTimestamp {
    font-size: 10px;
    color: #999;
    margin-top: 2px;
  }

  .userMessageTimestamp {
    align-self: flex-end;
  }

  .chatGptMessageTimestamp {
    align-self: flex-start;
  }

  .inputContainer {
    display: flex;
    align-items: center;
    padding: 8px;
    background-color: #f0f0f0;
  }

  .messageInput {
    flex-grow: 1;
    border: none;
    outline: none;
    padding: 12px;
    font-size: 16px;
    background-color: white;
    border-radius: 24px;
    margin-right: 8px;
  }

  .askButton {
    background-color: #1877F2;
    color: white;
    font-size: 16px;
    padding: 8px 16px;
    border: none;
    outline: none;
    cursor: pointer;
    border-radius: 24px;
    transition: background-color 0.3s ease-in-out;
  }

  .askButton:hover {
    background-color: #145CB3;
  }

  @media (max-width: 480px) {
    .container {
      width: 100%;
      max-width: none;
      border-radius: 0;
    }
  }

  .chatbox-container {
    position: fixed;
    bottom: 24px;
    z-index: 1000;
  }

  .messageBox {
    padding: 16px;
    flex-grow: 1;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .messageFromUser,
  .messageFromChatGpt {
    display: flex;
  }
</style>