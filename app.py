# from data.single_pred_tasks.tasks import _TASKS
import backend.task_datasets as data
from backend.metadata.publications import _PUBLICATIONS as publications
from backend.data.loader.navigation import get_navigation_data
from backend.data.loader.content import get_callouts_data, get_team_data
from backend.data.loader.models import get_models_data
import benchmark.groups as benchmark_groups
import benchmark.leaderboards as benchmark_leaderboards

from flask import Flask, flash, send_from_directory, redirect, render_template, request, session, url_for, make_response
from flask_restful import Api, Resource

app = Flask(__name__)
app.url_map.strict_slashes = False
api = Api(app)

navigation_data = get_navigation_data()
callouts_data = get_callouts_data()
team_data = get_team_data()
models_data = get_models_data()

class TDCRequest(dict):

    def __init__(self,
                 title: str,
                 description: str,
                 endpt: str,
                 navbar: object,
                 current_url: str,
                 **kwargs):
        super().__init__(**kwargs)
        self["title"] = title
        self["description"] = description
        self["endpt"] = endpt
        self["navbar"] = navbar
        self["current_url"] = current_url

@app.route('/')
def index():
    publications.sort(key=lambda x: (-x["year"], -x["month"]))
    args = {
        "publications": publications,
        "navbar": navigation_data,
        "current_url": request.path,
        "callouts": callouts_data,
        "title": "PyTDC: A Community Platform for AI-driven Drug Discovery and Development",
        "description": "PyTDC is a community platform for AI-driven drug discovery and development that provides a comprehensive overview of the field, including models, datasets, and tasks.",
        "endpt": ""
    }
    args = TDCRequest(**args)
    return render_template('index_template.html', **args)

@app.route('/start')
def start():
    args = {
        "navbar": navigation_data,
        "current_url": request.path,
        "title": "PyTDC: A Community Platform for AI-driven Drug Discovery and Development",
        "description": "PyTDC is a community platform for AI-driven drug discovery and development that provides a comprehensive overview of the field, including models, datasets, and tasks.",
        "endpt": ""
    }
    args = TDCRequest(**args)
    return render_template('start.html', **args)

@app.route('/overview')
def overview():
    args = {
        "navbar": navigation_data,
        "current_url": request.path,
        "title": "PyTDC: A Community Platform for AI-driven Drug Discovery and Development",
        "description": "PyTDC is a community platform for AI-driven drug discovery and development that provides a comprehensive overview of the field, including models, datasets, and tasks.",
        "endpt": ""
    }
    args = TDCRequest(**args)
    return render_template('overview/index.html', **args)

@app.route("/news")
def news():
    return render_template('news.html')

@app.route("/team")
def team():
    args = TDCRequest(
        title="Team",
        description="Meet the PyTDC team.",
        endpt="team",
        navbar=navigation_data,
        current_url=request.path,
        team = team_data,
        )
    return render_template('team.html', **args)

@app.route('/single_pred_tasks/overview')
def single_pred_tasks():
    vars = {
        "items": data.single_pred_tasks.tasks,
        "data": [(endpt, label, data.single_pred_tasks.datasets[endpt]) for endpt, label, _ in data.single_pred_tasks.tasks[1:]] # skip adme 
    }
    args = {
        "navbar": navigation_data,
        "current_url": request.path,
        "title": "Single-instance prediction tasks | PyTDC: A Community Platform for AI-driven Drug Discovery and Development",
        "description": "PyTDC is a community platform for AI-driven drug discovery and development that provides a comprehensive overview of the field, including models, datasets, and tasks.",
        "endpt": ""
    }
    args = TDCRequest(**args)
    vars.update(args)
    return render_template('single_pred_tasks/index.html', **vars)

