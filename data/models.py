from testrail import *
class Models:
    client = APIClient('https://sungevity.testrail.net')
    def getProjects(self):
        projects = self.client.send_get('get_projects')
        #return json.dumps(projects)
        return projects
    def getRuns(self,projId):
        runs = self.client.send_get('get_runs/'+`projId`)
        return runs

    def getResultsForRun(self, runId):
            runs = self.client.send_get('get_results_for_run/' + `runId`)
            return runs

    def getMilestonesForProject(self,projId):
        milestones=self.client.send_get('get_milestones/'+`projId`+'&is_completed=0')
        return milestones


