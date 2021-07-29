You will need to pull down this repository, as it contains the CSV necessary to run challenge 1 as well as the requirements.txt.

You can make the virtual environment in this repository itself or wherever you store your virtual environments.
Once made, come into this repository and do a "pip install -r requirements.txt" for the dependency packages.

To avoid uploading this challenge as a public pip package, you'll need to install the package in your virtual environment.
To do so use this project as your active directory and run "python setup.py install" as setuptools is usually included by default.
If not, then you will need to pip install setuptools.

Once that has finished, you can then run the scripts as console commands(ex. challenge-1).


challenge-1 will require you to be in a directory that has the challengeCSV directory and Appeals_Filed_In_2017.csv file in that directory.
The repository has this by default, but if you were wanting to run this command anywhere else, you could copy the directory elsewhere.

challenge-4 will generate the CSV in the current directory you are calling it from.
challenge-5 will generate the html in the current directory you are calling it from.