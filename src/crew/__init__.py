from flask          import current_app

current_app.menu.root().submenu(".crew").register(visible_when=False)
