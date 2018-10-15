from flask import render_template
import pandas as pd
from flask_dropzone import Dropzone
import os
from flask import Flask, request, jsonify
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *


app = Flask(__name__)
data = [{
    "name": "bootstrap-table",
    "commits": "10",
    "attention": "122",
    "uneven": "An extended Bootstrap table"
},
    {
        "name": "multiple-select",
        "commits": "288",
        "attention": "20",
        "uneven": "A jQuery plugin"
    }, {
        "name": "Testing",
        "commits": "340",
        "attention": "20",
        "uneven": "For test"
    },
    {
        "name": "bootstrap-table",
        "commits": "10",
        "attention": "122",
        "uneven": "An extended Bootstrap table"
    },

]

columns = [
    {
        "field": "name",  # which is the field's name of data key
        "title": "name",  # display as the table header's name
        "sortable": True,
    },
    {
        "field": "commits",
        "title": "commits",
        "sortable": True,
    },
    {
        "field": "attention",
        "title": "attention",
        "sortable": True,
    },
    {
        "field": "uneven",
        "title": "uneven",
        "sortable": True,
    }
]


app = Flask(__name__)
Bootstrap(app)
Dropzone(app)
nav=Nav()
nav.register_element('top',Navbar(u'ISPM Accelerator',
                                    View(u'Home','index'),
                                    Subgroup(u'Service',
                                             View(u'RRIC Shareholding Rule Recon','shareholding_rule_recon'),

                                             Separator(),
                                             View(u'FCMO Monthly Report Automation', 'index'),
                                    ),
))

nav.init_app(app)


@app.route('/shareholding_rule_recon_uploads', methods=['GET', 'POST'])
def shareholding_rule_recon_uploads():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join('upload/shareholding_rule_recon/', f.filename))
    return 'uploads template'

@app.route('/shareholding_rule_recon')
def shareholding_rule_recon():
   # d = pd.read_excel("upload/shareholding_rule_recon/tableExport.xlsx")
   # return render_template("shareholding_rule_recon.html", data=d.to_dict(orient='records'), columns=columns )
     return render_template("shareholding_rule_recon.html" )

@app.route('/')
def index():
    d = pd.DataFrame(data)
    return render_template("home.html")

@app.route('/shareholding_rule_recon_get_report')
def shareholding_rule_recon_get_report():
    d = pd.read_excel("upload/shareholding_rule_recon/tableExport.xlsx")
    return jsonify(result=d.to_dict(orient='records'))

if __name__ == '__main__':
    # print jdata
    app.run(debug=True)
