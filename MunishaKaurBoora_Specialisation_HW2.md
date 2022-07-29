# HOMEWORK WEEK 2 - Revision Game App

### Group members:
 - Munisha Boora
 - Rebecca Brunning
 - Ellie Mayne
 - Shida Koka
 - Xian-Ting Lee

### 1. What are you building?
- Our project involves creating a revision application which will consist of multiple quizzes. These quizzes would all be split by the categories to which they relate. For instance, in our application, we will include a quiz on classes and another on decorators to start with. We endeavour to add more quiz categories to our application over time.
- When our application is run, an individual would be presented with all possible quiz categories. Upon selecting a category, an individual would then be presented with all of the questions relating to that particular category. As an individual answers a question, their score would increase by 1 for each question answered correctly and by 0 for each question answered incorrectly. After completing a single quiz, the overall score for the quiz in question would be displayed on the screen. 
- To create our application, we will write the logic of the application in python, create a Database using MySQL, and use Flask with python to build the API. 
   - As an additional goal, we aim to create a frontend using HTML, JavaScript and CSS.



### 2. What does it do or what kind of problem does it solve?
- The revision application will allow a user to test their knowledge of the various topics taught throughout the CFG nanodegree. The application does this by presenting the user with a selection of quizzes to choose from and complete. 
   - A particular quiz would contain questions relating to a topic taught as part of the CFG curriculum. For instance the classes category would test an individual on the material covered in the PowerPoint presentations of the classes lessons.
- This application solves the problem faced by a user who may be struggling to learn complex topics in a memorable and fun manner. 
- The app we are building aims to help improve the knowledge of CFG students whilst they’re taking the course and also assist them in their revision for their assessments. We hope to reach this objective through the creation of an application consisting of various revision-based quizzes. 
- Ultimately, we aim to increase retention for CFG students so they can learn the material covered as part of the CFG nanodegree more easily.


### 3. What are the key features of your system?
- User interface
   - Displays quiz questions
   - Displays score
   - *Stretch goal:* Enter user login details
   - *Stretch goal:* Display a leaderboard 
   - *Stretch goal:* Ability to add user questions
   - *Stretch goal:* Sound playing in background
   - *Stretch goal:* Countdown timer

- Database
   - 3 tables
      - quiz_categories
      - all_quiz_questions
      - quiz_question_answers

   - *STRETCH*
      - quiz_participant_scores_history
      - quiz_participants



### 4. Provide a sample architecture diagram of your system.
![An architecture diagram of the system!](https://drive.google.com/uc?export=view&id=1eAvIzpoXHF_ahXs64vyJ8TY-_p2IQtFs)
- The diagram above shows the design of the revision quiz application. 
- CFG students will access the quiz application via their individual web browsers. The web browsers interact with the API endpoints using flask in the middleware. 
   - The flask endpoints call on eihter the quiz game, the leaderboard, or login page, all of which will be writen in python. 
- To access the database, a data access layer handles all calls to the database.

### 5. Describe the team approach to the project work: how are you planning to distribute the workload, how are you managing your code, how are you planning to test your system.
- The team are working in an agile manner i.e. using daily stand ups and retros
- We are planning to work using pair programming so that we have continuous support throughout the project. This will also ensure no one is left behind and we are aware of one anothers progress and any blockers.
- We use several collaboration tools, such as miro, trello, etc, to share resources and make sure everyone is up to date.
- We will be using code reviews to assess each other's code. We will also be working closely against the requirements given to us at the beginning of the project. We will try to use best practices throughout, referring to previous lessons and codebases for inspiration.
- We will also be using branches and pull requests to ensure no one overrides any important code and nothing is pushed without the approval of the team. This is to further ensure the coherence of the code base.
- Tests:
   - only adds a new user name when not existing in db.
   - only updates the high score when higher than the previous score.
   - When user selects correct answer score is increase +1

