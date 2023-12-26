#Some basic Git commands are:
```
//Git Configuration
git config --global user.name "usname"
git config --global user.email johndoe@example.com


git status                          //check status of your current git project on desktop
git commit -am                      //commit changes and ready to push
git checkout -b branchname          //create branch
git push origin branchname          //pushing changes to your branch
git push origin master              //pushing changes to origin master

git branch checkout branchname      //switch branch
git branch -a                       //check all branches on computer


git fetch --all                     //downloads content from the repository without merge
git merge branchname                //integrate changes from another branch
git pull origin branchname          //git pull does a git fetch followed by a git merge

//---------- Update your branch with master ---------
git checkout branchname
git pull origin master
//---------------------------------------------------

git checkout .                      //revert all changes to your working copy

git fetch --all                     //get data
git reset --hard origin/master      //Erase your changes and pulls from master
git reset --hard origin/branchname  //Erase your changes and pulls from branch

git revert <commit 1> <commit 2>    //If you want to revert a change that you have committed,

git add .                           //adds all modified and new files to current directory

//Erase your local changes and pull from master
git reset --hard 
git pull origin/master

```
*** `pull` is designed around merging changes together in some way, whereas `reset` is designed around simply making your local copy match a specific commit.***
