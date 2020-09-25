from setuptools import setup, find_packages


with open("README.md", "r") as f:
    long_desc = f.read()

setup(
    name="shopalone",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "geoalchemy2",
        "flask",
        "matplotlib",
        "numpy",
        "psycopg2-binary",
        "python-dateutil",
        "shapely"
    ],
    extras_require={"server": ["gunicorn"]},
    description="",
    long_description=long_desc,
    long_description_mime_type="text/markdown",
    url="https://github.com/jvytee/shopalone",
    author="Julian Theis",
    author_email="jvytee@posteo.org"
)
