import re
import pdfplumber
import docx2txt

# --- Extract text from different file types ---
def extract_text(file_path):
    if file_path.name.endswith('.pdf'):
        with pdfplumber.open(file_path) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text() or ''
    elif file_path.name.endswith('.docx'):
        text = docx2txt.process(file_path)
    else:
        raise ValueError("Unsupported file type. Please upload a PDF or DOCX file.")
    return text

# --- Extract name, email, phone, skills, etc. ---
def parse_resume(text):
    # Basic patterns
    name_pattern = r"^[A-Z][a-zA-Z]+\s[A-Z][a-zA-Z]+"
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    phone_pattern = r"(\+?\d{1,3}[\s-]?)?\d{10}"

    # Skill keywords
    skills = ["Python", "Java", "C++", "Machine Learning", "Data Analysis", "SQL",
              "Excel", "TensorFlow", "Deep Learning", "Power BI", "Communication",
              "Leadership", "Project Management"]

    # Education keywords
    education_keywords = ["B.Tech", "B.E", "M.Tech", "MBA", "B.Sc", "M.Sc", "PhD", "Diploma"]

    # Extract info
    name = re.search(name_pattern, text)
    email = re.search(email_pattern, text)
    phone = re.search(phone_pattern, text)

    found_skills = [skill for skill in skills if skill.lower() in text.lower()]
    found_edu = [edu for edu in education_keywords if edu.lower() in text.lower()]

    return {
        "Name": name.group(0) if name else "Not Found",
        "Email": email.group(0) if email else "Not Found",
        "Phone": phone.group(0) if phone else "Not Found",
        "Skills": ", ".join(found_skills) if found_skills else "Not Found",
        "Education": ", ".join(found_edu) if found_edu else "Not Found"
    }
