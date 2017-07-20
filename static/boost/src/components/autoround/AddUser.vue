<template>
  <v-tabs id="mobile-tabs-4" grow icons light v-model="activeTab">
    <v-card class="primary white--text">
      <div>
        <v-card-row @click="$emit('goback')">
          <v-btn icon light>
            <v-icon>arrow_back</v-icon>
          </v-btn>
        </v-card-row>
        <v-card-row>
          <v-card-title>Add user</v-card-title>
        </v-card-row>
      </div>
    </v-card>
    <v-tabs-bar slot="activators">
      <v-tabs-slider></v-tabs-slider>
      <v-tabs-item href="#mobile-tabs-4-1">
        STEP
        <v-icon>looks_one</v-icon>
      </v-tabs-item>
      <v-tabs-item href="#mobile-tabs-4-2">
        STEP
        <v-icon>looks_two</v-icon>
      </v-tabs-item>
      <v-tabs-item href="#mobile-tabs-4-3">
        STEP
        <v-icon>looks_3</v-icon>
      </v-tabs-item>
    </v-tabs-bar>
    <v-tabs-content :id="'mobile-tabs-4-1'">
      <v-card class="elevation-0">
        <v-card-text>
          <v-container fluid>
            <v-layout row>
              <v-flex xs4>
                <v-subheader>How Many Accounts</v-subheader>
              </v-flex>
              <v-flex xs8>
                <v-select required v-model="Userinfo.selectedPack" :error="Userinfo.selectedPack ? false : true" v-bind:items="packages" label="Select" class="input-group--focused" dark item-value="text"></v-select>
              </v-flex>
            </v-layout>
            <v-layout row>
              <v-flex xs4>
                <v-subheader>Subscription Packs</v-subheader>
              </v-flex>
              <v-flex xs8>
                <v-btn v-for="(item, index) in subscription" :key="index" @click.native="chosen_subscription=item" :outline="chosen_subscription==item" :class="chosen_subscription==item ? 'primary primary--text' : 'primary white--text'">
                  {{item}}
                </v-btn>
              </v-flex>
            </v-layout>
            <v-layout row>
              <v-flex xs4>
                <v-subheader>Total</v-subheader>
              </v-flex>
              <v-flex xs8>
                <v-subheader>{{Userinfo.purchaseOrder}}</v-subheader>
              </v-flex>
            </v-layout>
            <v-layout row>
              <v-flex xs3 offset-xs8>
                <div v-on:click="activeTab = check1() || 'mobile-tabs-4-1'">
                  <v-btn light info>
                    Next</v-btn>
                </div>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card-text>
      </v-card>
    </v-tabs-content>
    <v-tabs-content :id="'mobile-tabs-4-2'">
      <v-card class="elevation-0">
        <v-card-text>
          <v-container fluid>
            <v-layout row>
              <v-flex xs4>
                <v-subheader>Enter Email</v-subheader>
              </v-flex>
              <v-flex xs8>
                <v-text-field type="email" required label="Email" :error="Userinfo.email ? false : true" v-model="Userinfo.email"></v-text-field>
              </v-flex>
            </v-layout>

            <v-layout row v-for="(user,index) in Userinfo.username" :key="index">
              <v-flex xs4>
                <v-subheader>Enter User Name</v-subheader>
              </v-flex>
              <v-flex xs8>
                <v-text-field required label="Name" :error="Userinfo.username[index] ? false : true" v-model="Userinfo.username[index]"></v-text-field>
              </v-flex>
            </v-layout>
            <v-layout row>
              <v-flex xs3 offset-xs8>
                <div v-on:click="activeTab = check2() || 'mobile-tabs-4-2'">
                  <v-btn light info>
                    Next</v-btn>
                </div>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card-text>
      </v-card>
    </v-tabs-content>
    <v-tabs-content :id="'mobile-tabs-4-3'">
      <v-card class="elevation-0">
        <v-card-text>
          <v-container fluid>
            <v-layout v-if="!loader" row>
              <v-flex xs12>
                <v-list subheader>
                  <v-subheader>Review</v-subheader>
                  <v-list-item v-for="(value,key) in Userinfo" v-bind:key="key">
                    <v-list-tile avatar>
                      <v-list-tile-content>
                        {{reviewNames[key]}}
                      </v-list-tile-content>
                      <v-list-tile-content>
                        <v-list-tile-title>{{value ? value.toString() : value}}</v-list-tile-title>
                      </v-list-tile-content>
                    </v-list-tile>
                  </v-list-item>
                </v-list>
              </v-flex>
            </v-layout>
            <v-layout row>
              <v-flex xs3 offset-xs7 v-if="!loader">
                <a type="link" style="cursor:pointer" v-on:click="paypal">
                  <img src="//www.paypalobjects.com/en_US/i/btn/btn_xpressCheckout.gif">
                </a>
              </v-flex>
              <v-flex xs12 v-else>
                <v-progress-linear v-bind:indeterminate="true"></v-progress-linear>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card-text>
      </v-card>
    </v-tabs-content>
  </v-tabs>
