from setuptools import setup, find_packages


def get_requirements(file_path):
    requirements = []
    with open(file_path) as f:
        requirements = f.read().splitlines()
        if "-e ." in requirements:
            requirements.remove("-e .")
        requirements = [req for req in requirements if not req.startswith("#")]
        requirements = [req.replace("/n", "") for req in requirements]
    return requirements


setup(
    name="my_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    entry_points={
        "console_scripts": [
            "my_command=my_package.module:main_function",
        ],
    },
    author="sai",
    author_email="sai@gmail.com",
)