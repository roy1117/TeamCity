import scriptengine
import os

tempdir = os.path.dirname(os.path.realpath(__file__))
project = svn.checkout(url=r'https://sekreappche012/svn/CheonanSoftware/ReGISMk3/RegisAbingdonPLC/trunk', project_path=tempdir, project_name='test project')
