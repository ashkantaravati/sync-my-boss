let csrfToken = Cookies.get("csrftoken");
axios.defaults.headers.common["X-CSRFToken"] = csrfToken;
let updateFunc = ()=> console.log('func is empty');

const employeeDataMixin = {
    methods: {
        setEmployeeId(id) {
            this.employeeId = id;
            //   alert(id);
            //   alert(this.employeeId);
        }
    },
    data() {
        return {
            employeeId: 0
        };
    }
};
const statusBar = {
    delimiters: ["[[", "]]"],
    mixins: [employeeDataMixin],
    data() {
        return {
            employeeName: "",
            currentAvailabilityStatus: "",
            currentAvailabilityStatusText: "",
            currentWorkUpdate: "",
            statusClass: "",
            currentDateTime: ""
        };
    },
    computed: {
        classObject() {
            return {
                "bg-success": this.statusClass === "available",
                "bg-info": this.statusClass === "focusing",
                "bg-warning": this.statusClass === "away",
                "bg-primary": this.statusClass === "away-for-a-meal",
                "bg-danger": this.statusClass === "busy",
                "bg-secondary": this.statusClass === "in-a-meating",
                "bg-dark": this.statusClass === "on-hourly-leave",
                "bg-light": this.statusClass === "left-work",
                "bg-dark": this.statusClass === "on-daily-leave"
            };
        }
    },
    methods: {
        updateStatus() {
            axios.get(`/api/employee/${this.employeeId}`).then(response => {
                let employee = response.data;
                this.employeeName = employee.full_name;
                this.currentAvailabilityStatus = employee.current_availability_status;
                this.currentAvailabilityStatusText =
                    employee.current_availability_status_text;
                this.currentWorkUpdate = employee.current_work_update;
                this.statusClass = employee.current_availability_status_class;
            });
        }
    },
    mounted() {
        // this.username = this.globalusername;
        this.updateStatus();
        updateFunc = this.updateStatus;
    }
};
let statusBarApp = Vue.createApp(statusBar).mount("#statusBar");
const timeline = {
    delimiters: ["[[", "]]"],
    data() {
        return {
            logs: []
        };
    },
    methods: {
        refreshTimeline() {
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
        }
    },
    mounted() {
        setInterval(this.refreshTimeline, 2000);
    }
};
Vue.createApp(timeline).mount("#timeline");

const availabilityStatus = {
    delimiters: ["[[", "]]"],
    mixins: [employeeDataMixin],
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
            debugger;
            if (event) {
                let statusChangeData = {
                    reason: this.selected,
                    until: this.until,
                    employee: this.employeeId
                };

                console.log(statusChangeData);
                axios
                    .post("/api/availability-statuses/create", statusChangeData)
                    .then(response => {
                        console.log(response);
                        // this.logs = response.data;
                        // timeline.refreshTimeline()
                        updateFunc();
                    })
                    .catch(error => {
                        console.log(error);
                    });
            }
        }
    },
    mounted() {}
};
Vue.createApp(availabilityStatus).mount("#availabilityStatus");

const attendance = {
    delimiters: ["[[", "]]"],
    mixins: [employeeDataMixin],
    data() {
        return {
            options: [{
                    action: "Exit",
                    action_display: "خروج"
                },
                {
                    action: "Enter",
                    action_display: "ورود"
                }
            ],
            entered: false,
            workplaceOptions: [],
            selectedWorkplace: 1
        };
    },
    methods: {
        setAttendance(event) {
            if (event) {
                let requestedAction = this.entered ? "Exit" : "Enter";
                axios
                    .post("/api/attendance/set", {
                        employee: this.employeeId,
                        action_type: requestedAction,
                        workplace: this.selectedWorkplace
                    })
                    .then(response => {
                        this.entered = response.data.action_type == "Enter" ? true : false;
                        this.selectedWorkplace = response.data.workplace;
                    });
            }
        }
    },
    mounted() {
        axios.get("/api/workplace/all").then(response => {
            this.workplaceOptions = response.data;
        });
    }
};
Vue.createApp(attendance).mount("#attendance");