const passwordInput = document.getElementById('id_password');
const showPasswordCheckbox = document.getElementById('id_show_password');

showPasswordCheckbox.addEventListener('change', function() {
  if (showPasswordCheckbox.checked) {
    passwordInput.type = 'text';
  } else {
    passwordInput.type = 'password';
  }
});

