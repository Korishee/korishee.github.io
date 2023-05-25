// Function to toggle the mobile navigation menu
function toggleMenu() {
  const menu = document.querySelector('.menu');
  menu.classList.toggle('active');
}

// Function to handle form submission
function submitForm(event) {
  event.preventDefault();

  // Get form inputs
  const nameInput = document.querySelector('#name');
  const emailInput = document.querySelector('#email');
  const messageInput = document.querySelector('#message');

  // Validate form inputs
  if (nameInput.value.trim() === '' || emailInput.value.trim() === '' || messageInput.value.trim() === '') {
    alert('Please fill in all fields.');
    return;
  }

  // Create an object with form data
  const formData = {
    name: nameInput.value.trim(),
    email: emailInput.value.trim(),
    message: messageInput.value.trim(),
  };

  // You can now send the form data to your backend or perform any other desired action

  // Clear form inputs
  nameInput.value = '';
  emailInput.value = '';
  messageInput.value = '';

  alert('Form submitted successfully!');
}

// Add event listeners
document.querySelector('.toggle-btn').addEventListener('click', toggleMenu);
document.querySelector('#contact-form').addEventListener('submit', submitForm);
