<script setup>
import NavBar from '@/components/navbar.vue';
import { ref } from 'vue';
import axios from 'axios';
import router from '@/router';

const name = ref("");
const email = ref("");
const password = ref("");
const role = ref("")

function reset() {
    this.name = "";
    this.email = "";
    this.password = "";
    this.role = "";
}

function register(){
    console.log("register button is clicked")
    if (!this.name){
        alert("Please Fill Name")
    }
    if (!this.email){
        alert("Please Fill Email")
    }
    if (!this.password){
        alert("Please Fill Password")
    }
    if (!this.role){
        alert("Please Fill Role")
    }

    axios.post("http://127.0.0.1:8081/api/register",
        {
            "name":this.name,
            "email":this.email,
            "password":this.password,
            "role":this.role
        }).then((response) => {
            console.log(response)
            if (response.data.status === "failed"){
                alert(response.data.message);
                this.reset();
                if (response.data.message === "user email already registered"){
                    router.push({name : "login"})
                }
            }
            if (response.data.status === "success"){
                alert(response.data.message);
                this.reset();
                router.push({name : "login"})

            }
        }).catch((error) =>{
            alert("a error occure")
            console.error(error);
        })

}


</script>



<template>
    <div>
        <NavBar></NavBar>
        <div class="container">
            <div class="row">
                <div class="col-3">

                </div>
                <div class="col-6">
                    <h1>Register Page</h1>
                    <p>name : {{ name }}</p>
                    <p>user_name : {{ email }}</p>
                    <p>password : {{ password }}</p>
                    <p>role : {{ role }}</p>
                    <form>
                        <div class="mb-3">
                            <label for="exampleInputName" class="form-label">Name</label>
                            <input type="text" class="form-control" id="exampleInputName" aria-describedby="emailHelp"
                                v-model="name">
                        </div>
                        <div class="mb-3">
                            <label for="exampleInputEmail1" class="form-label">Email address</label>
                            <input type="email" class="form-control" id="exampleInputEmail1"
                                aria-describedby="emailHelp" v-model="email">
                        </div>
                        <div class="mb-3">
                            <label for="exampleInputPassword1" class="form-label">Password</label>
                            <input type="password" class="form-control" id="exampleInputPassword1" v-model="password">
                        </div>
                        <div class="mb-3">
                            <label for="exampleInputrole" class="form-label">Role</label>

                            <select class="form-select" aria-label="Default select example" id="exampleInputrole" v-model="role">
                                <option selected>Please Select Role</option>
                                <option value="librarian">Librarian</option>
                                <option value="student">Student</option>
                            </select>
                        </div>

                        <button type="button" class="btn btn-primary" @click="register()">Register</button> &nbsp;&nbsp;
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