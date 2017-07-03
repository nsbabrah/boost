<template>
  <div id="app">
    <v-app>
      <v-navigation-drawer persistent :enable-resize-watcher="true" :mini-variant="miniVariant" :clipped="clipped" v-model="drawer">
        <v-list>
          <v-list-item class="elevation-1" v-for="(item, i) in items" :key="i">
            <v-list-tile value="true" :to="item.href">
              <v-list-tile-action>
                <v-icon v-html="item.icon"></v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>{{item.text}}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
  
      <v-toolbar fixed>
        <v-toolbar-side-icon light @click.native.stop="drawer = !drawer"></v-toolbar-side-icon>
        <v-toolbar-title class="white--text" v-text="title"></v-toolbar-title>
        <v-spacer></v-spacer>
        <v-menu id="marriot" bottom left origin="top right">
          <v-btn icon="icon" slot="activator" class="white--text">
            <v-icon>more_vert</v-icon>
          </v-btn>
          <v-list>
            <v-list-item>
              <v-list-tile>
                <v-list-tile-title>Logout</v-list-tile-title>
              </v-list-tile>
            </v-list-item>
            <v-list-item>
              <v-list-tile>
                <v-list-tile-title>Send Feedback</v-list-tile-title>
              </v-list-tile>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-toolbar>
      <!--app renders in router-view-->
      <router-view></router-view>
      <v-footer :fixed="fixed">
        <span>&copy; 2017</span>
      </v-footer>
    </v-app>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'app',
  data() {
    return {
      clipped: true,
      drawer: true,
      fixed: false,
      items: [
        { icon: 'dashboard', text: 'Dashboard', 'href': '#/Autoround' },
        { icon: 'thumb_up', text: 'List Likes', 'href': '#/Listlike' },
        { icon: 'brightness_auto', text: 'Auto Round', 'href': '#/Autoround' },
        { icon: 'favorite_border', text: 'Boost', 'href': '#/' },
        { icon: 'account_circle', text: 'Manage Account', 'href': '#/' },
        { icon: 'settings', text: 'Settings', 'href': '#/' }
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Auto Round',
    }
  },
  mounted() {
    let url = window.location.href;
    if (/\?success/g.test(url)) {
      axios.post('/subscribe', { 'token': /token?=(.*)/g.exec(url)[1] })
        .then(function (response) {
          console.log(response);
          window.location.href = url.slice(0, url.indexOf('?'));
        })
        .catch(function (error) {
          console.log(error);
          window.location.href = url.slice(0, url.indexOf('?'));
        });
    }
  }
}
</script>

<style>
@import '../static/css/vuetify_fonts.css';
@import '../node_modules/vuetify/dist/vuetify.min.css';
</style>
