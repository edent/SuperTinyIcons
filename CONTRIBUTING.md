Thanks for submitting or fixing an icon! Here is a helpful guide to what you need to include.

- [ ] New file which is *under* 1,024 bytes.
- [ ] Which matches the guidelines.
- [ ] Add reference image.
- [ ] Add official brand guidelines URl.
- [ ] Run `python check.py` to makes sure everything is correct.

## Hacktoberfest - Important!

You do not need to be assigned to an issue. You can start working on it right now 😃

If you send an inappropriate PR, you will be marked as spam. If you have questions, please ask *before* sending a PR.

## New File

* The filename should be `nameofservice.svg` - all in lower-case.
* If a special character must be used, please replace it with an underscore (not a dot nor a dash). 
   * For example `arch_linux.svg`
* Place the file in `/images/svg/`
* At a minimum, your icon needs these components, in this layout:
  * The first `...` should be `nameofservice`
  * The second `...` should be the SVG paths/objects that make up the logo

```svg
<svg xmlns="http://www.w3.org/2000/svg"
aria-label="..." role="img"
viewBox="0 0 512 512"><path
d="m0 0H512V512H0"
fill="#fff"/> ... </svg>
```

## Shrinking

You can shrink the file size using tools like:
* [Yann Armelin's SVG Path Editor](https://yqnn.github.io/svg-path-editor/).
* [svgo](https://svgo.dev/).
* [svgcleaner](https://github.com/RazrFalcon/svgcleaner).
* [SVGOMG](https://jakearchibald.github.io/svgomg/).

### Guidelines

This is the standard guideline. Use this to help with sizing your icons and they will look good no matter what border radius is chosen.

<img src="https://edent.github.io/SuperTinyIcons/images/guidelines/guideline.svg" width="256" alt="A template for logos" />

- **Green** is the safe zone, where the main body of the icon should be.
- **Yellow** is like a road shoulder, it is there if more space is needed. It should be used for protruding elements, like corners or ornaments.
- **Red** is off limits. It should not be touched by the icons. Red is also how a circular icon would look.

## Reference Image and Brand Guidelines URl

* Find an *official* logo.
* Add it to `/images/reference/`
* It must have the same filename as the image you added to `/images/svg/`
   * It's OK if it has a different extension. `nameofservice.png` is fine.
* Add the brand guidelines URl in a new file within `/images/svg/`
   * For example, create a file called `/images/reference/nameofservice.url` with the contents `https://example.com/brand-guidelines`
   * The aim of this is to find an *official* source of the logo. Ideally with information about colours etc. If not, a link to the homepage or favicon will do.

## (Optional) Create Android Version

This is a manual process.

To convert in Android Studio, use [Vector Asset Studio](https://developer.android.com/studio/write/vector-asset-studio#running) and [import the SVG](https://developer.android.com/studio/write/vector-asset-studio#svg).

You can also use the [command line `vd-tool`](https://github.com/rharter/vd-tool) to batch convert images.

Please check the file carefully to see if the preview matches the original. You can check the image in Vector Asset Studio, [online](https://vd.floo.app/), or using `npx vector-drawable-svg logo.xml logo.svg`

If it does render correctly, add the file to `/images/android-vector-drawable/`