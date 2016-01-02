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


Sun Sight Reduction Practice Problems
========

by Andrew J. Zimolzak

All angles are given in dd:mm:ss (degrees, minutes, seconds) format.
The assumed position (and LHA, Hc, and Intercept) given in the
solution is just an example. Your AP may not equal the AP that the
machine uses, but yours should ultimately lead you to find a similar
celestial position. That is, after working three sights, compare your
calculated celestial position with the "True (secret) position" of
Sight number 3, and you should be close.


Problem number 1
========

Sight number 1
--------
* Hs 20:21:50.5
* IE 0:00:52.6 off the arc. Eye 2.5 meters. Sun UL.
* 2016/5/17 14:51:55 UTC
* Dead reckoning position -49:19:47.2 -57:55:36.5

Solution
--------
* Ha 20:19:56.3
* Ho 20:01:40.4
* GHA 43:52:32.0 / Dec 19:30:39.2
* Ass Long -56:52:32.0
* LHA 347:00:00.0
* Calculating at AP -49:00:00.0 -56:52:32.0.
* Hc 20:30:47.3 / Z 13:05:00.0
* Intercept 0:29:07.0 Away from Gp
* LOP thru -49:28:21.2 -57:02:40.6 in the 283:05:00.0 103:05:00.0 direction
* Hdg. from Intercept to true position 283:14:52.5 (Should be similar to LOP.)
* True (secret) position is currently -49:20:09.7 -57:54:47.4

Sight number 2
--------
* Hs 21:28:40.6
* IE 0:00:52.6 off the arc. Eye 2.5 meters. Sun UL.
* 2016/5/17 15:50:17 UTC
* Dead reckoning position -48:56:30.5 -58:06:48.5

Solution
--------
* Ha 21:26:46.5
* Ho 21:08:39.3
* GHA 58:28:01.0 / Dec 19:31:11.7
* Ass Long -57:28:01.0
* LHA 1:00:00.0
* Calculating at AP -48:00:00.0 -57:28:01.0.
* Hc 22:28:14.8 / Z 358:58:44.6
* Intercept 1:19:35.5 Away from Gp
* LOP thru -49:19:34.8 -57:25:50.5 in the 268:58:44.6 88:58:44.6 direction
* Hdg. from Intercept to true position 268:56:10.8 (Should be similar to LOP.)
* True (secret) position is currently -49:19:55.2 -58:01:35.6

Sight number 3
--------
* Hs 20:19:12.3
* IE 0:00:52.6 off the arc. Eye 2.5 meters. Sun UL.
* 2016/5/17 16:45:54 UTC
* Dead reckoning position -49:27:12.3 -58:17:49.9

Solution
--------
* Ha 20:17:18.2
* Ho 19:59:01.8
* GHA 72:22:16.2 / Dec 19:31:42.5
* Ass Long -57:22:16.2
* LHA 15:00:00.0
* Calculating at AP -49:00:00.0 -57:22:16.2.
* Hc 20:10:35.7 / Z 344:56:11.4
* Intercept 0:11:33.8 Away from Gp
* LOP thru -49:11:09.9 -57:17:40.3 in the 254:56:11.4 74:56:11.4 direction
* Hdg. from Intercept to true position 254:54:29.5 (Should be similar to LOP.)
* True (secret) position is currently -49:19:46.0 -58:07:37.9


Problem number 2
========

Sight number 1
--------
* Hs 53:12:34.0
* IE 0:01:28.1 off the arc. Eye 5.7 meters. Sun LL.
* 2016/8/29 14:43:24 UTC
* Dead reckoning position -27:33:27.9 -39:03:48.6

Solution
--------
* Ha 53:09:50.3
* Ho 53:25:02.8
* GHA 40:39:56.3 / Dec 9:03:25.4
* Ass Long -38:39:56.3
* LHA 2:00:00.0
* Calculating at AP -27:00:00.0 -38:39:56.3.
* Hc 53:53:16.1 / Z 356:38:43.2
* Intercept 0:28:13.3 Away from Gp
* LOP thru -27:28:10.4 -38:38:04.6 in the 266:38:43.2 86:38:43.2 direction
* Hdg. from Intercept to true position 266:47:25.1 (Should be similar to LOP.)
* True (secret) position is currently -27:28:21.6 -38:41:49.9

Sight number 2
--------
* Hs 50:21:42.2
* IE 0:01:28.1 off the arc. Eye 5.7 meters. Sun LL.
* 2016/8/29 15:36:32 UTC
* Dead reckoning position -26:53:29.3 -38:26:15.2

Solution
--------
* Ha 50:18:58.5
* Ho 50:34:06.6
* GHA 53:57:06.1 / Dec 9:02:38.1
* Ass Long -37:57:06.1
* LHA 16:00:00.0
* Calculating at AP -26:00:00.0 -37:57:06.1.
* Hc 51:39:18.9 / Z 333:58:18.7
* Intercept 1:05:12.3 Away from Gp
* LOP thru -26:58:31.9 -37:24:59.8 in the 243:58:18.7 63:58:18.7 direction
* Hdg. from Intercept to true position 244:33:00.8 (Should be similar to LOP.)
* True (secret) position is currently -27:32:31.0 -38:46:27.8

Sight number 3
--------
* Hs 42:58:49.5
* IE 0:01:28.1 off the arc. Eye 5.7 meters. Sun LL.
* 2016/8/29 16:36:34 UTC
* Dead reckoning position -27:49:30.7 -38:57:42.5

Solution
--------
* Ha 42:56:05.8
* Ho 43:11:00.7
* GHA 68:57:49.0 / Dec 9:01:44.5
* Ass Long -37:57:49.0
* LHA 31:00:00.0
* Calculating at AP -27:00:00.0 -37:57:49.0.
* Hc 43:04:39.7 / Z 315:51:37.0
* Intercept 0:06:21.0 Toward Gp
* LOP thru -26:55:26.5 -38:02:46.6 in the 225:51:37.0 45:51:37.0 direction
* Hdg. from Intercept to true position 226:22:30.1 (Should be similar to LOP.)
* True (secret) position is currently -27:36:42.1 -38:51:47.8
