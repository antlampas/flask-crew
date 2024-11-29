from flask          import current_app,request,redirect,render_template
from flask_security import auth_required
from flask_menu     import current_menu

from .blueprint     import crew_blueprint
from .models        import CrewMember
from .forms         import crewMemberForm


@crew_blueprint.route('/add',methods = ['GET','POST'])
@auth_required()
def add_member_view():
    crew_member_form = crewMemberForm();
    if request.method == 'POST':
        crew_member = crewMember()
        username   = request.form.username
        email      = request.form.email
        password   = hash_password(request.form.password)
        first_name = request.form.first_name
        last_name  = request.form.lastname

        crew_member.username = request.form.username
        crew_member.nickname = request.form.nickname
        crew_member.rank     = request.form.rank

        current_app.security.datastore.create_user(username=username,email=email,password=password)

        current_app.database.session.add(crew_member)
        current_app.database.session.commit()
        return redirect(url_for('articles.show_crew_view'))
    return render_template('addMember.html',form=crew_member_form,sectionname="Nuovo membro",next=request.path)

current_menu.submenu(".crew.add").register(text='Add',external_url=crew_blueprint.url_prefix+"/add",logged_only=True)
