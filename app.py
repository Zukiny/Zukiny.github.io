from flask import Flask, render_template, request

app = Flask(__name__)

# Calculate the required Midterm and Final grades
def calculate_grades(prelim):
    total_prelim = prelim * 0.20
    remaining = 75 - total_prelim
    required_midterm = (remaining / 0.80) * 0.30
    required_finals = (remaining / 0.80) * 0.50
    
    # For Dean's Lister (Grade > 90)
    dean_total = prelim * 0.20
    dean_remaining = 90 - dean_total
    dean_midterm = (dean_remaining / 0.80) * 0.30
    dean_finals = (dean_remaining / 0.80) * 0.50
    
    return required_midterm, required_finals, dean_midterm, dean_finals

# Check if the input is valid
def validate_input(grade):
    try:
        grade = float(grade)
        if 0 <= grade <= 100:
            return True, grade
        else:
            return False, 0
    except ValueError:
        return False, 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    prelim_grade = request.form['prelim']
    is_valid, prelim = validate_input(prelim_grade)

    if is_valid:
        required_midterm, required_finals, dean_midterm, dean_finals = calculate_grades(prelim)
        
        # Determine pass possibility
        final_score = prelim * 0.20 + required_midterm + required_finals
        if final_score >= 75:
            result = "You have a chance to pass!"
        else:
            result = "It is difficult to pass."

        # Determine Dean's Lister possibility
        dean_final_score = prelim * 0.20 + dean_midterm + dean_finals
        if dean_final_score >= 90:
            dean_lister = f"The required grades for Dean's Lister are Midterm: {dean_midterm:.2f} and Final: {dean_finals:.2f}."
        else:
            dean_lister = "It's difficult to qualify for Dean's Lister."

        return render_template('result.html', 
                               prelim=prelim, 
                               midterm=required_midterm, 
                               finals=required_finals, 
                               result=result, 
                               dean_lister=dean_lister)
    else:
        return render_template('index.html', error="Invalid input. Please enter a number between 0 and 100.")

if __name__ == '__main__':
    app.run(debug=True)
