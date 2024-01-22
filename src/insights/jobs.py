from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, file_path) -> List[Dict]:
        with open(file_path, encoding="utf8") as file:
            data = csv.DictReader(file)
            for row in data:
                self.jobs_list.append(row)

    def get_unique_job_types(self) -> List[str]:
        job_types = set()
        for job in self.jobs_list:
            job_types.add(job['job_type'])
        return list(job_types)

    def filter_by_multiple_criteria(self, jobs, infos) -> List[dict]:
        jobs_filter = []
        for job in jobs:
            if (job['industry'] == infos['industry'] and
                    job['job_type'] == infos['job_type']):
                jobs_filter.append(job)
        return list(jobs_filter)
