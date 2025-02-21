from nautobot.apps.jobs import Job, register_jobs, StringVar

# new
name = "Hello World Nautobot Jobs"

class HelloJobs(Job):

    # new
    class Meta:
        name = "Hello Jobs"
        description = "Demonstration for Day 4 of 100 Days of Nautobot"

    def run(self):
        self.logger.debug("This is the debug message from Day 3 of 100 Days of Nautobot")


class HelloJobsWithInputs(Job):

    username = StringVar()
    # new
    class Meta:
        name = "Hello Jobs with Input"
        description = "Inputs demonstration for Day 4 of 100 Days of Nautobot"

    def run(self, username):
        self.logger.info(f"Hello Jobs with {username}")


class HelloJobsWithLogs(Job):

    # new
    class Meta:
        name = "Hello Jobs with Logs"
        description = "Demonstration of logging for Day 4 of 100 Days of Nautobot"

    def run(self):
        self.logger.debug("This is the debug message from Day 3 of 100 Days of Nautobot")
        self.logger.info("This is an info message")
        self.logger.warning("This is a warning message")
        self.logger.error("This is an error message")
        self.logger.critical("This is a critical message")    
    
register_jobs(
    HelloJobs,
    HelloJobsWithLogs,
    HelloJobsWithInputs,
)