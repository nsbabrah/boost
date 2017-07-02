<template>
  <v-card>
    <v-list one-line>
      <v-list-item v-for="item in this.data" v-bind:key="item.title">
            <v-list-tile avatar>
              <v-list-tile-avatar>
                <img v-bind:src="item.avatar"/>
              </v-list-tile-avatar>
              <v-list-tile-content>
                <v-list-tile-title v-html="item.title"></v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list-item>
    </v-list>
  </v-card>
</template>
<script>
export default {
  props: ['data']
}
</script>
