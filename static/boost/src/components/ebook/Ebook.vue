<template>
  <main>
    <v-container fluid>
      <v-layout row wrap>
        <v-flex offset-xs4 offset-lg5 offset-sm4 xs5 sm5 lg4>
          <a @click="show_dialog">
          <img src="http://1.bp.blogspot.com/-DFZSo3Mj6sc/T5ajpLJFRVI/AAAAAAAAAJ8/AuIB_Tfhlmk/s1600/locked-pdf.jpg" />
          </a>
        </v-flex>
      </v-layout>
      </v-container>
       <v-layout row justify-center>
      <v-dialog v-model="dialog">
        <v-card v-if="!loader">
          <v-card-row>
            <v-card-title>This transaction costs $15
            </v-card-title>
          </v-card-row>
          <v-card-row>
            <v-card-text>
              <v-text-field v-model="email" label="Enter email to continue" required></v-text-field>
            </v-card-text>
          </v-card-row>
          <v-card-row actions>
            <v-btn class="blue--text darken-1" flat @click.native="dialog = false">No</v-btn>
            <v-btn class="blue--text darken-1" flat @click.native="pay">Yes</v-btn>
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
      </v-layout>

      </main>
      </template>
<script>
export default {
  data() {
    return {
      dialog: false,
      loader: false,
      email:''
    }
  },
  methods: {
    show_dialog(){
      this.dialog = true;
    },
    pay() {
      if(this.email.length>1){
      console.log('change');
      // this.dialog = false;
      this.loader = true;
      let self = this;
      this.axios.post('/email', {
        'email': self.email
      })
        .then(function (response) {
          window.location.href = response.data;
        })
        .catch(function (error) {
          // self.loader = false;
        });
      }
      else{
        alert('invalid email');
      }
    }

  }
}
</script>

<style>

</style>
