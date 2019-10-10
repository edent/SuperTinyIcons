Thanks for submitting or fixing an icon! Here is a helpful guide to what you need to include.

- [ ] New file which is *under* 1,024 bytes
- [ ] Edit Readme
- [ ] Add reference image
- [ ] Edit reference page
- [ ] (optional) Android Image

## New File

Filename should be `nameofservice.svg` - all in lower-case.

Place the file in `/images/svg/`

At a minimum, your icon needs these components:

```
<svg
xmlns="http://www.w3.org/2000/svg"
aria-label="..." role="img"
viewBox="0 0 512 512"><rect
width="512" height="512"
rx="15%"
fill="#fff"/>...</svg>
```

Please keep the whitespace as-is. This makes viewing diffs easier.

## Edit Readme

Add a table cell to README.md - it must be in this format:

```
<td>Name of Service<br><img src="images/svg/nameofservice.svg" width="125" title="Name Of Service" /><br>123 Bytes</td>
```

Please add the correct file size.

## Reference Image

* Find an *official* logo.
* Add it to `/images/reference/`

## Reference Page

* Edit the file `/images/reference/index.md`
* Add a link to the *official* style guide or brand guidelines.
* For example `| <img src="/images/svg/nameofservice.svg" width="256" />	| <img src="/images/reference/nameofservice.jpg" width="256" />	| https://example.com/press |`

## (Optional) Create Android Version

* Use https://inloop.github.io/svg2android/ to create an Android-compatible XML file.
* Add the file to `/images/android-vector-drawable/`
