# I Description Of Project

## 1.1 Project Overview

A real estate property management system aims to develop a system that uses data structures such as AVL trees and queues to manage property listings and customer requests. The system ensures efficient property management and customer service.

## 1.2 The main task

1\. Define the data structure of the property and the customer.

2\. Implement an AVL tree for property management (add, remove, update, and search properties).

3\. Use queues to manage customer requests for efficient processing.

4\. Load the dataset initialization system.

## 1.3 Functional modules

\- Property information management

\- Customer request processing

\- Data structure optimization

## 1.4 target

Create an efficient and reliable property management system that improves the efficiency of property management and customer service.

# II Requirement Analysis of Project

## 2.1. Functional requirements：

Realty management:

Create, update, delete, and search property information.

Use AVL trees to manage property listings, ensuring balanced and efficient retrieval of data.

Customer Management:

Manage customer requests through queues, handle view and purchase requests.

Customer information includes ID, name, contact details, and budget.

## 2.2. Data requirements：

Property data: property ID, address, price, type (apartment, house, commercial land, land), status (available, sold) and owner.

Customer data: customer ID, name, contact details, and budget.

## 2.3. Performance requirements：

Fast property retrieval and updates.

System scalability to handle increased property and customer data.

## 2.4. Interface requirements：

User-friendly property and customer management interface.

The administrator interface is used for system administration and data entry.

## 2.5. Security requirements：

Role-based authentication and authorization mechanisms.

Encryption and secure storage of sensitive data.

## 2.6. System initialization：

Load initial property and customer data from a predefined data set.

## 2.7. Non-functional requirements：

The system should be highly reliable, scalable, and maintainable.

The system should be highly available and able to recover quickly from failures.

The goal of the system is to create an efficient and reliable real estate property management system that improves the efficiency of property management and customer service. By using data structures such as AVL trees and queues, the system ensures balanced and fast access to data for efficient property and customer management.

# III Design of Project

## 3.1. System architecture

Front-end: Build user interfaces using HTML, CSS, and JavaScript.

Backend: Python is used to implement business logic and the Flask framework is used.

Database: Use MySQL to store property and customer information.

## 3.2. Data structure design

Property Class: Contains property ID, address, price, type (apartment, house, commercial land, land), status (available, sold), and owner.

Customer Category: Contains the customer ID, name, contact information, and budget.

AVL Tree: Used to store and manage properties for efficient add, delete, and search operations.

Queue: Used to manage customer requests, processed on a first-come, first-served basis.

## 3.3. Main modules

The specific function module diagram is shown in the figure:

