<template>
    <div class="main">
      <h3>Bot</h3>
      <ul>
        <li>
            <a href="/chatgpt">ChatGPT</a>
        </li>
        <li>
            <a href="/bard">Bard</a>
        </li>
        <li>
            <a href="/setting">Setting</a>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'MainComponent',
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
  </style>
  