import os

build = os.getenv("BUILD_NUMBER")
commit = os.getenv("GIT_COMMIT")
branch = os.getenv("BRANCH_NAME")

print(build)
print(commit)
print(branch)