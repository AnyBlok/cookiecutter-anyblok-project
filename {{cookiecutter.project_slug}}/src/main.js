import Vue from 'vue'
import 'furetui/src/views';
import 'furetui/src/fields';
import 'furetui/src/app';
import createFuretUIClient from 'furetui/src/client';

console.log('plop', createFuretUIClient)
createFuretUIClient('#furet-ui-custom')

Vue.config.productionTip = false
