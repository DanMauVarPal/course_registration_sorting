"""CS major courses, copied from the assignment: course -> its prerequisites."""

from course_registration_sorting.graph import Graph

PREREQS: dict[str, list[str]] = {
    "CS 1411": [],
    "MATH 1451": [],
    "ENGL 1301": [],
    "CS 1412": ["CS 1411"],
    "MATH 1452": ["MATH 1451"],
    "PHYS 1408": ["MATH 1451"],
    "ENGL 1302": ["ENGL 1301"],
    "CS 2413": ["CS 1412"],
    "CS 1382": ["CS 1411"],
    "ECE 2372": ["MATH 1451"],
    "MATH 2450": ["MATH 1452"],
    "PHYS 2401": ["PHYS 1408"],
    "CS 2350": ["CS 1412", "ECE 2372"],
    "CS 2365": ["CS 2413"],
    "ENGR 2392": [],
    "POLS 1301": [],
    "MATH 2360": ["MATH 1452"],
    "ENGL 2311": ["ENGL 1301", "ENGL 1302"],
    "CS 3361": ["CS 2413"],
    "CS 3364": ["CS 2413", "CS 1382", "MATH 2360"],
    "MATH 3342": ["MATH 2450"],
    "POLS 2306": [],
    "CS 3365": ["CS 2365", "CS 2413", "MATH 3342"],
    "CS 3375": ["CS 2350"],
    "CS 3383": ["CS 1382"],
    "CS 4365": ["CS 3365"],
    "CS 4352": ["CS 3364", "CS 3375"],
    "CS 4354": ["CS 3364"],
    "CS 4366": ["CS 4365"],
}

TITLES: dict[str, str] = {
    "CS 1411": "Programming Principles I",
    "MATH 1451": "Calculus I with Applications",
    "ENGL 1301": "Essentials of College Rhetoric",
    "CS 1412": "Programming Principles II",
    "MATH 1452": "Calculus II with Applications",
    "PHYS 1408": "Principles of Physics I",
    "ENGL 1302": "Advanced College Rhetoric",
    "CS 2413": "Data Structures",
    "CS 1382": "Discrete Computational Structures",
    "ECE 2372": "Modern Digital System Design",
    "MATH 2450": "Calculus III with Applications",
    "PHYS 2401": "Principles of Physics II",
    "CS 2350": "Computer Organization and Assembly Language Programming",
    "CS 2365": "Object-Oriented Programming",
    "ENGR 2392": "Engineering Ethics and Its Impact on Society",
    "POLS 1301": "American Government",
    "MATH 2360": "Linear Algebra",
    "ENGL 2311": "Introduction to Technical Writing",
    "CS 3361": "Concepts of Programming Languages",
    "CS 3364": "Design and Analysis of Algorithms",
    "MATH 3342": "Mathematical Statistics for Engineers and Scientists",
    "POLS 2306": "Texas Politics and Topics",
    "CS 3365": "Software Engineering I",
    "CS 3375": "Computer Architecture",
    "CS 3383": "Theory of Automata",
    "CS 4365": "Software Engineering II",
    "CS 4352": "Operating Systems",
    "CS 4354": "Concepts of Database Systems",
    "CS 4366": "Senior Capstone Project",
}


def course_graph() -> Graph:
    graph = Graph({course: [] for course in PREREQS})
    for course, prereqs in PREREQS.items():
        for prereq in prereqs:
            graph.add_edge(prereq, course)
    return graph
