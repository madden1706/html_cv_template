## HTML CV -> .pdf CV

This is a Docker container that builds a pdf CV from a HTLM and CSS input by a simple Python scipt.

### Getting the code from GitHub

To clone this git repository from GitHub run:

```
git clone https://github.com/madden1706/html_cv_template.git
```

This command will clone the files into a directory called 'html_cv_template'.

### Using git branches for CV versions

git branches could be used for different CV versions.

To create a branch for a new CV version (new_job_branch) use:

```
# run this on the branch you want to use as the source branch
git branch new_job_branch
# list branches
git branch --list
# change branches : git checkout [branch_name]
git checkout new_job_branch
```

When files have been altered on the new branch you'll need to commit (any maybe add there are new files git is not trackign changes for) them:

```
git add path/to/file.txt
git commit path/to/file.txt -m "Message for the commit for what you have done."

# Show a log of commits
git log

# git log output
commit 12becc203e88d6b5b6920825180fd3919bcbb230 (HEAD -> master)
Author: Ross Madden <madden1706@gmail.com>
Date:   Mon Oct 11 20:33:24 2021 +0100

    Added details about git.

commit 3b83cb1e2b1544e396f97e85ec178f25b2d7e2e9 (origin/master)
Author: Ross Madden <madden1706@gmail.com>
Date:   Mon Oct 11 20:27:01 2021 +0100

    Initial commit of README.

# To checkout a specific commit
git checkout 3b83cb1e2b1544e396f97e85ec178f25b2d7e2e9
git checkout new_job_branch
```

This repository can be pushed to a remote repo e.g. GitHub. 

### Building the Docker container

To use build a container from the image with:

```shell
docker build -t cv_maker ~/Desktop/html_cv/cv/. 
```

where 'cv_maker' is tagged as the name of the container. Change the path to the Dockerfile as needed.

### Making the pdf CV

The file 'cv.html' in the html_css folder can be opened in a web browser (drag and dropping should open the file) to view changes (just reload the page to view them).

To generate a pdf from the CV html and CSS files run:

```shell 
# '~/Desktop/html_cv/cv/cv_maker' - this directory will need to be the correct path to the files on your machine
docker run  -v ~/Desktop/html_cv/cv/cv_maker:/home/maker/cv_maker cv_maker
```

The command mounts the 'cv_maker' directory in the container. The naming of the files is important, they should not be changed.

The output files are added to the directory './cv/cv_maker/outputs/'. The date and time are the prefix to the file name for one file. The file 'cv.pdf' is always the most recent version.

