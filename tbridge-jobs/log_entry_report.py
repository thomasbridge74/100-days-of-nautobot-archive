from nautobot.apps.jobs import Job, register_jobs
from nautobot.extras.models import JobLogEntry


class ReportInfoLogEntries(Job):
    class Meta:
        name = "Delete Information Level Log Entries"
        description = "A job to delete all information level log entries."

    def run(self):
        # Filter for information level log entries
        info_log_entries = JobLogEntry.objects.filter(log_level="info")

        # Log the number of entries to be deleted
        info_entries_count = info_log_entries.count()
        self.logger.debug(f"Found {info_entries_count} information level log entries")

        report = {}
        for entry in info_log_entries:
            if entry.job_result.name not in report:
                report[entry.job_result.name] = 0
            report[entry.job_result.name] += 1

        for job_name, log_count in report.items():
            self.logger.debug(f"Job: {job_name} has {log_count} info entries")

register_jobs(
    ReportInfoLogEntries,
)