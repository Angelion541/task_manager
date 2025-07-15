#models.py

from datetime import datetime

class Task:
    """
    Represents a task with a title, optional description, deadline, and completion status.
    Attributes:
        title (str): The title of the task.
        description (str): A detailed description of the task (default is an empty string).
        deadline (Any): The deadline for the task (default is None).
        done (bool): Indicates whether the task is completed (default is False).
    Methods:
        mark_done():
            Marks the task as completed by setting 'done' to True.
        to_dict():
            Serializes the task instance to a dictionary.
        from_dict(data):
            Creates a Task instance from a dictionary.
    """
    def __init__(self, title, description='', deadline=None, done=False):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.done = done

    def mark_done(self):
        """
        Marks the task as completed by setting the 'done' attribute to True.
        """
        self.done = True

    def to_dict(self):
        """
        Converts the model instance into a dictionary representation.

        Returns:
            dict: A dictionary containing the 'title', 'description', 'deadline', and 'done' attributes of the instance.
        """
        return {
            'title': self.title,
            'description': self.description,
            'deadline': self.deadline,
            'done': self.done
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates an instance of the class from a dictionary.

        Args:
            data (dict): A dictionary containing the keys 'title', and optionally 'description', 'deadline', and 'done'.

        Returns:
            cls: An instance of the class initialized with values from the dictionary.

        Raises:
            KeyError: If 'title' is not present in the data dictionary.
        """
        return cls(
            title=data['title'],
            description = data.get('description', ''),
            deadline = data.get('deadline'),
            done = data.get('done')
        )
