CS 3364 Algorithms: Project 2  
Find the order of taking courses by applying topological ordering algorithm  
In real life, we have many things to do. We always need to think of the sequence to get things done: which we need to do first, which we can do next. This is a topological ordering problem. For example, in order to finish our program, we also need to think about the sequence of taking the courses, since some courses have their prerequisites. The following are the courses required by an undergraduate program in our computer science department. Could you find the solution for you and your fellows?  


**Computer Science Major (prerequisites in the bracket)**  
CS 1411 - Programming Principles I (N/A)  
MATH 1451 - Calculus I with Applications (N/A)   
ENGL 1301 - Essentials of College Rhetoric (N/A)  
CS 1412 - Programming Principles II (CS 1411)  
MATH 1452 - Calculus II with Applications (MATH 1451)  
PHYS 1408 - Principles of Physics I (MATH 1451)  
ENGL 1302 - Advanced College Rhetoric (ENGL 1301)  
CS 2413 - Data Structures (CS 1412)  
CS 1382 - Discrete Computational Structures (CS 1411)  
ECE 2372 - Modern Digital System Design (MATH 1451)  
MATH 2450 - Calculus III with Applications (MATH 1452)  
PHYS 2401 - Principles of Physics II (PHYS 1408)  
CS 2350 - Computer Organization and Assembly Language Programming (CS 1412 and ECE 2372)  
CS 2365 - Object-Oriented Programming (CS 2413)  
ENGR 2392 - Engineering Ethics and Its Impact on Society (N/A)  
POLS 1301 - American Government (N/A)  
MATH 2360 - Linear Algebra (MATH 1452)  
ENGL 2311 - Introduction to Technical Writing (ENGL 1301 and ENGL 1302)  
CS 3361 - Concepts of Programming Languages (CS 2413)  
CS 3364 - Design and Analysis of Algorithms (CS 2413, CS 1382 and MATH 2360)  
MATH 3342 - Mathematical Statistics for Engineers and Scientists (MATH 2450)  
POLS 2306 - Texas Politics and Topics (N/A)  
CS 3365 - Software Engineering I (CS 2365, CS2413 and MATH 3342)  
CS 3375 - Computer Architecture (CS 2350)  
CS 3383 - Theory of Automata (CS 1382)  
CS 4365 - Software Engineering II (CS 3365)  
CS 4352 - Operating Systems (CS 3364 and CS 3375)  
CS 4354 - Concepts of Database Systems (CS 3364)  
CS 4366 - Senior Capstone Project (CS 4365)  


**Acquirement:**  
Graphs are broadly used in modeling real-world applications. In this project, you are asked to design, implement, and test an abstract data type (ADT) graph in its prototype. It can include frequently used algorithms, such as DFS, BFS, and so on. In this project, you are required to implement the topological ordering algorithm only, which is based on DFS. Other algorithms can be extended in the future.   


**Project Objective:** In completing this project, you will further develop your ability to:
1. Simplify and solve real-world problems;  
2. Apply the existing algorithms into real-world applications;   
3. Design reasonable software solutions;  
4. Implement and verify potential solutions;  
5. Collaborate with team members.  


**What to submit:**
A report that documents the design and the process of the project;


**How it will be graded – Rubric**  

|  |  |  |  |  |  
| - | - | - | - | - |  
|   |  Excellent (100%\~90%) |  Good (89%\~80%) |  Need Improvement (79%\~60%) |  Does Not Meet Requirements (59%\~0%) |  
| Designing correctness (40 pts) |  The algorithms are designed correctly, with certain flexibilities, meeting all of the specifications. |  The algorithms are designed correctly, for the specific real-world problem formats, meeting most of specifications. |  The algorithms are designed partially correct, meeting part of specifications. |  The design is not correct |  
| Implementation Correctness (40 pts) |  The algorithm/s is implemented completely correctly, and produces correct solutions. It meets all the specifications. |  The algorithm/s is implemented completely correctly, and produces correct solutions. It meets most specifications. |  The algorithm/s is implemented completely correctly, and produces correct solutions. It meets parts of the specifications. |  This program does not compile. Or all the implementations are incorrect, not produce correct solutions. |  
| Readability (10 pts) |  The code is exceptionally well organized and very easy to follow. |  The code is fairly easy to read. |  The code is readable only by someone who knows what it is supposed to be doing. |  The code is poorly organized and very difficult to read. |  
| Report Structure (10 pts) |  The documentation consists of four important components: interpretation of the given problem, methodology of the solution, experimental results, and conclusions. Each component is fully expanded. Besides, it also discussed future work and the team considerations |  The documentation consists of four important components: interpretation of the given problem, methodology of the solution, experimental results, and conclusions. Each component is fully expanded. |  The documentation consists of four important components: interpretation of the given problem, methodology of the solution, experimental results, and conclusions. But each component is partially expanded. |  The documentation does not consist of four important components: interpretation of the given problem, methodology of the solution, experimental results, and conclusions. |
