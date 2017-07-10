<template>
  <main>
    <v-container fluid>
        <v-layout row wrap>
          <v-flex xs12 sm12 lg12>
            <v-text-field
              name="input-1"
              label="Change Username"
            ></v-text-field>
          </v-flex>
          <v-flex xs12 sm12 lg12>
            <v-text-field
              name="input-2"
              label="Change Email"
            ></v-text-field>
          </v-flex>
          <v-flex xs12 sm12 lg12>
            <v-text-field
              name="input-3"
              label="Change Password"
            ></v-text-field>
          </v-flex>
          <v-flex xs12 sm12 lg12>
            <v-btn primary light>Save</v-btn>
          </v-flex>
        </v-layout>
    </v-container>
  </main>
</template>

<script>
export default {
  data() {
    return {

    }
  }
}
</script>
