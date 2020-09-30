const timeline = {
    delimiters: ['[[', ']]'],
    data() {
        return {
          counter: 0,
          logs: [],
        }
      },
      mounted() {
        setInterval(() => {
          this.counter++;
        //   axios.get('/api/logs', { params: { id: id }})
        axios.get('/api/logs')
        .then(response => {
          console.log(response);
          this.logs = response.data;
        }).catch(error => {
          console.log(response)
        })
        }, 2000)
    }
  }
  Vue.createApp(timeline).mount("#timeline");