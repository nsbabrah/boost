// var d = {{usern}};
// cosole.log(d)

var template = new Vue({
    el: '#app',
    data: {
        showUsers: true,
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

        users:''


    },
    methods: {
        add: function () {
            // console.log(this.users);
            // this.users.push({ name: 'random', id: '123456' });
            this.showUsers = false;
        },
        auth:function () {
            axios.post('http://0.0.0.0:2300/userauth',{"username":"nav"})
                    .then(function (response) {

//in Vue js call template which is page variable and send data from here

                        usrname = response.data;
                        console.log(usrname)
                        template.users = (usrname)

                        console.log(usrname['username'])

                        })
                    .catch(function (error) {
                        console.log(error);
                    });

        }
    },
    mounted: function () {
            this.auth();
    }
});