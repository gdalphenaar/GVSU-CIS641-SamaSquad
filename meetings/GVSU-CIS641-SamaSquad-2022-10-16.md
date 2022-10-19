## Meeting minutes

Team name: Sama Squad

Members present: Grant Alphenaar (GA)

Date: Sunday, Oct. 16, 2022

Time: 3PM-ish

Discussion points:

* Straight browser notifications (aka, ability to show notification even when site is not accessed) *might* not work
    * But might be able to enable something when the page is active, at least
    * Didn't get a chance to do any of the demos yet, but I did find a couple
    * Look more into "web push" implementation

* Data front: will need to deal with memory issues - Raspberry Pi doesn't have a ton of memory, so will likely need to periodically save to disk and load current chunk(s)
    * Will need to get further along to see what memory usage looks like, but maybe save in chunks of the latest week? (or at least latest day)
    * Can at least simulate/test some of this aspect as well - probably won't need to be super realistic data

* On the notification front: even of super fancy notifications aren't possible, it's definitely possible to log periods out of the normal ranges
    * Can probably add some kind of ***urgent*** flag the next time the user visits

* Pushed first pass of requirements - ended up "discovering" several additional requirements (and/or simplifying/clarifying existing ones)

Goals for next week (include responsibilities):

* Start working on web interface - can be done in parallel with the rest of the project and refined/tweaked as things get more fleshed out (responsibility: GA)
* Keep working through through sensor tutorials (responsibility: GA)
