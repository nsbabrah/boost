<template>
  <main>
    <v-container fluid>
      <!--<ppdialog></ppdialog>-->
      <v-layout row-sm wrap column v-if="showUsers">
        <v-flex xs12 sm12 lg1>
          <v-btn floating large @click.native="add_user" class="blue text-xs-right ma-1">
            <v-icon light>add</v-icon>
          </v-btn>
        </v-flex>
        <div v-for="(item,index) in users">
          <v-flex xs12>
            <cards :key="users" v-on:remove="users.splice(index, 1)" :data="item" class="ma-1"></cards>
          </v-flex>
        </div>
      </v-layout>
      <v-layout row-lg wrap column v-else>
        <tabs v-on:goback="showUsers = true"> </tabs>
      </v-layout>
    </v-container>
  </main>
</template>

<script>
import cards from './UserList.vue';
import tabs from './AddUser.vue';
export default {
  components: {
    cards, tabs
  },
  data() {
    return {
      showUsers: true,
      users: null
    }
  },
  methods: {
    add_user: function () {
      this.showUsers = false;
    },
    auth: function () {
      console.log('auth');
      setTimeout(() => {
        this.users = [{ 'name': 'random', 'usr_id': '1' }, { 'name': 'random1', 'usr_id': '2' }];
      }, 1000);
      // axios.post('http://0.0.0.0:2300/userauth', { "username": "nav" })
      //   .then(function (response) {

      //     //in Vue js call template which is page variable and send data from here

      //     usrname = response.data;
      //     console.log(usrname)
      //     template.users = (usrname)

      //     console.log(usrname['username'])

      //   })
      //   .catch(function (error) {
      //     console.log(error);
      //   });

    }
  },
  mounted: function () {
    this.auth();
  }
}
</script>

<style>

</style>
