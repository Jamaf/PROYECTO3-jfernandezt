from models.usuario import Usuario
from database.db import login_manager

from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from flask_login import login_user
from flask_login import login_required 
from flask_login import current_user


login_blueprint = Blueprint('login_bp', __name__, url_prefix="/login")

@login_manager.user_loader
def load_user(user_id):
    usuario = Usuario.consultar_por_id(int(user_id))

    return usuario



@login_blueprint.route('/', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]

        usuario = Usuario.consultar_por_nombre_password(username, password)
        
        login_user(usuario[0])
        return redirect(url_for('login_bp.dashboard'))

        # if usuario is not None:
        #     login_user(usuario[0])
        #     if usuario[0].rol.Nombre == 'Administrador':
        #         return redirect(url_for('heladeria_bp.index'))
        #     else:
        #         return redirect(url_for('dashboard'))
        # else:
        #     return redirect(url_for('login'))

@login_blueprint.route('/dashboard')
#@login_required
def dashboard():
    return render_template("dashboard.html", usuario = current_user)       

    # if current_user.rol.nombre != 'Administrador':
    #     return render_template("dashboard.html", usuario = current_user)       
    # else:
    #     return redirect(url_for('login_bp.login'))