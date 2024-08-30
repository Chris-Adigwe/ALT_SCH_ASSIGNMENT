class Person:
    """
    Represents a person with a first name, last name, and an ID.

    Attributes:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person.
        id (str): The unique identifier for the person.
    """

    def __init__(self, first_name, last_name, id):
        """
        Initializes a new Person instance.

        Args:
            first_name (str): The first name of the person.
            last_name (str): The last name of the person.
            id (str): The unique identifier for the person.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __str__(self):
        """
        Returns a string representation of the Person instance.

        Returns:
            str: A string describing the person.
        """
        return f'This is {self.first_name} {self.last_name} with ID NUMBER {self.id}'


class Students(Person):
    """
    Represents a student who is a person with an additional major field of study.

    Attributes:
        major (str): The student's major.
        enrolled_courses (list): A list of courses the student is enrolled in.
    """

    def __init__(self, first_name, last_name, id, major):
        """
        Initializes a new Students instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            id (str): The unique identifier for the student.
            major (str): The student's major field of study.
        """
        super().__init__(first_name, last_name, id)
        self.major = major
        self.enrolled_courses = []

    def __str__(self):
        """
        Returns a string representation of the Students instance.

        Returns:
            str: A string describing the student and their major.
        """
        return f'This is {self.first_name} {self.last_name} and this is your major {self.major}'

    def update(self, id, fname, lname, major):
        """
        Updates the student's information.

        Args:
            id (str): The new ID for the student.
            fname (str): The new first name of the student.
            lname (str): The new last name of the student.
            major (str): The new major field of study.
        """
        self.first_name = fname
        self.last_name = lname
        self.id = id
        self.major = major


class Instructor(Person):
    """
    Represents an instructor who is a person with an additional department affiliation.

    Attributes:
        department (str): The department the instructor belongs to.
    """

    def __init__(self, first_name, last_name, id, department):
        """
        Initializes a new Instructor instance.

        Args:
            first_name (str): The first name of the instructor.
            last_name (str): The last name of the instructor.
            id (str): The unique identifier for the instructor.
            department (str): The department the instructor belongs to.
        """
        super().__init__(first_name, last_name, id)
        self.department = department

    def __str__(self):
        """
        Returns a string representation of the Instructor instance.

        Returns:
            str: A string describing the instructor and their department.
        """
        return f'This is Lecturer {self.first_name} {self.last_name} with ID NUMBER {self.id} in {self.department} Department'

    def update(self, id, fname, lname, dept):
        """
        Updates the instructor's information.

        Args:
            id (str): The new ID for the instructor.
            fname (str): The new first name of the instructor.
            lname (str): The new last name of the instructor.
            dept (str): The new department affiliation.
        """
        self.first_name = fname
        self.last_name = lname
        self.id = id
        self.department = dept


class Course:
    """
    Represents a course with a name, ID, and an instructor, and manages enrolled students.

    Attributes:
        course_name (str): The name of the course.
        id (str): The unique identifier for the course.
        instructor (Instructor): The instructor teaching the course.
        enrolled_students (dict): A dictionary of enrolled students and their grades.
    """

    def __init__(self, course_name, id, instructor):
        """
        Initializes a new Course instance.

        Args:
            course_name (str): The name of the course.
            id (str): The unique identifier for the course.
            instructor (Instructor): The instructor teaching the course.
        """
        self.course_name = course_name
        self.id = id
        self.instructor = instructor
        self.enrolled_students = {}

    def add_student(self, enrollment):
        """
        Adds a student to the course.

        Args:
            enrollment (Enrollment): The enrollment object containing the student and their grade.
        """
        student_id = enrollment.student.id
        student_name = f"{enrollment.student.first_name} {enrollment.student.last_name}"
        grade = enrollment.grade
        if student_id not in self.enrolled_students:
            self.enrolled_students[student_id] = grade
        else:
            print(f"{student_name} already enrolled")

    def remove_student(self, enrollment):
        """
        Removes a student from the course.

        Args:
            enrollment (Enrollment): The enrollment object containing the student to be removed.
        """
        student_id = enrollment.student.id
        student_name = f"{enrollment.student.first_name} {enrollment.student.last_name}"
        if student_id in self.enrolled_students:
            self.enrolled_students.pop(student_id)
        else:
            print(f"{student_name} does not exist")

    def update(self, id, cname, instructor):
        """
        Updates the course's information.

        Args:
            id (str): The new ID for the course.
            cname (str): The new name of the course.
            instructor (Instructor): The new instructor for the course.
        """
        self.course_name = cname
        self.id = id
        self.instructor = instructor

    def list_of_students(self):
        """
        Returns the list of students enrolled in the course.

        Returns:
            dict: A dictionary of student IDs and their grades.
        """
        return self.enrolled_students


class Enrollment:
    """
    Represents an enrollment of a student in a course.

    Attributes:
        student (Students): The student being enrolled.
        course (Course): The course in which the student is enrolled.
        grade (str, optional): The grade assigned to the student.
    """

    def __init__(self, student, course):
        """
        Initializes a new Enrollment instance.

        Args:
            student (Students): The student being enrolled.
            course (Course): The course in which the student is enrolled.
        """
        self.student = student
        self.course = course
        self.grade = None

    def add_grade(self, grade):
        """
        Assigns a grade to the student for the course.

        Args:
            grade (str): The grade to assign.

        Returns:
            str: The assigned grade.
        """
        self.grade = grade
        return self.grade

    def __str__(self):
        """
        Returns a string representation of the Enrollment instance.

        Returns:
            str: A string describing the enrollment.
        """
        return f'{self.student} has been enrolled for {self.course} with grade {self.grade}'


class StudentManagementSystem:
    """
    Manages students, instructors, and courses within an educational institution.

    Attributes:
        students (list): A list of all students in the system.
        instructors (list): A list of all instructors in the system.
        courses (list): A list of all courses in the system.
    """

    def __init__(self):
        """
        Initializes a new StudentManagementSystem instance.
        """
        self.students = []
        self.instructors = []
        self.courses = []

    def find_student(self, result):
        """
        Finds a student in the system by their ID.

        Args:
            result (Students): The student to find.

        Returns:
            Students or None: The found student or None if not found.
        """
        for student in self.students:
            if result.id == student.id:
                return student
        return None

    def find_instructor(self, result):
        """
        Finds an instructor in the system by their ID.

        Args:
            result (Instructor): The instructor to find.

        Returns:
            Instructor or None: The found instructor or None if not found.
        """
        for instructor in self.instructors:
            if result.id == instructor.id:
                return instructor
        return None

    def find_course(self, result):
        """
        Finds a course in the system by its ID.

        Args:
            result (Course): The course to find.

        Returns:
            Course or None: The found course or None if not found.
        """
        for course in self.courses:
            if result.id == course.id:
                return course
        return None

    def add_student(self, student):
        """
        Adds a student to the system.

        Args:
            student (Students): The student to add.
        """
        if student.id not in [student.id for student in self.students]:
            self.students.append(student)
        else:
            print(f"{student.first_name} {student.last_name} already exists")

    def add_instructor(self, instructor):
        """
        Adds an instructor to the system.

        Args:
            instructor (Instructor): The instructor to add.
        """
        if instructor.id not in [instructor.id for instructor in self.instructors]:
            self.instructors.append(instructor)
        else:
            print(f"{instructor.first_name} {instructor.last_name} already exists")

    def add_course(self, course):
        """
        Adds a course to the system.

        Args:
            course (Course): The course to add.
        """
        if course.id not in [course.id for course in self.courses]:
            self.courses.append(course)
        else:
            print(f"{course.course_name} already exists")

    def remove_student(self, student):
        """
        Removes a student from the system.

        Args:
            student (Students): The student to remove.
        """
        if self.find_student(student):
            self.students.remove(student)
        else:
            print(f"{student.first_name} {student.last_name} does not exist")

    def remove_instructor(self, instructor):
        """
        Removes an instructor from the system.

        Args:
            instructor (Instructor): The instructor to remove.
        """
        if self.find_instructor(instructor):
            self.instructors.remove(instructor)
        else:
            print(f"{instructor.first_name} {instructor.last_name} does not exist")

    def remove_course(self, course):
        """
        Removes a course from the system.

        Args:
            course (Course): The course to remove.
        """
        if self.find_course(course):
            self.courses.remove(course)
        else:
            print(f"{course.course_name} does not exist")

    def course_enrolled_students(self, course):
        """
        Returns a list of students enrolled in a specific course.

        Args:
            course (Course): The course to retrieve students for.

        Returns:
            dict: A dictionary of student IDs and their grades.
        """
        return course.list_of_students()

    def enroll_students(self, enrollment):
        """
        Enrolls a student in a course.

        Args:
            enrollment (Enrollment): The enrollment object containing the student and course.
        """
        course = enrollment.course
        course_id = enrollment.course.id
        student_id = enrollment.student.id

        if student_id not in course.enrolled_students.keys():
            if course_id in [course.id for course in self.courses] and student_id in [student.id for student in self.students]:
                course.add_student(enrollment)
        else:
            print("Student has been enrolled")

    def update_student(self, student):
        """
        Updates a student's information in the system.

        Args:
            student (Students): The student with updated information.
        """
        result = self.find_student(student)
        if result:
            result.update(student.id, student.first_name, student.last_name, student.major)

    def update_instructor(self, instructor):
        """
        Updates an instructor's information in the system.

        Args:
            instructor (Instructor): The instructor with updated information.
        """
        result = self.find_instructor(instructor)
        if result:
            result.update(instructor.id, instructor.first_name, instructor.last_name, instructor.department)

    def update_course(self, course):
        """
        Updates a course's information in the system.

        Args:
            course (Course): The course with updated information.
        """
        result = self.find_course(course)
        if result:
            result.update(course.id, course.course_name, course.instructor)

    def assigned_grade(self, enrollment):
        """
        Assigns a grade to a student in a course.

        Args:
            enrollment (Enrollment): The enrollment object containing the student and course.
        """
        course = enrollment.course
        course_id = enrollment.course.id
        student_id = enrollment.student.id
        student_name = f"{enrollment.student.first_name} {enrollment.student.last_name}"
        grade = enrollment.grade
        students = enrollment.course.enrolled_students

        if course_id in [course.id for course in self.courses] and student_id in [student.id for student in self.students]:
            students[student_id] = enrollment.add_grade(grade)

    def list_courses(self, student):
        """
        Lists all courses in which a specific student is enrolled.

        Args:
            student (Students): The student to list courses for.

        Returns:
            dict: A dictionary of course IDs and course details.
        """
        result = {}

        for course in self.courses:
            if student.id in course.enrolled_students.keys():
                result[course.id] = f'{course.course_name} by {course.instructor}'
        return result
            
        
                   
        
       
   

