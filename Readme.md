Sight Reduction Problems
========================

Generates data that can be used to practice calculating sun sight
reductions in celestial navigation.

Usage:

    ./sight.py

Broadly, for each sight, the program generates a sextant reading,
date/time, and approximate (dead reckoning) position. Three sextant
readings a certain length of time apart will allow the navigator to
find a more precise position than the dead reckoning positions. Most
existing celestial navigation software will easily interpret sextant
readings into a position, but few, if any, software packages will
generate sensible random positions, times, etc. to permit students of
navigation to practice doing the calculations themselves.

**Example output starts here:**



    Guessing new parameters...
    Guessing new parameters...
    Guessing new parameters...
    Guessing new parameters...
    Guessing new parameters...

Fix number 1
========

Problem
--------
* Hs 55:33:36.1
* IE 0:02:33.3 on the arc. Eye 8.3 meters. Sun UL.
* 2016/1/21 14:41:21 UTC
* Dead reckoning position -54:33:30.2 -38:47:56.6

Solution
--------
* Ha 55:25:58.9
* Ho 55:09:09.0
* GHA 37:32:18.5 / Dec -19:56:12.9
* Ass Long -37:32:18.5
* LHA 360:00:00.0
* calculating at AP -54:00:00.0 -37:32:18.5
* Hc 55:56:00.7 / Z 359:59:51.1
* Intercept 0:46:51.7 Away from Gp
* LOP thru -54:46:51.7 -37:32:18.3 in the 269:59:51.1 89:59:51.1 direction
* Z from x to secret 270:40:13.6

Problem
--------
* Hs 54:28:52.7
* IE 0:02:33.3 on the arc. Eye 8.3 meters. Sun UL.
* 2016/1/21 15:34:30 UTC
* Dead reckoning position -54:41:40.7 -39:07:00.8

Solution
--------
* Ha 54:21:15.5
* Ho 54:04:24.2
* GHA 50:49:25.2 / Dec -19:55:43.8
* Ass Long -38:49:25.2
* LHA 12:00:00.0
* calculating at AP -54:00:00.0 -38:49:25.2
* Hc 54:42:32.8 / Z 340:13:19.1
* Intercept 0:38:08.6 Away from Gp
* LOP thru -54:35:51.6 -38:27:08.4 in the 250:13:19.1 70:13:19.1 direction
* Z from x to secret 250:16:24.1

Problem
--------
* Hs 50:27:08.6
* IE 0:02:33.3 on the arc. Eye 8.3 meters. Sun UL.
* 2016/1/21 16:32:00 UTC
* Dead reckoning position -54:49:34.6 -39:15:07.2

Solution
--------
* Ha 50:19:31.4
* Ho 50:02:34.1
* GHA 65:11:46.6 / Dec -19:55:12.2
* Ass Long -38:11:46.6
* LHA 27:00:00.0
* calculating at AP -54:00:00.0 -38:11:46.6
* Hc 50:10:22.7 / Z 318:12:15.7
* Intercept 0:07:48.6 Away from Gp
* LOP thru -54:05:49.0 -38:02:54.0 in the 228:12:15.7 48:12:15.7 direction
* Z from x to secret 228:42:48.2



Fix number 2
========

Problem
--------
* Hs 58:02:15.2
* IE 0:01:22.3 on the arc. Eye 14.0 meters. Sun UL.
* 2016/4/23 14:44:23 UTC
* Dead reckoning position -19:24:12.6 -42:21:21.3

Solution
--------
* Ha 57:54:18.2
* Ho 57:37:52.5
* GHA 401:32:29.3 / Dec 12:48:15.3
* Ass Long -41:32:29.3
* LHA 360:00:00.0
* calculating at AP -19:00:00.0 -41:32:29.3
* Hc 58:11:35.0 / Z 359:59:51.3
* Intercept 0:33:42.5 Away from Gp
* LOP thru -19:33:42.5 -41:32:29.2 in the 269:59:51.3 89:59:51.3 direction
* Z from x to secret 270:56:20.2

Problem
--------
* Hs 55:02:00.9
* IE 0:01:22.3 on the arc. Eye 14.0 meters. Sun UL.
* 2016/4/23 15:46:47 UTC
* Dead reckoning position -19:57:28.1 -42:20:43.5

Solution
--------
* Ha 54:54:03.9
* Ho 54:37:34.2
* GHA 417:08:37.2 / Dec 12:49:07.0
* Ass Long -41:08:37.2
* LHA 16:00:00.0
* calculating at AP -19:00:00.0 -41:08:37.2
* Hc 54:29:10.4 / Z 332:26:14.9
* Intercept 0:08:23.8 Toward Gp
* LOP thru -18:52:33.3 -41:12:43.6 in the 242:26:14.9 62:26:14.9 direction
* Z from x to secret 243:36:41.1

Problem
--------
* Hs 47:22:54.2
* IE 0:01:22.3 on the arc. Eye 14.0 meters. Sun UL.
* 2016/4/23 16:43:46 UTC
* Dead reckoning position -19:44:01.4 -42:14:14.7

Solution
--------
* Ha 47:14:57.3
* Ho 46:58:15.8
* GHA 71:23:30.2 / Dec 12:49:54.1
* Ass Long -41:23:30.2
* LHA 30:00:00.0
* calculating at AP -19:00:00.0 -41:23:30.2
* Hc 46:33:23.6 / Z 314:50:47.7
* Intercept 0:24:52.2 Toward Gp
* LOP thru -18:42:26.7 -41:42:07.2 in the 224:50:47.7 44:50:47.7 direction
* Z from x to secret 225:39:49.8
