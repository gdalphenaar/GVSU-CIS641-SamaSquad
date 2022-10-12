## Meeting minutes

Team name: Sama Squad

Members present: Grant Alphenaar (GA)

Date: Sunday, Oct. 9, 2022

Time: Around the hour of 7pm, accompanied by curry and wine

Discussion points:

* How to handle web dashboard alerts - desktop notifications?
    * Probably can't really do mobile push notifications since it'll be a browser app on the local network
    * Probably don't want to mess with setting up email notifications either
* Web dashboard tech stack?
    * Major limitation: will need to be able to run on an Raspberry Pi that's also managing the sensor and analyzing data (i.e., relatively low performance specs)
* Data storage?
    * Small database (maybe mongodb or sqlite?) vs something like pandas / numpy / something similar with scheduled backups

Goals for next week (include responsibilities):

* Look into / play around with desktop notifications from browser (responsibility: GA)
* Keep working through sensor tutorials (responsibility: GA)
* Start working on simulated data for web-side development (responsibility: GA)