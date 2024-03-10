#!/usr/bin/python3
"""Creates a unique file storage for the app.
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
