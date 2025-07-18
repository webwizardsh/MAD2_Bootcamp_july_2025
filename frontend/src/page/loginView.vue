<script setup>
import NavBar from '@/components/navbar.vue';
import axios from 'axios';
import { ref } from 'vue';
import router from '@/router';

const email = ref("");
const password = ref("");
const tabs = ref({
    1: ["Login", "/login"],
    2: ["Register", "/register"]
})

function login_user() {
    if (!this.email || !this.password) {
        alert("Please Fill the fields")
        return;
    }
    axios.post("http://127.0.0.1:8081/api/login",
        {
            "email": this.email,
            "password": this.password
        }).then((response) => {
            console.log(response)
            if (response.data.status === "failed") {
                alert(response.data.message);
                this.reset();
                if (response.data.message === "user email not registered") {
                    router.push({ name: "login" })
                }
            }
            if (response.data.status === "success") {
                const access_token = response.data.access_token
                const email =  response.data.email
                const role = response.data.role
                
                localStorage.setItem("access_token", access_token)
                localStorage.setItem("email", email)
                localStorage.setItem("role", role)
                alert(response.data.message);
                this.reset();
                if (role === "student"){
                    router.push({ name: "student_home" })
                }
                if (role === "librarian"){
                    router.push({ name: "librarian_home" })
                }
            }
        }).catch((error) => {
            alert("a error occurr")
            console.error(error);
        })
}



function reset() {
    this.email = "";
    this.password = "";
}
</script>

<template>
    <div>
        <NavBar :tabs="tabs" :show_logout=false></NavBar>
        <div class="container">
            <div class="row">
                <div class="col-3">

                </div>
                <div class="col-6">
                    <h1>Login Page</h1>
                    <p>user_name : {{ email }}</p>
                    <p>password : {{ password }}</p>
                    <form>
                        <div class="mb-3">
                            <label for="exampleInputEmail1" class="form-label">Email address</label>
                            <input type="email" class="form-control" id="exampleInputEmail1"
                                aria-describedby="emailHelp" v-model="email">
                            <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                        </div>
                        <div class="mb-3">
                            <label for="exampleInputPassword1" class="form-label">Password</label>
                            <input type="password" class="form-control" id="exampleInputPassword1" v-model="password">
                        </div>

                        <button type="button" class="btn btn-primary" @click="login_user()">Submit</button> &nbsp;&nbsp;
                        <button type="button" class="btn btn-warning" @click="reset()">ReSet</button>
                    </form>
                </div>
                <div class="col-3">

                </div>
            </div>
        </div>

    </div>
</template>



<style scoped></style>