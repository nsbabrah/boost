<template>
  <main>
    <v-container fluid >
      <v-layout row>
          <v-flex xs12 sm12 lg12>
            <notifications :data="notify"></notifications>
          </v-flex>
        </v-layout>
    </v-container>
  </main>
</template>

<script>
  import notifications from './NotificationArea';
  export default {
    components: {
      notifications,
    },
    data() {
      return {
        notify: [

          {
            title: 'Test title',
            subtitle: "Test — test subtitle"
          },
          {
            title: 'Test title',
            subtitle: "Test — test subtitle"
          },
          {
            title: 'Test title',
            subtitle: "Test — test subtitle"
          },
          {
            title: 'Test title',
            subtitle: "Test — test subtitle"
          },
        ]
      }
    }
  }
</script>



<style>

</style>
