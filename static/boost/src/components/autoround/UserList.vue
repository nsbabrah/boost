<template>
  <v-card>
    <v-card-row class="green darken-1">
      <v-card-title>
        <span class="white--text">User</span>
        <v-spacer></v-spacer>
        <div>
          <v-menu id="marriot" bottom left origin="top right">
            <v-btn icon="icon" slot="activator" class="white--text">
              <v-icon>more_vert</v-icon>
            </v-btn>
            <v-list>
              <v-list-item>
                <v-list-tile>
                  <v-list-tile-title @click="$emit('remove')">Remove</v-list-tile-title>
                </v-list-tile>
              </v-list-item>
              <v-list-item>
                <v-list-tile>
                  <v-list-tile-title>Send Feedback</v-list-tile-title>
                </v-list-tile>
              </v-list-item>
            </v-list>
          </v-menu>
        </div>
  
      </v-card-title>
    </v-card-row>
    <v-card-text>
      <v-card-row height="75px">
        <img :src="this.data.image" width="100px" height="100px">
        <v-spacer></v-spacer>
        <div>
          <strong>{{this.data.Auto_ac_name}}</strong>
          <!--<div>{{this.data.usr_id}}</div>-->
        </div>
      </v-card-row>
    </v-card-text>
    <v-divider></v-divider>
    <v-card-row actions class="mt-0">
      <!--<v-layout row justify-center>-->
      <v-dialog v-model="dialog">
        <v-btn flat class="green--text darken-1" slot="activator">Contact Info</v-btn>
  
        <v-card>
          <v-card-row>
            <v-card-title>User Profile</v-card-title>
          </v-card-row>
          <v-card-row>
            <v-card-text>
              <v-text-field v-model="newuser" label="New username" required></v-text-field>
            </v-card-text>
          </v-card-row>
          <v-card-row actions>
            <v-btn class="blue--text darken-1" flat @click.native="dialog = false">Close</v-btn>
            <v-btn class="blue--text darken-1" flat @click.native="changename">Save</v-btn>
          </v-card-row>
        </v-card>
      </v-dialog>
      <!--</v-layout> -->
      <v-spacer></v-spacer>
      <v-btn medium floating primary @click.native="play_pause" class="ml-2">
        <v-icon v-show="!play" light>play_arrow</v-icon>
        <v-icon v-show="play" light>pause_circle_filled</v-icon>
      </v-btn>
    </v-card-row>
  </v-card>
</template>

<script>
import axios from 'axios';
export default {
  props: ['data'],
  data() {
    return {
      play: false,
      dialog: false,
      newuser : ''
    }
  },
  methods: {
    play_pause() {
      this.play = !this.play;
    },
    changename() {
      console.log('change');
      this.dialog = false;
      let self = this;
      axios.post('/changeUser', { 'old': self.data.Auto_ac_name, 'new': self.newuser })
        .then(function (response) {
          console.log(response);
          // location.reload();
        })
        
        .catch(function (error) {
          console.log(error);
        });

    }

  }
}
</script>

<style>

</style>
