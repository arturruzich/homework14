from homework_16.employee import TeamLead
from assertpy import assert_that


class TestEmployee:
    qa_automation_team_lead: TeamLead = TeamLead("Artur", salary=5000, department="Best Test", team_size=5)

    expected_mark_attrs: dict[str, object] = {
        "name": "Artur",
        "salary": 5000,
        "department": "Best test",
        "team_size": 5
    }

    expected_failed_mark_attrs: dict[str, object] = {
        "name": "Artur",
        "salary": 5000,
        "department": "Best test",
        "team_size": 6
    }

    def test_employee_attrs(self):
        print(self.qa_automation_team_lead.__dict__)

        (assert_that(self.qa_automation_team_lead.__dict__,
                     description="Desired user's attrs are nor equal to desired dict of attributes").
         is_equal_to(self.expected_mark_attrs))

    def test_employee_negative_attrs(self):
        (assert_that(self.qa_automation_team_lead.__dict__,
                     description="Desired user's attrs are nor equal to desired dict of attributes").
         is_equal_to(self.expected_failed_mark_attrs))
