from flask          import current_app

current_app.menu.root().submenu(".crew").register()
current_app.menu.root().submenu(".crew").hide()
