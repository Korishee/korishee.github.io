// Add any JavaScript logic or interactivity here (if required)

// Example: Adding animation and transitions

// Navbar scroll animation
window.addEventListener('scroll', () => {
  const navbar = document.querySelector('header');
  if (window.scrollY > 0) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// Smooth scrolling
document.querySelectorAll('nav ul li a').forEach((link) => {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    const target = document.querySelector(link.getAttribute('href'));
    window.scrollTo({
      top: target.offsetTop - 50,
      behavior: 'smooth'
    });
  });
});

// Example: Adding a dynamic class to projects
const projects = document.querySelectorAll('.project');

projects.forEach((project, index) => {
  project.addEventListener('mouseover', () => {
    project.classList.add('highlight');
  });

  project.addEventListener('mouseout', () => {
    project.classList.remove('highlight');
  });
});

// Add any additional JavaScript functionality or interactivity as needed
