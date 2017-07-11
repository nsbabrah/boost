<template>
  <main>
    <v-container fluid>
      <v-layout row wrap>
        <v-flex xs12 sm12 lg12>
          <v-select v-bind:items="change" v-model="selected_to_change" single-line auto required class="input-group--focused" prepend-icon="edit"></v-select>
          <v-text-field name="input-1" :label="'Change '+selected_to_change" v-model="input" required></v-text-field>
        </v-flex>
        <v-flex xs12 sm12 lg12>
          <v-btn primary light @click.native="save">Save</v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </main>
</template>

<script>
  export default {
    data() {
      return {
        selected_to_change: '',
        change: ['Username', 'Email', 'Password'],
        input: null
      }
    },
    methods: {
      save() {
        if (this.input && this.input.length > -1) {
          console.log("Post:", {
            'change': this.selected_to_change,
            'value': this.input
          });
          let self = this;
          this.axios.post('/manage', {
              'change': this.selected_to_change,
              'value': this.input
            })
            .then(function(response) {
              console.log(response);
              // location.reload();
            })
            .catch(function(error) {
              console.log(error);
            });
        } else {
          alert('Input field shouldn\'t be empty');
        }
      }
    }
  }
</script>
