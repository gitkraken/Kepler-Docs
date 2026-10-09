# ADE-Docs

## Screenshot markers

Pages flag images that need work with an HTML comment, which doesn't render on the site:

| Marker | Meaning |
|---|---|
| `<!-- TODO(screenshot): Replace — … -->` | Placed right after an existing figure whose UI has changed. The text says what the new image should show |
| `<!-- TODO(screenshot): New — … -->` | A place that needs an image that doesn't exist yet. The text describes it |

Find them all with `grep -rn "TODO(screenshot)" kepler/`. When you add or replace the image, delete the marker.
