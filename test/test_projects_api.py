# coding: utf-8

"""
    Patch API V1

    The core API used to integrate with Patch's service  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: developers@usepatch.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import os

from patch_api.api_client import ApiClient


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self):
        api_client = ApiClient(api_key=os.environ.get("SANDBOX_API_KEY"))
        self.api = api_client.projects  # noqa: E501

    def tearDown(self):
        self.api = None

    def test_retrieve_project(self):
        """Test case for retrieve_project

        Retrieves a project  # noqa: E501
        """
        project_id = "pro_test_2b67b11a030b66e0a6dd61a56b49079a"
        project = self.api.retrieve_project(id=project_id).data
        self.assertTrue(project)
        self.assertEqual(project.production, False)
        self.assertTrue(isinstance(project.photos, list))

        self.assertTrue(hasattr(project, "tagline"))
        self.assertTrue(hasattr(project, "latitude"))
        self.assertTrue(hasattr(project, "longitude"))
        self.assertTrue(hasattr(project, "highlights"))

        self.assertTrue(isinstance(project.mechanism, str))
        self.assertTrue(isinstance(project.state, str))

        technology_type = project.technology_type
        self.assertTrue(isinstance(technology_type.name, str))
        self.assertTrue(isinstance(technology_type.slug, str))

        parent_technology_type = technology_type.parent_technology_type
        self.assertTrue(isinstance(parent_technology_type.name, str))
        self.assertTrue(isinstance(parent_technology_type.slug, str))

        inventory = project.inventory
        self.assertTrue(isinstance(inventory, list))
        self.assertTrue(isinstance(inventory[0].vintage_year, int))
        self.assertTrue(isinstance(inventory[0].vintage_start_year, int))
        self.assertTrue(isinstance(inventory[0].vintage_end_year, int))
        self.assertTrue(isinstance(inventory[0].amount_available, int))
        self.assertTrue(isinstance(inventory[0].price, int))
        self.assertTrue(isinstance(inventory[0].currency, str))
        self.assertTrue(isinstance(inventory[0].unit, str))

        issuance_type = project.issuance_type
        self.assertTrue(isinstance(issuance_type, str))

        disclaimers = project.disclaimers
        self.assertTrue(isinstance(disclaimers, list))
        self.assertTrue(isinstance(disclaimers[0].header, str))
        self.assertTrue(isinstance(disclaimers[0].body, str))
        self.assertTrue(isinstance(disclaimers[0].severity, str))
        self.assertTrue(isinstance(disclaimers[0].link_text, str))
        self.assertTrue(isinstance(disclaimers[0].link_destination, str))

    def test_retrieve_project_language(self):
        """Test case for retrieve_project

        Retrieves a project  # noqa: E501
        """
        project_id = "pro_test_2b67b11a030b66e0a6dd61a56b49079a"
        project = self.api.retrieve_project(id=project_id, accept_language="fr").data
        self.assertIn("Démo", project.name)  # French

    def test_retrieve_projects(self):
        """Test case for retrieve_projects

        Retrieves a list of projects  # noqa: E501
        """
        projects = self.api.retrieve_projects().data
        self.assertTrue(isinstance(projects, list))

        if len(projects) > 0:
            project = projects[0]

            self.assertEqual(project.production, False)
            self.assertIsInstance(project.standard, object)
            self.assertIsInstance(project.name, str)
            self.assertTrue(project.description)
            self.assertIsInstance(project.country, str)
            self.assertIsInstance(project.project_partner, str)
            self.assertIsInstance(project.photos, list)

    def test_retrieve_biomass_projects(self):
        """Test case for retrieve_projects with a type filter

        Retrieves a list of projects  # noqa: E501
        """
        project_type = "biomass"
        projects = self.api.retrieve_projects(type=project_type).data
        self.assertTrue(isinstance(projects, list))

        for project in projects:
            self.assertEqual(project.technology_type.slug, project_type)

    def test_retrieve_american_projects(self):
        """Test case for retrieve_projects with a country filter

        Retrieves a list of projects  # noqa: E501
        """
        project_country = "US"
        projects = self.api.retrieve_projects(country=project_country).data
        self.assertTrue(isinstance(projects, list))

        for project in projects:
            self.assertEqual(project.country, project_country)

    def test_retrieve_projects_with_more_than_100_grams_of_inventory(self):
        """Test case for retrieve_projects with a country filter

        Retrieves a list of projects  # noqa: E501
        """
        minimum_available_mass = 100
        projects = self.api.retrieve_projects(
            minimum_available_mass=minimum_available_mass
        ).data
        self.assertTrue(isinstance(projects, list))

        for project in projects:
            remaining_amount = sum(inv.amount_available for inv in project.inventory)
            self.assertTrue(remaining_amount >= minimum_available_mass)

    def test_retrieve_projects_language(self):
        """Test case for retrieve_projects with a type filter

        Retrieves a list of projects  # noqa: E501
        """
        projects = self.api.retrieve_projects(accept_language="fr").data

        for project in projects:
            self.assertIn("Démo", project.name)  # French


if __name__ == "__main__":
    unittest.main()
