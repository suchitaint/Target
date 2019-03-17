# Target

In our production environment, we don’t allow developers to SSH into servers
without VP approval. Therefore, it is critical that our team provide tools to allow
developers to debug problems using our monitoring tools.
For example, when we get an alert that a disk is getting full, you would want to
know what files are using up all of the space.
Write a program in a language of your choice which will take a mount point as an
argument and return a list of all the files on the mountpoint and their disk usage in
bytes in json format.
Eg

getdiskusage.py /tmp
{
"files":
[
{"/tmp/foo", 1000},
{"/tmp/bar", 1000000},
{"/tmp/buzzz", 42},
],
}
