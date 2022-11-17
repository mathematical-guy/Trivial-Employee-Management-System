import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import '@mdi/font/css/materialdesignicons.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import vuetify from './plugins/vuetify'
// import mdiVue from 'mdi-vue/v2'
// import * as mdijs from '@mdi/js'


Vue.config.productionTip = false
Vue.use(Vuetify)
// Vue.use(mdiVue, {
//   icons: mdijs
// })


new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
