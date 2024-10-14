Thanks for submitting or fixing an icon! Here is a helpful guide to what you need to include.

- [ ] New file which is *under* 1,024 bytes

You can shrink the file size uusing tools like [Yann Armelin's SVG Path Editor](https://yqnn.github.io/svg-path-editor/), or [svgo](https://github.com/svg/svgo), or [svgcleaner](https://github.com/RazrFalcon/svgcleaner).

Additionally, you can do these helpful things if you have time:
- [ ] Add reference image
- [ ] Add official brand guidelines URl
- [ ] Update README using the python script
- [ ] Android Image

## Hacktoberfest - Important!

You do not need to be assigned to an issue. You can start working on it right now 😃

If you send an inappropriate PR, you will be marked as spam. If you have questions, please ask *before* sending a PR.

## New File

Filename should be `nameofservice.svg` - all in lower-case.
If a special character must be used, please replace it with an underscore (not a dot nor a dash).

Place the file in `/images/svg/`

At a minimum, your icon needs these components, in this layout:

```svg
<svg xmlns="http://www.w3.org/2000/svg"
aria-label="..." role="img"
viewBox="0 0 512 512"><path
d="m0 0H512V512H0"
fill="#fff"/> ... </svg>
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

## Reference Image and Brand Guidelines URl

* Find an *official* logo.
* Add it to `/images/reference/`
* It must have the same filename as the image you added to `/images/svg/`
   * It's OK if it has a different extension. `nameofservice.png` is fine.
* Add the brand guidelines URl in a new file within `/images/svg/`
   * For example, create a file called `/images/reference/nameofservice.url` with the contents `https://example.com/brand-guidelines`

## Edit Readme

You will need to update the README. To do this, run:

`python3 update_readme.py`

This will update the average file size at the top of the file as well as regenerate the table of icons.
It will also update the REFERENCE.md and CHECK.html files.

## (Optional) Create Android Version

To convert in Android Studio, go to Tools ➡ Resource Manager ➡ Drawable ➡ + ➡ Import Drawables ➡ then select the SVGs.

*Note* Android Studio doesn't like rounded corners with a percentage length value. Before importing, run `sed -i '/rx\=\"15\%\"/d' ./*.svg` to remove the corner or `sed -i -e '/rx\=/s/\"15\%\"/\"77\"/' ./*.svg` to replace the percentage length value with a corresponding fixed length value.

See: https://issuetracker.google.com/issues/176694227

Or, use https://inloop.github.io/svg2android/ to create an Android-compatible XML file.

Add the file to `/images/android-vector-drawable/`
