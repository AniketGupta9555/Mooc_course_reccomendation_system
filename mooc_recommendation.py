import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def content_based_recommendation(preferred_topics, courses_df):
    # Using TF-IDF on course descriptions
    tfidf = TfidfVectorizer(stop_words='english')
    courses_df['Course Description'] = courses_df['Course Description'].fillna('')
    tfidf_matrix = tfidf.fit_transform(courses_df['Course Description'])
    
    # Compute similarity between preferred topics and course descriptions
    query_tfidf = tfidf.transform([preferred_topics])
    cosine_similarities = linear_kernel(query_tfidf, tfidf_matrix).flatten()
    
    # Get top 10 course recommendations
    top_indices = cosine_similarities.argsort()[-10:][::-1]
    recommendations = courses_df.iloc[top_indices][['Course Name', 'University / Industry Partner Name', 'Difficulty Level', 'Course Rating', 'Course URL']]
    
    return recommendations.to_dict('records')

def collaborative_filtering(user_id, users_df, courses_df):
    # Placeholder for collaborative filtering function
    # Would require user-course interaction data for collaborative filtering
    return []

def update_user_profile(user_data, users_df):
    # Convert the user data into a DataFrame and append it to the existing users_df
    user_df = pd.DataFrame([user_data])
    users_df = pd.concat([users_df, user_df], ignore_index=True)
    return users_df
