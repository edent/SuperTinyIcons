# Super Tiny Social Icons
Under 1KB each! Super Tiny Social Icons are minuscule SVG versions of your favourite logos. The average size is 600 bytes!

The logos are 400x400 & have a 512x512 viewbox. They will scale up and down to suit your needs.

Originally created for my contact page - [https://edent.tel/](https://edent.tel/)

## How Small?

| 765 Bytes SVG	| 31,061 Bytes PNG	|   412 Bytes SVG	| 26,980 Bytes PNG	|  220 Bytes SVG	| 16,093 Bytes PNG	|
|------	        |-----------     	|------	            |----------	        |------	        |-----------	        |
| <img src="https://edent.github.io/SuperTinySocialIcons/tiny/github.svg" width="100" />  	| <img src="https://edent.github.io/SuperTinySocialIcons/original/github.png" width="100" />        	| <img src="https://edent.github.io/SuperTinySocialIcons/tiny/twitter.svg" width="100" />   	| <img src="https://edent.github.io/SuperTinySocialIcons/original/twitter.png" width="100" />       	| <img src="https://edent.github.io/SuperTinySocialIcons/tiny/flickr.svg" width="100" />   	| <img src="https://edent.github.io/SuperTinySocialIcons/original/flickr.png" width="100" />       	|

## What's Available so far?

<img src="https://edent.github.io/SuperTinySocialIcons/tiny/hackernews.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/flickr.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/facebook.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/tumblr.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/mail.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/telegram.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/dropbox.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/instagram.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/linkedin.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/stackoverflow.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/vimeo.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/twitter.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/lock.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/html5.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/paypal.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/email.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/pinterest.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/slideshare.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/soundcloud.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/spotify.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/steam.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/whatsapp.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/wikipedia.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/wordpress.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/github.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/phone.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/skype.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/wire.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/amazon.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/google_plus.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/snapchat.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/wechat.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/youtube.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/rss.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/pdf.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/reddit.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/vk.svg" width="100" /> <img src="https://edent.github.io/SuperTinySocialIcons/tiny/mastodon.svg" width="100" />

## Why so smallious?

Bytes cost money.  They cost money to store, transport, and process.  Simplicity should be our goal in all endeavours.

## Scream if you want to go smaller

These files edited by hand in Inkscape, then were minified using [svgo](https://github.com/svg/svgo) and [svgcleaner](https://github.com/RazrFalcon/svgcleaner). Further smallification may be possible.

* Each of these has an `xmlns="http://www.w3.org/2000/svg"` in the `<svg>` tag. This isn't strictly necessary - but some web browsers won't display them as an image without it.
* Newlines can be stripped - they've been kept for readability where possible.
* Rounded corners can be dropped - `rx="15%"` - the effect can be done in CSS if you want.
* The background colour can also be excluded if you're including it elsewhere.
* Colours can be simplified. `#FF0000` becomes `red`.
* The precision of the paths is *mostly* 0 decimal places. A few logos have 1 or 2 dp to make them look more accurate. The precision can be reduced if necessary.

You can see the difference this makes in [`youtube.svg`](https://github.com/edent/SuperTinySocialIcons/raw/master/tiny/youtube.svg) which is a ginormous 1,032 Bytes. By applying some of the above techniques we can get it down to a svelte 981 Bytes in [`youtube-tiny.svg`](https://github.com/edent/SuperTinySocialIcons/raw/master/tiny/youtube-tiny.svg).

Think you can make them smaller? Tell me by raising an issue!

Want more icons?  Tell me by raising an issue!

## Licenses

The majority of these vector logos are based on someone else's work.

* [Social Media Icons by Aha-Soft](https://www.iconfinder.com/iconsets/social-flat-rounded-rects) - CC-BY
* [Phone Icon](https://www.iconfinder.com/icons/1807538/phone_icon#size=128) - Free
* [Lock Icon](https://www.iconfinder.com/icons/1814107/lock_padlock_secure_icon#size=512) - MIT
* [Wire Logo](https://commons.wikimedia.org/wiki/File:Wire_software_logo.svg) - Public Domain
* [Signal Logo](https://github.com/WhisperSystems/Signal-iOS/blob/master/Signal/Images.xcassets/logoSignal.imageset/logoSignal.pdf) - GPLv3
* [RSS Icon](https://commons.wikimedia.org/wiki/File:Generic_Feed-icon.svg) - MPL 1.1
* [PDF Icon](https://www.iconfinder.com/iconsets/line-icons-set) - Free
* [Reddit's Snoo](http://ionicons.com/) - MIT
* [Google+](https://commons.wikimedia.org/wiki/File:Google_Plus_logo_2015.svg) - Public Domain
* [Mastodon](https://github.com/tootsuite/mastodon/blob/0ad694f96b7f0e951950e7525bde52cd11454cb2/app/assets/images/logo.svg) - AGPLv3
* [HTML5 Shield](https://www.w3.org/html/logo/) - CC-BY

Where possible, they retain their original licenses.  Some logos may be subject to copyright and trademark laws, but these files are small enough to memorise.
