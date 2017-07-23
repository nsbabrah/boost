<template>
  <main v-if="!loader">
    <v-container fluid>
      <v-layout row wrap v-if="alert">
        <v-flex xs12 sm12 lg12>
          <v-alert :success="response" :error="!response" dismissible v-model="alert">
            {{response ? approved_message : unapproved_message}}
          </v-alert>
        </v-flex>
      </v-layout>
      <v-btn v-if="showUsers" floating large @click.native="add_user" primary class="text-xs-right ma-1">
        <v-icon light>add</v-icon>
      </v-btn>
      <v-layout row wrap align-start v-if="showUsers">
        <div v-for="(item,index) in users" :key="index">
          <cards :postData="item" class="ma-1"></cards>
        </div>
      </v-layout>
      <v-layout row-lg wrap column v-else>
        <tabs v-on:goback="showUsers = true"> </tabs>
      </v-layout>
    </v-container>
  </main>
  <main v-else>
    <v-container fluid>
      <v-layout row wrap>
        <v-flex xs12 sm12 lg12>
          <v-progress-linear v-bind:indeterminate="true"></v-progress-linear>
        </v-flex>
      </v-layout>
    </v-container>
  </main>
</template>

<script>
import cards from './UserList.vue';
import tabs from './AddUser.vue';
export default {
  components: {
    cards,
    tabs
  },
  data() {
    return {
      showUsers: true,
      loader: false,
      users: null,
      alert: null,
      response: null,
      approved_message: 'Thanks, Your Payment Has Been Approved!',
      unapproved_message: 'Sorry, Payment Failed.',
    }
  },
  methods: {
    add_user: function () {
      this.showUsers = false;
    },
    auth: function () {
      const self = this;
      this.axios.get('/userauth').then((res) => {
        console.log(res);
        self.users = res.data;
        localStorage.setItem("LoggedOnUser", this.users[0]['username']);
      }).catch((err) => {
        console.log(err);
      })
      this.users = [{
        'username': 'test',
        'listlike': 'test',
        'usr_id': '1',
        'Auto_ac_name': 'test',
        'play': true
      }, {
        'username': 'test',
        'listlike': 'test',
        'usr_id': '1',
        'Auto_ac_name': 'test',
        'play': true
      }];
    },
    paypal_addUser: function (url) {
      this.loader = true;
      let self = this;
      this.axios.post('/subscribe', {
        'token': /token?=(.*)/g.exec(url)[1],
        'userdata': sessionStorage.getItem('paypal_data')
      })
        .then(function (response) {
          sessionStorage.removeItem('paypal_data');
          window.location.href = url.slice(0, url.indexOf('?'));
          self.alert = true;
          self.response = true;

          self.auth();
          self.loader = false;
        })
        .catch(function (error) {
          sessionStorage.removeItem('paypal_data');
          self.alert = true;
          self.response = false;
          window.location.href = url.slice(0, url.indexOf('?'));
          self.loader = false;
        });
    },
    paypal_changeUser: function (url) {
      let self = this;
      this.loader = true;
      let paypal_res = /(?:.+paymentid=)(.+?)(?:&.+payerid=)(.+)/ig.exec(url)
      this.axios.post('/Usernamechanged', {
        'paymentid': paypal_res[1],
        'payerid': paypal_res[2]
      })
        .then(function (response) {
          window.location.href = url.slice(0, url.indexOf('?'));
          self.alert = true;
          self.response = true;
          self.auth();
          self.loader = false;
          sessionStorage.removeItem('paypal_data');
          let a = document.createElement("a");
          a.href = "#/Listlike";
          a.click();
        })
        .catch(function (error) {
          self.alert = true;
          self.response = false;
          window.location.href = url.slice(0, url.indexOf('?'));
          self.loader = false;
          sessionStorage.removeItem('paypal_data');
          let a = document.createElement("a");
          a.href = "#/Listlike";
          a.click();
        });
    },
    paypal_failed() {
      this.alert = true;
      this.response = false;
      self.loader = false;
    }
  },
  mounted() {
    this.auth();
    let url = window.location.href;
    switch (true) {
      case /\?success_user/g.test(url):
        this.paypal_addUser(url);
        break;
      case /\?failed_user/g.test(url):
        this.paypal_failed();
        break;
      case /\?success_onetime/g.test(url):
        this.paypal_changeUser(url);
        break;
      case /\?failed_onetime/g.test(url):
        this.paypal_failed();
        break;
      default:
        this.alert = false;
        this.response = false;
        break;
    }
  }
}
</script>

<style>

</style>


