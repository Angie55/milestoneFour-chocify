$(document).ready(function () {
    // Code required by emailJS to send email on submission
    const contactForm = document.querySelector('#contact-form');
    
    contactForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const data = {
            service_id: "gmail",
            template_id: "chocifyemails",
            user_id: emjs,
            template_params: {
                "name": contactForm.name.value,
                "email": contactForm.email.value,
                "message": contactForm.message.value,
            }
        };
 
    $.ajax('https://api.emailjs.com/api/v1.0/email/send', {
            type: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json'
        }).done(function () {
            contact_form_success(contactForm.name.value);
            $('input').val('');
            $('textarea').val('');
            
        }).fail(function (error) {
            contact_form_error();
            console.log('Oops... ' + JSON.stringify(error));
        });
    });

    // Sweet alert pop up message if submission successful
    function contact_form_success(name) {
        let message = `Thank you ${name}.`;
        Swal.fire({
            type: 'success',
            title: message,
            text: "Your message has been sent successfully!",
            showConfirmButton: false,
            timer: 3000
        }).then((result) => {
            if (result.value) {
                window.location.replace("/");
            }
        });
    }
    // Sweet alert pop up message if submission fails
    function contact_form_error() {
        let message = `Sorry!`;
        Swal.fire({
            type: 'warning',
            title: message,
            text: "Something went wrong with our contact form, please try again",
            showConfirmButton: false,
            timer: 3000,
        });
    }
});
