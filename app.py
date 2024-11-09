from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from mooc_recommendation import content_based_recommendation, collaborative_filtering, update_user_profile

app = Flask(__name__)

# Load the datasets
courses_df = pd.read_excel(r'C:\Users\anike\minor_mooc_course_Reccomendation\datasets\MOOC.xlsx', engine='openpyxl')
user_data_df = pd.read_excel(r'C:\Users\anike\minor_mooc_course_Reccomendation\datasets\mooc_user_data.xlsx', engine='openpyxl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Retrieve form data
        user_data = {
            'Name': request.form['name'],
            'Email': request.form['email'],
            'Age': int(request.form['age']),
            'Country': request.form['country'],
            'Learning Goals': request.form['learning_goals'],
            'Preferred Topics': request.form['preferred_topics'],
            'Skill Level': request.form['skill_level'],
            'Preferred Difficulty Level': request.form['preferred_difficulty'],
            'Past Experience': request.form['experience']
        }
        # Update user profile dataset
        global users_df
        users_df = update_user_profile(user_data, users_df)
        users_df.to_excel('dataset/user_profiles.xlsx', index=False)
        
        return redirect(url_for('home'))
    
    return render_template('register.html')

@app.route('/recommendation', methods=['GET', 'POST'])
def recommendation():
    recommendations = []
    if request.method == 'POST':
        preferred_topics = request.form['preferred_topics']
        
        # Generate recommendations using content-based and collaborative filtering
        recommendations = content_based_recommendation(preferred_topics, courses_df)
        
    return render_template('recommendation.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
