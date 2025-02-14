# IGA HIFADHI - Machine Learning Counseling Recommender System

**IGA HIFADHI** is a machine learning-powered counseling recommender system designed to assist secondary school students in Kigali in making informed academic decisions. By analyzing student data, interests, and labor market trends, the system offers personalized subject and career recommendations.

## Project Overview

IGA HIFADHI aims to bridge the gap between students' academic choices and the dynamic demands of the labor market. By leveraging data-driven insights, the system ensures that students are guided towards subjects and career paths that align with their strengths and market opportunities.

## Features

- **User Authentication:** Secure login and registration for students and teachers.
- **Personalized Recommendations:** AI-driven suggestions for subjects and career paths tailored to individual student profiles.
- **Student Dashboard:** A centralized platform for students to view recommendations, track progress, and access resources.
- **Teacher Dashboard:** Tools for educators to monitor student progress, provide feedback, and manage counseling sessions.
- **Data Analytics:** Insights into academic performance and trends to support data-driven decision-making.

## Tech Stack

- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **Backend:** Python (Flask)
- **Database:** SQLite with SQLAlchemy ORM
- **Machine Learning:** Scikit-Learn, Pandas, NumPy
- **Authentication:** Flask-Login, Flask-Bcrypt

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- Virtual environment tool (e.g., `venv`)

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/IGA_mission-capstone.git
   cd IGA_mission-capstone
   ```

2. **Set Up Virtual Environment:**
   ```bash
   python -m venv venv
   # Activate the virtual environment
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations and Initialize the Database:**
   ```bash
   flask db upgrade
   ```

5. **Run the Application:**
   ```bash
   flask run
   ```
   Access the application at `http://127.0.0.1:5000`.

## Usage

### For Students

- **Sign Up/Login:** Create an account or log in to access personalized features.
- **View Recommendations:** Access subject and career suggestions tailored to your profile.
- **Update Profile:** Modify personal information and academic interests as needed.

### For Teachers

- **Monitor Students:** View student profiles and their recommended paths.
- **Provide Feedback:** Offer insights and guidance to students based on their performance and interests.
- **Manage Sessions:** Schedule and document counseling sessions.

## Machine Learning Model

The system employs a Random Forest Classifier to predict suitable subject tracks for students. Key features considered include:

- Academic performance metrics
- Attendance records
- Subject interests
- Career aspirations

The model has demonstrated an accuracy of approximately 85% during evaluation.


## Contributors

- ROLINE UMUNYANA

## License

