<template>
  <main>
    <v-container fluid>
      <v-layout justify-center wrap>
        <a @click.stop="dialog = true">
          <img src="http://1.bp.blogspot.com/-DFZSo3Mj6sc/T5ajpLJFRVI/AAAAAAAAAJ8/AuIB_Tfhlmk/s1600/locked-pdf.jpg" />
        </a>
        <v-dialog transition v-model="dialog" width="350">
          <v-card v-if="!loader">
            <v-card-row>
              <v-card-title>This transaction costs $15
              </v-card-title>
            </v-card-row>
            <v-card-row>
              <v-card-text>
                <v-text-field type="email" v-model="email" label="Enter email to continue" required></v-text-field>
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
    </v-container>
  </main>
</template>
<script>
export default {
  data() {
    return {
      dialog: false,
      loader: false,
      email: ''
    }
  },
  methods: {
    pay() {
      let email_regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      if (email_regex.test(this.email)) {
        console.log('change');
        this.loader = true;
        let self = this;
        this.axios.post('/ebook', {
          'email': self.email
        })
          .then(function (response) {
            window.location.href = response.data;
          })
          .catch(function (error) {
            self.loader = false;
          });
      }
      else {
        alert('invalid email');
      }
    }

  }
}
</script>

<style>

</style>
