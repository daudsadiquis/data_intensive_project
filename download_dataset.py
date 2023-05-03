import wget
import shutil

# Define the remote file to retrieve
remote_url = 'http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip'
# Define the local filename to save data
local_file = 'dataset.zip'
# Make http request for remote file data
wget.download(remote_url, local_file)

# unzip dataset
shutil.unpack_archive("dataset.zip", ".")
