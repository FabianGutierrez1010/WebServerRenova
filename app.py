import flask
import time
app = flask.Flask(__name__)
app.config['SECRET_KEY']='clavesupersecreta'

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'POST':
        form = flask.request.form
        flask.session['fecha'] = form['fecha']
        flask.session['path_accdb'] = form['access path']
        flask.session['path_bernc'] = form['bernc path']
        flask.session['path_dicc'] = form['dicc path']
        flask.session['path_dec_last_month'] = form['dec last month path']
        return flask.redirect(flask.url_for('createCSV'))
    return flask.render_template('./main.html')

@app.route('/createCSV', methods=['GET'])
def createCSV():
    fecha = flask.session['fecha']
    time.sleep(30)
    return flask.render_template('./result.html', fecha=fecha)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)