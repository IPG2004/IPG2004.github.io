document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("login-form");
    const registerForm = document.getElementById("register-form");
    const switchToRegister = document.getElementById("switch-to-register");
    const switchToLogin = document.getElementById("switch-to-login");
    const logoutButton = document.getElementById("logout");

    // Sidebar toggle functionality
    const sidebarToggle = document.getElementById("sidebar-toggle");
    const sidebar = document.getElementById("sidebar");

    // Navigation links
    const homeLink = document.getElementById("home-link");
    const tasksLink = document.getElementById("tasks-link");
    const homePage = document.getElementById("home-page");
    const tasksPage = document.getElementById("tasks-page");

    // Switching between login and register forms
    switchToRegister.addEventListener("click", function (e) {
        e.preventDefault();
        loginForm.style.display = "none";
        registerForm.style.display = "block";
    });

    switchToLogin.addEventListener("click", function (e) {
        e.preventDefault();
        registerForm.style.display = "none";
        loginForm.style.display = "block";
    });

    // Dummy login and register actions (this should be connected to a backend)
    loginForm.addEventListener("submit", function (e) {
        e.preventDefault();
        document.getElementById("auth-page").style.display = "none";
        document.getElementById("main-content").style.display = "flex";
    });

    registerForm.addEventListener("submit", function (e) {
        e.preventDefault();
        alert("Usuario registrado con éxito!");
        registerForm.style.display = "none";
        loginForm.style.display = "block";
    });

    // Sidebar toggle action
    sidebarToggle.addEventListener("click", function () {
        sidebar.classList.toggle("open");
    });

    // Logout action
    logoutButton.addEventListener("click", function () {
        document.getElementById("main-content").style.display = "none";
        document.getElementById("auth-page").style.display = "flex";
    });

    // Navigation actions
    homeLink.addEventListener("click", function () {
        if (sidebar.classList.contains("open")) {
            sidebar.classList.toggle("open");
        }
        homePage.style.display = "block";
        tasksPage.style.display = "none";
    });

    tasksLink.addEventListener("click", function () {
        sidebar.classList.toggle("open");
        homePage.style.display = "none";
        tasksPage.style.display = "block";
    });

    // Default page
    homeLink.click();
});
