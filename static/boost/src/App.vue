<template>
  <div id="app">
    <v-app>
      <v-navigation-drawer persistent :enable-resize-watcher="true" :mini-variant="miniVariant" :clipped="clipped" v-model="drawer">
        <v-list>
          <v-list-item class="elevation-1" v-for="(item, i) in items" :key="i" @click="title=item.text">
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
        <v-toolbar-title class="white--text">{{title}}</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-menu id="marriot" bottom left origin="top right">
          <v-btn icon="icon" slot="activator" class="white--text">
            <v-icon>more_vert</v-icon>
          </v-btn>
          <v-list>
            <v-list-item>
              <v-list-tile>
                <v-list-tile-title @click="logout">Logout</v-list-tile-title>
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
      items: [{
        icon: 'dashboard',
        text: 'Dashboard',
        'href': '#/Dashboard'
      },
      {
        icon: 'thumb_up',
        text: 'List Likes',
        'href': '#/Listlike'
      },
      {
        icon: 'brightness_auto',
        text: 'Auto Round',
        'href': '#/Autoround'
      },
      {
        icon: 'favorite_border',
        text: 'Boost',
        'href': '#/Boost'
      },
      {
        icon: 'account_circle',
        text: 'Manage Account',
        'href': '#/ManageAccount'
      },
      {
        icon: 'settings',
        text: 'Ebook Guide',
        'href': '#/Ebook'
      }
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Auto Round'
    }
  },
  methods: {
    logout: function () {
      let self = this;
      this.axios.post('/logout', {
        'logout': localStorage.getItem("LoggedOnUser")
      })
        .then(function (response) {
          window.location.href = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    }
  }
}
</script>

<style>
@import '../static/css/vuetify_fonts.css';
@import '../node_modules/vuetify/dist/vuetify.min.css';
</style>
