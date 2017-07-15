<template>
  <main>
    <v-container fluid>
      <v-layout row wrap v-if="alert">
        <v-flex xs12 sm12 lg12>
          <v-alert :success="response" :error="!response" dismissible v-model="alert">
            {{response ? approved_message : unapproved_message}}
          </v-alert>
        </v-flex>
      </v-layout>
      <v-layout row-sm wrap column v-if="showUsers">
        <v-flex xs12 sm12 lg1>
          <v-btn floating large @click.native="add_user" class="blue text-xs-right ma-1">
            <v-icon light>add</v-icon>
          </v-btn>
        </v-flex>
        <div v-for="(item,index) in users" :key="index">
          <v-flex xs12>
            <cards :key="users" v-on:help="showhelp=true" :data="item" class="ma-1"></cards>
          </v-flex>
        </div>
      </v-layout>
      <v-layout row-lg wrap column v-else>
        <tabs v-on:goback="showUsers = true"> </tabs>
      </v-layout>
    </v-container>
    <v-layout row justify-center>
      <v-dialog v-model="showhelp" width="700px" scrollable height="100px">
        <!--<v-btn primary dark slot="activator">Open Dialog</v-btn>-->
        <v-card>
          <v-card-title>
            <span class="headline">Use Google's location service?</span>
          </v-card-title>
          <v-card-text>Lan tyaLorem ipsum dolor sit amet,</v-card-text>
          <!--<v-card-actions>-->
          <v-btn class="green--text darken-1" flat="flat" @click.native="showhelp = false">Disagree</v-btn>
          <v-btn class="green--text darken-1" flat="flat" @click.native="showhelp = false">Agree</v-btn>
          <!--</v-card-actions>-->
        </v-card>
      </v-dialog>
    </v-layout>
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
      showhelp: false,
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
      }).catch((err) => {
        console.log(err);
      })
      this.users = [{
        'username': 'test',
        'listlike': 'test',
        'usr_id': '1',
        'Auto_ac_name': 'test'
      }];
    },
    paypal_addUser: function (url) {
      let self = this;
      this.axios.post('/subscribe', {
        'token': /token?=(.*)/g.exec(url)[1]
      })
        .then(function (response) {
          console.log(response);
          window.location.href = url.slice(0, url.indexOf('?'));
          self.alert = true;
          self.response = true;
          self.auth();
        })
        .catch(function (error) {
          console.log(error);
          self.alert = true;
          self.response = false;
          window.location.href = url.slice(0, url.indexOf('?'));
        });
    },
    paypal_changeUser: function (url) {
      let self = this;
      let paypal_res = /(?:.+paymentid=)(.+?)(?:&.+payerid=)(.+)/ig.exec(url)
      console.log(paypal_res);
      this.axios.post('/Usernamechanged', {
        'paymentid': paypal_res[1],
        'payerid': paypal_res[2]
      })
        .then(function (response) {
          console.log(response);
          window.location.href = url.slice(0, url.indexOf('?'));
          self.alert = true;
          self.response = true;
          self.auth();
        })
        .catch(function (error) {
          console.log(error);
          self.alert = true;
          self.response = false;
          window.location.href = url.slice(0, url.indexOf('?'));
        });
    },
    paypal_failed() {
      this.alert = true;
      this.response = false;
    }
  },
  created: function () {
    this.auth();
  },
  mounted() {
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


