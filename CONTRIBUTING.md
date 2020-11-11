Thanks for submitting or fixing an icon! Here is a helpful guide to what you need to include.

- [ ] New file which is *under* 1,024 bytes


Additionally, you can do these helpful things if you have time:
- [ ] Edit Readme
- [ ] Add reference image
- [ ] Edit reference page
- [ ] Android Image

## New File

Filename should be `nameofservice.svg` - all in lower-case.
If a special character must be used, please replace it with an underscore (not a dot nor a dash).

Place the file in `/images/svg/`

At a minimum, your icon needs these components, in this layout:

```svg
<svg xmlns="http://www.w3.org/2000/svg"
aria-label="..." role="img"
viewBox="0 0 512 512"><rect
width="512" height="512"
rx="15%"
fill="#fff"/>...</svg>
```

Please keep the whitespace as-is. This makes viewing diffs easier. Please use UNIX line-endings `LF` rather than Windows-style `CRLF`.

If you can, remove the end of line at the end of the file:
* VIm: `:set noeol` (optionally `:set nofixendofline`)
* perl: `perl -pi -e 'chomp if eof' $filename`
* shell: `printf %s "$(cat $filename)" > filename-without-nl.svg`

Please remove any trailing newlines from the file with:

`sed -i -z s/\\n$// filename.svg`

### Guidelines

This is the standard guideline. Use this to help with sizing your icons and they will look good no matter what border radius is chosen.

<img src="https://edent.github.io/SuperTinyIcons/images/guidelines/guideline.svg" width="256" alt="A template for logos" />

- **Green** is the safe zone, where the main body of the icon should be.
- **Yellow** is like a road shoulder, it is there if more space is needed. It should be used for protruding elements, like corners or ornaments.
- **Red** is off limits. It should not be touched by the icons. Red is also how a circular icon would look.


## Edit Readme

Add a table cell to README.md - it must be in this format:

```html
<td>Name of Service<br><img src="https://edent.github.io/SuperTinyIcons/images/svg/nameofservice.svg" width="125" title="Name Of Service"/><br>123 Bytes</td>
```

Please add the correct file size.

## Reference Image

* Find an *official* logo.
* Add it to `/images/reference/`

## Reference Page

* Edit the file [`images/reference/index.md`](images/reference/index.md)
* Add a link to the *official* style guide or brand guidelines.
* For example `| <img src="/images/svg/nameofservice.svg" width="256" />	| <img src="/images/reference/nameofservice.jpg" width="256" />	| https://example.com/press |`

## (Optional) Create Android Version

* Use https://inloop.github.io/svg2android/ to create an Android-compatible XML file.
* Add the file to `/images/android-vector-drawable/`
