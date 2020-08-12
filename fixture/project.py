import random
import string

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.open_projects_page()

    def open_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            self.app.return_to_home_page()
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def project_with_name_exists_on_projects_page(self, project_name):
        wd = self.app.wd
        if len(wd.find_elements_by_link_text(project_name)) == 0:
            return False
        else:
            return True

    def delete_project_by_name(self, project_name):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_link_text(project_name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.open_projects_page()

    def fill_project_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(contact.name)
        self.select_status_value_in_list(contact.status)
        self.select_view_state_value_in_list(contact.view_state)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(contact.description)

    def select_status_value_in_list(self, status):
        wd = self.app.wd
        if status is not None:
            wd.find_element_by_name("status").click()
            if status == "development":
                wd.find_element_by_xpath("//option[@value='10']").click()
            if status == "release":
                wd.find_element_by_xpath("//option[@value='30']").click()
            if status == "stable":
                wd.find_element_by_xpath("//option[@value='50']").click()
            if status == "obsolete":
                wd.find_element_by_xpath("//option[@value='70']").click()

    def select_view_state_value_in_list(self, view_state):
        wd = self.app.wd
        if view_state is not None:
            wd.find_element_by_name("view_state").click()
            if view_state == "public":
                wd.find_element_by_xpath("(//option[@value='10'])[2]").click()
            if view_state == "private":
                wd.find_element_by_xpath("(//option[@value='50'])[2]").click()

    def get_project_names_list(self):
        wd = self.app.wd
        self.open_projects_page()
        project_names = []
        for element in wd.find_elements_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=')]"):
                project_names.append(element.text)
        return project_names

    def random_project_name(self, prefix, maxlen):
        symbols = string.ascii_letters + string.digits + string.punctuation + " " * 5
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