![微信图片_20240704150129](https://github.com/Xiexinqiao/realestate_first-final/assets/173774309/12faf5b0-312b-4cb3-8435-d3bfb9871d0d)


Property Management Module

Add Property: Add a new property to the AVL tree.

Update Property: Update the information of an existing property.

Delete Property: Deletes the property from the AVL tree.

Search for a property: Search based on property ID.

Customer Management Module

Search for a property: Search based on property ID.

Add Customer Request: Add the customer request to the queue.

Process customer requests: Process customer requests in a queue in order.

System initialization

Load initial property and customer data from a predefined data set.

## 3.4. Algorithm design

AVL tree algorithm

（1）. Insert Operation:

Once the new node is inserted, update the node height and check the balance factor.

If it is not balanced, rotate accordingly (left, right, left and right, right left).

（2）. Deletion Actions:

After the node is deleted, update the node height and check the balance factor.

If it is not balanced, rotate accordingly (left, right, left and right, right left).

（3）. Search Actions:

Starting from the root node, a binary search is performed based on the key value of the node.

Queue algorithm

（1）. Enqueue operation:

Add a new customer request to the end of the queue.

（2）. Out-of-Team Operations:

Remove from the head of the queue and return a customer request.

## 3.5 Database tables：

Property table

| The name of the field | data type                                             | Primary/foreign key | Constraints                  |
|-----------------------|-------------------------------------------------------|---------------------|------------------------------|
| property_id           | INT                                                   | PRIMARY KEY         |                              |
| address               | VARCHAR(255)                                          |                     | NOT NULL                     |
| price                 | DECIMAL(10, 2)                                        |                     | NOT NULL                     |
| property_type         | ENUM('APARTMENT', 'HOUSE',\<br\>'COMMERCIAL', 'LAND') |                     | NOT NULL                     |
| status                | ENUM('AVAILABLE', 'SOLD')                             |                     | NOT NULL                     |
| owner_id              | INT                                                   | FOREIGN KEY         | REFERENCES Client(client_id) |

Client table

| The name of the field | data type      | Primary/foreign key | Constraints |
|-----------------------|----------------|---------------------|-------------|
| client_id             | INT            | PRIMARY KEY         |             |
| name                  | VARCHAR(100)   |                     | NOT NULL    |
| contact_info          | VARCHAR(255)   |                     | NOT NULL    |
| budget                | DECIMAL(10, 2) |                     |             |

Client_Request table

| The name of the field | data type                   | Primary/foreign key | Constraints                      |
|-----------------------|-----------------------------|---------------------|----------------------------------|
| request_id            | INT                         | PRIMARY KEY         |                                  |
| client_id             | INT                         | FOREIGN KEY         | REFERENCES Client(client_id)     |
| property_id           | INT                         | FOREIGN KEY         | REFERENCES Property(property_id) |
| request_type          | ENUM('VIEWING', 'PURCHASE') |                     | NOT NULL                         |
| request_date          | DATE                        |                     |                                  |

# IV.Implementation of Project

Implementation progress

Needs Analysis: Completed

System Design: Completed

Data Structure Implementation: Completed

Functional module development: completed

Tested: Completed

# V Running and Debugging of Project

The following figure shows the result：

1\. Class description

<img width="420" alt="图片1" src="https://github.com/Xiexinqiao/realestate_first-final/assets/173774309/59920499-aa47-4dc7-9a4a-ed0c56fc1899">


2\. Print and process customer requests

<img width="326" alt="图片2" src="https://github.com/Xiexinqiao/realestate_first-final/assets/173774309/b7a0fecf-595a-487b-9192-11ed4579653e">

3.Test（we have three part test）

![1fd8b9b62ba86dff749df689bc399f7](https://github.com/Xiexinqiao/realestate_first-final/assets/173774309/08bf0c53-0686-4801-bc52-111d0c37d8e4)![20b847885f15e74d79f5696c444c387](https://github.com/Xiexinqiao/realestate_first-final/assets/173774309/8c4c1c04-af06-4f81-85b3-5f5aff5e62bc)![975aae47c58b541feb6e65612500ad7](https://github.com/Xiexinqiao/realestate_first-final/assets/173774309/0bc3db50-f8fd-4148-84ad-685dd123aa00)![b9f0f3680242c66d0e73f0a24d3535b](https://github.com/Xiexinqiao/realestate_first-final/assets/173774309/faba14f5-426b-49c2-8108-b45a9d917f0e)![0cbb029d72d3bb2886222c4f23c6878](https://github.com/Xiexinqiao/realestate_first-final/assets/173774309/7c652f2f-dede-4b9f-823c-314779df1a23)
![b32757ba6ba27451478b4283e52f9dc](https://github.com/Xiexinqiao/realestate_first-final/assets/173774309/e36b3ff4-8553-4f44-bff2-a7a378ec99f0)







4.UI：

![e513ad9661913a178e63263c8dec447](https://github.com/Xiexinqiao/realestate_first-final/assets/173774309/7f1b92c3-3bfe-4f7b-8db0-07033ee40010)
![image](https://github.com/Xiexinqiao/realestate_first-final/assets/173774309/cb1282f3-b475-44bd-b347-914c01949f89)
![image](https://github.com/Xiexinqiao/realestate_first-final/assets/173774309/b7e7bb93-4821-49bd-bf12-e127e03726e2)

5.Visualization

![image](https://github.com/Xiexinqiao/realestate_first-final/assets/173774309/8f6960bc-fe43-4092-8bcd-6628c3222299)



# VI Summary

## 6.1 Daily Work Schedule

| Date     | Activities                                        | Detailed description                                                                                                                                                                                         |
|----------|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 6.24     | discuss                                           |                                                                                                                                                                                                              |
| 6.25-28  | Back-end development                              | Use Python and Flask to implement business logic and data processing  Feature Development: Implement and test property and customer management functions. Unit Testing: Use unittest for functional testing. |
| 6.29-7.1 | Front-end development                             |                                                                                                                                                                                                              |
| 6.26-7.2 | Database management/data structure implementation | Database: Design and update MySQL databases. Data structure: Implement AVL trees and queues for property and customer management.                                                                            |
| 7.2-7.3  |                                                   | Use unittest for functional testing and test coverage                                                                                                                                                        |
| All time | Code review and debugging                         | Review code with the team to identify and fix bugs.                                                                                                                                                          |
| 7.4      | Documentation updates                             | Update project documentation to document recent changes and new features                                                                                                                                     |

## 6.2 Division of Labor within the Group

| Teammate     | Job                                                                    | Tasks                                                                                                                                                                                               |
|--------------|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Xinqiao Xie  | Project management and coordination Business logic and data processing | Develop project plans, assign tasks, and track progress to ensure projects are completed on time. Implement business logic, handle user requests, and ensure data security and efficient processing |
| Yizhang Wan  | User interface design and implementation                               | Design and develop user interfaces that are user-friendly and fully functional.                                                                                                                     |
| Yuze Du      | Database design and maintenance System testing and quality assurance   | Design and maintain a MySQL database to ensure data integrity and consistency. Perform unit testing, integration testing, and system testing to ensure system stability and reliability.            |
| Tiefeng Zhou | Writing and maintaining project documentation                          | Write and update project documentation, documenting system functionality and operating instructions.                                                                                                |

## 6.3 Tips(Everyone's thoughts)

Xinqiao Xie: Through this project, I learned how to better coordinate the team and manage the project schedule. This not only improved my project management skills, but also made me realize the importance of teamwork. In the face of various challenges and unexpected situations, I have gradually mastered the methods and skills to deal with them flexibly. In the project, I have mastered more skills in data processing and business logic implementation. By solving complex back-end problems, my programming skills have improved significantly. At the same time, I also learned how to optimize the code, improve the performance of the system, and ensure that the data processing is efficient and accurate.

Yizhang Wan: This project has given me a deeper understanding of UX design and greatly improved my front-end skills. During the development process, I learned many new front-end technologies and frameworks, and applied them to practical projects, not only to improve the user interface, but also to improve the interactivity and responsiveness of the system.

Yuze Du: The challenges encountered in the project have made me more proficient in database design and maintenance. Working with large amounts of data and complex queries, I learned how to optimize the database structure to ensure data consistency and integrity. These experiences will be of great help to me in my future work. This project has strengthened my testing capabilities to ensure the stability and reliability of the system. Through a comprehensive testing process and methodology, I was able to quickly identify and resolve issues, improving the quality of the system and user satisfaction.

Tiefeng Zhou: I learned how to write and maintain project documents clearly and accurately. Project documentation not only helps team members understand system functionality and design, but also provides valuable reference material for future maintenance and upgrades.

Overall, through this project, each member gained valuable experience, improved their professional skills, and gained a deeper understanding of teamwork. These gains will have a profound impact on our future work.

## 6.4 Difficulties and Solution of Problems

During the implementation of the project, we encountered several technical and collaborative challenges. First, the complexity of AVL trees and queues creates considerable difficulty when implementing data structures. We solved these problems step by step by digging into the algorithm books and literature, with the help of online code samples and discussion communities. Second, when the system is processing large amounts of data, performance bottlenecks lead to slower response times. We identified and resolved performance issues by optimizing database queries, refactoring code, introducing caching mechanisms, and using load testing and performance analysis tools. In addition, during the front-end and back-end joint debugging, interface data transmission errors frequently occur. To this end, we have clarified the front-end and back-end interface specifications, established detailed API documents, and conducted interface tests through tools such as Postman, which gradually solved the problem of data transmission.

We also faced some challenges when it came to team communication and collaboration. Due to inconsistent task assignments and schedules, there was poor communication between team members, which affected the progress of the project. To this end, we hold regular team meetings to ensure that everyone is kept up to date on the progress of the project and their respective tasks. In addition, we use project management tools such as Trello and JIRA for task tracking and management, which improves collaboration efficiency. By establishing a good communication channel and solving problems in a timely manner, the smooth progress of the project was ensured. These measures not only improved the team's technical capabilities, but also strengthened the team spirit, laying a solid foundation for the success of the project. By solving these problems, we have accumulated valuable experience and laid a good foundation for future projects.
