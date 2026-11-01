// Mobile navigation
const menuBtn = document.querySelector('.menu-btn');
const nav = document.querySelector('.nav');
menuBtn?.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  menuBtn.setAttribute('aria-expanded', String(open));
});

// Enquiry form handler (Web3Forms API)
// Replace with your Web3Forms access key from https://web3forms.com
const WEB3FORMS_ACCESS_KEY = '7fefdb2a-3cf7-4f66-b78b-80c24cf3df92';

document.querySelectorAll('form[data-enquiry]').forEach((form) => {
  const status = form.querySelector('.status');
  form.addEventListener('submit', async (event) => {
    event.preventDefault();

    if (!form.checkValidity()) {
      if (status) {
        status.style.color = '#dc2626';
        status.textContent = 'Please fill in all required fields with valid details.';
      }
      form.reportValidity();
      return;
    }

    const button = form.querySelector('button[type="submit"]');
    const originalText = button ? button.textContent : 'Send enquiry';
    if (button) {
      button.disabled = true;
      button.textContent = 'Sending...';
    }
    if (status) {
      status.style.color = 'inherit';
      status.textContent = 'Sending your enquiry...';
    }

    const formData = new FormData(form);
    if (!formData.get('access_key')) {
      formData.append('access_key', WEB3FORMS_ACCESS_KEY);
    }
    formData.append('from_name', 'Digivexora Solution Website');
    formData.append('subject', 'New Website Enquiry - Digivexora Solution');

    try {
      const response = await fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        body: formData
      });
      const data = await response.json();

      if (data.success) {
        if (status) {
          status.style.color = '#16a34a';
          status.textContent = 'Thank you! Your enquiry has been received. We will get back to you shortly.';
        }
        form.reset();
      } else {
        throw new Error(data.message || 'Submission failed');
      }
    } catch (err) {
      if (status) {
        status.style.color = '#dc2626';
        status.textContent = 'Something went wrong. Please email us directly at digivexorasolution@gmail.com';
      }
    } finally {
      if (button) {
        button.disabled = false;
        button.textContent = originalText;
      }
    }
  });
});
