import { createApp } from 'vue'
import App from './App.vue'
import ChatBox from './components/ChatBox.vue'
import BardChatBox from './components/BardChatBox.vue'
import HelloWorld from './components/HelloWorld.vue'
import { createRouter, createWebHistory } from 'vue-router';


const routes = [
    { path: '/chatgpt', name: 'ChatBox', component: ChatBox },
    { path: '/bard', name: 'BardChatBox', component: BardChatBox },
    { path: '/helloworld', name: 'HelloWorld', component: HelloWorld },
  ]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

const app = createApp(App)

app.use(router)
app.mount('#app')
