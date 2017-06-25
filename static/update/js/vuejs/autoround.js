Vue.component('ppdialog', {
    template: "#ppdialog",
    methods: {
        isOpen: function() {
            if (/approve/g.test(window.location.href)) {
                console.log(window.location.href);
                return true;
            }
            return false;
        },
        close: function(event) {
            if (event) {
                event.preventDefault();
                window.location.href = window.location.href.substr(0, window.location.href.indexOf("?"));
            }
        }
    }
});

var template = new Vue({
    el: '#app',
    data: {
        showUsers: true,
        clipped: false,
        drawer: true,
        fixed: false,
        items: [
            { icon: 'contacts', text: 'Contacts' },
            { icon: 'history', text: 'Frequently contacted' },
            { icon: 'content_copy', text: 'Duplicates' },
            { icon: 'settings', text: 'Settings' },
            { icon: 'chat_bubble', text: 'Send feedback' },
            { icon: 'help', text: 'Help' },
            { icon: 'phonelink', text: 'App downloads' },
            { icon: 'keyboard', text: 'Got to the old version' }
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
})