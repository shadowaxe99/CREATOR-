from data_detective import DataDetective


class ProjectPilot:
    def __init__(self):
        self.projects = []

    def start_project(self, title, description):
        project = Project(title, description)
        self.projects.append(project)

    def add_task(self, project_index, task_name):
        project = self.projects[project_index]
        project.add_task(task_name)

    def complete_task(self, project_index, task_index):
        project = self.projects[project_index]
        project.complete_task(task_index)

    def get_project_status(self, project_index):
        project = self.projects[project_index]
        return project.get_status()

    def save_project(self, project_index, file_path):
        project = self.projects[project_index]
        project.save(file_path)


class Project:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.tasks = []

    def add_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)

    def complete_task(self, task_index):
        task = self.tasks[task_index]
        task.complete()

    def get_status(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(task.completed for task in self.tasks)
        progress = completed_tasks / total_tasks if total_tasks > 0 else 0
        return {
            'title': self.title,
            'description': self.description,
            'progress': progress,
            'completed_tasks': completed_tasks,
            'total_tasks': total_tasks
        }

    def save(self, file_path):
        # Save project details to a file
        pass


class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def complete(self):
        self.completed = True
