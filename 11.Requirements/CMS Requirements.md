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
 - FID1.1 - A multi tenanted bulletin board with tennants as follows
     - faculty 
     - student groups by course 
- FID1.1.2 - A facility to allow the upload of course materials to include, 
    - Microsoft formats and text files. **TBA**
    - A view only permission group for students
    - A read/write permission group for faculty
- FID1.1.3 - A facility for faculty to create, delete and update messages  
- FID2 - An area for student posting of papers and other assignments
- FID2.1 - A multi tennated bulletin board facility must be provided
- FID2.3 - A facility to allow students to upload course assignments must be provided
- FID2.4 - A facility to allow faculty to download student assignments must be provided
- FID3 - A grade book where faculty can record grades and each student can view his or her grades 
- FID3.1 - The grade book should access the grade database in real time
- FID3.2 - The grade book must only show grades relating to the authenticated student
- FID3.3 - The grade book will allow reading of all student grades by a faculty member - **TBC**
- FID4 - An integrated email tool allowing participants to send announcement email messages to the entire class or to a subset of the entire class - Definition of a participant **TBA**
- FID4.1 - A facility that allows the creation and sending of e-mails 
- FID5 - A chat tool allowing synchronous communication among class participants
- FID5.1 - Integration of chat gateway 
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

- NFID3 – Must have an Email SMTP gateway  
- NFID4 – Chat agent and server functionality
- NFID5 – The CMS System needs to be connected to the University Network with access to databases as follows:
    - **TBD**
- NFID6 - CMS users will authenticated using a Single Sign On system using the existing university authentication mechanism
- NFID7 - CMS users will be authorised access to specific CMS roles using the exist university authentication and authorisation mechanism
- NFID8 – The CMS must be a website	
- NFID9 - Document sizes must be at least 10Mb - TBA
- NFID10 - Housekeeping of files in bulletin boards will be automated. 
- NFID10.1 - Student files will be deleted after 6 months of the student leaving the university 

