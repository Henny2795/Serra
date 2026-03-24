function toggleMobileMenu() {
    const menu = document.getElementById('mobile-menu');
    menu.classList.toggle('hidden');
}

// Navbar scroll effect
window.addEventListener('scroll', () => {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 20) {
        navbar.classList.add('shadow-sm', 'bg-serra-bg/95');
        navbar.classList.remove('bg-serra-bg/80');
    } else {
        navbar.classList.remove('shadow-sm', 'bg-serra-bg/95');
        navbar.classList.add('bg-serra-bg/80');
    }
});
