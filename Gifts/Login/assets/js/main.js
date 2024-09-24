/*=============== CHECK CORRECT CREDENTIALS ===============*/
document.querySelector('.login__form').addEventListener('submit', function(event) {
   event.preventDefault(); // Prevents the form from submitting

   // Get the values from the input fields
   const name = document.getElementById('login-name').value.toLowerCase();
   const nickname = document.getElementById('login-nickname').value.toLowerCase();
   const date = document.getElementById('login-date').value;

   // Define the correct values
   const correctName = 'indira';
   const correctNickname = 'marinera';
   const correctDate = '2024-08-21'; // Format YYYY-MM-DD

   // Verify the values
   if (name === correctName && nickname === correctNickname && date === correctDate) {
       window.location.href = '../Flowers/main.html'; // Redirects to main.html
   } else {
       alert('Datos incorrectos, abortando');
       document.getElementById('login-name').value = '';
      document.getElementById('login-nickname').value = '';
      document.getElementById('login-date').value = '';
   }
});

