# to render html pages we put "render template"
from flask import Flask , render_template

# The way for naming our flask app
skills_app = Flask(__name__) 

# slash meaning the domain for your website route like freecode.com 
# The way for distributing the app sections into paths Ex: home & about & services & .....
my_skills = [ ("Html" , 70) , ("CSS" , 60) ,("Python" , 80) , ("PostgreSql" , 65)]
@skills_app.route("/")
def homepage():
  # return "Hello From Flask framework"  
  # هنا لازم نعرف اننا كنا لازم نعمل فولدر التمبلتس الاول عشان نحط فية اى تمبلت هنشغلة
  # to control more ont page title we can add page title attr to render template and Html page title tag
  # to build a css file for every single file e put attr for it like custom
  return render_template("homepage.html" ,
                          title = "home" , 
                          custom_css = "home" ,
                          page_head = "home for me",
                          desc = "It's my homes")


@skills_app.route("/about")
def about():
  # return "About From Flask framework" 
  return render_template( "abouut.html" ,
                          title = "aboute" ,
                          custom_css = "about",
                          page_head = "about for me",
                          desc = "It's my abouts" )

@skills_app.route("/add")
def add():
  return render_template("/add.html" ,
                          title = "ADDITION",
                          custom_css = "add",
                          page_head = "add for me",
                          desc = "It's my adds")


@skills_app.route("/Skills")
def skills():
  return render_template("/skills.html" ,
                          title = "Skills",
                          custom_css = "skill",
                          page_head = "Skills for me",
                          desc = " What I Good with ",
                          skills = my_skills  )


if __name__ == "__main__": 
  skills_app.run( debug = True , port = 9000)

# it's meaning this method will be run if we run this file file only 
