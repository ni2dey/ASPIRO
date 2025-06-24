from flask import Flask, render_template, redirect,session,request, jsonify
from flask_cors import CORS
import torch  
from torch_geometric.data import Data
from model.gnn_model import GNN
import numpy as np
import pickle
from func import recommend_domains

app = Flask(__name__)
CORS(app) 

# Load model
model = GNN(64, 64, 32)
model.load_state_dict(torch.load('model/gnn_model.pth'))
model.eval()

@app.route('/')
def home():
  return render_template('main.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.get_json()  
        skills = data['skills']    
        print("Input Skills:", skills)

     
        with open('multiple_data.pkl', 'rb') as f:
            multiple_data = pickle.load(f)

        # ✅ Unpack data correctly
        data_graph = multiple_data['data']
        node_mapping = multiple_data['node']
        reverse_mapping = multiple_data['reverse']
        combined_df = multiple_data['df']

        # ✅ Normalize skills
        user_input_skills = [skill.lower() for skill in skills]

        # ✅ Run recommendation logic
        recommendations = recommend_domains(
            user_input_skills, model, data_graph, node_mapping, reverse_mapping, combined_df
        )
        print("Recommended Job Domains:", recommendations)

        return jsonify(recommendations)

    except Exception as e:
        print("Error occurred:", e)
        return jsonify({'error': str(e)})

# Dictionary of job domains to Coursera course links
course_links = {
    "software-developer": "https://www.coursera.org/specializations/java-programming",
    "web-developer": "https://www.coursera.org/specializations/web-design",
    "mobile-app-developer": "https://www.coursera.org/specializations/android-app-development",
    "data-analyst": "https://www.coursera.org/specializations/data-analytics",
    "data-scientist": "https://www.coursera.org/specializations/data-science-python",
    "machine-learning-engineer": "https://www.coursera.org/learn/machine-learning",
    "ai-engineer": "https://www.coursera.org/specializations/ai-for-everyone",
    "cloud-engineer": "https://www.coursera.org/specializations/cloud-computing",
    "cybersecurity-analyst": "https://www.coursera.org/professional-certificates/ibm-cybersecurity-analyst",
    "blockchain-developer": "https://www.coursera.org/learn/blockchain-basics",
    "full-stack-developer": "https://www.coursera.org/specializations/full-stack-react",
    "game-developer": "https://www.coursera.org/specializations/game-development",
    "network-engineer": "https://www.coursera.org/specializations/networking-basics",
    "devops-engineer": "https://www.coursera.org/specializations/devops",
    "ui-ux-designer": "https://www.coursera.org/specializations/ui-ux-design",
    "database-administrator": "https://www.coursera.org/learn/database-management",
    "product-manager": "https://www.coursera.org/specializations/product-management",
    "systems-administrator": "https://www.coursera.org/learn/system-administration-it",
    "embedded-systems-engineer": "https://www.coursera.org/learn/embedded-systems",
    "iot-engineer": "https://www.coursera.org/specializations/iot",
    "electrical-design-engineer": "https://www.coursera.org/learn/electrical-engineering",
    "power-systems-engineer": "https://www.coursera.org/learn/electric-power-systems",
    "vlsi-engineer": "https://www.coursera.org/learn/vlsi-cad",
    "robotics-engineer": "https://www.coursera.org/specializations/modern-robotics",
    "control-systems-engineer": "https://www.coursera.org/learn/control-of-mobile-robots",
    "structural-engineer": "https://www.coursera.org/learn/structural-engineering",
    "geotechnical-engineer": "https://www.coursera.org/learn/geotechnical-engineering",
    "construction-manager": "https://www.coursera.org/learn/construction-project-management",
    "transportation-engineer": "https://www.coursera.org/learn/transportation-engineering",
    "environmental-engineer": "https://www.coursera.org/learn/environmental-management"
}

@app.route('/api/course/<job_domain>')
def get_course(job_domain):
    job_domain = job_domain.lower()
    if job_domain in course_links:
        return redirect(course_links[job_domain])
    return "Course not found", 404

if __name__ == '__main__':
    app.run(debug=True)
