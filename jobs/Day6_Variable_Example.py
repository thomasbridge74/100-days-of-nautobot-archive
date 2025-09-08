from nautobot.apps.jobs import MultiChoiceVar, Job, ObjectVar, register_jobs, TextVar, IntegerVar
from nautobot.dcim.models.locations import Location


name = "Day 6 Variables"

class HelloVariables(Job):

    CHOICES = (
        ('h', 'Happy'),
        ('s', 'Sad'),
        ('e', 'Excited')
    )
    feelings = MultiChoiceVar(choices=CHOICES)
    message = TextVar() 
    days = IntegerVar(
        default="10"
    )
    location = ObjectVar(model=Location)

    class Meta:

        name = "Hello Variables"
        description = "Jobs Variable Examples"

    def run(self, message,  days, feelings, location):
        self.logger.info(f"Please give the message: {message} in {days} days.")
        self.logger.info(f"I am feeling {feelings}")
        self.logger.info(f"Location: {location}")

register_jobs(
    HelloVariables,
)