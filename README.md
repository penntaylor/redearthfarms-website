# redearthfarms-website

Code and public assets for redearthfarms.org website.

---

Did a Red Earth member send you here to find editable versions of our basic documents? If so, look under `content/docs/editable` to find open-document versions of some of our documents.

Otherwise, there isn't anything here that isn't available directly from our website, aside from some python scripts that make the sausage.

---

# For Community members

**DO NOT CHECK SECRETS, CREDENTIALS, OR PRIVATE INFO INTO THIS REPOSITORY. IT IS OPEN TO ANY AND ALL PRYING EYES!**

Everything you are concerned with lives in the content directory. All pages in /content use Markdown formatting rather than raw html. Here's a [cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for Markdown if you need some help getting the formatting you want.

## To edit a page:
* find it in `/content` (or perhaps `/content/people` or `/content/leaseholds`; you get the idea)
* click on the **name** of the page (eg. `cooperatives.md`). The page's text contents should now be displayed in a text pane.
* select the little icon that looks like a pencil in the upper right of the text pane
* edit the text however you want. (Don't try to use the "Preview changes" tab on the text pane. It doesn't do what you expect, and you'll wonder why everything looks wrong.)
* once everything looks good, run down to the box below the text pane that says "Commit chnages", and
  * put a very brief description of the changes you made into the first box; eg. "Added basic instructions to the README"
  * ensure that "Commit directly to the `master` branch." is selected
  * click the "Commit changes" button
  * after ~20 seconds, the live website should be updated with your changes. Test by browsing to the site and being sure to refresh the particular page(s) you edited. If your changes still don't show up, try clearing your browser's cache and refreshing the page again. If you're still having trouble, email Penn.
  
## Super-secret tips and hints
Open this page again in a new tab. Open the [Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) in another tab as well. Now you can easily flip between these instructions, the markdown docs, and the page you're trying to edit.

## Images

Images on people and leasehold pages should have a maximum width of 400 pixels.

### On the rotating sidebar
Images should be jpeg, 180x120 pixels (max), and have all metadata stripped. Batch conversion can be done with imagemagick as follows:
```
mkdir small
for f in *.jpg; do convert -strip -resize 180x120 $f small/$f; done
```
Alternatively, black bars can be added to pad out images that don't have 3:2 aspect ratio by replacing the `convert` part above with:
```
convert -strip -resize 180x120 -background black -gravity center -extent 180x120 $f small/$f
```

# How Do I ... ?
## Rename a file
Upload a file with the new name, then delete the version with the old name.

## Edit / Resize an image
Download the image to your local computer, then use whichever image manipulation program you're familiar with to resize, rescale, adjust colors, etc. Overwrite your local version with the edited version, then upload it back to the repository.
