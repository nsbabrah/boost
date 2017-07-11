<template>
  <v-card>
    <v-list two-line>
      <template v-for="item in this.data">
        <v-list-item v-bind:key="item.title">
          <v-list-tile avatar>
            <v-list-tile-content>
              <v-list-tile-title v-html="item.title"></v-list-tile-title>
              <v-list-tile-sub-title v-html="item.subtitle"></v-list-tile-sub-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list-item>
      </template>
    </v-list>
  </v-card>
</template>

<script>
export default {
  props: ['data']
}
</script>
