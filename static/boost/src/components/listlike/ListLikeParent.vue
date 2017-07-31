<template>
  <main>
    <v-container fluid v-if="!add_user">
      <v-alert v-if="alert" success :value="alert" transition="scale-transition">Settings Updated
      </v-alert>
      <v-layout row justify-space-around class="mb-4">
        <v-btn outline @click.native="change_active_user = true">
          <h5>Active User Account:
            <b>{{selected_active_user}}</b>
          </h5>
        </v-btn>
        <v-btn primary light medium @click.native="manage_dialog = true">Manage Account</v-btn>
      </v-layout>
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
      </v-layout>
    </v-container>
    <v-layout row justify-center>
      <v-dialog v-model="manage_dialog" persistent width="350">
        <v-card>
          <v-card-title>
            <span class="headline">User Profile</span>
          </v-card-title>
          <v-card-text>
            <v-text-field required label="Change Insta Username" v-model="insta_username"></v-text-field>
            <v-text-field required label="Change Insta Password" :append-icon="insta_password_visibility ? 'visibility' : 'visibility_off'" :append-icon-cb="() => (insta_password_visibility = !insta_password_visibility)" type="password" class="input-group--focused" :type="insta_password_visibility ? 'text' : 'password'" v-model="insta_password"></v-text-field>
          </v-card-text>
          <v-spacer></v-spacer>
          <v-btn class="blue--text darken-1" flat @click.native="manage_dialog = false">Close</v-btn>
          <v-btn class="blue--text darken-1" flat @click.native="changeInstaData()">Save</v-btn>
        </v-card>
      </v-dialog>
    </v-layout>
    <v-layout row justify-center>
      <v-dialog v-model="change_active_user" scrollable persistent>
        <v-card>
          <v-card-title>Select User Account</v-card-title>
          <v-divider></v-divider>
          <v-card-text style="height: 300px;overflow:overlay">
            <v-radio :label="user" v-model="temp_active_user" v-for="(user, index) in userAccounts" :key="user" :value="user"></v-radio>
          </v-card-text>
          <v-divider></v-divider>
          <v-btn class="blue--text darken-1" flat @click.native="change_active_user = false">Close</v-btn>
          <v-btn class="blue--text darken-1" flat @click.native="change_active_user = false,changeActiveUser()">Save</v-btn>
        </v-card>
      </v-dialog>
    </v-layout>
  </main>
</template>

<script>
import users from './UserTable';
import notifications from './NotificationArea';
import listliketabs from './AddUser';
export default {
  components: {
    users,
    notifications,
    listliketabs
  },
  data() {
    return {
      alert: false,
      user_input: null,
      add_user: false,
      manage_dialog: false,
      change_active_user: false,
      insta_username: null,
      insta_password: null,
      insta_password_visibility: false,
      selected_active_user: '',
      temp_active_user: '',
      userAccounts: null,
      users: [{
        title: '@Test'
      },],
      notify: [

        {
          title: 'Test title',
          subtitle: "Test — test subtitle"
        },
        {
          title: 'Test title',
          subtitle: "Test — test subtitle"
        },
        {
          title: 'Test title',
          subtitle: "Test — test subtitle"
        },
        {
          title: 'Test title',
          subtitle: "Test — test subtitle"
        },
      ]
    }
  },
  methods: {
    startLiking() {
      this.users = this.users.concat(this.user_input.replace(/\s+|,+/g, " ").split(/[\s,]/).map((el) => {
        return {
          'title': el
        };
      }));
      let self = this;
      this.axios.post('/startlistlike', {
        'users': self.users,
      }).then(function (response) {
        console.log('data sent');
      }).catch(function (error) {
        alert(error);
      });
    },
    getUser() {
      this.selected_active_user = 'test';
      let self = this;
      this.axios.get('/listlikeinfo')
        .then(function (response) {
          console.log(response);
          self.userAccounts = response.data;
        }).catch(function (error) {
          alert(error);
        });
    },
    changeActiveUser() {
      let self = this;
      this.axios.post('/changeActiveUser', {
        'old_active_user': self.selected_active_user,
        'new_active_user': self.temp_active_user,
      })
        .then(function (response) {
          self.selected_active_user = self.temp_active_user;
        }).catch(function (error) {
          alert(error);
        });
    },
    changeInstaData() {
      let self = this;
      if (this.insta_username && this.insta_password && this.insta_username.length > 1 && this.insta_password.length > 1) {
        this.axios.post('/changeInstaData', {
          'insta_username': self.insta_username,
          'insta_password': self.insta_password,
        }).then(function (response) {
          self.manage_dialog = false;
          self.alert = true;
          setTimeout(() => {
            self.alert = false;
          }, 4000);
        }).catch(function (error) {
          alert(error);
        });
      }
    },
  },
  mounted() {
    this.getUser();
  }
}
</script>



<style>

</style>
