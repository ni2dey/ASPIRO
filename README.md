# Aspiro – Career Recommendation System
Aspiro is an intelligent career recommendation system designed to help users discover the most suitable career paths based on their skills. Built as our final year project, ASpiro leverages modern web technologies and advanced machine learning models to deliver personalized recommendations in real-time.

🚀 Features:

    🧠 AI-Powered Suggestions using Graph Neural Networks (GNN)
    
    🖥️ Interactive Frontend developed with HTML, CSS, JavaScript, and Vue.js
    
    🔙 Flask Backend to manage user interactions and model inference
    
    📊 Skill-based input to guide career path recommendations
    
    🔐 User-friendly and responsive design

🛠️ Tech Stack:

    Frontend: HTML, CSS, JavaScript, Vue.js
    
    Backend: Python (Flask)
    
    Machine Learning Model: Graph Neural Network (GNN)
    
    Others: REST API for communication between frontend and backend

🧩 How It Works:

    Users enter their current skills and interests into the application.
    
    The frontend communicates with the Flask backend via API requests.
    
    The backend processes the input and feeds it to the trained GNN model.
    
    Based on the user’s skills and the structure of career-skill relationships, the GNN predicts the most relevant career domains.
    
    The top recommended careers are displayed on the frontend.

🧠 Why GNN?

    Graph Neural Networks are ideal for problems where entities and their relationships can be represented as graphs. In this project:
    
    Nodes represent careers and skills
    
    Edges represent dependencies or relevance between them
    This allows for a more structured and relationship-aware recommendation process.

📸 Screenshots:

![image](https://github.com/user-attachments/assets/10124fe2-5191-494d-a233-caceaf1804be)
![image](https://github.com/user-attachments/assets/af082ff8-7e40-4b8b-bae6-8735b27787f6)



🧪 Future Improvements:

    Add user login and profile management
    
    Introduce feedback mechanism to improve model predictions
    
    Visualize career paths and skill gaps
    
    Include more datasets to widen career coverage