@app.route("/single_pred_tasks/<task>")
def single_pred_tasks_data(task):
    args = TDCRequest(
        title=f"{task}",
        description=f"{task} datasets",
        endpt=f"/single_pred_tasks/{task}",
        navbar=navigation_data,
        current_url=request.path,
    )
    if task == "adme":
        return render_template("single_pred_tasks/adme.html", **args)
    if task.lower() == "mpc":
        return render_template("single_pred_tasks/MPC.html", **args)
    elif task in data.single_pred_tasks.datasets:
        datasets = []
        for var in data.single_pred_tasks.datasets[task]:
            if var in data.single_pred_tasks.meta:
                if len(data.single_pred_tasks.meta[var]) != 10:
                    raise Exception(var, len(data.single_pred_tasks.meta[var])) 
                datasets.append([var] + data.single_pred_tasks.meta[var])
        desc = data.single_pred_tasks.desc[task]
        args2 = {
            "datasets": datasets,
            "task": task,
            "desc_id": desc[0],
            "desc_title": desc[1],
            "desc_desc": desc[2],
            "desc_impact": desc[3],
            "desc_gen": desc[4],
            "desc_product": desc[5],
            "desc_pipeline": desc[6],
        }
        args.update(args2)
        return render_template("single_pred_tasks/task.html", **args)
    return redirect("/single_pred_tasks/overview")

@app.route("/multi_pred_tasks/overview")
def multi_pred_tasks():
    vars = {
        "items": data.multi_pred_tasks.tasks,
        "data": [(endpt, label, data.multi_pred_tasks.datasets[endpt]) for endpt, label, _ in data.multi_pred_tasks.tasks]
    }
    args = {
        "navbar": navigation_data,
        "current_url": request.path,
        "title": "Multi-instance prediction tasks | PyTDC: A Community Platform for AI-driven Drug Discovery and Development",
        "description": "PyTDC is a community platform for AI-driven drug discovery and development that provides a comprehensive overview of the field, including models, datasets, and tasks.",
        "endpt": ""
    }
    args = TDCRequest(**args)
    vars.update(args)
    return render_template("multi_pred_tasks/index.html", **vars)

@app.route("/multi_pred_tasks/<task>")
def multi_pred_task_data(task):
    args = {
        "navbar": navigation_data,
        "current_url": request.path,
        "title": f"{task} | PyTDC: A Community Platform for AI-driven Drug Discovery and Development",
        "description": "PyTDC is a community platform for AI-driven drug discovery and development that provides a comprehensive overview of the field, including models, datasets, and tasks.",
        "endpt": ""
    }
    args = TDCRequest(**args)
    if task == "catalyst":
        return render_template("multi_pred_tasks/catalyst.html", **args)
    elif task == "ddi":
        return render_template("multi_pred_tasks/ddi.html", **args)
    elif task == "drugres":
        return render_template("multi_pred_tasks/drugres.html", **args)
    elif task == "dti":
        return render_template("multi_pred_tasks/dti.html", **args)
    elif task == "mti":
        return render_template("multi_pred_tasks/mti.html", **args)
    elif task == "ppi":
        return render_template("multi_pred_tasks/ppi.html", **args)
    elif task == "proteinpeptide":
        return render_template("multi_pred_tasks/proteinpeptide.html", **args)
    elif task == "tcrepitope":
        return render_template("multi_pred_tasks/tcrepitope.html", **args)
    elif task == "antibodyaff":
        return render_template("multi_pred_tasks/antibodyaff.html", **args)
    elif task == "trialoutcome":
        return render_template("multi_pred_tasks/trialoutcome.html", **args)
    elif task == "scdti":
        return render_template("multi_pred_tasks/scdti.html", **args)
    elif task == "counterfactual":
        return render_template("multi_pred_tasks/counterfactual.html", **args)
    elif task in data.multi_pred_tasks.datasets:
        datasets = []
        for var in data.multi_pred_tasks.datasets[task]:
            if var in data.multi_pred_tasks.meta:
                if len(data.multi_pred_tasks.meta[var]) != 10:
                    raise Exception(var, len(data.multi_pred_tasks.meta[var])) 
                datasets.append([var] + data.multi_pred_tasks.meta[var])
        desc = data.multi_pred_tasks.desc[task]
        args2 = {
            "datasets": datasets,
            "task": task,
            "desc_id": desc[0],
            "desc_title": desc[1],
            "desc_desc": desc[2],
            "desc_impact": desc[3],
            "desc_gen": desc[4],
            "desc_product": desc[5],
            "desc_pipeline": desc[6],
        }
        args.update(args2)
        return render_template("multi_pred_tasks/task.html", **args)
    else:
        return redirect("/multi_pred_tasks/overview")
        
