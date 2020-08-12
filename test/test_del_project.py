from model.project import Project
import random

def test_delete_project(app):
    app.project.open_projects_page()
    if len(app.project.get_project_names_list()) == 0:
        app.project.create(Project(name="My Test Project"))

    project_names = app.project.get_project_names_list()
    project_name = random.choice(project_names)
    app.project.delete_project_by_name(project_name)

    assert not app.project.project_with_name_exists_on_projects_page(project_name)