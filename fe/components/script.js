const mobileMenuBtn = document.getElementById("mobile-menu-btn");
  const closeMobileMenu = document.getElementById("close-mobile-menu");
  const mobileMenu = document.getElementById("mobile-menu");

  mobileMenuBtn.addEventListener("click", () => {
    mobileMenu.classList.remove("hidden");
  });

  closeMobileMenu.addEventListener("click", () => {
    mobileMenu.classList.add("hidden");
  });


  // Toggle Sidebar for Mobile
  const toggleSidebarBtn = document.getElementById("toggle-sidebar");
  const sidebar = document.getElementById("sidebar");

  toggleSidebarBtn.addEventListener("click", () => {
    sidebar.classList.toggle("hidden");
  });