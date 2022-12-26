# Python

### Table of Contents
**[Description](#description)**<br>
**[Requirements](#requirements)**<br>
**[Tested On](#tested-on)**<br>
**[Sample Execution](#sample-execution)**<br>
**[Overview](#overview)**<br>
**[Bug Fix Request](#bug-fix-request)**<br>
**[Feature Request](#feature-request)**<br>
**[Authors](#authors)**<br>
**[Conclusion](#conclusion)**<br>

# Description
This Python repository briefly introduces Python as a suitable language for learning coding and real-world programming. Control-flow statements, types of data structures, Python's well-known standard libraries, handling errors in Python, and object-oriented programming have all been covered in this Git repository.

## Requirements
- Operating System : > Windows-10, Ubuntu 22.04.1 LTS
- Python :  > Version 3.10.7 

## Tested On

Windows-10-10.0.22621-SP0 with Python version 3.10.7

## Sample Execution 

Go to the Exercises directory and run below command :
```python
python <script_name>.py
``` 

## Overview

| Exercises   |      Description     | 
|----------| :---------------|
| Exercises_01 | To comprehend assignment, operators, and variables' interactions   | 
| Exercises_02 | To understand the importance of comments and docstrings while writing scripts   | 
| Exercises_03 | To explore the use of Python's data structures |
| Exercises_04 | To begin writing Python code that uses control flows and statements  | 
| Exercises_05 | To illustrate use of functions for code reuse | 
| Exercises_06 | To understand modules, and packages in Python| 
| Exercises_07 | To systematically handle errors in Python |
| Exercises_08 | To improve scalability and code reuse via Object-Oriented (OO) coding | 
| Exercises_09 | To develop Python tests that effectively demonstrate unit testing | 
| Exercises_10 | To demonstrate use of Python standard libraries  |
| Exercises_11 | To demonstrate how Python can be used to manage network utilities  | 
| Exercises_12 | To delve into the Python project structure  | 

## Bug Fix Request

Reported bugs can be found at [Bug Fix](https://github.com/krishnenduATU/Python/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)  

If developers encounter a bug with one of the Python programs, please follow the below steps:
- A "Bug" issue is created for the identified bug as shown below.

![image](https://user-images.githubusercontent.com/119352610/209512161-854ed88e-c16c-474d-b11d-da1ad1154951.png)

- Clone the Python repo to local machine.
```
git clone https://github.com/krishnenduATU/Python.git
``` 

- A new branch is created from the "test" branch, named "bug_fix_#<bug_fix_number>"
  
  ![image](https://user-images.githubusercontent.com/119352610/209512959-1c818968-b75a-4623-8da4-0d8ba7fb0074.png)

- A developer will work on the bug and fix the issue, then commit the changes. Make sure to add the bug fix number to the commit message, for example, "BugFix #4 : Corrected Pie value "
- Now merge the newly created bug fix branch into the "test" branch. Delete the bugfix branch once it has been merged.
- Checkout to "dev" branch and merge the changes made in the "test" branch so that all the branch are in same state..
- Push the changes on local "dev" and "test" branches to remote repo 
- In the end, the changes from "dev" branch is pulled to "main" branch and issue is closed in GitHub.
 
## Feature Request

Feature requests can be found at [Features](https://github.com/krishnenduATU/Python/issues?q=is%3Aissue+is%3Aclosed+label%3Aenhancement+)

To create a new feature in the Python programs, developer should follow below steps :

- A "Enhancement" issue is created as shown below.

![image](https://user-images.githubusercontent.com/119352610/209514336-9782f35b-9747-4cbf-8f4e-07a7eddee361.png)

- Clone the Python repo to the local machine.
```
git clone https://github.com/krishnenduATU/Python.git
``` 

- A new branch is created from "dev" branch, named "Feature_#<issue number>" as shown below.  

  ![image](https://user-images.githubusercontent.com/119352610/209512959-1c818968-b75a-4623-8da4-0d8ba7fb0074.png)
  
- Developer will work on the new feature. Then commits the changes. Make sure to add issue number to the commit message, for example "Feature #8 : Created UDP server and client scripts" to track the changes.
- Now, checkout to "dev" branch and merge the newly created feature branch. Delete the feature branch.
- Checkout to "test" branch and merge the changes made in "dev" branch so that all the branch are in same state.
- Push the changes on local "dev" and "test" branches to remote repo.
- In the end, the changes from "dev" branch is pulled to "main" branch and the feature request is closed in GitHub.

## Authors

This Python repository was developed as a part of Infrastructure as Code module's assignment by Krishnendu VP.  

## Conclusion

This Python repository covered the fundamental concepts of Python and offered a doable strategy for improving programming skills. In accordance with the provided exercises and research on the same, learners should be able to build and organise Python projects for network or server administration, log analysis, and the automation of routine tasks.


