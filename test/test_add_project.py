from model.project import Project

def test_add_project(app):
    # app.session.login("administrator", "root")
    test_name = app.project.random_project_name("My_project", 7)

    app.project.open_projects_page()
    test_project = Project(name=test_name, status="release", view_state="private",
                               description="My description")
    app.project.create(test_project)

    assert app.project.project_with_name_exists_on_projects_page(test_name)


