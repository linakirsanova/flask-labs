# Template Inheritance

Emily is still a bit slow to get her app in good shape, so after bribing you with more dog costumes, she's asked you to help overhaul her HTML pages. She's getting super tired of having to copy all her HTML from one page to the next, and rightly so! You remembered from your Flask lessons that Jinja supports **template inheritance** so you know just what to do.

___

## Instructions

**Read everything before you start!**

(Before you start, you can copy `app.py` and `costumes.html` from the last lab once you've already solved it.)

Similar to how you inherited your grandfather's itchy sweaters against your own will (thanks gramps), in this lab you'll be using template inheritance to prevent code reuse.

**Remember to create and use a separate Python virtual environment for each lab.** You'll be glad you did. :)

### Task: Make a Base Template

There's a lot you can reuse in these templates, but to make it easier for you, make a base template that defines blocks for:

- `head`
  - `title`
- `body`
  - `header`
    - `navbar`
  - `content` (parent content section)
    - `page_content` (renders most of the content within `content`)
  - `footer`

You can also add any other blocks you think might make sense. The above also gives you a hint for where how these blocks might be structured. ;)

Then have the other templates inherit from that base template. For this lab, keep in mind there is no one right answer. Once you are done with this step, the webpages should look about the same as they did before.
