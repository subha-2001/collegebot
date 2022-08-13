from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy
spacy.load('en_core_web_sm')
# from spacy.lang.en import English
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('<b>TPGIT BOT</b>')

# nlp = spacy.load("en_core_web_sm")

chatbot = ChatBot(
    'ChatBot for College Enquiry',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Hi there, Welcome to TPGIT ! 👋 If you need any assistance, I'm always here.Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br><br>",
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)
trainer = ListTrainer(chatbot)

# python app.py
# Training with Personal Ques & Ans
conversation = [
"Hi",
"Helloo!",
"Hey",

"How are you?",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Great",
"Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"good",
"Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"fine",
"Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Thank You",
"Your Welcome 😄",

"Thanks",
"Your Welcome 😄",

 "ok",
 "Your Welcome 😄",


"Bye",
"Thank You for visiting!..",

"What do you do?",
"I am made to give Information about TPGIT College.",

"What else can you do?",
"I can help you know more about TPGIT",



    "1",
    "<b>STUDENT <br>The following are frequently searched terms related to student . Please select one from the options below : <br> <br> 1.1 Courses offered <br>1.2  Extra curricular<br>1.3  Administrative<br>1.4 Examination <br>1.5 Placements </b>",

    "1.1",
    "<b>  Courses offered<br>  These are the top results: <br> <br> 1.1.1 Courses <br> 1.1.2 Fees structure <br> 1.1.3 Syllabus </b>",
    "1.1.1",
    "<b> 1.1.1 Courses <br>The link to courses 👉 <a href='http://tpgit.edu.in/index.php/student-corner/courses-offered/' >Click Here</a> </b>",
    "1.1.2",
    "<b > 1.1.2 Fees structure<br>The link to Fees structure👉<a href=" 'http://tpgit.edu.in/index.php/student-corner/fees-structure/' ">Click Here</a> </b>",
    "1.1.3",
    "<b> 1.1.3 Syllabus<br>The link to Syllabus 👉 <a href=" 'http://tpgit.edu.in/index.php/student-corner/syllabus/' ">Click Here</a> </b>",

    "1.2",
    "<b>EXTRA-CURRICULAR<br>These are the top results: <br> <br> 1.2.1 Events<br> 1.2.2 NSS <br> 1.2.3 Student's Council</b>",
    "1.2.1",
    "<b > 1.2.1 Events<br>The link to Events👉 <a href=" 'https://tpgit.edu.in/index.php/recent-events/' ">Click Here</a></b>",
    "1.2.2",
    "<b > 1.2.2 NSS<br>The link to NSS 👉<a href=" 'https://tpgit.edu.in/index.php/nss-2/' ">Click Here</a> </b>",
    "1.2.3",
    "<b > 1.2.3 Youth Red Cross society activities <br>The link to Youth Red Cross society activities👉 <a href=" 'https://tpgit.edu.in/index.php/student-corner/youth-red-cross-society-activities-2019-20/' ">Click Here</a> </b>",

    "1.3",
    "<b>1.3 ADMINISTRATIVE<br>These are the top results: <br> <br> 1.3.1 Students Cornerl<br> 1.3.2 Newsletter </b>",
    "1.3.1",
    "<b> 1.3.1 Students Corner<br>The link to Students Portal👉 <a href=" 'http://tpgit.edu.in/index.php/student-corner/' ">Click Here</a> </b>",
    "1.3.2",
    "<b> 1.3.2 Newsletter<br>The link to Notices👉 <a href=" 'http://tpgit.edu.in/index.php/tpgit-news-letter/' ">Click Here</a> </b>",

    "1.4",
    "<b > EXAMINATION <br>These are the top results:<br> 1.4.1 Academic Schedule <br> 1.4.2 Internal Assesment Schedule <br> 1.4.3 Syllabus </b>",
    "1.4.1",
    "<b > 1.4.1 Academic Schedule<br>The link to  Academic Schedule👉 <a href=" 'http://tpgit.edu.in/index.php/student-corner/academic-schedule/' ">Click Here</a> </b>",
    "1.4.2",
    "<b > 1.4.2 Internal Assesment Schedule<br>The link to Internal Assesment Schedules👉<a href=" 'http://tpgit.edu.in/index.php/student-corner/internal-assessment-schedule/' ">Click Here</a> </b>",
    "1.4.3",
    "<b > 1.4.3 Syllabus<br>The link to  Syllabus👉 <a href=" 'https://tpgit.edu.in/index.php/student-corner/syllabus/' ">Click Here</a> </b>",

    "1.5",
    "<b > PLACEMENTS These are the top results:<br> 1.5.1 Placed Informations<br> 1.5.2Placement Photos <br> 1.5.3 Career site </b>",
    "1.5.1",
    "<b> 1.5.1 Placed Information<br>The link to Placed Information👉 <a href=" 'http://tpgit.edu.in/index.php/placement/placement-info/' ">Click Here</a> </b>",
    "1.5.2",
    "<b> 1.5.2 Placement Photos<br>The link to Placement Photos👉<a href=" 'http://tpgit.edu.in/index.php/placement/placement-photos/' ">Click Here</a> </b>",
    "1.5.3",
    "<b > 1.5.3 Career site<br>The link to Career site👉 <a href=" 'http://tpgit.edu.in/index.php/placement/career-sites/' ">Click Here</a> </b>",

    "2",
    "<b >DEPARTMENTS<br>The following are frequently searched terms related to faculty. Please select one from the options below :</br></br>2.1 B.E. Civil Engineering<br>2.2  B.E. Mechanical Engineering<br>2.3  B.E. Electronics and Communication Engineering<br>2.4 B.E. Electrical and Electronics Engineering<br>2.5 B.E. Computer Science and Engineering</b>",

    "2.1",
    "<b > B.E. Civil Engineering These are the top results:<br> 2.1.1 About Civil Engineering <br>2.1.2 Vision and Mission <br>2.1.3  Faculty & Staff Details  </b>",
    "2.1.1",
    "<b> 2.1.1 About Civil Engineering<br>The link to About Civil Engineering👉<a href=" 'http://tpgit.edu.in/index.php/departments/civil-engineering/' ">Click Here</a> </b>",

    "2.1.2",
    "<b> 2.1.2 Vision and Mission<br>The link to Vision and Mission👉<a href=" 'http://tpgit.edu.in/index.php/departments/civil-engineering/vision-and-mission/' ">Click Here</a> </b>",
    "2.1.3",
    "<b> 2.1.3 Faculty & Staff Details<br>The link to Faculty & Staff Details👉<a href=" 'http://tpgit.edu.in/index.php/departments/civil-engineering/staff-details/' ">Click Here</a> </b>",

    "2.2",
    "<b > B.E. Mechanical Engineering These are the top results:<br> 2.2.1 About Mechanical Engineering <br>2.2.2 Vision and Mission <br>2.2.3  Faculty & Staff Details  </b>",
    "2.2.1",
    "<b> 2.2.1 About Mechanical Engineering<br>The link to About Mechanical Engineering👉<a href=" 'http://tpgit.edu.in/index.php/departments/mechanical-engineering/' ">Click Here</a> </b>",

    "2.2.2",
    "<b> 2.2.2 Vision and Mission<br>The link to Vision and Mission👉<a href=" 'http://tpgit.edu.in/index.php/departments/mechanical-engineering/vision-and-mission/' ">Click Here</a> </b>",
    "2.2.3",
    "<b> 2.2.3 Faculty & Staff Details<br>The link to Faculty & Staff Details👉<a href=" 'http://tpgit.edu.in/index.php/departments/mechanical-engineering/staff-details/' ">Click Here</a> </b>",

    "2.3",
    "<b > B.E. Electronics and Communication engineering These are the top results:<br> 2.3.1 About Electronics and Communication engineering  <br>2.3.2 Vision and Mission <br>2.3.3  Faculty & Staff Details </b>",
    "2.3.1",
    "<b> 2.3.1 About Electronics and Communication engineering <br>The link to About Electronics and Communication engineering 👉<a href=" 'http://tpgit.edu.in/index.php/departments/elec-comm-engineering/vision-and-mission/' ">Click Here</a> </b>",
    "2.3.2",
    "<b> 2.3.2 Vision and Mission <br>The link to Vision and Mission👉<a href=" 'http://tpgit.edu.in/index.php/departments/elec-comm-engineering/staff-details/' ">Click Here</a> </b>",
    "2.3.3",
    "<b> 2.3.3 Faculty & Staff Details<br>The link to Faculty & Staff Details👉<a href=" 'https://tpgit.edu.in/index.php/departments/elec-comm-engineering/staff-details/' ">Click Here</a> </b>",

    "2.4",
    "<b > B.E.  Electrical and Electronics Engineering These are the top results:<br> 2.4.1 About  Electrical and Electronics Engineering <br> 2.4.2 Faculty & Staff Details </b>",
    "2.4.1",
    "<b> 2.4.1 About  Electrical and Electronics Engineering <br>The link to About Electrical and Electronics Engineering  👉<a href=" 'http://tpgit.edu.in/index.php/departments/b-e-electrical-and-electronics-engineering/' ">Click Here</a> </b>",
    "2.4.2",
    "<b> 2.4.2 Faculty & Staff Details <br>The link to Faculty & Staff Details👉<a href=" 'http://tpgit.edu.in/index.php/departments/b-e-electrical-and-electronics-engineering/faculty-staff-details/' ">Click Here</a> </b>",

    "2.5",
    "<b > B.E. Computer Science and Engineering These are the top results:<br> 2.5.1 About Computer Science and Engineering<br> 2.5.2 Faculty & Staff Details </b>",
    "2.5.1",
    "<b> 2.5.1 About Computer Science and Engineering <br>The link to About Computer Science and Engineering 👉<a href=" 'http://tpgit.edu.in/index.php/departments/b-e-computer-science-engineering/' ">Click Here</a> </b>",
    "2.5.2",
    "<b> 2.5.3 Faculty & Staff Details<br>The link to Faculty & Staff Details👉<a href=" 'http://tpgit.edu.in/index.php/departments/b-e-computer-science-engineering/faculty-staff-details/' ">Click Here</a> </b>",

    "3",
    "<b> PARENTS <br>The following are frequently searched terms related to Parents. Please select one from the options below : <br> <br> 3.1 About Us <br>3.2 Library <br>3.3 Hostels  </b> " ,

    "3.1",
    "<b > ABOUT US<br>These are the top results:<br> <br> 3.1.1 About TPGIT<br> 3.1.2 Principal legacys <br> 3.1.3 Vice Principal's Address </b>",
    "3.1.1",
    "<b > 3.1.1 About TPGIT<br>The link to About TPGIT👉 <a href=" 'http://tpgit.edu.in/' ">Click Here</a> </b>",
    "3.1.2",
    "<b > 3.1.2 Principal legacy <br>The link to  Principal's  Address👉<a href=" 'http://tpgit.edu.in/index.php/about-us/principal-legacy/' ">Click Here</a> </b>",
    "3.1.3",
    "<b > 3.1.3 Vice Principal's Address <br>The link to  Vice Principal's Address👉 <a href=" 'http://tpgit.edu.in/index.php/about-us/vice-principal/' ">Click Here</a> </b>",

    "3.2",
    "<b > LIBRARY<br>These are the top results:<br> <br> 3.2.1 Books Details <br>3.2.2 Timing and other <br> 3.2.3 Staff Details  </b>",
    "3.2.1",
    "<b > 3.2.1  Books Details<br>The link to Books Details👉 <a href=" 'https://tpgit.edu.in/index.php/library/book-details/' ">Click Here</a> </b>",

    "3.2.2",
    "<b >3.2.2 Timing and other<br>The link to Timing and othe👉 <a href=" 'https://tpgit.edu.in/index.php/library/timing-other/' ">Click Here</a> </b>",

    "3.2.3",
    "<b > 3.2.3 Staff Details<br>The link to Staff Details 👉 <a href=" 'https://tpgit.edu.in/index.php/library/staff-details/' ">Click Here</a> </b>",

    "3.3",
    "<b > HOSTELS These are the top results:<br> <br>3.3.1 Boys Hostel <br> 3.3.2 Girls Hostel <br> 3.3.3 Hostel Officials <br> 3.3.4 Hostel Fee</b>",
    "3.3.1",
    "<b> 3.3.1 Boys Hostel<br>The link to Boys Hostel👉 <a href=" 'https://tpgit.edu.in/index.php/hostels/boys-hostel/' ">Click Here</a> </b>",
    "3.3.2",
    "<b> 3.3.2 Girls Hostel<br>The link to Girls Hostel👉<a href=" 'https://tpgit.edu.in/index.php/hostels/girls-hostel/' ">Click Here</a> </b>",
    "3.3.3",
    "<b > 3.3.3 Hostel Officials <br>The link to Hostel Officials👉 <a href=" 'https://tpgit.edu.in/index.php/hostels/hostel-officials/' ">Click Here</a> </b>",
    "3.3.4",
    "<b > 3.3.3 Hostel Fee <br>The link to Hostel Fee👉 <a href=" 'https://tpgit.edu.in/index.php/hostels/hostel-fee/' ">Click Here</a> </b>",

    "4",
    "<b VISITORS <br>The following are frequently searched terms related to visitors. Please select one from the options below : <br> <br> 4.1 Anna university links <br>4.2 Alumni <br>4.3 Bonafide <br>4.4 Research </b>",

    "4.1",
    "<b > <br>These are the top results:<br> <br>4.1.1 Anna University  <br> 4.1.2 Stucor Website <br> 4.1.3 AU Results Official App </b>",
    "4.1.1",
    "<b > 4.1.1  Anna University<br>The link to Anna University 👉 <a href=" 'https://www.annauniv.edu/nwsnew/' ">Click Here</a> </b>",
    "4.1.2",
    "<b > 4.1.2  Stucor Website <br>The link to Stucor Website 👉<a href=" 'https://stucor.in/' ">Click Here</a> </b>",
    "4.1.3",
    "<b > 4.1.3 AU Results Official App <br>The link to AU Results Official App 👉 <a href=" 'https://play.google.com/store/apps/details?id=com.coeofficial.coe.dll_coe&hl=en_IN&gl=US' ">Click Here</a> </b>",

    "4.2",
    "<b > ALUMNI <br>These are the top results:<br> <br>4.2.1 About alumni </b>",
    "4.2.1",
    "<b > 4.2.1 About Alumni<br>The link to  About Alumni👉 <a href=" 'https://tpgit.edu.in/index.php/alumni/' ">Click Here</a> </b>",

    "4.3",
    "<b > BONAFIDE <br>These are the top results:<br> <br>4.3.1 Student login  <br> 4.3.2 Staff login  </b>",
    "4.3.1",
    "<b > 4.3.1 Student login <br>The link to Student login 👉 <a href=" 'http://tpgit.edu.in/bonafide/student_login.php' ">Click Here</a> </b>",
    "4.3.2",
    "<b > 4.3.2 Staff login <br>The link to Staff login 👉<a href=" 'http://tpgit.edu.in/bonafide/bonafide_home.php' ">Click Here</a> </b>",

    "4.4",
    "<b >RESEARCH <br>These are the top results:<br> <br>4.2.1 About Research</b>",
    "4.4.1",
    "<b > 4.4.1 About Research<br>The link to  About Research👉 <a href=" 'https://tpgit.edu.in/index.php/research//' ">Click Here</a> </b>",

]

trainer.train(conversation)