</template>

<script>
export default {
  data() {
    return {
      activeTab: null,
      loader: false,
      packages: ['1', '2', '3', '4', '5'],
      subscription: ['3 months', '6 months', '12 months'],
      subscription_cost: {
        '3 months': 10, '6 months': 60, '12 months': 120
      },
      chosen_subscription: null,
      Userinfo: {
        selectedPack: null,
        username: [''],
        email: null,
        purchaseOrder: '$ 0',
      },
      reviewNames: {
        'selectedPack': 'Selected pack',
        'username': 'Usernames',
        'email': 'Email',
        'purchaseOrder': 'Purchase Order'
      }
    }
  },
  watch: {
    'Userinfo.selectedPack': function () {
      if (this.Userinfo.selectedPack > this.Userinfo.username.length) {
        while (this.Userinfo.selectedPack != this.Userinfo.username.length) {
          this.Userinfo.username.push('');
        }
      } else if (this.Userinfo.selectedPack < this.Userinfo.username.length) {
        while (this.Userinfo.selectedPack != this.Userinfo.username.length) {
          this.Userinfo.username.splice(this.Userinfo.username.length - 1, 1);
        }
      }

    },
    chosen_subscription: function () {
      this.Userinfo.purchaseOrder = '$' + this.subscription_cost[this.chosen_subscription]
    }
  },
  methods: {
    check1: function () {
      console.log(this.Userinfo.username);
      if (this.chosen_subscription !== null && this.Userinfo.selectedPack != null) {
        return 'mobile-tabs-4-2';
      }
    },
    check2: function () {
      let count = 0;
      for (var k in this.Userinfo) {
        if (!this.Userinfo.hasOwnProperty(k)) continue;
        if (this.Userinfo[k] === null || this.Userinfo[k].length < 1) {
          count++;
        }

      }
      if (count == 0 && this.Userinfo.username.length >= 1) {
        return 'mobile-tabs-4-3';
      }
    },
    paypal: function () {
      if (this.check2() === 'mobile-tabs-4-3') {
        this.loader = true;
        this.Userinfo['payment_for'] = "autoround";
        this.Userinfo['LoggedOnUser'] = localStorage.getItem("LoggedOnUser");
        let self = this;
        this.axios.post('/start_paypal', this.Userinfo)
          .then(function (response) {
            sessionStorage.removeItem('paypal_data');
            sessionStorage.setItem('paypal_data', JSON.stringify(self.Userinfo));
            localStorage.removeItem("LoggedOnUser");
            console.log(response);
            window.location.href = response.data;
          })
          .catch(function (error) {
            self.loader = false;
            delete self.Userinfo['payment_for'];
            delete self.Userinfo['LoggedOnUser'];
          });

      } else {
        alert('All input fields are required.');

      }
    }
  }
}
</script>

<style>

</style>
