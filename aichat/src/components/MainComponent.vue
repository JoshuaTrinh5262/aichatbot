<template>
  <div>
    <div class="button-list">
      <h3 class="button-heading">Chat Bot</h3>
      <ul>
        <li>
            <a href="/chatgpt">ChatGPT Chat Box</a>
        </li>
        <li>
            <a href="/bard">Bard Chat Box</a>
        </li>
      </ul>
    </div>
    <div class="button-list">
      <h3 class="button-heading">Setting</h3>
      <ul>
        <li>
            <a href="/setting">Setting</a>
        </li>
        <li>
          <a href="/test">404</a>
        </li>
      </ul>
    </div>
  </div>
</template>
  
  <script>
  export default {
    name: 'MainComponent',
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
.button-list {
  list-style: none;
  padding: 0;
  text-align: center;
}

.button-heading {
  font-size: 24px;
  margin-bottom: 20px;
}

.button-list li {
  display: inline-block;
}

.button-list li a {
  display: inline-block;
  padding: 10px 20px;
  background-color: #4285f4;
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
  margin-right: 10px;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

.button-list li a:hover {
  background-color: #3367d6;
}
  </style>
  