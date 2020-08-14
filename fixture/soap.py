from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    soap_url = "api/soap/mantisconnect.php?wsdl"

    def __init__(self, app):
        self.app = app

    def can_login(self):
        client = Client(self.app.base_url + self.soap_url)
        try:
            client.service.mc_login(self.app.login, self.app.password)
            return True
        except WebFault:
            return False

    def get_projects_list(self):
         client = Client(self.app.base_url + self.soap_url)
         try:
              soap_result = client.service.mc_projects_get_user_accessible(self.app.login, self.app.password)
              projects = []
              for rec in soap_result:
                   id = rec.id
                   name = rec.name
                   status = rec.status
                   view_state = rec.view_state
                   enabled = rec.enabled
                   description = rec.description
                   projects.append(Project(id=id, name=name, status=status, view_state=view_state,
                                           enabled=enabled, description=description))
              return projects
         except WebFault:
              return False