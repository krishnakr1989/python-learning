import shutil

#Backup the current application before deployment.
shutil.copytree(
    "application",
    "backup/application"
)