import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue'

import ChatBox from './components/ChatBox.vue'
import BardChatBox from './components/BardChatBox.vue'
import MainComponent from './components/MainComponent.vue'
import SettingComponent from './components/SettingComponent.vue'



const routes = [
    { path: '/chatgpt', name: 'ChatBox', component: ChatBox },
    { path: '/bard', name: 'BardChatBox', component: BardChatBox },
    { path: '/setting', name: 'SettingComponent', component: SettingComponent },
    { path: '/', name: 'MainComponent', component: MainComponent },
  ]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

const app = createApp(App)

app.use(router)
app.mount('#app')
