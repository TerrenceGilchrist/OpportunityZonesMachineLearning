# Structure for the page views
# December 11, 2020 ~5:51 p.m. to 

from flask import Flask, render_template, request
oppzones_app = Flask(__name__)

@oppzones_app.route('/home/', methods=['GET','POST'])
def home_view():
    # return "<h1>Hello, world!</h1>"
    # return render_template('home.html')
      if request.method == 'POST':
        options_selected = request.form.get('regressor')
        print(options_selected)
        return render_template('input_selections.html') 
      else render_template('home.html')

#@oppzones_app.route('/result/', methods=['GET','POST'])
#def index():
 #   if request.method == 'POST':
 #       options_selected = request.form.get('regressor')
 #       print(options_selected)
 #       return render_template('input_selections.html') 

if __name__ == "__main__":
    oppzones_app.run(debug=TRUE)
