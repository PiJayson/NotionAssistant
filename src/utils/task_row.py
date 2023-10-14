class TaskRow():
    
    def __init__(self,
                 task_name = None,
                 status = None,
                 assignee = None,
                 due = None,
                 priority = None,
                 tags = None,
                 project = None):
        self.task_name = task_name
        self.status = status
        self.assignee = assignee
        self.due = due
        self.priority = priority
        self.tags = tags
        self.project = project
        
    def get_task_name(self):
        return self.task_name
    
    def get_status(self):
        return self.status

    def get_assignee(self):
        return self.assignee

    def get_due_date(self):
        return self.due

    def get_priority(self):
        return self.priority

    def get_tags(self):
        return self.tags

    def get_project(self):
        return self.project
    
    
    def print(self):
        print(self.task_name, self.status, self.assignee, self.due, self.priority, self.tags, self.project)