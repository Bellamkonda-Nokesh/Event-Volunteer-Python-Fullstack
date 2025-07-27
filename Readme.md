Event Volunteer Assignment System (Python Full-Stack)
A dynamic, full-stack web application designed to streamline the process of managing and assigning event volunteers. This system uses a smart priority algorithm to rank volunteers based on their experience and availability, ensuring the most qualified individuals are assigned first. The application features an interactive frontend and a robust Python/Flask backend with persistent data storage.

✨ Key Features
🧠 Smart Prioritization: Automatically calculates a priority score for each volunteer (60% experience + 40% availability).

🖥️ Interactive UI: A clean, responsive, and user-friendly interface for adding volunteers and visualizing the priority queue.

💾 Persistent Data Storage: Your data is saved! The Python backend stores all volunteer information in a JSON file, so nothing is lost.

🚀 Full-Stack Architecture: A clear and scalable separation between the frontend (HTML/CSS/JS) and the backend (Python/Flask).

✅ Real-time Updates: The interface instantly reflects changes made, providing a seamless user experience.

📝 RESTful API: A well-defined API for managing volunteer data.

📸 Live Preview
Here's a look at the application in action.
![Event Volunteer Assignment System Screenshot](frontend/assets/Screenshot%202025-07-27%20110744-1.png)

![Event Volunteer Assignment System Screenshot 2](frontend/assets/Screenshot%202025-07-27%20111002.png)


🛠️ Tech Stack & Architecture
This project is built with a modern, decoupled architecture.

Frontend: HTML5, Tailwind CSS, Vanilla JavaScript

Backend: Python 3, Flask

Database: JSON file for simple, persistent storage.

System Architecture
+----------------------+        HTTP Requests        +---------------------+
|                      |  (GET, POST /api/...)  |                     |
|   Frontend Browser   | <----------------------> |    Python Backend   |
|     (index.html)     |                        |      (Flask App)    |
|                      | <----------------------> |                     |
+----------------------+      JSON Responses      +----------+----------+
                                                              |
                                                              | Read/Write
                                                              v
                                                        +-----------+
                                                        |           |
                                                        |  db.json  |
                                                        |           |
                                                        +-----------+


🚀 Project Implementation Guide
Follow these steps carefully to get the project running on your local machine.

Prerequisites
Make sure you have the following software installed on your system:

Python 3.8+: Download Python

pip (Python's package installer, usually comes with Python)

A modern web browser (like Chrome, Firefox, or Edge)

Step 1: Clone the Repository
First, clone this repository to your local machine using Git.

git clone [https://github.com/Bellamkonda-Nokesh/Event-Volunteer-Python-Fullstack.git](https://github.com/Bellamkonda-Nokesh/Event-Volunteer-Python-Fullstack.git)
cd Event-Volunteer-Python-Fullstack

Step 2: Backend Setup & Launch
The backend server must be running before you can use the application.

Navigate to the Backend Directory:

cd backend
Create and Activate a Virtual Environment: This creates an isolated environment for your Python packages, which is a best practice.

On macOS/Linux:

python3 -m venv venv
source venv/bin/activate

On Windows:

python -m venv venv
.\venv\Scripts\activate

Your terminal prompt should now be prefixed with (venv).

Install Required Packages:

pip install -r requirements.txt

Run the Flask Server:

python app.py

The backend server is now running and listening on http://localhost:5000. You will see output in the terminal. Keep this terminal window open.

Step 3: Frontend Launch
Open a new terminal window.

Navigate to the frontend directory from the project's root folder.

# Make sure you are in the root 'Event-Volunteer-Python-Fullstack' directory first
cd frontend

Open index.html in your browser. The simplest way is to find the index.html file in your file explorer and double-click it.

Congratulations! The application is now fully running. You can start adding volunteers.


📋 API Endpoints
The backend provides the following API endpoints:

| Method | Endpoint | Description |
| GET | /api/data | Fetches all queued and assigned volunteers. |
| POST | /api/volunteers | Adds a new volunteer to the queue. |
| POST | /api/assign | Assigns the volunteer with the highest priority. |

🤝 Contributing
Contributions are welcome! If you have ideas for improvements or find any bugs, feel free to open an issue or submit a pull request.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is distributed under the MIT License. See the LICENSE file for more information.