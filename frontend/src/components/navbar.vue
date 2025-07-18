<script setup>

import router from '@/router';
defineProps({
    tabs: Object,
    show_logout: Boolean
})

function logOut() {
    localStorage.removeItem("email");
    localStorage.removeItem("access_token");
    localStorage.removeItem("role");
    router.push({ "name": "login" })
}

</script>



<template>
    <div>
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Navbar</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                    aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item" v-for="(list, key) in tabs" :key="key">
                            <RouterLink class="nav-link" :to=list[1]>{{ list[0] }}</RouterLink>
                        </li>
                        <li class="nav-item align-left" v-show="show_logout">
                            <a @click="logOut()">
                                Logout
                            </a>

                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>
</template>



<style scoped></style>