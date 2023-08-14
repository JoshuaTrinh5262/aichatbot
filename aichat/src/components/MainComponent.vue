<template>
  <div>
    <div class="button-list">
      <h1 class="button-heading">CHAT BOT</h1>
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
      
      <h1 class="button-heading">SETTING</h1>
      <ul>
        <li>
            <a href="/setting">Setting</a>
        </li>
        <li>
          <a href="/test">404</a>
        </li>
      </ul>
    </div>
    <div class="button-list">
      <h1 class="button-heading">VECTOR INDEX</h1>
      <alert-component v-if="showAlert" :type="alertType" :message="alertMessage" />
      <ul>
        <li>
            <a type="button" @click="indexdocumentapi">Normal Index</a>
        </li>
        <li>
          <a type="button" @click="indexdocumentbygptapi">GPT Index</a>
        </li>
      </ul>
    </div>
  </div>
</template>
  
  <script>
  import axios from 'axios';
  import AlertComponent from '@/components/AlertComponent.vue';

  export default {
    name: 'MainComponent',
    components: {
      AlertComponent
    },

    data() {
      return {
        showAlert: false,
        alertType: '',
        alertMessage: ''
      };
    },

    methods: {
      async indexdocumentapi() {
        await axios.get('http://127.0.0.1:5000/api/documentsindex')
        .then((response) => {
          console.log(response.data)
          this.showAlertMessage('success', 'API call successful');
        })
        .catch(error => {
          this.showAlertMessage('error', error);
        });
      },

      async indexdocumentbygptapi() {
        await axios.get('http://127.0.0.1:5000/api/documentsgptindex')
        .then((response) => {
          console.log(response.data)
          this.showAlertMessage('success', 'API call successful');
        })
        .catch(error => {
          this.showAlertMessage('error', error);
        });
      },

      showAlertMessage(type, message) {
        this.alertType = type;
        this.alertMessage = message;
        this.showAlert = true;

        setTimeout(() => {
          this.hideAlert();
        }, 3000);
      },

      hideAlert() {
        this.showAlert = false;
        this.alertType = '';
        this.alertMessage = '';
      },
    }
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
  