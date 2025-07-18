<script setup>
import { ref, onMounted } from 'vue';
import NavBar from '@/components/navbar.vue';
import axios from 'axios';

const tabs = ref({ 1: ["Home", "/home"], 2: ["Manage Users", "/manage_users"] })
const allBooks = ref([])

onMounted(() => {
    console.log("in the mount")
    getAllBooks()
})

function getAllBooks() {
    console.log("in the get all books")
    const access_token = localStorage.getItem("access_token")
    console.log(access_token)
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + access_token
    axios.get("http://127.0.0.1:8081/api/book").then((response) => {
        console.log(response.data)
        console.log(allBooks.value)

        allBooks.value = response.data
    }).catch((error) => {
        console.error(error)
    })
}



</script>

<template>
    <div>
        <NavBar :tabs=tabs :show_logout=true></NavBar>
        <h1>This is Librarian Home</h1>
        
        <div class="card" style="width: 18rem;" v-for="book in allBooks" :key="book.id">
            <div class="card-body">
                <h5 class="card-title">{{book.name}}</h5>
                <h6 class="card-subtitle mb-2 text-muted">Author: {{ book.author }}</h6>
            </div>
        </div>
    </div>
</template>

<style scoped></style>