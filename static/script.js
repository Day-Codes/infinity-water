document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('newsletter-form');
    const responseMessage = document.getElementById('response-message');
  
    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      const email = document.getElementById('email').value;
  
      try {
        const response = await fetch('/newsletter', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ email }),
        });
  
        const result = await response.json();
        if (response.ok) {
          responseMessage.textContent = result.message;
          responseMessage.style.color = 'green';
        } else {
          responseMessage.textContent = result.error || 'An error occurred.';
          responseMessage.style.color = 'red';
        }
      } catch (error) {
        responseMessage.textContent = 'Network error.';
        responseMessage.style.color = 'red';
      }
    });
  });
  