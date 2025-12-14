from app import create_app, db
from app.models import Course, FAQ

app = create_app()

def seed():
    with app.app_context():
        print("Resetting database...")
        db.drop_all()
        db.create_all()
        
        print("Seeding NIRT Courses & Fees...")
        # Fees are approximate market rates for Bhopal engineering colleges as placeholders
        courses = [
            # Undergraduate
            Course(title="B.Tech Computer Science (CSE)", duration="4 Years", fees="₹70,000 per year", 
                   description="Focus regarding algorithms, software engineering, and systems.", 
                   eligibility="12th PCM with min 45%"),
            Course(title="B.Tech AI & Data Science", duration="4 Years", fees="₹75,000 per year", 
                   description="Advanced specs in Machine Learning and Big Data.", 
                   eligibility="12th PCM with min 45%"),
            Course(title="B.Tech Mechanical Engineering", duration="4 Years", fees="₹60,000 per year", 
                   description="Core engineering discipline covering mechanics and thermodynamics.", 
                   eligibility="12th PCM with min 45%"),
            Course(title="B.Tech Civil Engineering", duration="4 Years", fees="₹60,000 per year", 
                   description="Construction, structural analysis and design.", 
                   eligibility="12th PCM with min 45%"),
            
            # Postgraduate
            Course(title="M.Tech (CSE/Core)", duration="2 Years", fees="₹80,000 per year", 
                   description="Master's level specialization.", 
                   eligibility="B.Tech in relevant branch"),
            Course(title="MBA", duration="2 Years", fees="₹65,000 per year", 
                   description="Business administration with HR, Finance, Marketing options.", 
                   eligibility="Graduation in any stream"),
             
            # Diploma
            Course(title="Diploma in Engineering", duration="3 Years", fees="₹30,000 per year", 
                   description="Polytechnic diploma in various branches.", 
                   eligibility="10th Pass")
        ]
        db.session.bulk_save_objects(courses)
        
        print("Seeding NIRT FAQs...")
        faqs = [
            FAQ(question="What is the full name of the college?", answer="NRI Institute of Research and Technology, Bhopal (NIRT).", category="General"),
            FAQ(question="What are the hostel fees?", answer="Approx. ₹60,000 per year (including food). Separate for Boys and Girls.", category="Hostel"),
            FAQ(question="What are the admission fees?", answer="One time admission fee: ₹5,000 (Approx).", category="Fees"),
            FAQ(question="What are the exam fees?", answer="Exam fees are charged per semester as per university norms (approx ₹2,500/sem).", category="Fees"),
            FAQ(question="Where is the campus located?", answer="Raisen Road, Bhopal, Madhya Pradesh.", category="Location")
        ]
        db.session.bulk_save_objects(faqs)
        
        db.session.commit()
        print("NIRT Database Seeded Successfully!")

if __name__ == "__main__":
    seed()
