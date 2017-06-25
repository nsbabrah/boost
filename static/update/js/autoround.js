Vue.component('card', {
    template: "#card",
    props: ['data']
})
var data = {
    activeTab: null,
    packages: ['$15', '$25', '$35', '$45'],
    Userinfo: {
        selectedPack: null,
        firstName: null,
        AccountInfo: null,
        name: null,
        email: null,
        purchaseOrder: null,
    }
}
Vue.component('tabs', {
    template: "#tabs",
    data: function() {
        return data;
    },
    methods: {
        check1: function() {
            console.log(data.Userinfo.firstName);
            if (data.Userinfo.selectedPack != null && data.Userinfo.firstName != null || data.Userinfo.firstName > 1) {
                return 'mobile-tabs-4-2';
            }
        },
        check2: function() {
            let count = 0;
            for (var k in data.Userinfo) {
                if (!data.Userinfo.hasOwnProperty(k)) continue;
                if (data.Userinfo[k] === null || data.Userinfo[k].length < 1) {
                    count++;
                }

            }
            if (count == 0) {
                console.log(count);
                return 'mobile-tabs-4-3';
            }
        }
    }
})
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