<template>
  <v-list-item>
    <v-list-tile>
      <v-list-tile-content>
        <v-list-tile-title v-html="this.data.title"></v-list-tile-title>
      </v-list-tile-content>
    </v-list-tile>
  </v-list-item>
</template>
<script>
export default {
  props: ['data']
}
</script>
