# Django Chat Application

A simple and scalable chat application built using Django and WebSockets. This project allows users to sign up, log in, and interact with each other in real-time via a WebSocket-based chat system. The chat application supports direct messaging between users and stores all chat messages in the database.

## Features

- **User Authentication**: Users can sign up and log in to the application using Django's built-in authentication system.
- **Real-Time Chat**: The app uses WebSockets to provide real-time messaging between users.
- **Collapsible User List**: A collapsible menu displays all registered users, allowing users to easily select who to chat with.
- **Message History**: All previous chat messages are stored in the database and can be retrieved and displayed when users open a chat window.
- **Responsive Design**: The user interface is fully responsive, ensuring the chat application works well on all devices.

## Installation

### Prerequisites

- Python 3.x
- Django 5.x
- Channels for WebSocket support
- SQLite (or another database, if configured)

### Steps to Install

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/django-chat-app.git
   cd django-chat-app
