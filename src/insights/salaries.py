from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary = 0
        for job in self.jobs_list:
            salary = job.get('max_salary')
            if salary and isinstance(salary, str) and salary.isdigit():
                salary = int(salary)
                if salary > max_salary:
                    max_salary = salary
        return max_salary

    def get_min_salary(self) -> int:
        min_salary = float('inf')
        for job in self.jobs_list:
            salary = job.get('min_salary')
            if salary and isinstance(salary, str) and salary.isdigit():
                salary = int(salary)
                if salary < min_salary:
                    min_salary = salary
        return min_salary

    def matches_salary_range(self, job: Dict, salary: Union[str, int]) -> bool:
        try:
            max = int(job['max_salary'])
            min = int(job['min_salary'])

            self._validate_salaries(max, min)
            if min > max or min == '' or max == '':
                raise ValueError()

            # max = int(max)
            # min = int(min)
            if not isinstance(salary, (str, int)):
                raise ValueError()
            return min <= int(salary) <= max
        except (ValueError, TypeError, KeyError):
            raise ValueError()

    def _validate_salaries(self, max_salary, min_salary):
        if max_salary is None or min_salary is None:
            raise ValueError()

        if not (isinstance(max_salary, (str, int))
                and isinstance(min_salary, (str, int))):
            raise ValueError()

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        filter_jobs = []
        for job in jobs:
            try:
                if self.matches_salary_range(job, salary):
                    filter_jobs.append(job)
            except ValueError:
                pass
        return filter_jobs
