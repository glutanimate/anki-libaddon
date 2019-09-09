
# Handling async JS execution when saving editor content

def editorSaveThen(callback):
    def onSaved(editor, *args, **kwargs):
        # uses evalWithCallback internally:
        editor.saveNow(lambda: callback(editor, *args, **kwargs))
    return onSaved


def widgetEditorSaveThen(callback):
    def onSaved(widget, *args, **kwargs):
        """[summary]
        
        Arguments:
            callback {[type]} -- [description]
            widget {Qt widget or widget} -- Qt object the editor is a member of
            (e.g. Browser, AddCards, EditCurrent)
        """
        # uses evalWithCallback internally:
        widget.editor.saveNow(lambda: callback(widget, *args, **kwargs))
    return onSaved
