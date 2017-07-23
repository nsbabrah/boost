<template>
  <main>
    <v-container fluid>
      <v-layout justify-center wrap v-if="!pay_view">
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
      <v-layout row wrap v-else>
        <v-flex xs12>
          <v-btn round outline primary medium fab class="mr-5" @click.native.stop="page--">
            <v-icon>keyboard_arrow_left</v-icon>
          </v-btn>
          <!-- <v-btn outline primary small fab class="ml-5" floating @click.native.stop="rotate += 90">
                      <v-icon>rotate_right</v-icon>
                    </v-btn>
                    <v-btn outline primary small fab class="ml-5  mr-5" right floating @click.native.stop="rotate -= 90">
                      <v-icon>rotate_left</v-icon>
                    </v-btn> -->
          <v-btn round outline primary style="float:right" medium fab @click.native.stop="page++">
            <v-icon>keyboard_arrow_right</v-icon>
          </v-btn>
          <v-progress-linear v-if="loadedRatio > 0 && loadedRatio < 1" :value="Math.floor(loadedRatio * 100)" height="5"></v-progress-linear>
          <pdf :page="page" src="./static/static_vuejs/pdf/ebook.pdf" :rotate="rotate" @progress="loadedRatio = $event" @numPages="numPages = $event"></pdf>
        </v-flex>
      </v-layout>
    </v-container>
  </main>
</template>
<script>
import pdf from 'vue-pdf';
export default {
  components: {
    pdf
  },
  data() {
    return {
      dialog: false,
      loader: false,
      email: '',
      pay_view: false,
      page: 1,
      numPages: 0,
      loadedRatio: 0,
      rotate: 0,
    }
  },
  watch: {
    page() {
      if (this.page === this.numPages + 1) {
        this.page = 0;
      }
      else if (this.page === 0) {
        this.page = this.numPages;
      }
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
  }, created() {
    if (window.location.href.substr(-2) !== "?r") {
      window.location = window.location.href + "?r";
      window.location.reload(false);
    } else {
      let self = this;
      this.axios.post('/hasPaid_ebook', {
        'LoggedOnUser': localStorage.getItem("LoggedOnUser")
      })
        .then(function (response) {
          if (response.data === true) {
            self.pay_view = true;
          }
          else {
            self.pay_view = false;
          }
        })
        .catch(function (error) {
          self.pay_view = false;
        });
    }
  }
}
</script>

<style>

</style>
