from app import app
from flask import render_template, request
from app.models import model, formopener
    
        
jobs = {
    "Mathematician": [3, 2, 1, 2, 1],
    "Lawyer": [1, 2, 1, 1, 1],
    "Doctor": [2, 2, 1, 1, 2],
    "Nurse": [1, 2, 2, 2, 2],
    "Entrepeneur": [1, 1, 1, 1, 1],
    "Researcher": [2, 3, 1, 2, 2],
    "Veterinarian": [2, 3, 1, 2, 1],
    "Astronaut": [2, 1, 1, 2, 2],
    "Teacher": [1, 1, 2, 2, 1],
    "Philosopher": [2, 1, 1, 2, 3],
    "Professor": [2, 1, 1, 1, 2]
}
#     "Airplane pilot ": [1, 2, 2, 3, 3],
#     "Accountant": [3, 1, 1, 1, 1],
#     "Banker": [3, 1, 1, 1, 1],
#     "Pharmacist": [3, 1, 1, 1, 1],
#     "Electrical engineer": [3, 1, 1, 1, 1],
#     "Chemist": [3, 1, 1, 1, 1],
#     "Security guard": [3, 1, 1, 1, 1],
#     "Paramedic": [3, 1, 1, 1, 1],
#     "Firefighter": [3, 1, 1, 1, 1],
#     "Athletic coach": [3, 1, 1, 1, 1],
#     "Artist": [3, 1, 1, 1, 1],
#     "Surgeon": [3, 1, 1, 1, 1],
#     "Technician": [3, 1, 1, 1, 1],
#     "Painter": [3, 1, 1, 1, 1],
#     "Graphics designer": [3, 1, 1, 1, 1],
#     "Real-estate agent": [3, 1, 1, 1, 1],
#     "Janitor": [3, 1, 1, 1, 1],
#     "Counselor": [3, 1, 1, 1, 1],
#     "Police officer": [3, 1, 1, 1, 1],
#     "Architect": [3, 1, 1, 1, 1],
#     "Computer scientist": [3, 1, 1, 1, 1],
#     "Carpenter": [3, 1, 1, 1, 1],
#     "Electrician": [3, 1, 1, 1, 1],
#     "Librarian": [3, 1, 1, 1, 1],
#     "Actor": [3, 1, 1, 1, 1],
#     "Athlete": [3, 1, 1, 1, 1],
#     "Producer": [3, 1, 1, 1, 1],
#     "Director": [3, 1, 1, 1, 1],
#     "Farmer": [3, 1, 1, 1, 1],
#     "Chef": [3, 1, 1, 1, 1],
#     "Waiter": [3, 1, 1, 1, 1],
#     "Clerk": [3, 1, 1, 1, 1],
#     "Mechanic": [3, 1, 1, 1, 1],
#     "Judge": [3, 1, 1, 1, 1],
#     "Historian": [3, 1, 1, 1, 1],
#     "Forensic scientist": [3, 1, 1, 1, 1],
#     "Manager": [3, 1, 1, 1, 1],
#     "Salesman": [3, 1, 1, 1, 1],
#     "Analyst": [3, 1, 1, 1, 1],
#     "Executive": [3, 1, 1, 1, 1],
#     "Photographer": [3, 1, 1, 1, 1],
#     "Author": [3, 1, 1, 1, 1],
#     "News reporter": [3, 1, 1, 1, 1],
#     "Soldier": [3, 1, 1, 1, 1],
#     "Receptionist": [3, 1, 1, 1, 1],
#     "Baker": [3, 1, 1, 1, 1],
#     "Butcher": [3, 1, 1, 1, 1],
#     "Jeweler": [3, 1, 1, 1, 1],
#     "Model": [3, 1, 1, 1, 1],
#     "Chaffeur": [3, 1, 1, 1, 1],
#     "Insurance agent": [3, 1, 1, 1, 1],
#     "Retail worker": [3, 1, 1, 1, 1],
#     "Travel agent": [3, 1, 1, 1, 1],
#     "Flight attendant": [3, 1, 1, 1, 1],
#     "Postman": [3, 1, 1, 1, 1],
#     "Barber": [3, 1, 1, 1, 1],
#     "Plumber": [3, 1, 1, 1, 1],
#     "Biologsit": [3, 1, 1, 1, 1],
#     "Logistician": [3, 1, 1, 1, 1],
#     "Masseur": [3, 1, 1, 1, 1],
#     "Cartographer": [3, 1, 1, 1, 1],
#     "Interpreter": [3, 1, 1, 1, 1],
#     "Critic": [3, 1, 1, 1, 1],
#     "Announcer": [3, 1, 1, 1, 1],
#     "Archivist": [3, 1, 1, 1, 1],
#     "Bartender": [3, 1, 1, 1, 1],
#     "Composer": [3, 1, 1, 1, 1],
#     "Curator": [3, 1, 1, 1, 1],
#     "Hairstylist": [3, 1, 1, 1, 1],
#     "Maid": [3, 1, 1, 1, 1],
#     "Assembly worker": [3, 1, 1, 1, 1],
#     "Journalist": [3, 1, 1, 1, 1],
#     "Landscaper": [3, 1, 1, 1, 1],
#     "Detective": [3, 1, 1, 1, 1],
#     "Radio caster": [3, 1, 1, 1, 1],
#     "Fisherman": [3, 1, 1, 1, 1],
#     "Surveyor": [3, 1, 1, 1, 1],
#     "Usher": [3, 1, 1, 1, 1],
#     "Secretary": [3, 1, 1, 1, 1],
#     "Actuary": [3, 1, 1, 1, 1],
#     "Chief Executive": [3, 1, 1, 1, 1],
#     "Legislator": [3, 1, 1, 1, 1],
#     "Chiropractor": [3, 1, 1, 1, 1],
#     "Podiatrist": [3, 1, 1, 1, 1],
#     "Orthodontist": [3, 1, 1, 1, 1],
#     "Dentist": [3, 1, 1, 1, 1],
#     "Zoologist": [3, 1, 1, 1, 1],
#     "Nutritionist": [3, 1, 1, 1, 1],
#     "Tour guide": [3, 1, 1, 1, 1],
#     "Clergy": [3, 1, 1, 1, 1],
#     "Social worker": [3, 1, 1, 1, 1],
#     "Computer programmer": [3, 1, 1, 1, 1],
#     "Software engineer": [3, 1, 1, 1, 1],
#     "Web developer": [3, 1, 1, 1, 1],
#     "Network administrator": [3, 1, 1, 1, 1],
#     "Metalworker": [3, 1, 1, 1, 1],
#     "Advertisting manager": [3, 1, 1, 1, 1],
#     "Marketer": [3, 1, 1, 1, 1],
#     "Broker": [3, 1, 1, 1, 1],
#     "Telemarketer": [3, 1, 1, 1, 1],
#     "Archeologist": [3, 1, 1, 1, 1],
#     "Astronomer": [3, 1, 1, 1, 1],
#     "Geographer": [3, 1, 1, 1, 1],
#     "Civil engineer": [3, 1, 1, 1, 1],
#     "Mechanical engineer": [3, 1, 1, 1, 1],
#     "Physicist": [3, 1, 1, 1, 1],
#     "Dispatcher": [3, 1, 1, 1, 1],
#     "Aerospace engineer": [3, 1, 1, 1, 1],
#     "Agricultural engineer": [3, 1, 1, 1, 1],
#     "Geologist": [3, 1, 1, 1, 1]
# }

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template ("index.html")

@app.route('/results', methods = ["GET", "POST"])
@app.route('/results.html', methods = ["GET", "POST"])

def tellMeTheFuture ():
    userdata = request.form.to_dict()
    mind = int(userdata["mind"])
    body = int(userdata["energy"])
    soul = int(userdata["nature"])
    feet = int(userdata["tactics"])
    toes = int(userdata["identity"])
    
    for key in jobs:
        print(key)
        job_data = jobs[key]
        print(job_data)
        print(mind)
        print(body)
        print(soul)
        print(feet)
        print(toes)
        
        
        
        if job_data[0] == mind and job_data[1] == body and job_data[2] == soul and job_data[3] == feet and job_data[4] == toes:
            print("Did we get here?")
            user_job = key
            break;
        else:
            user_job = "ERROR"
    
    return user_job
    # for eachItem in userdata:
    #     userResponses.push(userdata[eachItem])
        
    

# for each in jobs:
#     if userResponses == jobs(each):
#         return each