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
        <div v-for="(item,index) in users" :key="index">
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
import axios from 'axios';
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
      const self = this;
      axios.get('/userauth').then((res) => {
        console.log(res);
        self.users = res.data;
      }).catch((err) => {
        console.log(err);
      })
      this.users = [{ 'username': 'test', 'listlike': 'test', 'usr_id': '1', 'Auto_ac_name': 'test' }];
    }
  },
  created: function () {
    this.auth();
  }
}
</script>

<style>

</style>


