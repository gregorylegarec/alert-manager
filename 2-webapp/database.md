# Database

Our database may be a relational Database or a NoSQL database. It does not matter much at this time and the definitive choice should be made when knowing more about the constraints we will face to.

All we should know is that our database must store two kinds of data or documents :

- Alerts
- Files informations

Alerts must be, if possible, indexed on almost every attributes, as filters should be available for every one of them (`category`, `score`, `data`, `status`, `client` and `summary`).
