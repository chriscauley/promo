import Markdown from 'vue3-markdown-it'
import auth from '@unrest/vue-auth'
import UrVue from '@unrest/vue'
import form from '@unrest/form'
import '@unrest/tailwind/dist.css'

import AddChannel from '@/components/AddChannel'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './styles/base.scss'

auth.config.oauth_providers = ['github']

createApp(App)
  .component('Markdown', Markdown)
  .component('AddChannel', AddChannel)
  .use(router)
  .use(form.plugin)
  .use(auth.plugin)
  .use(UrVue.plugin)
  .use(store)
  .use(UrVue.ui)
  .mount('#app')
