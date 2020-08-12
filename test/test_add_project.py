from model.project import Project

def test_add_project(app, db):
    old_projects = db.get_projects_list()
    test_name = app.project.random_project_name("My_project", 7)

    test_project = Project(name=test_name, status="release", view_state="private",
                               description="My description")
    app.project.create(test_project)

    new_projects = db.get_projects_list()
    old_projects.append(test_project)

    assert app.project.project_with_name_exists_on_projects_page(test_name)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)



