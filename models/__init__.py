#!/usr/bin/python3
"""make a unique file storage for all of the app.
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
