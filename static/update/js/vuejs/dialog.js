Vue.component('ppdialog', {
    template: `<v-layout row justify-center>
            <v-dialog persistent v-model="isOpen()">
                <v-card>
                    <v-card-row>
                        <v-card-title>Payment Approved</v-card-title>
                    </v-card-row>
                    <v-card-row>
                        <v-card-text>
                            <h3>Thank You</h3>
                        </v-card-text>
                    </v-card-row>
                    <v-card-row actions>
                        <v-btn floating medium class="green" @click.native="close($event)">
                            <v-icon light>check</v-icon>
                        </v-btn>
                    </v-card-row>
                </v-card>
            </v-dialog>
        </v-layout>`,
    methods: {
        isOpen: function () {
            if (/approve/g.test(window.location.href)) {
                console.log(window.location.href);
                return true;
            }
            return false;
        },
        close: function (event) {
            if (event) {
                event.preventDefault();
                window.location.href = window.location.href.substr(0, window.location.href.indexOf("?"));
            }
        }
    }
});