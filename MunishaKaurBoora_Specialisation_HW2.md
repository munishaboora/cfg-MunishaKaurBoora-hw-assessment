# HOMEWORK WEEK 2 - Revision Game App

### Group members:
 - Munisha Boora
 - Rebecca Brunning
 - Ellie Mayne
 - Shida Koka
 - Xian-Ting Lee

### 1. What are you building?
- Our project involves creating a revision application which will consist of multiple quizzes. These quizzes would all be split by the categories to which they relate. For instance, in our application, we will include a quiz on classes and another on decorators to start with, both in the python category. We endeavour to add more quizzes and categories to our application over time.
- When our application is run, an individual would be presented with all possible quiz categories. Upon selecting a category, an individual would then be presented with all of the quizzes relating to that particular category. As an individual selects a quiz and begins answering the quiz questions, their score would increase by 1 for each question answered correctly and by 0 for each question answered incorrectly. After completing a single quiz, the overall score for the quiz in question would be displayed on the screen. 
- To create our application, we will write the logic of the application in Python, create a database using MySQL, and use Flask with python to build the API. 
   - As an additional goal, we aim to create a frontend using HTML, JavaScript, and CSS.



### 2. What does it do or what kind of problem does it solve?
- The revision application will allow a user to test their knowledge of the various topics taught throughout the CFG nanodegree. The application does this by presenting the user with a selection of categories to choose from and quizzes to complete within the catgories. 
   - A particular quiz would contain questions relating to a topic taught as part of the CFG curriculum. For instance, the classes quiz would test an individual on the material covered in the PowerPoint presentations of the classes lessons.
- This application solves the problem faced by a user who may be struggling to learn complex topics in a memorable and enjoyable manner. 
- The application we are building aims to help improve the knowledge of CFG students whilst they’re taking the course and also assist them in their revision for their assessments. We hope to reach this objective through the creation of an application consisting of various revision-based quizzes. 
- Ultimately, we aim to increase retention for CFG students so they can learn the material covered as part of the CFG nanodegree more easily.


### 3. What are the key features of your system?
- User interface
   - Displays quiz categories
   - Displays quiz topics
   - Displays quiz questions
   - Displays user's score
   - *Stretch goal:* Ability to enter user login details
   - *Stretch goal:* Display a leaderboard containing the names of high scoring users 
   - *Stretch goal:* Ability to add quiz questions
   - *Stretch goal:* Sound playing in background
   - *Stretch goal:* Countdown timer for each quiz

- Database
   - 3 tables
      - quiz_categories
      - all_quiz_questions
      - quiz_question_answers
   - *Stretch goal:*
      - quiz_participant_scores_history
      - quiz_participants



### 4. Provide a sample architecture diagram of your system.
![An architecture diagram of the system!](https://drive.google.com/uc?export=view&id=1eAvIzpoXHF_ahXs64vyJ8TY-_p2IQtFs)
- The diagram above shows the design of the revision quiz application. 
- CFG students will access the quiz application via their individual web browsers. The web browsers interact with the API endpoints using flask in the middleware. 
   - The flask endpoints call on either the quiz game, the leaderboard, or login page, all of which will be writen in python. 
- To access the database, a data access layer handles all calls to the database.

### 5. Describe the team approach to the project work: how are you planning to distribute the workload, how are you managing your code, how are you planning to test your system.
- The team are working in an agile manner i.e. using daily stand ups, sprint reviews, sprint retrospective, etc.
- We are planning to work using pair programming so that each team member has continuous support throughout the project. This will also ensure no one is left behind and we are aware of one anothers progress and any blockers.
- We will use several collaboration tools, such as miro, trello, etc. These collaboration tools will help to share resources wiht other team mmebers and ensure everyone is up to date on the group's progress.
- We will be conducting regular code reviews to assess each other's code. We will also be working closely to meet the requirements set out at the beginning of the project on both the miro board and the kanban board. We will try to use best practices throughout, referring to previous lessons and codebases for inspiration.
- We will also be using githib branches and pull requests to ensure no one overrides any important code and so that the code on a particular branch is only merge into the main branch with approval of the whole team. This is to further ensure the coherence of the code base.

- Tests to be conducted:
   - A new username is only added when it does not exist in the database.
   - The highscore only updates when the new score exceeds the present highscore.
   - When a user select a correct answer, the score increases by 1.

