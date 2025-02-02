document.getElementById("sidebarCollapse").addEventListener("click", function() {
    let sidebar = document.getElementById("sidebar");
    let content = document.getElementById("main-content");

    // Toggle the 'collapsed' class on the sidebar to collapse/expand
    sidebar.classList.toggle('collapsed');
    content.classList.toggle('collapsed');
});
