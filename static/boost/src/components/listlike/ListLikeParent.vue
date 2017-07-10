<template >
  <main>
    <v-container fluid  v-if="!add_user">
      <v-layout row-sm wrap colum>
        <v-flex xs12 sm12 lg1>
          <v-btn @click.native="add_user = true" floating primary large class="text-xs-right ma-1">
            <v-icon light>add</v-icon>
          </v-btn>
        </v-flex>
        <v-flex xs12 sm12 lg11>
          <v-text-field label="Add Users" v-model="user_input" :append-icon="'clear'" :append-icon-cb="() => (user_input = null)"></v-text-field>
        </v-flex>
        <v-flex xs2 offset-xs5>
          <v-btn light primary @click.native="startLiking">
            Start Liking
            <v-icon right light>thumb_up</v-icon>
          </v-btn>
        </v-flex>
        <v-flex xs12>
          <v-card style="overflow-y:scroll;" height="200px">
            <v-list one-line>
              <div v-for="item in users" v-bind:key="item.title">
                <users :data="item"></users>
              </div>
            </v-list>
          </v-card>
        </v-flex>
      </v-layout>
      <v-divider class="mt-3"></v-divider>

      <!--<v-layout row>
        <v-flex xs12 sm12 lg12>
          <notifications :data="notify"></notifications>
        </v-flex>
      </v-layout>-->
    </v-container>
    <v-container fluid v-if="add_user">
      <v-layout row-sm wrap column>
        <v-flex xs12 sm12 lg1>
          <listliketabs v-on:goback="add_user = false"></listliketabs>
        </v-flex>
      </v-layout></v-container>
  </main>
</template>
<script>
import users from './UserTable';
import notifications from './NotificationArea';
import listliketabs from './AddUser';
export default {
  components: {
    users, notifications,listliketabs
  },
  data() {
    return {
      user_input: null,
      add_user:false,
      users: [
        { title: '@Test' },
      ],
      notify: [

        { title: 'Test title', subtitle: "Test — test subtitle" },
        { title: 'Test title', subtitle: "Test — test subtitle" },
        { title: 'Test title', subtitle: "Test — test subtitle" },
        { title: 'Test title', subtitle: "Test — test subtitle" },
      ]
    }
  },
  methods: {
    startLiking: function () {
      this.users = this.users.concat(this.user_input.replace(/\s+|,+/g, " ").split(/[\s,]/).map((el) => {
        return { 'title': el };
      }));
    },
  },
}

</script>



<style>

</style>
