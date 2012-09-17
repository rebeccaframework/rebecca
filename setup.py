from setuptools import setup, find_packages

requires = [
    "pyramid",
    "sqlalchemy",
    "zope.sqlalchemy",
    "psycopg2",
    "pyramid_tm",
    "webhelpers",
    "deform",
    "deform_bootstrap",
]

tests_require = [
]

docs_require = [
    'sphinx',
    'repoze.sphinx.autointerface',
]

setup(name="rebecca",
      test_suite="rebecca",
      install_requires=requires,
      tests_require=tests_require,
      extras_require={
        "testing": tests_require,
        "docs": docs_require,
        },
      )
