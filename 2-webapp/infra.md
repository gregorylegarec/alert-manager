# Infrastructure

We assume here that a system creating alerts and copying files into the file system already both exist.

Our Alert Monitor's infrastructure needs to handle three concerns :

- Web server
- Database
- File server

Separating those concerns will allow us better scalability if needed in the future.

## Web server

Our web server's role is to connect to the database and expose our [API](api.md).

## Database

Our database need to store two kind of data : alerts and file informations.
We want to store were to find files on the File server as well.

## File server

The file server provides access to binary files. It could maintain a really simple index of files. Information about those index must be transmitted to the database at some point, when creating an alert for example.
