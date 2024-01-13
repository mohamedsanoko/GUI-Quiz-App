# Quizzler - A Python Quiz Game
Quizzler is a simple Python quiz game using the Tkinter library for the graphical user interface. The game fetches trivia questions from the Open Trivia Database API, and users can answer True/False questions to test their knowledge.

# Getting Started
  1. Clone the Repository.
  2. Make sure you have Python installed on your system.
  3. Install the required libraries using the following commands; pip install requests.
  4. Run the Game.

# Project Structure
The project is organized into three main files: 
  1. 'main.py': The main script to run the Quizzler game.
  2. 'quiz_brain.py': Contains the 'QuizBrain' class responsible for managing quiz-related logic.
  3. 'ui.py': Defines the 'QuizInteface' class, which sets up the graphical user interface using     tkinter.

# How It Works
  1. The game fetches 10 True/False questions from the Open Trivia Database API.
  2. The questions are presented to the user in a graphical user interface created using Tkinter.
  3. Users can answer each question by clicking the "True" or "False" buttons.
  4. After answering all questions, the final score is displayed.

# Customization
You can customize the quiz questions by updating ther 'question_data' list in the 'main.py' file. Alternatively, you cna use a different trivia API fetch questions.
You can customize the Tkinter UI by modifying the 'QuizInterface' class in the 'ui.py' file.

# Notes
The game uses the Open Trivia Database API to fetch trivia questions. The API parameters can be adjusted in the main.py file.
The project includes example code for fetching questions from the Open Trivia Database API, even though the actual game uses a predefined set of questions in the commented-out question_data.
