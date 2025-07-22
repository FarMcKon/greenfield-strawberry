import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import { apolloPlugin } from './graphql/apollo'

const app = createApp(App)

app.use(apolloPlugin)

app.mount('#app')
