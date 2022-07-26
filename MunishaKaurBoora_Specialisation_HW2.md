# HOMEWORK WEEK 2 - Revision Game App

### Group members:
 - Munisha Boora
 - Rebecca Brunning
 - Ellie Mayne
 - Shida Koka
 - Xian-Ting Lee

### 1. What are you building?
- Our project involves creating a revision app consisting of multiple quizzes. For instance, in our app, we will include a quiz on classes and another on decorators.
- When our application is run, an individual would be presented with all possible categories. Upon selecting a category, an individual would be presented with all of the questions within that particular category. As an individual answers a question, their score would increase by 1 for each question answered correctly. After completing a quiz, the overall score for the quiz would be displayed. 
- To create the application, we will create an API, use MySQL, and write the logic in python. As an additional goal, we aim to create a frontend using HTML, JavaScript and CSS.


### 2. What does it do or what kind of problem does it solve?
- The app we are building aims to help improve the knowledge of CFG students. 
- The app's aim is to create a revision-based quiz. 
- The app will allow the user to test their knowledge on CFG topics in the form of a quiz. The problem this solves is a user may struggle to learn complex topics in a memorable and fun way, the app solves this. Ultimately we aim to increase retention for CFG students, so they can learn software engineering topics easier.


### 3. What are the key features of your system?
- User interface
 1. Displays quiz questions
 2. Displays score
 3. *STRETCH* Enter username
 4. *STRETCH* Display scoreboard 
 5. *STRETCH* Ability to add user questions
- Database
 1. 3 tables
     1. quiz_categories
     2. all_quiz_questions
     3. quiz_question_answers
 2. *STRETCH*
     1. users


### 4. Provide a sample architecture diagram of your system
![An architecture diagram of the system!](https://drive.google.com/uc?export=view&id=1eAvIzpoXHF_ahXs64vyJ8TY-_p2IQtFs)

### 5. Describe the team approach to the project work: how are you planning to distribute the workload, how are you managing your code, how are you planning to test your system.
- The team are working in an agile manner i.e. using daily stand ups and retros
- We are planning to work using pair programming so that we have continuous support throughout the project. This will also ensure no one is left behind and we are aware of one anothers progress and any blockers.
- We will be using code reviews to assess each other's code. We will also be working closely against the requirements given to us at the beginning of the project. We will try to use best practices throughout, referring to previous lessons and codebases for inspiration.
- We will also be using branches and pull requests to ensure no one overrides any important code and nothing is pushed without the approval of the team. This is to further ensure the coherence of the code base.
- Tests:
 1. only adds a new user name when not existing in db.
 2. only updates the high score when higher than the previous score.
 3. When user selects correct answer score is increase +1
