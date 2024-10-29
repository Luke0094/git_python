const { createApp } Vue 

const app = createApp({
    data() {
        return{
            message:"Bella ciao"
            subs:["beffe", "lorenzoilmagnifico"]
        }
    },
    methods:{
        scriviTunz(event){
            this.message = "Thunz"
            console.log(event)
        }
    }
})

app.ount('#app')