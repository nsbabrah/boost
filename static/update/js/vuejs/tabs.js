var data = {
    activeTab: null,
    packages: ['$15', '$25', '$35', '$45'],
    Userinfo: {
        selectedPack: null,
        firstName: null,
        AccountInfo: null,
        name: null,
        email: null,
        purchaseOrder: null,
    }
}
Vue.component('tabs', {
    template: `        <v-tabs id="mobile-tabs-4" grow icons light v-model="activeTab">
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
                                    <v-subheader>Enter First Name</v-subheader>
                                </v-flex>
                                <v-flex xs8>
                                    <v-text-field required label="Name" :error="Userinfo.firstName ? false : true" v-model="Userinfo.firstName"></v-text-field>
                                </v-flex>
                            </v-layout>
                            <v-layout row>
                                <v-flex xs4>
                                    <v-subheader>Choose a Package</v-subheader>
                                </v-flex>
                                <v-flex xs8>
                                    <v-select v-model="Userinfo.selectedPack" :error="Userinfo.selectedPack ? false : true" v-bind:items="packages" label="Select" class="input-group--focused" dark item-value="text"></v-select>
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
                                    <v-subheader>Enter Account Info</v-subheader>
                                </v-flex>
                                <v-flex xs8>
                                    <v-text-field required label="Account Info" :error="Userinfo.AccountInfo ? false : true" v-model="Userinfo.AccountInfo"></v-text-field>
                                </v-flex>
                            </v-layout>
                            <v-layout row>
                                <v-flex xs4>
                                    <v-subheader>Enter Name</v-subheader>
                                </v-flex>
                                <v-flex xs8>
                                    <v-text-field required label="Name" :error="Userinfo.name ? false : true" v-model="Userinfo.name"></v-text-field>
                                </v-flex>
                            </v-layout>
                            <v-layout row>
                                <v-flex xs4>
                                    <v-subheader>Enter Email</v-subheader>
                                </v-flex>
                                <v-flex xs8>
                                    <v-text-field type="email" required label="Email" :error="Userinfo.email ? false : true" v-model="Userinfo.email"></v-text-field>
                                </v-flex>
                            </v-layout>
                            <v-layout row>
                                <v-flex xs4>
                                    <v-subheader>Enter Purchase Order</v-subheader>
                                </v-flex>
                                <v-flex xs8>
                                    <v-text-field required label="Purchase Order" :error="Userinfo.purchaseOrder ? false : true" v-model="Userinfo.purchaseOrder"></v-text-field>
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
                            <v-layout row>
                                <v-flex xs3>
                                    <img src="//www.paypalobjects.com/en_US/i/btn/btn_xpressCheckout.gif">
                                    </div>
                                </v-flex>
                            </v-layout>
                            <v-layout row>
                                <v-flex xs3 offset-xs8>
                                    <!--<div v-on:click="">-->
                                    <v-btn light info>
                                        Submit</v-btn>
                                    <!--</div>-->
                                </v-flex>

                            </v-layout>
                        </v-container>
                    </v-card-text>
                </v-card>
            </v-tabs-content>
        </v-tabs>`,
    data: function() {
        return data;
    },
    methods: {
        check1: function() {
            console.log(data.Userinfo.firstName);
            if (data.Userinfo.selectedPack != null && data.Userinfo.firstName != null || data.Userinfo.firstName > 1) {
                return 'mobile-tabs-4-2';
            }
        },
        check2: function() {
            let count = 0;
            for (var k in data.Userinfo) {
                if (!data.Userinfo.hasOwnProperty(k)) continue;
                if (data.Userinfo[k] === null || data.Userinfo[k].length < 1) {
                    count++;
                }

            }
            if (count == 0) {
                console.log(count);
                return 'mobile-tabs-4-3';
            }
        }
    }
})