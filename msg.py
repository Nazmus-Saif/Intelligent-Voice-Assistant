from fbchat import Client
from fbchat.models import *

# Initialize the client (assuming you're already logged in on your device)
client = Client("CLIENT NAME", "<password>")

# Find a specific user by their name
search_name = "FACEBOOK PROFILE NAME"
users = client.searchForUsers(search_name)
if len(users) > 0:
    user = users[0]  # Get the first user (top result)
    friend_id = user.uid

    # Send a message to the specified user
    message = "ENTER YOU MESSAGE"
    sent = client.send(Message(text=message), thread_id=friend_id, thread_type=ThreadType.USER)
    if sent:
        print("Message sent successfully!")
    else:
        print("Message sending failed.")
else:
    print("User not found.")
