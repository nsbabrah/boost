var template = new Vue({
    el: '#app',
    data: {
        showUsers: false,
        clipped: true,
        drawer: true,
        fixed: false,
        items: [
            { icon: 'dashboard', text: 'Dashboard' },
            { icon: 'thumb_up', text: 'List Likes' },
            { icon: 'brightness_auto', text: 'Auto Round' },
            { icon: 'favorite_border', text: 'Boost' },
            { icon: 'account_circle', text: 'Manage Account' },
            { icon: 'settings', text: 'Settings' }
        ],
        miniVariant: false,
        right: true,
        rightDrawer: false,
        title: 'Auto Round',
        users: [
            { name: 'random1', id: '123456' },
            { name: 'random2', id: '123456' },
            { name: 'random3', id: '123456' }
        ]

    },
    methods: {
        add: function() {
            // console.log(this.users);
            // this.users.push({ name: 'random', id: '123456' });
            this.showUsers = false;
        }
    }
});