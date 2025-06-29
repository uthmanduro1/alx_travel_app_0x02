from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_payment_confirmation(email, booking_ref):
    send_mail(
        subject="Payment Confirmation",
        message=f"Your booking {booking_ref} has been confirmed.",
        from_email="noreply@travel.com",
        recipient_list=[email],
    )
