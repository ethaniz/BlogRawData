Title: git push -- matching or simple
Date: 2015-6-15 16:38:00
Modified: 2015-6-15
Tags: git
Authur: Ethaniz

不带任何参数的git push，默认只推送当前分支，这叫做simple方式。此外，还有一种matching方式，会推送所有有对应的远程分支的本地分支。Git 2.0版本之前，默认采用matching方法，现在改为默认采用simple方式。如果要修改这个设置，可以采用git config命令。
>`$ git config --global push.default matching`

或者

>`$ git config --global push.default simple`

还有一种情况，就是不管是否存在对应的远程分支，将本地的所有分支都推送到远程主机，这时需要使用–all选项。

>`$ git push --all origin`

上面命令表示，将所有本地分支都推送到origin主机。