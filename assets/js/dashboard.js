let csrfToken = Cookies.get("csrftoken");
axios.defaults.headers.common["X-CSRFToken"] = csrfToken;
let updateFunc = () => console.log("func is empty");
let _employeeId = null;

function getFormattedCurrentTime(clockConfig) {
  date = new Date();
  hours = date.getHours();
  minutes = date.getMinutes();
  seconds = date.getSeconds();
  var session = clockConfig.AM_Display;
  if (hours == 0) {
    hours = 12;
  }
  if (hours > 12) {
    hours = hours - 12;
    session = clockConfig.PM_Display;
  }
  hours = hours < 10 ? "0" + hours : hours;
  minutes = minutes < 10 ? "0" + minutes : minutes;
  seconds = seconds < 10 ? "0" + seconds : seconds;
  var time = hours + ":" + minutes + ":" + seconds + " " + session;
  return time;
}

const statusBar = {
  delimiters: ["[[", "]]"],
  data() {
    return {
      employeeName: "",
      currentAvailabilityStatus: "",
      currentAvailabilityStatusText: "",
      currentWorkUpdate: "",
      statusClass: "",
      currentDateTime: "",
      clock: "",
      clockConfig: {
        AM_Display: "قبل از ظهر",
        PM_Display: "بعد از ظهر",
      },
    };
  },
  computed: {
    classObject() {
      return {
        "green-bg": this.statusClass === "available",
        "bg-info": this.statusClass === "focusing",
        "orange-bg": this.statusClass === "away",
        "orange-bg": this.statusClass === "away-for-a-meal",
        "bg-danger": this.statusClass === "busy",
        "bg-secondary": this.statusClass === "in-a-meating",
        "gray-bg": this.statusClass === "on-hourly-leave",
        "white-bg": this.statusClass === "left-work",
        "gray-bg": this.statusClass === "on-daily-leave",
      };
    },
  },
  methods: {
    updateStatus() {
      axios.get("/api/employee/me").then((response) => {
        let employee = response.data;
        _employeeId = employee.id;
        this.employeeName = employee.full_name;
        this.currentAvailabilityStatus = employee.current_availability_status;
        this.currentAvailabilityStatusText =
          employee.current_availability_status_text;
        this.currentWorkUpdate = employee.current_work_update;
        this.statusClass = employee.current_availability_status_class;
      });
    },
    tick() {
      this.clock = getFormattedCurrentTime(this.clockConfig);
    },
  },
  mounted() {
    setInterval(() => this.tick(), 1000);
    this.updateStatus();
    updateFunc = this.updateStatus;
  },
};
let statusBarApp = Vue.createApp(statusBar).mount("#statusBar");
const timeline = {
  delimiters: ["[[", "]]"],
  data() {
    return {
      logs: [],
    };
  },
  methods: {
    refreshTimeline() {
      axios
        .get("/api/logs")
        .then((response) => {
          this.logs = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.refreshTimeline();
    setInterval(this.refreshTimeline, 2000);
  },
};
Vue.createApp(timeline).mount("#timeline");

const availabilityStatus = {
  delimiters: ["[[", "]]"],
  data() {
    return {
      options: [],
      selected: "Available",
      until: "",
    };
  },
  methods: {
    submit(event) {
      if (event) {
        let statusChangeData = {
          reason: this.selected,
          until: this.until,
          employee: _employeeId,
        };

        console.log(statusChangeData);
        axios
          .post("/api/availability-statuses/create", statusChangeData)
          .then((response) => {
            console.log(response);
            updateFunc();
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
  mounted() {
    axios.get("/api/types/availability-status").then((response) => {
      this.options = response.data;
      this.selected = this.options[0].reason;
    });
  },
};
Vue.createApp(availabilityStatus).mount("#availabilityStatus");

const attendance = {
  delimiters: ["[[", "]]"],
  data() {
    return {
      options: [
        {
          action: "Exit",
          action_display: "خروج",
        },
        {
          action: "Enter",
          action_display: "ورود",
        },
      ],
      entered: false,
      workplaceOptions: [],
      selectedWorkplace: 1,
    };
  },
  methods: {
    setAttendance(event) {
      if (event) {
        let requestedAction = this.entered ? "Exit" : "Enter";
        axios
          .post("/api/attendance/set", {
            employee: _employeeId,
            action_type: requestedAction,
            workplace: this.selectedWorkplace,
          })
          .then((response) => {
            this.entered = response.data.action_type == "Enter" ? true : false;
            this.selectedWorkplace = response.data.workplace;
          });
      }
    },
  },
  mounted() {
    axios.get("/api/employee/me").then((response) => { 
        let employee = response.data;
        this.entered = employee.is_present_now;});
    axios.get("/api/workplace/all").then((response) => {
      this.workplaceOptions = response.data;
    });
  },
};
Vue.createApp(attendance).mount("#attendance");

const workUpdate = {
  delimiters: ["[[", "]]"],
  data() {
    return {
      updateTypeOptions: [],
      selectedUpdateType: "Work Started",

      activities: [],
      selectedActivity: 0,

      workTitle: "",

      estimatedRemainingTime: "",

      notes: "",
    };
  },
  methods: {
    submitWorkUpdate(event) {
      if (event) {
        let workUpdateData = {
          employee: _employeeId,
          update_type: this.selectedUpdateType,
          activity: this.selectedActivity,
          work_title: this.workTitle,
          notes: this.notes,
          estimated_remaining_time: this.estimatedRemainingTime,
        };

        console.log(workUpdateData);
        axios
          .post("/api/workupdate", workUpdateData)
          .then((response) => {
            console.log(response);
            updateFunc();
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
  mounted() {
    axios
      .get("/api/types/workupdate")
      .then((response) => {
        this.updateTypeOptions = response.data;
      })
      .catch((error) => console.log(error));

    axios.get("/api/activity/all-active").then((response) => {
      this.activities = response.data;
      this.selectedActivity = this.activities.length
        ? this.activities[0].id
        : 0;
    });
  },
};
Vue.createApp(workUpdate).mount("#workUpdate");


const insights = {
    delimiters: ["[[", "]]"],
    data() {
      return {
        presentEmployees: {},
      };
    },
    methods: {
      updateInsights() {
        axios
          .get("/api/employee/active")
          .then((response) => {
            this.presentEmployees = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
      },
    },
    mounted() {
      this.updateInsights();
      setInterval(this.updateInsights, 120000);
    },
  };
  Vue.createApp(insights).mount("#insights");