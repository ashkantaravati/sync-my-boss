let csrfToken = Cookies.get("csrftoken");
axios.defaults.headers.common['X-CSRFToken'] = csrfToken

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
      username: "",
      currentAvailabilityStatus: "",
      currentWorkUpdate: "",
      currentDateTime: ""
    };
  },
  mounted() {
    this.username = this.globalusername;
  }
};
Vue.createApp(statusBar).mount("#statusBar");
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
      options: [
        {
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
      options: [
        {
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
      selectedWorkplace:0
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
      axios.get('/api/workplace/all')
      .then(response => {
          this.workplaceOptions = response.data;
      })
  }
};
Vue.createApp(attendance).mount("#attendance");
