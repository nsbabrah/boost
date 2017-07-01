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
        <v-icon class="mr-5" dark>card_membership</v-icon>
        <div>
          <div>{{this.data.name}}</div>
          <strong>{{this.data.usr_id}}</strong>
        </div>
      </v-card-row>
    </v-card-text>
    <v-divider></v-divider>
    <v-card-row actions class="mt-0">
      <v-btn flat class="green--text darken-1">Contact Info</v-btn>
      <v-spacer></v-spacer>
      <v-btn small floating primary class="ml-2">
        <v-icon light>play_arrow</v-icon>
      </v-btn>
      <v-spacer></v-spacer>

      <v-btn small floating primary class="ml-2">
        <v-icon light>pause_circle_filled</v-icon>
      </v-btn>

    </v-card-row>
  </v-card>
</template>

<script>
export default {
  props: ['data']
}
</script>

<style>

</style>
