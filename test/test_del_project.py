from model.project import Project
import random

def test_delete_project(app, db):
    app.project.open_projects_page()
    if len(app.project.get_project_names_list()) == 0:
        app.project.create(Project(name="My Test Project"))

    old_projects = db.get_projects_list()
    project = random.choice(old_projects)

    app.project.delete_project_by_name(project.name)
    new_projects = db.get_projects_list()
    old_projects.remove(project)

    assert not app.project.project_with_name_exists_on_projects_page(project.name)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
