<template>
  <div id="app">
    <v-app>
      <v-navigation-drawer persistent :mini-variant="miniVariant" :clipped="clipped" v-model="drawer">
        <v-list>
          <v-list-item v-for="(item, i) in items" :key="i">
            <v-list-tile value="true">
              <v-list-tile-action>
                <v-icon v-html="item.icon"></v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                  <router-link style="text-decoration:none" :to="item.href"> <v-list-tile-title>{{item.text}}</v-list-tile-title>
               </router-link>
              </v-list-tile-content>
            </v-list-tile>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-toolbar>
        <v-toolbar-side-icon light  @click.native.stop="drawer = !drawer"></v-toolbar-side-icon>
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
export default {
  name: 'app',
  data() {
    return {
      clipped: true,
      drawer: true,
      fixed: false,
      items: [
        { icon: 'dashboard', text: 'Dashboard', 'href':'/' },
        { icon: 'thumb_up', text: 'List Likes', 'href':'/listlike' },
        { icon: 'brightness_auto', text: 'Auto Round', 'href':'/' },
        { icon: 'favorite_border', text: 'Boost', 'href':'/' },
        { icon: 'account_circle', text: 'Manage Account', 'href':'/' },
        { icon: 'settings', text: 'Settings', 'href':'/' }
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Auto Round',
    }
  }
}
</script>

<style>
@import '../static/css/vuetify_fonts.css';
@import '../node_modules/vuetify/dist/vuetify.min.css';
</style>
