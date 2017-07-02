<template>
  <main>
    <v-container fluid>
      <v-layout row-sm wrap column>
        <v-flex xs12 sm12 lg1>
          <v-btn floating primary large class="text-xs-right ma-1">
            <v-icon light>add</v-icon>
          </v-btn>
        </v-flex>
        <v-flex xs12 sm12 lg11>
          <v-text-field label="Add Users"></v-text-field>
        </v-flex>
        <v-flex xs2 offset-xs5>
          <v-btn light primary>
            Start Liking
            <v-icon right light>thumb_up</v-icon>
          </v-btn>
        </v-flex>
        <v-flex xs12>
          <users :data="users"></users>
        </v-flex>
      </v-layout>
      <v-divider class="mt-3"></v-divider>

      <v-layout row>
        <v-flex xs12 sm12 lg12>
          <notifications :data="notify"></notifications>
        </v-flex>
      </v-layout>
    </v-container>
  </main>
</template>
<script>
import users from './UserTable';
import notifications from './NotificationArea';
export default {
  components: {
    users,notifications
  },
  data() {
    return {
      users: [
        { title: 'Test title', avatar: '/static/test.png' },
        { title: 'Test title', avatar: '/static/test.png' },
        { title: 'Test title', avatar: '/static/test.png' },
        { title: 'Test title', avatar: '/static/test.png' },
      ],
      notify: [

        { title: 'Test title', subtitle: "Test — test subtitle" },
        { title: 'Test title', subtitle: "Test — test subtitle" },
        { title: 'Test title', subtitle: "Test — test subtitle" },
        { title: 'Test title', subtitle: "Test — test subtitle" },
      ]
    }
  }
}
</script>



<style>

</style>
