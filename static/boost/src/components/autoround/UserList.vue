<template>
  <v-card raised>
    <v-card-row class="green darken-1" height="10px">
      <v-card-title>
        <span class="white--text">{{'@'+postData.Auto_ac_name}}</span>
        <v-spacer></v-spacer>
        <div>
          <v-menu id="marriot" bottom left origin="top right">
            <v-btn icon="icon" slot="activator" class="white--text">
              <v-icon>more_vert</v-icon>
            </v-btn>
            <v-list>
              <v-list-item @click.capture="showhelp = true">
                <v-list-tile>
                  <v-list-tile-title> Help </v-list-tile-title>
                </v-list-tile>
              </v-list-item>
              <v-list-item @click.capture="changename_dialog = true">
                <v-list-tile>
                  <v-list-tile-title> Change Name </v-list-tile-title>
                </v-list-tile>
              </v-list-item>

            </v-list>
          </v-menu>
        </div>

      </v-card-title>
    </v-card-row>
    <v-card-text>
      <v-card-row height="75px">
        <img :src="postData.image" width="100px" height="100px">
      </v-card-row>
    </v-card-text>
    <v-divider></v-divider>
    <v-card-row actions class="mt-0">
      <v-dialog v-model="changename_dialog">
        <v-card v-if="!loader">
          <v-card-row>
            <v-card-title>$1 will be charged for this action Continue ?
            </v-card-title>
          </v-card-row>
          <v-card-row>
            <v-card-text>
              <v-text-field v-model="newuser" label="New username" required></v-text-field>
            </v-card-text>
          </v-card-row>
          <v-card-row actions>
            <v-btn primary flat @click.native="changename_dialog = false">No</v-btn>
            <v-btn primary flat @click.native="changename">Yes</v-btn>
          </v-card-row>
        </v-card>
        <v-card v-else>
          <v-card-row>
            <v-card-text>
              Redirecting to Paypal...
            </v-card-text>
          </v-card-row>
          <v-card-row>
            <v-card-title>
              <v-progress-linear v-bind:indeterminate="true"></v-progress-linear>
            </v-card-title>
          </v-card-row>
        </v-card>
      </v-dialog>
      <v-dialog v-model="showhelp" width="700px" scrollable height="100px">
        <v-card>
          <v-card-title>
            <span class="headline">Help</span>
          </v-card-title>
          <v-card-text>1) Default active your three autoround accounts timings: 1) 8 PM 2)11 PM 2)3AM Second 1)You can gain likes in Autoround depend on traffic 2)Get likes from real user in pool ready for liking your images
          </v-card-text>
          <!--<v-card-actions>-->
          <v-btn primary flat="flat" @click.native="showhelp = false">Okay</v-btn>
          <!--</v-card-actions>-->
        </v-card>
      </v-dialog>
      <v-spacer></v-spacer>
      <v-btn small floating primary @click.native="play_pause" class="ml-2">
        <v-icon v-if="!postData.play" light>play_arrow</v-icon>
        <v-icon v-else light>pause_circle_filled</v-icon>
      </v-btn>
    </v-card-row>
  </v-card>
</template>

<script>
export default {
  props: ['postData'],
  data() {
    return {
      changename_dialog: false,
      newuser: '',
      loader: false,
      showhelp: false,

    }
  },
  methods: {
    play_pause() {
      this.postData.play = !this.postData.play;
      let self = this;
      this.axios.post('/changeState', {
        'name': self.postData.Auto_ac_name,
        'state': self.postData.play
      })
        .then(function (response) {
          // location.reload();
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    changename() {
      // this.changename_dialog = false;
      this.loader = true;
      let self = this;
      this.axios.post('/changeUser', {
        'old': self.postData.Auto_ac_name,
        'new': self.newuser
      })
        .then(function (response) {
          window.location.href = response.data;
        })
        .catch(function (error) {
          self.loader = false;
        });

    }

  }
}
</script>

<style>

</style>
