"""
    Patch API V1

    The core API used to integrate with Patch's service  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: engineering@usepatch.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "patch-api"
VERSION = "1.22.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "urllib3 >= 1.25.3",
    "python-dateutil",
    "certifi",
]

setup(
    name=NAME,
    version=VERSION,
    description="Patch API V1",
    author="Developer Support",
    author_email="engineering@usepatch.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Patch API V1"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    The core API used to integrate with Patch&#39;s service  # noqa: E501
    """,
)
