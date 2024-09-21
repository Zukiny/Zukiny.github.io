How It Works
HTML Elements:

Input Field: Allows the student to enter their Prelim grade.
Submit Button: Triggers the grade processing.
Output Div: Displays the results.
Styling: Basic CSS styling for a clean and user-friendly interface.

Pyodide Integration:

The Pyodide script is loaded from a CDN.
The loadPyodideAndPackages function initializes Pyodide when the page loads.
Processing Function (processGrade):

Input Retrieval: Gets the Prelim grade entered by the user.
Python Code Execution: Defines and runs Python code to:
Validate the input.
Calculate the required Midterm and Final grades to pass.
Determine if the student can achieve Dean’s Lister status.
Output Parsing: Captures and parses the Python script's output.
Result Display: Shows the Prelim grade, required Midterm and Final grades, pass/fail message, and Dean’s Lister status on the web page.
Grade Calculation Logic:

Passing Grade: The student needs an overall grade of at least 75.
Grade Weights: Prelim (20%), Midterm (30%), Final (50%).
Required Grades:
Calculates the remaining grade needed after the Prelim.
Determines the minimum Final grade required if Midterm is assumed to be 0.
If the minimum Final grade exceeds 100, it adjusts by setting Final to 100 and calculates the required Midterm.
If both required Midterm and Final grades exceed 100, it concludes that passing is not possible.
Dean’s Lister: Checks if the overall grade exceeds 90.
Testing the Application
Run Locally:

Save the above code in an index.html file.
Open the file in your browser using Live Server or any local server setup to simulate the web environment.
Enter Prelim Grade:

Input a Prelim grade between 0 and 100.
Click the Submit button.
View Results:

The application will display the required Midterm and Final grades to pass.
It will indicate whether you have a chance to pass.
If applicable, it will also inform you about Dean’s Lister eligibility.
Example Scenarios
Scenario 1: High Prelim Grade
Prelim Grade: 80
Calculation:
Prelim Contribution: 0.2 * 80 = 16
Remaining Needed: 75 - 16 = 59
Required Final: 59 / 0.5 = 118 (Exceeds 100)
Adjust Required Final to 100:
Remaining after Final: 59 - (0.5 * 100) = 59 - 50 = 9
Required Midterm: 9 / 0.3 = 30
Result:
Required Midterm: 30
Required Final: 100
Pass: Yes
Dean’s Lister: Depends on the overall grade.
Scenario 2: Low Prelim Grade
Prelim Grade: 50
Calculation:
Prelim Contribution: 0.2 * 50 = 10
Remaining Needed: 75 - 10 = 65
Required Final: 65 / 0.5 = 130 (Exceeds 100)
Adjust Required Final to 100:
Remaining after Final: 65 - 50 = 15
Required Midterm: 15 / 0.3 = 50
Result:
Required Midterm: 50
Required Final: 100
Pass: Yes
Dean’s Lister: Depends on the overall grade.
Scenario 3: Very Low Prelim Grade
Prelim Grade: 20
Calculation:
Prelim Contribution: 0.2 * 20 = 4
Remaining Needed: 75 - 4 = 71
Required Final: 71 / 0.5 = 142 (Exceeds 100)
Adjust Required Final to 100:
Remaining after Final: 71 - 50 = 21
Required Midterm: 21 / 0.3 = 70
Check if Midterm and Final are within 100
Result:
Required Midterm: 70
Required Final: 100
Pass: Yes
Dean’s Lister: Depends on the overall grade.
Scenario 4: Impossible to Pass
Prelim Grade: 10
Calculation:
Prelim Contribution: 0.2 * 10 = 2
Remaining Needed: 75 - 2 = 73
Required Final: 73 / 0.5 = 146 (Exceeds 100)
Adjust Required Final to 100:
Remaining after Final: 73 - 50 = 23
Required Midterm: 23 / 0.3 ≈ 76.67
If Midterm exceeds 100, passing is impossible
Result:
If Required Midterm ≤ 100: Pass
Else: Cannot Pass
Notes
Input Validation: The program ensures that the entered Prelim grade is a number between 0 and 100. If invalid input is detected, an error message is displayed.
Flexibility: The grade calculation assumes that if the required Final grade exceeds 100, it compensates by increasing the Midterm grade. You can adjust this logic based on your specific requirements.
Enhancements: You can further enhance the application by allowing users to input Midterm and Final grades to see their overall grade or to handle different grading schemes.