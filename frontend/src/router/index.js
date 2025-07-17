import { createWebHistory, createRouter } from "vue-router";

import LoginView from "@/page/loginView.vue";
import RegisterView from "@/page/registerView.vue";
import StudentDashboard from "@/page/studentDashborad.vue"
import LibrarianDashboard from "@/page/librarianDashBoard.vue"

const routes = [
    {path: "/login", name:"login", component:LoginView},
    {path: "/register", name:"register", component:RegisterView},
    {path: "/student_home", name:"student_home", component:StudentDashboard},
    {path: "/librarian_home", name:"librarian_home", component:LibrarianDashboard}
]

const router = createRouter({
    history:createWebHistory(),
    routes
})

export default router;