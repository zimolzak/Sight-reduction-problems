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



Fix number 1
========

Problem
--------
* Hs 57:11:42.8
* IE 0:00:58.5 on the arc. Eye 6.7 meters. Sun LL.
* 2016/5/23 14:25:42 UTC
* Dead reckoning position 46:50:23.9 -13:04:59.4

Solution
--------
* Ha 57:06:11.2
* Ho 57:21:26.4
* GHA 37:13:47.5 / Dec 20:43:43.9
* Ass Long -12:13:47.5
* LHA 25:00:00.0
* calculating at AP 46:00:00.0 -12:13:47.5
* Hc 57:30:09.9 / Z 227:22:16.8
* Intercept 0:08:43.5 Away from Gp
* LOP thru 46:05:54.2 -12:04:32.0 in the 137:22:16.8 317:22:16.8 direction
* Z from x to secret 316:58:52.3
* True coords 46:33:29.9 -12:42:07.3

Problem
--------
* Hs 49:01:29.6
* IE 0:00:58.5 on the arc. Eye 6.7 meters. Sun LL.
* 2016/5/23 15:23:58 UTC
* Dead reckoning position 46:43:28.9 -13:12:37.8

Solution
--------
* Ha 48:55:58.0
* Ho 49:11:01.3
* GHA 51:47:38.5 / Dec 20:44:11.4
* Ass Long -12:47:38.5
* LHA 39:00:00.0
* calculating at AP 46:00:00.0 -12:47:38.5
* Hc 49:25:31.3 / Z 244:48:35.1
* Intercept 0:14:30.1 Away from Gp
* LOP thru 46:06:08.8 -12:28:43.0 in the 154:48:35.1 334:48:35.1 direction
* Z from x to secret 334:46:31.8
* True coords 46:29:05.7 -12:44:25.8

Problem
--------
* Hs 39:06:44.8
* IE 0:00:58.5 on the arc. Eye 6.7 meters. Sun LL.
* 2016/5/23 16:25:00 UTC
* Dead reckoning position 46:14:54.4 -13:01:40.5

Solution
--------
* Ha 39:01:13.3
* Ho 39:15:56.7
* GHA 67:03:06.6 / Dec 20:44:40.1
* Ass Long -12:03:06.6
* LHA 55:00:00.0
* calculating at AP 46:00:00.0 -12:03:06.6
* Hc 38:51:24.6 / Z 259:39:33.2
* Intercept 0:24:32.0 Toward Gp
* LOP thru 45:55:30.5 -12:37:48.4 in the 169:39:33.2 349:39:33.2 direction
* Z from x to secret 349:00:53.5
* True coords 46:25:57.7 -12:46:23.1


    Guessing new parameters...

Fix number 2
========

Problem
--------
* Hs 63:45:10.1
* IE 0:00:04.7 off the arc. Eye 5.2 meters. Sun LL.
* 2016/9/27 14:08:51 UTC
* Dead reckoning position 7:09:36.3 -9:58:18.1

Solution
--------
* Ha 63:41:14.3
* Ho 63:56:47.3
* GHA 34:31:02.8 / Dec -1:56:43.2
* Ass Long -8:31:02.8
* LHA 26:00:00.0
* calculating at AP 7:00:00.0 -8:31:02.8
* Hc 62:33:06.6 / Z 251:54:31.1
* Intercept 1:23:40.6 Toward Gp
* LOP thru 6:33:54.3 -9:51:06.7 in the 161:54:31.1 341:54:31.1 direction
* Z from x to secret 340:57:18.7
* True coords 7:17:55.7 -10:06:26.0

Problem
--------
* Hs 49:28:43.9
* IE 0:00:04.7 off the arc. Eye 5.2 meters. Sun LL.
* 2016/9/27 15:08:39 UTC
* Dead reckoning position 7:36:51.2 -10:16:04.3

Solution
--------
* Ha 49:24:48.0
* Ho 49:40:02.0
* GHA 49:28:11.9 / Dec -1:57:41.4
* Ass Long -9:28:11.9
* LHA 40:00:00.0
* calculating at AP 7:00:00.0 -9:28:11.9
* Hc 49:05:09.0 / Z 258:47:47.8
* Intercept 0:34:53.0 Toward Gp
* LOP thru 6:53:12.1 -10:02:39.9 in the 168:47:47.8 348:47:47.8 direction
* Z from x to secret 348:30:14.3
* True coords 7:13:58.8 -10:06:55.5

Problem
--------
* Hs 35:32:58.4
* IE 0:00:04.7 off the arc. Eye 5.2 meters. Sun LL.
* 2016/9/27 16:05:40 UTC
* Dead reckoning position 6:55:35.0 -10:11:58.5

Solution
--------
* Ha 35:29:02.6
* Ho 35:43:46.5
* GHA 63:43:40.1 / Dec -1:58:36.9
* Ass Long -9:43:40.1
* LHA 54:00:00.0
* calculating at AP 6:00:00.0 -9:43:40.1
* Hc 35:29:27.9 / Z 263:15:04.4
* Intercept 0:14:18.6 Toward Gp
* LOP thru 5:58:18.9 -9:57:57.4 in the 173:15:04.4 353:15:04.4 direction
* Z from x to secret 352:47:12.7
* True coords 7:09:30.9 -10:07:02.3
