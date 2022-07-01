"""Homework 5-6"""
"""TASK 1 (Agile Techniques)"""
###Question 1###
"""
SCRUM CEREMONIES
· Product backlog refinement
   - Product backlog refinement is the act of adding detail, estimates, and order to items in the product backlog. 
   - This is an ongoing process in which the product owner and the development team come together to discuss the details of the items in the product backlog. 
   - During product backlog refinement, items are reviewed and revised. 
   - The product backlog is essentially a list of improvements to be made to one's product.

· Sprint planning 
   - Sprint planning is an event in scrum where the team determines the items to be in the product backlog which they will work on during the upcoming sprint.  
   - Plans for how the items in the product backlog will be completed are also discussed.
   
· Daily scrum
   - A daily scrum meeting is a 15-minute event for the developers of the scrum team.
   - The meeting typically takes place at the same time and place every working day of the sprint.
   - The purpose of the daily scrum meeting is to ensure progress towards the sprint goal.
   - In the daily scrum meeting the development team would produce an actionable plan for the next working day. 
   
· Sprint review
   - The sprint review is a scrum event that takes place at the end of the sprint (but before the retrospective). 
   - The purpose of the sprint review is for the scrum team to show what they have accomplished during the sprint to key stakeholders.
   - The sprint review is also used to determine whether or not any alterations are to be made to the product in the future. 
   
· Sprint retrospective
   - The sprint retrospective is a meeting held at the end of a sprint -  it is usually the last thing done in a sprint.
      - Many teams will hold a sprint retrospective it immediately after the sprint review.
   - The purpose of the sprint retrospective is to plan ways to increase quality and effectiveness.
      - It is an opportunity for the scrum team to reflect and plan improvements that should be made during the next sprint.
   - The scrum team would normally discuss what went well during the sprint, the problems that were encountered, and how those problems were resolved (if they were).

SCRUM ROLES
· Scrum Master
   - The scrum master is an individual that ensures the scrum framework is followed. 
      - The scrum master helps everyone understand scrum theory and practice, both within the scrum team and the organisation.
  - The scrum master is held accountable for the scrum team’s effectiveness. They ensure the team's effectiveness by enabling the scrum team to improve its practices, within the scrum framework.

· Product Owner
   - The product owner is accountable for maximising the value of the product that results from the work of the scrum team.
   - The product owner is also responsible for effective product backlog management, including:
      - developing and communicating the product goal
      - creating and clearly communicating product backlog items
      - ordering product backlog items
      - ensuring that the product backlog is transparent, visible and understood
      
· Development Team
   - The developers are the individuals in the scrum team that create any aspect of a usable increment each sprint.
   - Developers are accountable for:
      - creating a plan for the sprint
      - instilling quality
      - daily adapting their plan to ensure progress towards the sprint goal
      - holding one another accountable as professionals
"""

###Question 2###
"""
User stories:
- As a yoga enthusiast, I want to be able to book yoga classes online in advance, so that I accidentally turn up to a full class again.
- As the owner of the yoga studio, I want to be able to access all data related to bookings, appointments, schedules etc, so that I know how my studio is performing.
- As someone that is new to yoga, I want to be able to see all of the yoga studio's essential information clearly on the website, so that I can make in informed decision regarding whether or not I'd like to attend a yoga session.

-> The first user story above essentially requires the ability for a user to be able to book classes online. 
-> The second user story above requires the yoga studio owner to be able to access either some sort of a summary of the data stored in the SQL database or all of the data stored in the SQL database. 
-> The third user story a simple requires a simple view of the data stored in the SQL database without overwhelming the individual.

- As one can start writing the code for the backend or the frontend of a software in any order, all tasks above can be completed simultaneously, by three separate individuals in the development team.

- To build a simple prototype of new yoga booking system, I would follow the agile methodology because it helps analyse and improve products whilst they’re going through different phases of development. 
   - This methodology enables one to produce more valuable products to customers by following an incremental approach.
   
- Each sprint would last two weeks. A sprint is a short period of time when a scrum team works to complete a set amount of work.
- Each sprint would start with a sprint planning meeting - this would be conducted before every sprint and would be attended by the scrum master, the development team and the product owner. 
   - These individuals would all select the high priority items from the product backlog in such a way that the development team can deliver them in one single sprint. The list of selected items is known as the sprint backlog. The development team works on the sprint backlog throughout the sprint.
- During the sprint, every day, a daily scrum meeting is held. In this meeting each participant would answer 3 questions: what they did yesterday, what they'll do today, and the issues facing by the developers.
- The outcome of the sprint would be a potentially shippable product. Whether or not the product is ready to be shipped depends on whether the product owner wants to ship the product or add more features to the product.
- Finally, after the sprint has taken place, the sprint review and sprint retrospective occur.
   - In the sprint review, the scrum team would showcase what it has accomplished during the sprint, this may include a demo of new features added to the product.
   - In the sprint retrospective, the team contemplate on what went well, what went badly and what could be improved. The objective of a sprint retrospective is to improve the sprints held in the future.
"""

"""TASK 2 (Process Flow Design)"""
###Question 1###

"""
Key requirements:
- A database to store a user's name, surname, email address, available films, the times that each film is showing, the various ticket prices, etc.
- A user interface that makes booking cinema tickets fast and simple (should be faster and less cumbersome than booking tickets in person).
- The framework to build the user interface and connect to the database.
- The ability for the booking system to accept payment from the user and valid that payment is possible (the payment validation component could be external).

Main considerations:
- Will the booking system be used for one cinema or multiple cinemas operating under a particular brand or region?
- The options available for storing the data e.g Informix, MySQL, MongoDB, etc.
- How the booking system would deal with multiple people attempting to book tickets simultaneously (as would be the case for the release of a popular film).
- How would the available seats be displayed to a user - would all seats be displayed, each with respective their availability status, or would only the available seats be displayed?
- What will the UI look like?
- Do we need to support both web apps and mobile apps.

Common or biggest problems:
- Booking tickets and not receiving confirmation of the booking
- Users accidentally inputting the wrong data e.g email address.
- Users not wanting to use the website because they dont like the user interface.
- The website taking a long time to load, leading to the user becoming frustrated.
- How many options should be displayed to the user when selecting films (a lot would be hard to display)

Components or tools I would use:
- For the cinema booking system, I would use a strategy design pattern as it requires choosing a specific implementation of an algorithm or task at run time – out of multiple other implementations for same task.
- For the website design, I would use react js (is a JavaScript library for building user interfaces).
   - I would use React because it is all about splitting an application into small building blocks, where every building block, every component, has a clear task and therefore one's code stays maintainable and manageable.
- I would use the Django python web framework.
   - I would use Django as it is well known to be a high-performing web framework out of the box and it is used by extremely high-traffic apps. This framework would help deal with the issue of alot of users attempting to book cinema tickets.
   
- Please refer to the picture for the process flow design.   
"""