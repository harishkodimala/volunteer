// static/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    console.log('scripts.js loaded!');
  
    // Volunteer form submission handling
    const volunteerForm = document.getElementById('volunteerForm');
    if (volunteerForm) {
      volunteerForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission
        const formData = new FormData(volunteerForm);
  
        fetch('/register_volunteer', {
          method: 'POST',
          body: formData
        })
        .then(response => response.json())
        .then(data => {
          alert(data.message);
          volunteerForm.reset();
        });
      });
    }
  
    // Ride request form submission handling
    const rideForm = document.getElementById('rideForm');
    if (rideForm) {
      rideForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission
        const formData = new FormData(rideForm);
  
        fetch('/request_ride', {
          method: 'POST',
          body: formData
        })
        .then(response => response.json())
        .then(data => {
          alert(data.message);
          rideForm.reset();
        });
      });
    }
  });