@app.route("/generation_tasks/overview")
def generation_tasks():
    args = {
        "navbar": navigation_data,
        "current_url": request.path,
        "title": "PyTDC: A Community Platform for AI-driven Drug Discovery and Development",
        "description": "PyTDC is a community platform for AI-driven drug discovery and development that provides a comprehensive overview of the field, including models, datasets, and tasks.",
        "endpt": ""
    }
    args = TDCRequest(**args)
    return render_template("generation_tasks/index.html", **args)

@app.route("/generation_tasks/<task>")
def generation_tasks_data(task):
    args = {
        "navbar": navigation_data,
        "current_url": request.path,
        "title": "PyTDC: A Community Platform for AI-driven Drug Discovery and Development",
        "description": "PyTDC is a community platform for AI-driven drug discovery and development that provides a comprehensive overview of the field, including models, datasets, and tasks.",
        "endpt": ""
    }
    args = TDCRequest(**args)
    if task == "molgen":
        return render_template("generation_tasks/molgen.html", **args)
    elif task == "reaction":
        return render_template("generation_tasks/reaction.html", **args)
    elif task == "retrosyn":
        return render_template("generation_tasks/retrosyn.html", **args)
    elif task == "sbdd":
        return render_template("generation_tasks/sbdd.html", **args)
    else:
        return redirect("/generation_tasks/overview")

@app.route("/fct_overview")
def fct_overview():
    args = {
        "navbar": navigation_data,
        "current_url": request.path,
        "title": "PyTDC: A Community Platform for AI-driven Drug Discovery and Development",
        "description": "PyTDC is a community platform for AI-driven drug discovery and development that provides a comprehensive overview of the field, including models, datasets, and tasks.",
        "endpt": ""
    }
    args = TDCRequest(**args)
    return render_template("/fct_overview.html", **args)

@app.route("/functions/<section>")
def function_page(section):
    args = {
        "navbar": navigation_data,
        "current_url": request.path,
        "title": "PyTDC: A Community Platform for AI-driven Drug Discovery and Development",
        "description": "PyTDC is a community platform for AI-driven drug discovery and development that provides a comprehensive overview of the field, including models, datasets, and tasks.",
        "endpt": ""
    }
    args = TDCRequest(**args)
    if section == "oracles":
        return render_template("/functions/oracles.html", **args)
    elif section == "data_evaluation":
        return render_template("/functions/data_evaluation.html", **args)
    elif section == "data_process":
        return render_template("/functions/data_process.html", **args)
    elif section == "data_split":
        return render_template("/functions/data_split.html", **args)
    else:
        return redirect("/fct_overview")

@app.route("/benchmark")
def benchmark():
    args = {
        "navbar": navigation_data,
        "current_url": request.path,
        "title": "PyTDC: A Community Platform for AI-driven Drug Discovery and Development",
        "description": "PyTDC is a community platform for AI-driven drug discovery and development that provides a comprehensive overview of the field, including models, datasets, and tasks.",
        "endpt": ""
    }
    args = TDCRequest(**args)
    return render_template("/benchmark/index.html", **args)

@app.route("/benchmark/overview")
def benchmark_overview():
    args = {
        "navbar": navigation_data,
        "current_url": request.path,
        "title": "PyTDC: A Community Platform for AI-driven Drug Discovery and Development",
        "description": "PyTDC is a community platform for AI-driven drug discovery and development that provides a comprehensive overview of the field, including models, datasets, and tasks.",
        "endpt": ""
    }
    args = TDCRequest(**args)
    return render_template("/benchmark/index.html", **args)

