
Installation
===

Install [Vagrant](http://www.vagrantup.com/downloads)

Then, from the project directory, login to your box:

    vagrant up
    vagrant ssh

`provision.sh` downloads and installs OpenCV:

    cd /vagrant
    chmod +x setup.sh
    ./provision.sh

This takes a while.

Usage
===

To run the [Crichardt panorama stitching](http://richardt.name/teaching/supervisions/vision-2011/practical/) code:

    cd crichardt
    python stitch.py Image1.jpg Image2.jpg

This outputs `correspondences.jpg`, `panorama.jpg`


To run the simplified affine transformation calculation:

    python affine/affine_many.py books/*

This prints out a JSON blob that can be used to align the images.

The [demo](http://smallredtile.com/align/) here uses this data.

---

Research Notes:

So many applications of image stitching!

* aligning observations of the sun's position
* brain scan images
* high resolution bio slides
* drones flying over terrain
* panorama photos of landscapes or architecture

And subsequently, quite a variety of techniques.

- Phase correlation with fft
- SIFT, feature detection, homography

---

Think about parallax: an object closer will show more perspective change after translation than an object farther away. Think of two picture, one of an object close, one of an object far. Or, two objects in the same picture, one near and one far. What kind of affine transformation would work for both images? It's not possible; you have to know something about the geometry of the subject.
  
  http://en.wikipedia.org/wiki/Parallax
  
  In a philosophic/geometric sense: An apparent change in the direction of an object, caused by a change in observational position that provides a new line of sight. The apparent displacement, or difference of position, of an object, as seen from two different stations, or points of view. In contemporary writing parallax can also be the same story, or a similar story from approximately the same time line, from one book told from a different perspective in another book. The word and concept feature prominently in James Joyce's 1922 novel, Ulysses. Orson Scott Card also used the term when referring to Ender's Shadow as compared to Ender's Game.

  The metaphor is invoked by Slovenian philosopher Slavoj Žižek in his work The Parallax View. Žižek borrowed the concept of "parallax view" from the Japanese philosopher and literary critic Kojin Karatani. "The philosophical twist to be added (to parallax), of course, is that the observed distance is not simply subjective, since the same object that exists 'out there' is seen from two different stances, or points of view. It is rather that, as Hegel would have put it, subject and object are inherently mediated so that an 'epistemological' shift in the subject's point of view always reflects an ontological shift in the object itself. Or—to put it in Lacanese—the subject's gaze is always-already inscribed into the perceived object itself, in the guise of its 'blind spot,' that which is 'in the object more than object itself', the point from which the object itself returns the gaze. Sure the picture is in my eye, but I am also in the picture."[35]

---

Install notes:

http://karytech.blogspot.in/2012/05/opencv-24-on-ubuntu-1204.html

Another OpenCV install, this time to build the examples:

http://mitchtech.net/raspberry-pi-opencv/

---

http://wiki.panotools.org/Stitching_a_photo-mosaic

  A photo-mosaic is an image that is stitched together by photographs all taken from different viewpoints. This differs from the panorama where all images are taken from one single viewpoint but with different angles.