const timeline = {
    delimiters: ["[[", "]]"],
    data() {
        return {
            logs: []
        };
    },
    mounted() {
        setInterval(() => {
            //   axios.get('/api/logs', { params: { id: id }})
            axios
                .get("/api/logs")
                .then(response => {
                    console.log(response);
                    this.logs = response.data;
                })
                .catch(error => {
                    console.log(response);
                });
        }, 2000);
    }
};
Vue.createApp(timeline).mount("#timeline");

const availabilityStatus = {
    delimiters: ["[[", "]]"],
    data() {
        return {
            options: [{
                    reason: "Available",
                    reason_display: "در دسترس"
                },
                {
                    reason: "In a Meeting",
                    reason_display: "در جلسه"
                },
                {
                    reason: "Focusing",
                    reason_display: "در حال تمرکز"
                },
                {
                    reason: "Busy",
                    reason_display: "مشغول"
                },
                {
                    reason: "On Hourly Leave",
                    reason_display: "در مرخصی ساعتی"
                },
                {
                    reason: "On Daily Leave",
                    reason_display: "در مرخصی روزانه"
                },
                {
                    reason: "Left Work",
                    reason_display: "سازمان را ترک کرده"
                },
                {
                    reason: "Away",
                    reason_display: "ترک میز"
                },
                {
                    reason: "Away for a meal",
                    reason_display: "ترک میز برای صرف وعده‌ی غذایی"
                }
            ],
            selected: "Available",
            until: ""
        };
    },
    methods: {
        submit(event) {
            if (event) {
                alert(event.target.tagName)
                // send post request using axios
            }
        }
    },
    mounted() {
        
    }
};
Vue.createApp(availabilityStatus).mount("#availabilityStatus");

const attendance = {
    delimiters: ["[[", "]]"],
    data() {
        return {
            options: [{
                action: "Exit",
                action_display: "خروج"
            }, {
                action: "Enter",
                action_display: "ورود"
            }],
            entered: false,
            workplace: ""
        };
    },
    methods: {
        submit(event) {
            if (event) {
                // send post request using axios
                this.entered = !this.entered;
            }
        }
    },
    mounted() {
       
    }
};
Vue.createApp(attendance).mount("#attendance");