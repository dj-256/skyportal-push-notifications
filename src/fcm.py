from firebase_admin import credentials, messaging


# This function sends a message to a user with a specific token using the Firebase Cloud Messaging service.
def send_message(token, message, app):
    message = messaging.Message(
        notification=messaging.Notification(
            title=message["title"], body=message["body"]
        ),
        token=token,
    )

    response = messaging.send(message, app=app)
    return response
