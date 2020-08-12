from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app
        self.username = "administrator"
        self.password = "root"
        self.soap_url = "http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl"

    def can_login(self):
        client = Client(self.soap_url)
        try:
            client.service.mc_login(self.username, self.password)
            return True
        except WebFault:
            return False

    def get_projects_list(self):
         client = Client(self.soap_url)
         try:
              soap_result = client.service.mc_projects_get_user_accessible(self.username, self.password)
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