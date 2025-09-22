# Super Tiny Icons

Under 1KB each! Super Tiny Web Icons are minuscule SVG versions of your favourite logos. There are currently 400 icons and the average size is _under_ 524 bytes!

The logos have a 512x512 viewbox, they will fit in a circle with radius 256. They will scale up and down to suit your needs.

[![DOI](https://zenodo.org/badge/88214511.svg)](https://doi.org/10.5281/zenodo.16944294)

## How Small?

| 527 Bytes SVG                                                                          | 3,328 Bytes PNG                                                                        | 352 Bytes SVG                                                                           | 2,987 Bytes PNG                                                                         | 235 Bytes SVG                                                                          | 1,615 Bytes PNG                                                                        |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| <img src="https://edent.github.io/SuperTinyIcons/images/svg/github.svg" width="100" /> | <img src="https://edent.github.io/SuperTinyIcons/images/png/github.png" width="100" /> | <img src="https://edent.github.io/SuperTinyIcons/images/svg/twitter.svg" width="100" /> | <img src="https://edent.github.io/SuperTinyIcons/images/png/twitter.png" width="100" /> | <img src="https://edent.github.io/SuperTinyIcons/images/svg/flickr.svg" width="100" /> | <img src="https://edent.github.io/SuperTinyIcons/images/png/flickr.png" width="100" /> |

## Hacktoberfest!

This project welcomes Hacktoberfest participants.  All we ask is that you:

* ✅ Make your logo *under* 1,024 bytes.
* ✅ Follow the [Contributing Guidance](CONTRIBUTING.md).
* ✅ Be friendly to other participants.
* ✅ Choose a logo which is highly recognisable.
* ❌ Don't use AI. That means no ChatGPT, Gemini, Claude, etc. This is your opportunity to learn.
* ❌ Don't [change the HTML](https://github.com/edent/SuperTinyIcons/pull/870)
* ❌ Don't send [broken logos](https://github.com/edent/SuperTinyIcons/pull/868)
* ❌ Don't [ignore the guidelines](https://github.com/edent/SuperTinyIcons/pull/809)

If you do not follow the instructions, your contribution will be marked as spam and you will be disqualified from Hacktoberfest.

## What's Available so far?

<table>
</table>

## Why so smallious?

Bytes cost money. They cost money to store, transport, and process. Simplicity should be our goal in all endeavours.

## Scream if you want to go smaller

These files were edited by hand in Inkscape, Illustrator, or a text editor, then were minified using [Yann Armelin's SVG Path Editor](https://yqnn.github.io/svg-path-editor/), [svgo](https://github.com/svg/svgo), and [svgcleaner](https://github.com/RazrFalcon/svgcleaner). Further smallification may be possible. Try it!

- Each of these has an `xmlns="http://www.w3.org/2000/svg"` in the `<svg>` tag. This isn't strictly necessary - but some web browsers won't display them as an image without it.
- The background colour can also be excluded if you're including it elsewhere.
- Colours can be simplified. `#FF0000` becomes `red`.
- The precision of the paths is _mostly_ 0 decimal places. A few logos have 1 or 2 dp to make them look more accurate. The precision can be reduced if necessary.

Think you can make them smaller? Tell me by raising an issue!

Want more icons? Tell me by raising an issue!

Think the icons look wrong? [Compare them against the official logos](https://github.com/edent/SuperTinyIcons/blob/master/REFERENCE.md). If they still look wrong, tell me by raising an issue!

## Android Vector Drawables

Icons also available as [Android Vector Drawables](https://developer.android.com/guide/topics/graphics/vector-drawable-resources.html), so you can easily use them in Android apps.

They are **not** guaranteed to be under 1KB.

## Submitting Icons

I'd _love_ you to submit something 😸 The rules are simple, your icon must:

- be **under** 1024 bytes. That is, the maximum file size is 1023 bytes. No arguments.
- fit inside a circle with radius 256 pixels. Set `rx="50%"` to check.
- represent a popular service's current logo.

### Template

At a minimum, your icon needs these components:

```svg
<svg xmlns="http://www.w3.org/2000/svg"
aria-label="..." role="img"
viewBox="0 0 512 512"><path
d="m0 0H512V512H0"
fill="#fff"/> ... </svg>
```

### Icon accessibility

The super tiny icons are accessible by default. Each icon has:

- `role="img"`, to expose the `<svg>` elements as images in the browser's accessibility tree
- `aria-label="XYZ"` (where XYZ is the icon's brand name), to give the icon an accessible name

`Note:` if using the `<svg>` as the `src` for an `<img>` element, the `alt` attribute should still be used on the `<img>` element because the ARIA is not recognised in this context.

CSS-Tricks has also an [article about accessible SVG icons](https://css-tricks.com/accessible-svgs/).

### Guidelines

This is the standard guideline. Use this to help with sizing your icons and they will look good no matter what border radius is chosen.

<img src="https://edent.github.io/SuperTinyIcons/images/guidelines/guideline.svg" width="256" alt="A template for logos" />

- **Green** is the safe zone, where the main body of the icon should be.
- **Yellow** is like a road shoulder, it is there if more space is needed. It should be used for protruding elements, like corners or ornaments.
- **Red** is off limits. It should not be touched by the icons. Red is also how a circular icon would look.

## Installation

```sh
npm install --save super-tiny-icons
```

## Usage

The old-school way:

```html
<img src="./node_modules/super-tiny-icons/images/svg/github.svg" />
```

The modern way, the React (JSX) example:

```jsx
import logo from "super-tiny-icons/images/svg/github.svg";

<img src={logo} />;
```

[CSS](https://developer.mozilla.org/docs/Web/CSS) can be used to customize an icon's appearance. The following example shows styles for small/medium/large icons with square/rounded/circular frames:

```html
<style>
  .small-square {
    width: 20px;
  }
  .medium-rounded {
    width: 50px;
    border-radius: 10%;
  }
  .large-circular {
    width: 100px;
    border-radius: 50%;
  }
</style>

<img src="images/svg/reddit.svg" class="small-square" />
<img src="images/svg/reddit.svg" class="medium-rounded" />
<img src="images/svg/reddit.svg" class="large-circular" />
```

## Contributors

### Code Contributors

This project exists thanks to all the people who contribute. [[Contribute](CONTRIBUTING.md)].
<a href="https://github.com/edent/SuperTinyIcons/graphs/contributors"><img src="https://opencollective.com/SuperTinyIcons/contributors.svg?width=890&button=false" /></a>

### Financial Contributors

Become a financial contributor and help us sustain our community. [[Contribute](https://opencollective.com/SuperTinyIcons/contribute)]

#### Individuals

<a href="https://opencollective.com/SuperTinyIcons"><img src="https://opencollective.com/SuperTinyIcons/individuals.svg?width=890"></a>

#### Organizations

Support this project with your organization. Your logo will show up here with a link to your website. [[Contribute](https://opencollective.com/SuperTinyIcons/contribute)]

<a href="https://opencollective.com/SuperTinyIcons/organization/0/website"><img src="https://opencollective.com/SuperTinyIcons/organization/0/avatar.svg"></a>
<a href="https://opencollective.com/SuperTinyIcons/organization/1/website"><img src="https://opencollective.com/SuperTinyIcons/organization/1/avatar.svg"></a>
<a href="https://opencollective.com/SuperTinyIcons/organization/2/website"><img src="https://opencollective.com/SuperTinyIcons/organization/2/avatar.svg"></a>
<a href="https://opencollective.com/SuperTinyIcons/organization/3/website"><img src="https://opencollective.com/SuperTinyIcons/organization/3/avatar.svg"></a>
<a href="https://opencollective.com/SuperTinyIcons/organization/4/website"><img src="https://opencollective.com/SuperTinyIcons/organization/4/avatar.svg"></a>
<a href="https://opencollective.com/SuperTinyIcons/organization/5/website"><img src="https://opencollective.com/SuperTinyIcons/organization/5/avatar.svg"></a>
<a href="https://opencollective.com/SuperTinyIcons/organization/6/website"><img src="https://opencollective.com/SuperTinyIcons/organization/6/avatar.svg"></a>
<a href="https://opencollective.com/SuperTinyIcons/organization/7/website"><img src="https://opencollective.com/SuperTinyIcons/organization/7/avatar.svg"></a>
<a href="https://opencollective.com/SuperTinyIcons/organization/8/website"><img src="https://opencollective.com/SuperTinyIcons/organization/8/avatar.svg"></a>
<a href="https://opencollective.com/SuperTinyIcons/organization/9/website"><img src="https://opencollective.com/SuperTinyIcons/organization/9/avatar.svg"></a>

## Licenses

The majority of these vector logos are based on someone else's work.

- [Social Media Icons by Aha-Soft](https://www.iconfinder.com/iconsets/social-flat-rounded-rects) - CC-BY
- [Phone Icon](https://www.iconfinder.com/icons/1807538/phone_icon#size=128) - Free
- [Lock Icon](https://www.iconfinder.com/icons/1814107/lock_padlock_secure_icon#size=512) - MIT
- [Wire Logo](https://commons.wikimedia.org/wiki/File:Wire_software_logo.svg) - Public Domain
- [Signal Logo](https://github.com/WhisperSystems/Signal-iOS/blob/master/Signal/Images.xcassets/logoSignal.imageset/logoSignal.pdf) - GPLv3
- [RSS Icon](https://commons.wikimedia.org/wiki/File:Generic_Feed-icon.svg) - MPL 1.1
- [PDF Icon](https://www.iconfinder.com/iconsets/line-icons-set) - Free
- [Google+](https://commons.wikimedia.org/wiki/File:Google_Plus_logo_2015.svg) - Public Domain
- [Google](http://svgshare.com/s/q)
- [Mastodon](https://github.com/tootsuite/mastodon/blob/0ad694f96b7f0e951950e7525bde52cd11454cb2/app/assets/images/logo.svg) - AGPLv3
- [GitLab](https://about.gitlab.com/press/)
- [HTML5 Shield](https://www.w3.org/html/logo/) - CC-BY
- [npm Logo](https://commons.wikimedia.org/wiki/File:Npm-logo.svg) - CC-BY
- [Docker Logo](https://github.com/docker/docker.github.io/blob/master/LICENSE) - Apache
- [Steam](https://commons.wikimedia.org/wiki/File:Steam_icon_logo.svg)
- [Symantec](https://commons.wikimedia.org/wiki/File:Symantec_logo10.svg)
- [Yubico](https://github.com/Yubico/yubikey-manager-qt/blob/master/resources/icons/ykman.png) - BSD
- [Keybase](https://github.com/keybase/client/blob/master/shared/images/iconfont/kb-iconfont-keybase-16.svg) - BSD
- [eBay](https://commons.wikimedia.org/wiki/File:EBay_logo.svg)
- [Kickstarter](https://www.kickstarter.com/help/brand_assets)
- [Bitcoin](https://commons.wikimedia.org/wiki/File:Bitcoin_logo.svg) - CC0
- [Bluetooth](https://commons.wikimedia.org/wiki/File:Bluetooth.svg)
- [Blogger](https://commons.wikimedia.org/wiki/File:Blogger_icon.svg)
- [Medium](https://medium.design/logos-and-brand-guidelines-f1a01a733592)
- [Ghost](https://commons.wikimedia.org/wiki/File:Ghost-Logo.svg)
- [Tumblr](https://www.tumblr.com/logo)
- [Intel](https://commons.wikimedia.org/wiki/File:Intel-logo.svg)
- [Badoo](https://team.badoo.com/new/)
- [YouTube](https://www.youtube.com/yt/about/brand-resources/#logos-icons-colors)
- [Google Play](https://commons.wikimedia.org/wiki/File:Google_Play_symbol_2016.svg)
- [Gmail](https://commons.wikimedia.org/wiki/File:Gmail_Icon.svg)
- [Samsung Internet](https://github.com/edent/SuperTinyIcons/pull/74/commits/8824bdaf1346a472ab425347f958e8e64c0948ee)
- [Plex](https://github.com/plexinc/plex-media-player/blob/master/resources/images/icon.svg) - GPLv2
- [NHS](https://www.england.nhs.uk/nhsidentity/identity-guidelines/nhs-logo/)
- [Threema.](https://threema.ch/de/press)
- [CoreUI](https://github.com/coreui/coreui-icons) - CC-BY
- [NixOS](https://github.com/NixOS/nixos-artwork) - CC-BY
- [Yii PHP Framework](https://www.yiiframework.com/logo) - CC BY-ND 3.0

From [SVGporn](https://github.com/gilbarbara/logos/) - CC0

IBM, Yammer, Android, Authy, Cloudflare, CodePen, DigitalOcean, Discord, Airbnb, WiFi, Delicious, Open Source, Patreon, Tim Cuthbertson

Where possible, they retain their original licenses. Some logos may be subject to copyright and trademark laws, but these files are small enough to memorise.
