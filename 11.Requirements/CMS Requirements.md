# Proposal
## COURSE MANAGEMENT SYSTEM (CMS)
### Problem Definition: 
A course management system (CMS) is a collection of software tools providing an online environment for course interactions. A CMS typically includes a variety of online tools and environments, such as:
- An area for faculty posting of class materials such as course syllabus and handouts
- An area for student posting of papers and other assignments
- A grade book where faculty can record grades and each student can view his or her grades
- An integrated email tool allowing participants to send announcement email messages to the entire class or to a subset of the entire class
- A chat tool allowing synchronous communication among class participants
- A threaded discussion board allowing asynchronous communication among participants

In addition, a CMS is typically integrated with other databases in the university so that students enrolled in a particular course are automatically registered in the CMS as participants in that course. The Course Management System (CMS) is a web application for department personnel, academic senate, and registrar staff to view, enter, and manage course information formerly submitted via paper. Departments can use CMS to create new course proposals, submit changes for existing courses, and track the progress of proposals as they move through the stages of online approval. 

- Construct the design element for a course management system that can be used to manage courses and classes for an organisation that specialize in providing training.
- The organisation offers a variety of courses in a variety of areas such as computer science courses and engineering courses (electrical, civil, etc.).
- Each course is made up of set of modules.
- Lecturers are assigned courses to teach according to the area that is specialized in and their availability.
- The organisation publish and maintain a calendar of different courses and assign tutors every year.
- There is a group of Course administrator to manage the courses including course content, assign courses to tutor and define the course schedule.

# Functional requirements
 - FID1 - An area for faculty posting of class materials such as course syllabus and handouts
  - 1.1 - A multi tenanted bulletin board with tennants as follows
   - faculty 
   - student groups by course 
   - A facility to allow the upload of course materials to include, 
    - 1.1.1 - Microsoft formats and text files. **TBA**
  - 1.2 - A view only permission group for students
  - 1.3 
 - FID2 - An area for student posting of papers and other assignments
 - FID3 - A grade book where faculty can record grades and each student can view his or her grades 
  - 3.1   
 - FID4 - An integrated email tool allowing participants to send announcement email messages to the entire class or to a subset of the entire class
 - FID5 - A chat tool allowing synchronous communication among class participants
 - FID6 - A threaded discussion board allowing asynchronous communication among participants 
 - FID7 - Department personnel, academic senate, and registrar staff to view, enter, and manage course information formerly submitted via paper.
 - FID8 - Departments can use CMS to create new course proposals, submit changes for existing courses, and track the progress of proposals as they move through the stages of online approval.
# Non Functional Requirements
 - NFID1 – Must be an online service
 - NFID2 – Must have different user roles 
    - Student
    - Faculty
    - Department personnel
    - Academic senate, 
    - Registrar staff
    - Course administrator

- NFID3 – Must have an Email SMTP service 
- NFID4 – Chat agent and server functionality
- NFID5 – System needs to be connected to the University Network with access to databases as follows:
    - TBD
- NFID6 – The CMS should be a website	
- NFID7 - Document sizes must be at least 10Mb - TBA
- NFID8 - Housekeeping of files in bulletin boards will be automated. 
 - 8.1 - Student files will be deleted after 6 months of the student leaving the university 