@app.route("/benchmark/<group>/<leaderboard>")
def benchmark_leaderboard_overview(group, leaderboard):
    args = {
        "navbar": navigation_data,
        "current_url": request.path,
        "title": "PyTDC: A Community Platform for AI-driven Drug Discovery and Development",
        "description": "PyTDC is a community platform for AI-driven drug discovery and development that provides a comprehensive overview of the field, including models, datasets, and tasks.",
        "endpt": ""
    }
    args = TDCRequest(**args)
    leads = benchmark_groups._GROUP_MEMBERSHIP[group]
    if leaderboard == "overview":
        if group != "clinical_trial":
            group = '_'.join(group.split("_")[:-1])
            s = "/benchmark/{}.html".format(group)
        else:
            s = "/benchmark/clinical_trial.html"
        args2 = {
            "leaderboards": leads
        }
        args.update(args2)
        return render_template(s, **args)
    elif leaderboard == "DrugComb_CSS" and group == "drugcombo_group":
        return render_template("/benchmark/drugcomb_css.html", **args)
    elif leaderboard == "DRD3" and group == "docking_group":
        return render_template("/benchmark/drd3.html", **args)
    elif leaderboard == "scperturb_drug_SrivatsanTrapnell2020_sciplex2" and group == "counterfactual_group":
        return render_template("/benchmark/scperturb_drug_SrivatsanTrapnell2020_sciplex2.html", **args)
    else:
        lb = benchmark_leaderboards._LEADERBOARDS[leaderboard]
        order, entries, scores = lb[2], lb[3], lb[4]
        if len(entries) != len(scores):
            raise ValueError("length of lb entries {} does not match length of provided scores {} for lb {}".format(len(entries), len(scores), leaderboard))
        increasing = order == "incr"
        sidxs = sorted([i for i in range(len(entries))], key=lambda idx: entries[idx][-1] if increasing else -entries[idx][-1])
        lb[3] = [entries[i] for i in sidxs]
        lb[4] = [scores[i] for i in sidxs]
        args2 = {
            "entries": entries,
            "scores": scores,
            "group": group,
            "leaderboard": leaderboard,
            "style": lb[0],
            "cols": lb[1],
            "extra_vals": lb[-1],
            "extra_cols": lb[-2],
            "leaderboards": leads,
        }
        args.update(args2)
        return render_template("/benchmark/leaderboard.html", **args)


### Resources

@app.route("/favicon.ico")
def favicon():
    return send_from_directory("static", "favicon-32x32.png", mimetype="image/png")

# Serve _next/static files
@app.route("/_next/static/<path:filename>")
def next_static_files(filename):
    return send_from_directory("static/_next/static", filename)

@app.route("/paper")
def paper():
    return send_from_directory('static/pdfs', "pytdc_icml_final_arxiv.pdf", as_attachment=True)


class TDC2Homepage(Resource):

    def get(self):
        return make_response(render_template("/MyApp.html"), 200, {'Content-Type': 'text/html'})

class LegacyHome(Resource):
    def get(self):
        publications.sort(key=lambda x: (-x["year"], -x["month"]))
        args = {
            "publications": publications,
            "navbar": navigation_data,
            "current_url": request.path,
            "callouts": callouts_data,
            "title": "PyTDC: A Community Platform for AI-driven Drug Discovery and Development",
            "description": "PyTDC is a community platform for AI-driven drug discovery and development that provides a comprehensive overview of the field, including models, datasets, and tasks.",
            "endpt": ""
        }
        args = TDCRequest(**args)
        return make_response(render_template("/index_template.html", **args), 200, {'Content-Type': 'text/html'})

class ModelsOverview(Resource):
    def get(self):
        args = {
            "navbar": navigation_data,
            "current_url": request.path,
            "title": "PyTDC: A Community Platform for AI-driven Drug Discovery and Development",
            "description": "PyTDC is a community platform for AI-driven drug discovery and development that provides a comprehensive overview of the field, including models, datasets, and tasks.",
            "endpt": "",
            "models": models_data,
        }
        args = TDCRequest(**args)
        return make_response(render_template("/models/overview.html", **args), 200, {'Content-Type': 'text/html'})
    
api.add_resource(TDC2Homepage, "/pytdc")
api.add_resource(LegacyHome, "/home")
api.add_resource(ModelsOverview, "/models")

if __name__ == '__main__':
    app.run() 
